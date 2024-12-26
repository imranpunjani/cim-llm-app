# backend/models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Float

Base = declarative_base()

class CIM(Base):
    __tablename__ = "cims"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    full_text = Column(Text)  # store entire PDF text if needed

class CIMExtractedData(Base):
    __tablename__ = "cim_extracted_data"

    id = Column(Integer, primary_key=True, index=True)
    cim_id = Column(Integer)  # foreign key to cims.id if desired
    revenue = Column(Float, nullable=True)
    ebitda = Column(Float, nullable=True)
    purchase_multiple = Column(Float, nullable=True)
    owner_name = Column(String, nullable=True)
    location = Column(String, nullable=True)