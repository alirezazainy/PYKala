from pydantic import BaseModel


class Users(BaseModel):
    userName : str 
    _passWord : str
    logged_in : bool
    trace : int
    

