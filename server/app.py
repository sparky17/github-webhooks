from flask import Flask, request, jsonify
from flask_cors import CORS
from models import events
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for React

@app.route("/webhook", methods=["POST"])
def github_webhook():
    print("🔔 Webhook hit!")
    
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.get_json()
    print(f"Event type: {event_type}")
    print(f"Payload: {payload}")

    event_data = {"timestamp": datetime.utcnow()}

    if event_type == "push":
        event_data.update({
            "event_type": "push",
            "author": payload.get("pusher", {}).get("name"),
            "to_branch": payload.get("ref", "").replace("refs/heads/", ""),
        })

    elif event_type == "pull_request":
        pr = payload.get("pull_request", {})
        action = payload.get("action")

        if action == "opened":
            event_data.update({
                "event_type": "pull_request",
                "author": pr.get("user", {}).get("login"),
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("created_at")
            })
        elif action == "closed" and pr.get("merged"):
            event_data.update({
                "event_type": "merge",
                "author": pr.get("user", {}).get("login"),
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("merged_at")
            })
        else:
            return "No action needed", 200
    else:
        return "Unsupported event", 200

    events.insert_one(event_data)
    return "Event saved", 201

@app.route("/events", methods=["GET"])
def get_events():
    latest = list(events.find().sort("timestamp", -1).limit(10))
    for event in latest:
        event["_id"] = str(event["_id"])  # Convert ObjectId for frontend
    return jsonify(latest)

if __name__ == "__main__":
    app.run(port=5000)
