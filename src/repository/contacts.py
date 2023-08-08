from typing import List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session


from src.database.models import Contact
from src.schemas import ContactModel


async def seven_days(db: Session) -> List[Contact]:
    today = datetime.today()
    cur_year = today.year
    week_after = today + timedelta(days=7)
    contacts = db.query(Contact).all()
    result = []
    for contact in contacts:
        if today < contact.birthday.replace(year=cur_year) <= week_after:
            result.append(contact)
    return result


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def find_contact(item: str, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.name == item | Contact.email == item | Contact.last_name == item).one_or_none()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(name=body.name, last_name=body.last_name, phone=body.phone, email=body.email, birthday=body.birthday,
                      description=body.description)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = body.name
        contact.last_name = body.last_name
        contact.phone = body.phone
        contact.email = body.email
        contact.birthday = body.birthday
        contact.description = body.description

        db.commit()
    return contact

