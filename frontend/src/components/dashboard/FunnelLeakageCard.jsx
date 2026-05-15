import React from "react";

export default function FunnelLeakageCard({

  funnelData

}) {

  if (!funnelData) return null;

  const steps = [

    {
      name: "Visited",
      value: funnelData.visited
    },

    {
      name: "Product View",
      value: funnelData.product_view
    },

    {
      name: "Add To Cart",
      value: funnelData.add_to_cart
    },

    {
      name: "Checkout",
      value: funnelData.checkout
    },

    {
      name: "Purchase",
      value: funnelData.purchase
    }
  ];

  let largestDrop = 0;

  let leakageStep = "";

  for (let i = 0; i < steps.length - 1; i++) {

    const drop =

      steps[i].value -
      steps[i + 1].value;

    if (drop > largestDrop) {

      largestDrop = drop;

      leakageStep =

        `${steps[i].name} → ${steps[i + 1].name}`;
    }
  }

  return (

    <div className="funnel-leakage-card">

      <h2>
        FUNNEL LEAKAGE
      </h2>

      <h1>
        {largestDrop}
      </h1>

      <p>
        Largest drop-off between:
      </p>

      <strong>
        {leakageStep}
      </strong>

    </div>
  );
}