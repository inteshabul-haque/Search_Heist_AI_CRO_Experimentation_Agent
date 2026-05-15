import React from "react";

export default function AIInsightFeed({
  insights
}) {

  if (!insights) return null;

  return (

    <div className="insight-feed">

      {insights.map(

        (item, index) => (

          <div
            key={index}
            className="ai-feed-card"
          >

            {item}

          </div>
        )
      )}

    </div>
  );
}