# app/models/group.py
from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    year = Column(String(4))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Enum("Created", "Active", "Finished", "Cancelled", name="group_statuses"))
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    modification_date = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationships
    students = relationship("Student", back_populates="group")