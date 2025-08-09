#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id:int = Path(..., gt=0)):
    """Retrieve an item by its ID."""
    return {"item_id":item_id, "name": f"Item {item_id}"}

if __name__ == "__main__":
    uvicorn.run("path_params:app", reload=True)
