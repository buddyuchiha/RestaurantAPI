class UserNotFound(Exception):
    detail = "User does not exists"
    
    
class WrongPassword(Exception):
    detail = "Wrong password"