import React from "react";

export default function ExecutiveRecommendation({

  uplift,
  significant

}) {

  let recommendation = "";

  if (uplift > 15 && significant) {

    recommendation =

      "Deploy winning variant immediately. Strong statistical confidence detected.";
  }

  else if (uplift > 5) {

    recommendation =

      "Continue experiment to gather more statistical confidence.";
  }

  else {

    recommendation =

      "Current experiment impact remains limited. Additional testing recommended.";
  }

  return (

    <div className="executive-recommendation">

      <h2>
        EXECUTIVE RECOMMENDATION
      </h2>

      <p>
        {recommendation}
      </p>

    </div>
  );
}