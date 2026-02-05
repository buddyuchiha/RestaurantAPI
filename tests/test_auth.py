import pytest

from app.services.auth_service import AuthService

@pytest.fixture
def auth_service():
    return AuthService(user_service=None)

def test_encode_decode_token(auth_service):
    test_user_id = 42
    
    token = auth_service.generate_access_token(test_user_id)
    assert isinstance(token, str)
    assert len(token) > 0
    
    decoded_id = auth_service.get_user_id_from_access_token(token)
    
    assert decoded_id == test_user_id

def test_token_expired_logic(auth_service):
    invalid_token = "some.garbage.payload"
    
    with pytest.raises(Exception):
        auth_service.get_user_id_from_access_token(invalid_token)