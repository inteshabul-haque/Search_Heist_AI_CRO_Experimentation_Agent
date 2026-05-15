import React from "react";

import MiniTrendChart
from "../charts/MiniTrendChart";

export default function KPIAnalyticsCard({

  title,
  value,
  subtitle,
  trendData,
  color

}) {

  return (

    <div className="analytics-mini-card">

      <h4>{title}</h4>

      <h1
        style={{ color }}
      >
        {value}
      </h1>

      <p>{subtitle}</p>

      <MiniTrendChart
        data={trendData}
        color={color}
      />

    </div>
  );
}