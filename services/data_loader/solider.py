from pydantic import BaseModel

class Solider(BaseModel):


        id: int
        first_name: str
        last_name: str
        phone_number: str
        rank: str
