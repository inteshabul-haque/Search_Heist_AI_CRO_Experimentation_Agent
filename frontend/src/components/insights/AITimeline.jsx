import React from "react";

export default function AITimeline({

  executionTrace

}) {

  if (!executionTrace) return null;

  return (

    <div className="ai-timeline">

      {

        executionTrace.map(

          (step, index) => (

            <div
              key={index}
              className="timeline-step"
            >

              <div className="timeline-dot" />

              <div>

                <strong>
                  {step.agent}
                </strong>

                <p>
                  {step.action}
                </p>

              </div>

            </div>
          )
        )
      }

    </div>
  );
}