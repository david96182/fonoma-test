from pydantic import BaseModel, Field
from typing import List

class Order(BaseModel):
    id: int = Field(..., gt=0)
    item: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)
    status: str = Field(..., pattern="^(completed|canceled|pending)$")

class SolutionInput(BaseModel):
    orders: List[Order]
    criterion: str = Field(..., pattern="^(completed|canceled|pending|all)$")

