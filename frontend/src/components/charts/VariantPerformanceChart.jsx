import React from "react";

import {

  ResponsiveContainer,

  BarChart,
  Bar,

  XAxis,
  YAxis,

  Tooltip,

  CartesianGrid

} from "recharts";

export default function VariantPerformanceChart({
  data
}) {

  return (

    <ResponsiveContainer
      width="100%"
      height={400}
    >

      <BarChart data={data}>

        <CartesianGrid stroke="#222" />

        <XAxis dataKey="variant" />

        <YAxis />

        <Tooltip />

        <Bar
          dataKey="conversion_rate"
          fill="#ff003c"
          radius={[10, 10, 0, 0]}
        />

      </BarChart>

    </ResponsiveContainer>
  );
}