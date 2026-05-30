from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

# ← new simple schema, no blogs inside
class UserInBlog(BaseModel):
    name: str
    email: str
    class Config():
        from_attributes = True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        from_attributes = True

# ← uses UserInBlog instead of ShowUser
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: UserInBlog    # ← no blogs inside this, recursion broken!
    class Config():
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None