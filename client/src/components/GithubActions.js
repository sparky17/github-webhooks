import { useEffect, useState } from "react";
import axios from "axios";
import React from 'react';

const GitHubActions = () => {
    const [actions, setActions] = useState([]);

    const fetchEvents = async () => {
      try {
        const res = await axios.get("http://localhost:5000/events");
        setActions(res.data);
      } catch (err) {
        console.error(err);
      }
    };
  
    useEffect(() => {
      fetchEvents();
      const interval = setInterval(fetchEvents, 15000);
      return () => clearInterval(interval);
    }, []);

  
    return (
        <div className="github-actions">
            {actions.map((action, index) => (
                <div key={index} className="action-card">
                    <div className="card-header">
                        <h3>{action.author}</h3>
                        <span className="timestamp">{new Date(action.timestamp).toLocaleString()}</span>
                    </div>
                    <div className="card-body">
                        <p>
                            <strong>{action.event_type}</strong>{" to "} 
                            <span className="branch">{action.to_branch}</span>
                            
                            {action.from_branch && (
                                <> 
                                    {" from "}<span className="branch">{action.from_branch}</span>
                                </>
                            )}
                        </p>
                    </div>
                </div>
            ))}
        </div>
    );
}; 

export default GitHubActions;