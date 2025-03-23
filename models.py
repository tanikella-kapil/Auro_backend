from sqlalchemy import Column, Integer, String, LargeBinary, Text
from database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    content = Column(Text)
    embedding = Column(LargeBinary)  # Store embeddings as binary data

class UserQuery(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    response = Column(Text)
