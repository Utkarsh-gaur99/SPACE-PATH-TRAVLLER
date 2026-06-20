from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import engine, Base
from routes import auth, missions, planets, dashboard
import os

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AstroPath API", version="1.0.0")

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(missions.router, prefix="/mission", tags=["Missions"])
app.include_router(planets.router, prefix="/planets", tags=["Planets"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

# Mount frontend files (creates static endpoint)
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
