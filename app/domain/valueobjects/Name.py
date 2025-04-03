from pydantic import BaseModel


class Name(BaseModel):
    first_name: str
    last_name: str

