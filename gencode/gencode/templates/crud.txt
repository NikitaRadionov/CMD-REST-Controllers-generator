from sqlalchemy.orm import Session

from . import models

from . import schemas


def get_object_by_uuid(db: Session, uuid: str):
    return db.query(models.App).filter(models.App.id == uuid).first()


def create_object(db: Session, object: schemas.Application, json_data:dict):
    app_data = object.model_dump()
    app_data.pop('configuration', None)
    app_data['json'] = json_data

    db_object = models.App(**app_data)
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object


def update_object_state(db: Session, uuid: str, state: str):
    db_object = get_object_by_uuid(db, uuid)
    db_object.state = state

    db.commit()
    db.refresh(db_object)
    return db_object


def delete_object(db: Session, uuid: str):
    db_object = get_object_by_uuid(db, uuid)
    db.delete(db_object)
    db.commit()


def update_object_config(db: Session, uuid: str, config: schemas.Configuration):
    db_object = get_object_by_uuid(db, uuid)
    db_object.json = config.model_dump()

    db.commit()
    db.refresh(db_object)
    return db_object


def update_object_settings(db: Session, uuid: str, config: schemas.Configuration):
    db_object = get_object_by_uuid(db, uuid)
    db_object.json["settings"] = config.model_dump().get("settings")

    db.commit()
    db.refresh(db_object)
    return db_object
