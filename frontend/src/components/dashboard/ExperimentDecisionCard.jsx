import React from "react";

export default function ExperimentDecisionCard({

  stats,
  winner,
  uplift

}) {

  if (!stats) return null;

  return (

    <div className="decision-card">

      <h2>
        EXPERIMENT DECISION
      </h2>

      <p>
        Winning Variant:
        <strong>
          {" "}
          {winner}
        </strong>
      </p>

      <p>
        Uplift:
        <strong>
          {" "}
          {uplift}%
        </strong>
      </p>

      <p>
        P-Value:
        <strong>
          {" "}
          {stats.p_value}
        </strong>
      </p>

      <p>
        Significance:
        <strong>

          {
            stats.significant

              ? " YES"

              : " NO"
          }

        </strong>
      </p>

    </div>
  );
}