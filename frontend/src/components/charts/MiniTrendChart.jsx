import React from "react";

import {

  LineChart,
  Line,
  ResponsiveContainer

} from "recharts";

export default function MiniTrendChart({

  data,
  color = "#39ff88"

}) {

  return (

    <ResponsiveContainer
      width="100%"
      height={70}
    >

      <LineChart data={data}>

        <Line

          type="monotone"

          dataKey="value"

          stroke={color}

          strokeWidth={3}

          dot={false}
        />

      </LineChart>

    </ResponsiveContainer>
  );
}