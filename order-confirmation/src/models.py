from pydantic import BaseModel, ConfigDict

class OrderCreate(BaseModel):
    id: int
    name: str
    quantity: int
    
class OrderResponse(BaseModel):
    id: int
    name: str
    quantity: int
    status: str
    
    model_config = ConfigDict(from_attributes=True)