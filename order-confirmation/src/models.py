from pydantic import BaseModel

class OrderCreate(BaseModel):
    id: int
    name: str
    quantity: int