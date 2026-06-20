from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.mission import Mission
from models.user import User
from schemas.mission import MissionCalculateRequest, MissionCalculateResponse, MissionCreate, MissionResponse
from auth.dependencies import get_current_user
from services.calculator import calculate_distance, calculate_travel_time

router = APIRouter()

@router.post("/calculate", response_model=MissionCalculateResponse)
def calculate_mission(request: MissionCalculateRequest):
    distance = calculate_distance(request.source, request.destination)
    if distance == 0 and request.source != request.destination:
         raise HTTPException(status_code=400, detail="Invalid planet selected.")
         
    time_data = calculate_travel_time(distance, request.speed)
    
    return MissionCalculateResponse(
        source=request.source,
        destination=request.destination,
        speed=request.speed,
        distance=distance,
        travel_time_hours=time_data["hours"],
        travel_time_days=time_data["days"],
        travel_time_years=time_data["years"]
    )

@router.post("/save", response_model=MissionResponse)
def save_mission(mission_data: MissionCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_mission = Mission(
        user_id=current_user.id,
        source=mission_data.source,
        destination=mission_data.destination,
        speed=mission_data.speed,
        distance=mission_data.distance,
        travel_time_hours=mission_data.travel_time_hours,
        travel_time_days=mission_data.travel_time_days,
        travel_time_years=mission_data.travel_time_years
    )
    db.add(new_mission)
    db.commit()
    db.refresh(new_mission)
    return new_mission

@router.get("/history", response_model=List[MissionResponse])
def get_mission_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    missions = db.query(Mission).filter(Mission.user_id == current_user.id).order_by(Mission.created_at.desc()).all()
    return missions

@router.delete("/{mission_id}")
def delete_mission(mission_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == mission_id, Mission.user_id == current_user.id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    db.delete(mission)
    db.commit()
    return {"message": "Mission deleted successfully"}
