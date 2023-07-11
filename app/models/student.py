# app/models/student.py
from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    email = Column(String(150))
    status = Column(Enum("Registered", "Released", "Blocked", "Finished", name="student_statuses"))
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    modification_date = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationships
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")
