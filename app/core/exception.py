class UserNotFound(Exception):
    detail = "User does not exists"
    
    
class WrongPassword(Exception):
    detail = "Wrong password"
    
    
class TokenExpired(Exception):
    detail = "Token expired"
    

class TokenNotCorrect(Exception):
    detail = "Token not correct"