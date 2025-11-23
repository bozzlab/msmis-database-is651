from fastapi import Security, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.utils import encode_util

bearer_scheme = HTTPBearer()


def get_access_token(
    credentials: HTTPAuthorizationCredentials = Security(bearer_scheme),
) -> int:
    encoded_token = credentials.credentials

    try:
        decoded_token = encode_util.decode_base64(encoded_token)
        user_id = int(decoded_token)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or undecodable token",
        ) from e

    return user_id
