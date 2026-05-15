import React from "react";

export default function ExperimentSummaryPanel({

  winner,
  uplift,
  pValue,
  significant

}) {

  return (

    <div className="experiment-summary-panel">

      <h2>
        EXPERIMENT SUMMARY
      </h2>

      <div className="summary-grid">

        <div>

          <p>Winning Variant</p>

          <h1>{winner}</h1>

        </div>

        <div>

          <p>Uplift</p>

          <h1>{uplift}%</h1>

        </div>

        <div>

          <p>P-Value</p>

          <h1>{pValue}</h1>

        </div>

        <div>

          <p>Significance</p>

          <h1>

            {
              significant

                ? "YES"

                : "NO"
            }

          </h1>

        </div>

      </div>

    </div>
  );
}