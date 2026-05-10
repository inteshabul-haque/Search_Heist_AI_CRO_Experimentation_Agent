from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from api.ai_routes import router as ai_router

app = FastAPI(
    title="Search Heist AI",
    description="AI CRO Experimentation Agent",
    version="1.0"
)

# Enable frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(router)
app.include_router(ai_router)


@app.get("/")
def home():
    return {
        "message": "Search Heist AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }