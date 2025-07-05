# 🚀 GitHub Tracker - (Github Activity Tracker using Webhook )

This project tracks GitHub activity using webhooks and displays it in real-time. It listens for `push`, `pull_request`, and `merge` events from a GitHub repo, stores the data in MongoDB, and shows it on a React-based frontend that updates every 15 seconds.

---

## 🧩 Project Structure

Test Repo for Github Actions
```
action-repo/ # A test GitHub repo to trigger events
```
Github Activity Tracker Structure
```
github-webhook-project/
├── webhook-repo/ # Flask backend to receive and store events
└── webhook-ui/ # React frontend to display activity
```

---

## 📌 Features

- ✅ GitHub Webhook integration for `push`, `pull_request`, and `merge`
- ✅ Flask API backend with MongoDB Atlas
- ✅ Real-time polling frontend (every 15s) using React
- ✅ Clean and minimal UI
- ✅ Fully decoupled architecture

---

## 🛠️ Tech Stack

- **Backend**: Flask + PyMongo
- **Frontend**: React + Axios
- **Database**: MongoDB Atlas
- **Dev Tools**: Ngrok, GitHub Webhooks

---

## 🔧 Setup Instructions

### 1. Clone the Repos

```bash
git clone https://github.com/sparky17/git-actions-repo.git
git clone https://github.com/sparky17/github-webhooks.git
```
### 2. Backend Setup (webhook-repo)
📦 Install dependencies
 ```
cd webhook-repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
📄 Create .env
```
env example
```
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/github_events?retryWrites=true&w=majority
```
▶️ Start the Flask server
```
python app.py
```
### 3. Expose Flask Server via Ngrok
```
ngrok http 5000
```
Copy the HTTPS URL (e.g. https://xyz.ngrok.io)

### 4. GitHub Webhook Setup
```
Go to action-repo → Settings → Webhooks → Add webhook
```
Fill Value
```
Payload URL	https://your-ngrok-url/webhook
Content type	application/json
Events to send	✅ Push, ✅ Pull request
Secret (optional)	(Leave blank for now)
```
### 5. Frontend Setup (webhook-ui)
```
cd webhook-ui
npm install
npm start
```
The app will run on
``` http://localhost:3000``` and fetch updates every 15 seconds.

### 6. Test the Flow
In action-repo:

# Push Event
```
echo "// test push" >> test.js
git add .
git commit -m "Trigger push event"
git push origin main
```
# Pull Request Event
```
git checkout -b feature-branch
```

# edit file
```

git commit -am "Add PR test"
git push origin feature-branch
```

# Go to GitHub UI → Open PR
🧾 MongoDB Schema
Each event document looks like:
```

{
  "event_type": "push" | "pull_request" | "merge",
  "author": "username",
  "to_branch": "main",
  "from_branch": "feature-xyz",     // only for PR and merge
  "timestamp": "2025-07-04T12:00:00Z"
}
```

🎯 Sample UI Output
```

JohnDoe pushed to main on 4th July 2025 - 9:30 PM UTC

JohnDoe submitted a pull request from dev to main on 4th July 2025 - 9:45 PM UTC

JohnDoe merged branch dev to main on 4th July 2025 - 10:00 PM UTC
```

