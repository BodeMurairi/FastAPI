#!/usr/bin/env python3
from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Orders(BaseModel):
    """BaseModel for orders"""
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)

@app.post("/users/{user_id}/orders")
def create_order(
    user_id: int,
    status: str = Query("pending"),
    order: Orders = Body(...)
):
    """Create an order for a user."""
    return {
        "user_id": user_id,
        "status": status,
        "order": order.model_dump()
    }
