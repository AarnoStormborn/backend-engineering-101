from pydantic import BaseModel

class ProductOrder(BaseModel):
    id: int
    name: str
    quantity: int