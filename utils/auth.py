import os
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import jwt
from jwt.exceptions import PyJWTError

# TODO: Retrieve secret key securely, e.g., from environment variables or a secrets manager
SECRET_KEY: str = os.getenv("JWT_SECRET", "replace-with-a-secure-secret")
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


def create_jwt(user_id: str) -> str:
    """
    Generates a JWT with user claims.
    
    :param user_id: The unique identifier for the user
    :return: A JWT token as a string
    """
    expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload: Dict[str, Any] = {
        "sub": user_id,
        "exp": expiration
    }
    token: str = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt(token: str) -> Dict[str, Any]:
    """
    Validates and decodes a JWT.
    
    :param token: The JWT token to be verified
    :return: The decoded token payload as a dictionary
    :raises ValueError: If the token is invalid or expired
    """
    try:
        decoded_token: Dict[str, Any] = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except PyJWTError as exc:
        # TODO: Add logging here if needed
        raise ValueError("Invalid or expired token") from exc