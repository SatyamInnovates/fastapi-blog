from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto",bcrypt__truncate_error=False) 

class Hash():
    def bcrypt(password: str):
        password = password[:72]  
        return pwd_cxt.hash(password)

    def verify(plain_password, hashed_password):
        plain_password = plain_password[:72]
        return pwd_cxt.verify(plain_password, hashed_password)