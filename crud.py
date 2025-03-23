from sqlalchemy.orm import Session
from models import Document, UserQuery
def add_document(db: Session, filename: str, content: str):
    doc = Document(filename=filename, content=content)  # Ensure no extra fields
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc



def get_documents(db: Session):
    return db.query(Document).all()

def add_query(db: Session, question: str, response: str):
    query = UserQuery(question=question, response=response)
    db.add(query)
    db.commit()
    return query
