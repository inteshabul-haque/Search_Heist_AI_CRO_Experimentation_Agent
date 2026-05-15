import React from "react";

import ReactMarkdown from "react-markdown";

import { useState } from "react";

import axios from "axios";

import "./index.css";

// ----------------------------------------------------
// DASHBOARD COMPONENTS
// ----------------------------------------------------

import ExecutiveKPIs
from "./components/dashboard/ExecutiveKPIs";

import KPIAnalyticsCard
from "./components/dashboard/KPIAnalyticsCard";

import ExperimentSummaryPanel
from "./components/dashboard/ExperimentSummaryPanel";

import SegmentComparisonCard
from "./components/dashboard/SegmentComparisonCard";

// ----------------------------------------------------
// CHARTS
// ----------------------------------------------------

import FunnelDropoffChart
from "./components/charts/FunnelDropoffChart";

import VariantPerformanceChart
from "./components/charts/VariantPerformanceChart";

import ConfidenceIntervalChart
from "./components/charts/ConfidenceIntervalChart";

// ----------------------------------------------------
// INSIGHTS
// ----------------------------------------------------

import AIInsightFeed
from "./components/insights/AIInsightFeed";

import ExecutiveRecommendation
from "./components/insights/ExecutiveRecommendation";

import AITimeline
from "./components/insights/AITimeline";

// ----------------------------------------------------
// ENV
// ----------------------------------------------------

const API_URL = import.meta.env.VITE_API_URL;

export default function App() {

  // ----------------------------------------------------
  // STATE
  // ----------------------------------------------------

  const [file, setFile] = useState(null);

  const [loading, setLoading] =
    useState(false);

  const [results, setResults] =
    useState(null);

  const [question, setQuestion] =
    useState("");

  const [analysisType, setAnalysisType] =
    useState("experiment");

  const [chatHistory, setChatHistory] =
    useState([]);

  // ----------------------------------------------------
  // LOAD DEMO DATA
  // ----------------------------------------------------

  const loadDemoData = async () => {

    try {

      const demoFile =

        analysisType === "funnel"

          ? "/demo/funnel_data.csv"

          : "/demo/ab_test_data.csv";

      const response = await fetch(
        demoFile
      );

      const blob = await response.blob();

      const demoLoadedFile = new File(

        [blob],

        analysisType === "funnel"

          ? "funnel_data.csv"

          : "ab_test_data.csv",

        {
          type: "text/csv"
        }
      );

      setFile(demoLoadedFile);

      alert(
        "Demo dataset loaded successfully!"
      );

    } catch (error) {

      console.error(error);

      alert(
        "Failed to load demo data."
      );
    }
  };

  // ----------------------------------------------------
  // ANALYZE DATASET
  // ----------------------------------------------------

  const handleAnalyze = async () => {

    if (!file) {

      alert(
        "Upload dataset first."
      );

      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    const endpoint =

      analysisType === "funnel"

        ? `${API_URL}/upload-funnel`

        : `${API_URL}/upload-experiment`;

    try {

      setLoading(true);

      const response = await axios.post(
        endpoint,
        formData
      );

      setResults(response.data);

      setChatHistory([]);

    } catch (error) {

      console.error(error);

      alert("Analysis failed.");

    } finally {

      setLoading(false);
    }
  };

  // ----------------------------------------------------
  // ASK AI
  // ----------------------------------------------------

  const handleAskAI = async () => {

    if (!question) return;

    try {

      const updatedHistory = [

        ...chatHistory,

        {
          role: "user",
          text: question
        }
      ];

      setChatHistory(updatedHistory);

      const response = await axios.post(

        `${API_URL}/ask-ai`,

        {
          question
        }
      );

      setChatHistory([

        ...updatedHistory,

        {
          role: "ai",
          text: response.data.answer
        }
      ]);

      setQuestion("");

    } catch (error) {

      console.error(error);
    }
  };

  // ----------------------------------------------------
  // CHART DATA
  // ----------------------------------------------------

  const experimentChart =
    results?.chart_data?.experiment_chart;

  const chartData = experimentChart

    ? experimentChart.labels.map(
        (label, index) => ({

          variant: label,

          conversion_rate:
            experimentChart.values[index]
        })
      )

    : [];

  // ----------------------------------------------------
  // UI
  // ----------------------------------------------------

  return (

    <div className="app-container">

      {/* HEADER */}

      <div className="header">

        <div>

          <h1 className="main-title">
            SEARCH HEIST AI
          </h1>

          <p className="sub-title">
            Tactical CRO Intelligence Platform
          </p>

        </div>

        <div className="status-box">
          PROFESSOR ONLINE
        </div>

      </div>

      {/* UPLOAD */}

      <Panel title="UPLOAD DATASET">

        <select

          value={analysisType}

          onChange={(e) =>
            setAnalysisType(e.target.value)
          }

          className="dropdown"
        >

          <option value="experiment">
            A/B Test Analysis
          </option>

          <option value="funnel">
            Funnel Analysis
          </option>

        </select>

        <br />
        <br />

        <input

          type="file"

          accept=".csv"

          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        {
          file && (

            <p className="selected-file">

              ACTIVE FILE:
              {" "}
              {file.name}

            </p>
          )
        }

        <br />
        <br />

        <button

          className="demo-btn"

          onClick={loadDemoData}
        >

          LOAD DEMO DATA

        </button>

        <button

          className="main-button"

          onClick={handleAnalyze}
        >

          {
            loading

              ? "PROFESSOR ANALYZING..."

              : "START ANALYSIS"
          }

        </button>

      </Panel>

      {/* EXECUTIVE KPIs */}

      {
        results?.kpis && (

          <ExecutiveKPIs
            kpis={results.kpis}
          />

        )
      }

      {/* MINI KPI GRID */}

      {
        results?.kpis && (

          <div className="analytics-mini-grid">

            <KPIAnalyticsCard

              title="UPLIFT"

              value={`${results?.kpis?.uplift || 0}%`}

              subtitle="Variant uplift"

              color="#39ff88"

              trendData={[

                { value: 10 },
                { value: 18 },
                { value: 25 },
                { value: 33 },
                { value: 45 }
              ]}
            />

            <KPIAnalyticsCard

              title="P-VALUE"

              value={
                results?.kpis?.p_value || 0
              }

              subtitle="Statistical confidence"

              color="#ffd000"

              trendData={[

                { value: 0.4 },
                { value: 0.3 },
                { value: 0.2 },
                { value: 0.1 },
                { value: 0.05 }
              ]}
            />

            <KPIAnalyticsCard

              title="TOTAL USERS"

              value={
                results?.kpis?.total_users || 0
              }

              subtitle="Experiment traffic"

              color="#ffffff"

              trendData={[

                { value: 300 },
                { value: 500 },
                { value: 800 },
                { value: 1200 },
                { value: 1700 }
              ]}
            />

          </div>
        )
      }

      {/* ALERTS */}

      {
        results?.alerts && (

          <Panel title="TACTICAL ALERTS">

            {

              results.alerts.map(

                (alert, index) => (

                  <div

                    key={index}

                    className={`alert-card ${alert.severity}`}
                  >

                    <strong>
                      {alert.severity.toUpperCase()}
                    </strong>

                    <p>
                      {alert.message}
                    </p>

                  </div>
                )
              )
            }

          </Panel>
        )
      }

      {/* SUMMARY */}

      {
        results?.statistical_test && (

          <ExperimentSummaryPanel

            winner={
              results.winning_variant
            }

            uplift={
              results.kpis?.uplift
            }

            pValue={
              results.kpis?.p_value
            }

            significant={
              results.statistical_test?.significant
            }

          />
        )
      }

      {/* RECOMMENDATION */}

      {
        results?.statistical_test && (

          <ExecutiveRecommendation

            uplift={
              results.kpis?.uplift
            }

            significant={
              results.statistical_test?.significant
            }

          />
        )
      }

      {/* CHART GRID */}

      <div className="chart-grid">

        {
          chartData.length > 0 && (

            <Panel title="VARIANT PERFORMANCE">

              <VariantPerformanceChart
                data={chartData}
              />

            </Panel>
          )
        }

        {
          results?.variant_summary && (

            <Panel title="CONFIDENCE INTERVALS">

              <ConfidenceIntervalChart

                variantSummary={
                  results.variant_summary
                }

              />

            </Panel>
          )
        }

      </div>

      {/* FUNNEL */}

      {
        results?.funnel_data && (

          <Panel title="FUNNEL PERFORMANCE">

            <FunnelDropoffChart
              data={results.funnel_data}
            />

          </Panel>
        )
      }

      {/* DEVICE SEGMENTS */}

      {
        results?.device_segments && (

          <SegmentComparisonCard

            title="DEVICE SEGMENTS"

            segments={
              results.device_segments
            }

          />
        )
      }

      {/* AI INSIGHTS */}

      {
        results?.autonomous_insights && (

          <Panel title="AI CRO INSIGHTS">

            <AIInsightFeed

              insights={
                results.autonomous_insights
              }

            />

          </Panel>
        )
      }

      {/* AI TIMELINE */}

      {
        results?.execution_trace && (

          <Panel title="AI EXECUTION TRACE">

            <AITimeline

              executionTrace={
                results.execution_trace
              }

            />

          </Panel>
        )
      }

      {/* ASK PROFESSOR */}

      <Panel title="ASK THE PROFESSOR">

        <input

          className="chat-input"

          type="text"

          placeholder="Ask tactical CRO question..."

          value={question}

          onChange={(e) =>
            setQuestion(e.target.value)
          }
        />

        <button

          className="main-button"

          onClick={handleAskAI}
        >

          ASK AI

        </button>

        <div className="chat-container">

          {

            chatHistory.map(

              (chat, index) => (

                <div

                  key={index}

                  className={

                    chat.role === "user"

                      ? "user-message"

                      : "ai-message"
                  }
                >

                  <strong>

                    {
                      chat.role === "user"

                        ? "YOU"

                        : "PROFESSOR"
                    }

                  </strong>

                  <div className="markdown-response">

                    <ReactMarkdown>

                      {
                        Array.isArray(chat.text)

                          ? chat.text.join("\n\n")

                          : String(chat.text || "")
                      }

                    </ReactMarkdown>

                  </div>

                </div>
              )
            )
          }

        </div>

      </Panel>

    </div>
  );
}

// ----------------------------------------------------
// PANEL
// ----------------------------------------------------

function Panel({

  title,
  children

}) {

  return (

    <div className="panel">

      <h2 className="panel-title">
        {title}
      </h2>

      {children}

    </div>
  );
}