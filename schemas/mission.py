from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MissionCalculateRequest(BaseModel):
    source: str
    destination: str
    speed: float

class MissionCalculateResponse(BaseModel):
    source: str
    destination: str
    speed: float
    distance: float
    travel_time_hours: float
    travel_time_days: float
    travel_time_years: float

class MissionCreate(MissionCalculateResponse):
    pass

class MissionResponse(MissionCalculateResponse):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
