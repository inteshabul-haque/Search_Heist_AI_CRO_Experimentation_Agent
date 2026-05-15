import React from "react";

import CountUp from "react-countup";

import {
  TrendingUp,
  DollarSign,
  Users,
  Target
} from "lucide-react";

const cardConfig = [

  {
    key: "conversion_rate",
    label: "Conversion Rate",
    icon: TrendingUp,
    suffix: "%"
  },

  {
    key: "total_revenue",
    label: "Revenue",
    icon: DollarSign,
    prefix: "$"
  },

  {
    key: "total_users",
    label: "Users",
    icon: Users
  },

  {
    key: "avg_order_value",
    label: "Avg Order Value",
    icon: Target,
    prefix: "$"
  }
];

export default function ExecutiveKPIs({
  kpis
}) {

  return (

    <div className="executive-grid">

      {cardConfig.map((card) => {

        const Icon = card.icon;

        const rawValue =
          kpis?.[card.key] || 0;

        const numericValue = Number(

          String(rawValue)

            .replace("%", "")
            .replace("$", "")
        );

        return (

          <div
            key={card.key}
            className="executive-card"
          >

            <div className="executive-top">

              <p>{card.label}</p>

              <Icon size={20} />

            </div>

            <h1>

              {card.prefix}

              <CountUp
                end={
                  isNaN(numericValue)
                    ? 0
                    : numericValue
                }
                duration={2}
                decimals={2}
              />

              {card.suffix}

            </h1>

          </div>
        );
      })}
    </div>
  );
}