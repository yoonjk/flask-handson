from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI() 

tax = {"tax": 0}

class Item(BaseModel):
  name: str 
  description: str | None = None 
  price : float 
  tax: float | None = None 
  
@app.post("/items")
async def create_item(item: Item):
  item_dict = item.dict()
 
    
  if item.tax:
    price_with_tax = tax['tax'] + item.price + item.tax 
    tax['tax'] = price_with_tax
    item_dict.update({"price_with_tax": price_with_tax})
    
  return item_dict 


@app.put("/items/{item-id}")
async def create_item_with_put(item_id : int , item: Item, q : str | None = None):
  result =  {"item_id": item_id , **item.dict()}
  
  if q:
    result.update({"q": q})
    
  return result