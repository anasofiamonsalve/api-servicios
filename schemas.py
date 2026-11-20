from pydantic import BaseModel, ConfigDict, Field


# Esquema para registrar un servicio
class ServicioCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: int = Field(gt=0)
    description: str = Field(min_length=3, max_length=200)


# Esquema para devolver un servicio
class ServicioResponse(BaseModel):
    id: int
    name: str
    price: int
    description: str

    model_config = ConfigDict(from_attributes=True)