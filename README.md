# SEARCH HEIST AI  
## AI CRO Experimentation & Funnel Intelligence Platform

SEARCH HEIST AI is an AI-powered CRO (Conversion Rate Optimization) analytics platform inspired by the Money Heist theme.

The platform analyzes:
- Funnel performance
- A/B testing experiments
- Conversion rates
- Funnel drop-offs
- Experiment variants
- CRO optimization opportunities

It also includes:
- Conversational AI analytics assistant
- Autonomous insights
- Tactical alerts
- Dynamic KPI engine
- Interactive visualizations
- Multi-dataset support

---

# FEATURES

## Funnel Analysis
Analyze:
- Visited users
- Product views
- Add to cart
- Checkout
- Purchases
- Conversion rates
- Funnel drop-offs

---

## A/B Testing Analysis
Analyze:
- Variant performance
- Conversion rate by variant
- Winning experiment
- Experiment insights
- Tactical recommendations

---

## AI CRO Assistant
Interactive AI chat system that:
- remembers latest uploaded dataset
- answers analytics questions
- provides CRO insights
- explains funnel performance
- summarizes experiment results

Example Questions:
- What is conversion rate?
- Any alerts?
- How many users?
- Which variant performed best?
- Give insights
- Revenue?
- Funnel issues?

---

## Dynamic KPI Engine
The platform NEVER hardcodes metrics.

If dataset does not contain:
- revenue
- order value
- sales

Then platform automatically shows:

N/A

instead of fake numbers.

---

# TECH STACK

## Frontend
- React.js
- Vite
- Axios
- Recharts

## Backend
- FastAPI
- Python
- Pandas

---

# PROJECT STRUCTURE

```bash
Search_Heist_AI_CRO_Experimentation_Agent/

│
├── backend/
│   ├── analytics/
│   ├── agents/
│   ├── api/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# INSTALLATION

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Search_Heist_AI_CRO_Experimentation_Agent.git
```

---

# BACKEND SETUP

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# FRONTEND SETUP

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# SUPPORTED DATASETS

## Funnel Dataset Columns

Required:

```text
visited
product_view
add_to_cart
checkout
purchase
```

Optional:

```text
revenue
```

---

## A/B Test Dataset Columns

Required:

```text
variant
converted
```

Optional:

```text
revenue
```

---

# AI MEMORY SYSTEM

The AI assistant stores the latest uploaded dataset in memory and answers questions contextually based on:
- latest funnel upload
- latest experiment upload

---

# FUTURE IMPROVEMENTS

- Real LLM integration (Gemini/OpenAI)
- Multi-file upload
- Statistical significance testing
- PDF export reports
- Authentication system
- SQL generation
- Real-time analytics
- Agent orchestration
- Voice assistant mode

---

# SCREENSHOTS

Add screenshots here after uploading project images.

Example:
- Funnel Dashboard
- A/B Testing Dashboard
- AI Chat
- Money Heist UI

---

# AUTHOR

Built by:
Inteshabul Haque

AI + CRO + Product Analytics Portfolio Project

# SAMPLE FILE FORMATS

---

## Funnel Dataset Example

CSV format:

```csv
visited,product_view,add_to_cart,checkout,purchase,revenue
1000,800,500,300,120,15000
900,700,450,250,100,12000
```

Required Columns:

```text
visited
product_view
add_to_cart
checkout
purchase
```

Optional Columns:

```text
revenue
```

---

## A/B Testing Dataset Example

CSV format:

```csv
variant,converted,revenue
A,1,120
A,0,0
B,1,180
B,1,200
B,0,0
```

Required Columns:

```text
variant
converted
```

Optional Columns:

```text
revenue
```

---

# IMPORTANT

If optional columns like revenue are missing, the platform automatically shows:

```text
N/A
```

instead of generating fake or hardcoded values.