import React from "react";

export default function SegmentComparisonCard({

  title,
  segments

}) {

  return (

    <div className="segment-card">

      <h2>{title}</h2>

      {

        segments.map(

          (segment, index) => (

            <div
              key={index}
              className="segment-row"
            >

              <span>
                {segment.label}
              </span>

              <strong>
                {segment.value}
              </strong>

            </div>
          )
        )
      }

    </div>
  );
}