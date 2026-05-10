import React from "react";

import { useState } from "react";

import axios from "axios";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

import "./index.css";

export default function App() {

  // -----------------------------
  // STATES
  // -----------------------------

  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [results, setResults] = useState(null);

  const [question, setQuestion] = useState("");

  const [analysisType, setAnalysisType] =
    useState("experiment");

  // Chat history
  const [chatHistory, setChatHistory] =
    useState([]);

  // -----------------------------
  // ANALYZE DATASET
  // -----------------------------

  const handleAnalyze = async () => {

    if (!file) {

      alert("Upload CSV dataset first.");

      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    // Dynamic endpoint
    const endpoint =

      analysisType === "funnel"

        ? "https://search-heist-ai-backend.onrender.com/upload-funnel"

        : "https://search-heist-ai-backend.onrender.com/upload-experiment";

    try {

      setLoading(true);

      const response = await axios.post(
        endpoint,
        formData
      );

      // Error validation
      if (response.data.error) {

        alert(response.data.message);

        return;
      }

      setResults(response.data);

      // Reset old chat after new upload
      setChatHistory([]);

    } catch (error) {

      console.error(error);

      alert("Analysis failed.");

    } finally {

      setLoading(false);
    }
  };

  // -----------------------------
  // ASK AI
  // -----------------------------

  const handleAskAI = async () => {

    if (!question) return;

    try {

      // Add user message
      const updatedHistory = [

        ...chatHistory,

        {
          role: "user",
          text: question
        }
      ];

      setChatHistory(updatedHistory);

      // API call
      const response = await axios.post(

        "https://search-heist-ai-backend.onrender.com/ask-ai",

        {
          question
        }
      );

      // Add AI response
      setChatHistory([

        ...updatedHistory,

        {
          role: "ai",
          text: response.data.answer
        }
      ]);

      // Clear input
      setQuestion("");

    } catch (error) {

      console.error(error);

      setChatHistory([

        ...chatHistory,

        {
          role: "ai",
          text: "AI system failure."
        }
      ]);
    }
  };

  // -----------------------------
  // CHART DATA
  // -----------------------------

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

  // -----------------------------
  // UI
  // -----------------------------

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

      {/* UPLOAD PANEL */}
      <Panel title="UPLOAD DATASET">

        {/* SELECT ANALYSIS TYPE */}
        <select

          value={analysisType}

          onChange={(e) =>
            setAnalysisType(e.target.value)
          }

          style={{
            marginBottom: "20px",
            padding: "12px",
            background: "#090909",
            color: "white",
            border: "1px solid #ff003c",
            borderRadius: "10px"
          }}
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

        {/* FILE INPUT */}
        <input

          type="file"

          accept=".csv"

          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        <br />
        <br />

        {/* ANALYZE BUTTON */}
        <button

          className="main-button"

          onClick={handleAnalyze}
        >

          {
            loading

              ? "PROFESSOR IS ANALYZING..."

              : "START ANALYSIS"
          }

        </button>

      </Panel>

      {/* KPI CARDS */}
      {results?.kpis && (

        <div className="kpi-grid">

          <KPI
            title="CONVERSION RATE"
            value={`${results.kpis.conversion_rate}`}
          />

          <KPI
            title="TOTAL REVENUE"
            value={`${results.kpis.total_revenue}`}
          />

          <KPI
            title="AVG ORDER VALUE"
            value={`${results.kpis.avg_order_value}`}
          />

          <KPI
            title="TOTAL USERS"
            value={`${results.kpis.total_users}`}
          />

        </div>
      )}

      {/* ALERTS */}
      {results?.alerts && (

        <Panel title="TACTICAL ALERTS">

          {results.alerts.map(

            (alert, index) => (

              <div
                key={index}
                className="alert-card"
              >

                <strong>
                  {alert.severity.toUpperCase()}
                </strong>

                <p>
                  {alert.message}
                </p>

              </div>
            )
          )}

        </Panel>
      )}

      {/* CHART */}
      {chartData.length > 0 && (

        <Panel title="ANALYTICS PERFORMANCE">

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <BarChart data={chartData}>

              <CartesianGrid stroke="#222" />

              <XAxis dataKey="variant" />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="conversion_rate"
                fill="#ff003c"
              />

            </BarChart>

          </ResponsiveContainer>

        </Panel>
      )}

      {/* INSIGHTS */}
      {results?.autonomous_insights && (

        <Panel title="AUTONOMOUS INSIGHTS">

          {results.autonomous_insights.map(

            (insight, index) => (

              <div
                key={index}
                className="insight-card"
              >

                {insight}

              </div>
            )
          )}

        </Panel>
      )}

      {/* EXECUTION TRACE */}
      {results?.execution_trace && (

        <Panel title="PROFESSOR THINKING TRACE">

          {results.execution_trace.map(

            (step, index) => (

              <div
                key={index}
                className="trace-card"
              >

                <strong>
                  {step.agent}
                </strong>

                <p>
                  {step.action}
                </p>

              </div>
            )
          )}

        </Panel>
      )}

      {/* AI CHAT */}
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

        {/* CHAT HISTORY */}
        <div className="chat-container">

          {chatHistory.map(

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

                <p>
                  {chat.text}
                </p>

              </div>
            )
          )}

        </div>

      </Panel>

    </div>
  );
}

// -----------------------------
// PANEL COMPONENT
// -----------------------------

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

// -----------------------------
// KPI COMPONENT
// -----------------------------

function KPI({

  title,
  value

}) {

  return (

    <div className="kpi-card">

      <p>{title}</p>

      <h1>{value}</h1>

    </div>
  );
}