from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

from . import crud, models
from .database import SessionLocal, engine

from . import schemas

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/{kind}/", status_code=201)
async def create_object(request: Request, app: schemas.Application, db: Session = Depends(get_db)):
    data = await request.json()
    return crud.create_object(db=db, object=app, json_data=data)


@app.get("/{kind}/{uuid}", status_code=200)
async def get_object(uuid: str, db: Session = Depends(get_db)):
    db_object = crud.get_object_by_uuid(db=db, uuid=uuid)

    if not db_object:
        raise HTTPException(status_code=404, detail=f"Object with uuid {uuid} does not exist")
    return db_object


@app.get("/{kind}/{uuid}/state", status_code=200)
async def get_object_state(uuid: str, db: Session = Depends(get_db)):
    db_object = crud.get_object_by_uuid(db=db, uuid=uuid)

    if not db_object:
        raise HTTPException(status_code=404, detail=f"Object with uuid {uuid} does not exist")
    return {"state": db_object.state}


@app.put("/{kind}/{uuid}/state", status_code=200)
async def put_state(request: Request, uuid: str, db: Session = Depends(get_db)):
    try:
        data = await request.json()
    except:
        raise HTTPException(status_code=400, detail=f"JSON was not sent or the request body is incorrect")
    
    state = data.get('state', None)
    if state is None:
        raise HTTPException(status_code=422, detail=f"The required parameter \"state\" was not passed in the request body")
    
    db_object = crud.get_object_by_uuid(db=db, uuid=uuid)
    if not db_object:
        raise HTTPException(status_code=404, detail=f"Object with uuid {uuid} does not exist")
    return crud.update_object_state(db=db, uuid=uuid, state=state)


@app.delete("/{kind}/{uuid}/", status_code=204)
async def delete_object(uuid: str, db: Session = Depends(get_db)):
    db_object = crud.get_object_by_uuid(db=db, uuid=uuid)
    if not db_object:
        raise HTTPException(status_code=404, detail=f"Object with uuid {uuid} does not exist")
    return crud.delete_object(db=db, uuid=uuid)


@app.put("/{kind}/{uuid}/configuration/", status_code=200)
async def put_configuration(config: schemas.Configuration, uuid: str, db: Session = Depends(get_db)):    
    db_object = crud.get_object_by_uuid(db=db, uuid=uuid)
    if not db_object:
        raise HTTPException(status_code=404, detail=f"Object with uuid {uuid} does not exist")
    return crud.update_object_config(db=db, uuid=uuid, config=config)


@app.put("/{kind}/{uuid}/settings/", status_code=200)
async def put_settings(config: schemas.Configuration, uuid: str, db: Session = Depends(get_db)):
    db_object = crud.get_object_by_uuid(db=db, uuid=uuid)
    if not db_object:
        raise HTTPException(status_code=404, detail=f"Object with uuid {uuid} does not exist")
    return crud.update_object_settings(db=db, uuid=uuid, config=config)