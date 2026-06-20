from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models.user import User
from models.mission import Mission
from auth.dependencies import get_current_user

router = APIRouter()

@router.get("/")
def get_dashboard_stats(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    total_missions = db.query(Mission).filter(Mission.user_id == current_user.id).count()
    total_distance = db.query(func.sum(Mission.distance)).filter(Mission.user_id == current_user.id).scalar() or 0
    
    # Calculate favorite destination
    favorite_dest_row = (
        db.query(Mission.destination, func.count(Mission.destination).label('dest_count'))
        .filter(Mission.user_id == current_user.id)
        .group_by(Mission.destination)
        .order_by(func.count(Mission.destination).desc())
        .first()
    )
    favorite_destination = favorite_dest_row.destination if favorite_dest_row else "None"

    return {
        "username": current_user.username,
        "total_missions": total_missions,
        "total_distance_km": total_distance,
        "favorite_destination": favorite_destination
    }
