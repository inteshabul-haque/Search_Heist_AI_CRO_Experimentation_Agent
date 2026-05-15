import React from "react";

import {

  ResponsiveContainer,

  ScatterChart,
  Scatter,

  XAxis,
  YAxis,

  Tooltip,

  CartesianGrid

} from "recharts";

export default function ConfidenceIntervalChart({

  variantSummary

}) {

  if (!variantSummary) return null;

  const chartData = Object.entries(
    variantSummary
  ).map(

    ([variant, data]) => ({

      variant,

      conversion_rate:
        data.conversion_rate,

      lower:
        data.confidence_interval?.[0],

      upper:
        data.confidence_interval?.[1]
    })
  );

  return (

    <div
      style={{
        width: "100%",
        height: 400
      }}
    >

      <ResponsiveContainer>

        <ScatterChart>

          <CartesianGrid
            stroke="#222"
          />

          <XAxis
            dataKey="variant"
            type="category"
          />

          <YAxis
            dataKey="conversion_rate"
            type="number"
          />

          <Tooltip />

          <Scatter
            data={chartData}
            fill="#39ff88"
          />

        </ScatterChart>

      </ResponsiveContainer>

    </div>
  );
}