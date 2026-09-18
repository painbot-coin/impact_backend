from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    campaign_name = Column(String)
    salesperson_name = Column(String)
    salesperson_role = Column(String)
    company_name = Column(String)
    company_business = Column(String)
    company_values = Column(String)
    conversation_purpose = Column(String)
    conversation_type=Column(String)
    use_custom_prompt = Column(String)
    custom_prompt = Column(String)
    twilio_sid = Column(String)
    twilio_token = Column(String)
    twilio_number = Column(String)
    voice_id = Column(String)
