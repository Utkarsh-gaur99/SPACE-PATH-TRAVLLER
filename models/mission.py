from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from database import Base

class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    source = Column(String, index=True)
    destination = Column(String, index=True)
    speed = Column(Float)
    distance = Column(Float)
    travel_time_hours = Column(Float)
    travel_time_days = Column(Float)
    travel_time_years = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="missions")
