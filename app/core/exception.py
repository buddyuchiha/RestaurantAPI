class UserNotFound(Exception):
    detail = "User does not exists"
    
    
class WrongPassword(Exception):
    detail = "Wrong password"
    
    
class TokenExpired(Exception):
    detail = "Token expired"
    

class TokenNotCorrect(Exception):
    detail = "Token not correct"
    
    
class UserExists(Exception):
    detail = "User already exists"
    
    
class TableNotFound(Exception):
    detail = "Table not found"