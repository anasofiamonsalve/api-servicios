from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Servicio
from schemas import ServicioCreate, ServicioResponse

# Crear la tabla en Neon si todavía no existe
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Services API")


# ====================================
# GET: Consultar todos los servicios
# ====================================
@app.get("/servicios", response_model=list[ServicioResponse])
def get_servicios(db: Session = Depends(get_db)):
    servicios = db.query(Servicio).all()
    return servicios


# ====================================
# GET: Consultar un servicio por id
# ====================================
@app.get("/servicios/{servicio_id}", response_model=ServicioResponse)
def get_servicio(
    servicio_id: int,
    db: Session = Depends(get_db)
):
    servicio = db.query(Servicio).filter(
        Servicio.id == servicio_id
    ).first()

    if servicio is None:
        raise HTTPException(
            status_code=404,
            detail="Servicio no encontrado"
        )

    return servicio


# ====================================
# POST: Registrar un servicio
# ====================================
@app.post("/servicios", response_model=ServicioResponse, status_code=201)
def create_servicio(
    data: ServicioCreate,
    db: Session = Depends(get_db)
):
    servicio = Servicio(
        name=data.name,
        price=data.price,
        description=data.description
    )

    db.add(servicio)
    db.commit()
    db.refresh(servicio)

    return servicio