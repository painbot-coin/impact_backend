from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer)
    email = Column(String, index=True)
    phone_number = Column(String,  index=True)
    name = Column(String)
    status = Column(String, default="none")
