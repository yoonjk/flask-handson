from pydantic import BaseModel


class Item(BaseModel):
  id: int
  item : str
  