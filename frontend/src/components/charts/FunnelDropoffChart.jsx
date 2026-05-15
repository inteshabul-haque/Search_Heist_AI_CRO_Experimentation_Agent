import React from "react";

import {
  ResponsiveContainer,
  FunnelChart,
  Funnel,
  LabelList,
  Tooltip,
  Cell
} from "recharts";

export default function FunnelDropoffChart({
  data
}) {

  if (!data) return null;

  const steps = [

    {
      name: "Visited",
      value: data.visited
    },

    {
      name: "Product View",
      value: data.product_view
    },

    {
      name: "Add To Cart",
      value: data.add_to_cart
    },

    {
      name: "Checkout",
      value: data.checkout
    },

    {
      name: "Purchase",
      value: data.purchase
    }
  ];

  // ------------------------------------------------
  // PERCENTAGES
  // ------------------------------------------------

  const firstStep =
    steps[0].value;

  const funnelData = steps.map(

    (step, index) => {

      const previous =
        index === 0

          ? firstStep

          : steps[index - 1].value;

      const retained = (

        (
          step.value / firstStep
        ) * 100

      ).toFixed(1);

      const dropoff = (

        (
          (
            previous - step.value
          )

          / previous
        ) * 100

      ).toFixed(1);

      return {

        ...step,

        retained:
          `${retained}%`,

        dropoff:
          index === 0

            ? "0%"

            : `${dropoff}%`
      };
    }
  );

  // ------------------------------------------------
  // FIND LARGEST DROPOFF
  // ------------------------------------------------

  let maxDrop = 0;

  let worstIndex = -1;

  for (
    let i = 1;
    i < funnelData.length;
    i++
  ) {

    const drop = parseFloat(
      funnelData[i].dropoff
    );

    if (drop > maxDrop) {

      maxDrop = drop;

      worstIndex = i;
    }
  }

  // ------------------------------------------------
  // COLORS
  // ------------------------------------------------

  const colors = [

    "#00ff99",
    "#00d68f",
    "#00b37a",
    "#008f66",
    "#00664d"
  ];

  return (

    <div
      style={{
        width: "100%",
        height: 520
      }}
    >

      <ResponsiveContainer>

        <FunnelChart>

          <Tooltip />

          <Funnel

            dataKey="value"

            data={funnelData}

            isAnimationActive
          >

            <LabelList

              position="right"

              fill="#ffffff"

              stroke="none"

              dataKey={(entry) =>

                `${entry.name}
                 (${entry.retained})`
              }
            />

            {
              funnelData.map(

                (entry, index) => (

                  <Cell

                    key={index}

                    fill={
                      index === worstIndex

                        ? "#ff003c"

                        : colors[index]
                    }
                  />
                )
              )
            }

          </Funnel>

        </FunnelChart>

      </ResponsiveContainer>

      {/* LEGEND */}

      <div className="funnel-legend">

        {
          funnelData.map(

            (step, index) => (

              <div
                key={index}
                className="legend-row"
              >

                <div
                  className="legend-color"
                  style={{

                    background:

                      index === worstIndex

                        ? "#ff003c"

                        : colors[index]
                  }}
                />

                <span>

                  {step.name}

                  {" — "}

                  {step.retained}

                  retained

                  {" | "}

                  Drop-off:

                  {" "}

                  {step.dropoff}

                </span>

              </div>
            )
          )
        }

      </div>

    </div>
  );
}