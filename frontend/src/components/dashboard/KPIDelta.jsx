import React from "react";

export default function KPIDelta({

  value

}) {

  const positive = value >= 0;

  return (

    <span

      style={{

        color:

          positive

            ? "#39ff88"

            : "#ff4f78",

        fontWeight: "bold"
      }}
    >

      {

        positive

          ? "▲"

          : "▼"
      }

      {" "}

      {Math.abs(value)}%

    </span>
  );
}