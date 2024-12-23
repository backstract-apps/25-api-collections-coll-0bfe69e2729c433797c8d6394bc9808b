from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_b_user(db: Session):


    b_user_all = db.query(models.B_user).all()
    res = {
        'b_user_all': b_user_all,
    }
    return res

async def get_b_user_id(db: Session, id: int):


    b_user_one = db.query(models.B_user).filter(models.B_user.id == id).first()
    res = {
        'b_user_one': b_user_one,
    }
    return res

async def post_b_user(db: Session, id: int, user_name: str, age: str):


    record_to_be_added = {'id': id, 'user_name': user_name}
    new_b_user = models.B_user(**record_to_be_added)
    db.add(new_b_user)
    db.commit()
    db.refresh(new_b_user)
    b_user_inserted_record = new_b_user
    res = {
        'b_user_inserted_record': b_user_inserted_record,
    }
    return res

async def put_b_user_id(db: Session, id: str, user_name: str):


    b_user_edited_record = db.query(models.B_user).filter(models.B_user.id == id).first()
    for key, value in {'id': id, 'user_name': user_name}.items():
          setattr(b_user_edited_record, key, value)
    db.commit()
    db.refresh(b_user_edited_record)
    b_user_edited_record = b_user_edited_record

    res = {
        'b_user_edited_record': b_user_edited_record,
    }
    return res

async def delete_b_user_id(db: Session, id: int):


    b_user_deleted = None
    record_to_delete = db.query(models.B_user).filter(models.B_user.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          b_user_deleted = record_to_delete
    res = {
        'b_user_deleted': b_user_deleted,
    }
    return res

