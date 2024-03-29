from typing import Any
from fastapi import Request, HTTPException, status, Depends
from fastapi.security import HTTPBearer

from proto import auth_pb2
from services.grpc_connector import get_grpc_stub


# async def middleware_get_token_from_cookies(request: Request, call_next):
#     token = request.cookies.get("JWToken")

#     if "authorization" not in request.headers and token:
#         request.scope["headers"].append((b"authorization", b"Bearer " + token.encode()))

#     return await call_next(request)


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request, grpc_stub=Depends(get_grpc_stub)) -> Any:
        cridentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

        token = await super().__call__(request)
        
        print(token)
        if token is None:
            raise cridentials_exception

        try:
            req = auth_pb2.VerifyJWTRequest(token=token.credentials)
            grpc_stub.VerifyJWT(req)
            
        except Exception as e:
            print("EXCEPTION:", e, flush=True)
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="EXCEPTION: " + str(e),
        )

        return token

   