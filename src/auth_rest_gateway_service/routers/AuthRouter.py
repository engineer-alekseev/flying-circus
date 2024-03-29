from fastapi import APIRouter, status,  HTTPException,  Depends
from services.JWTBearer import JWTBearer
from fastapi.responses import JSONResponse

import grpc
from proto import auth_pb2
from routers.schemas import RegistrationRequest, LoginRequest, ChangePasswordRequest, ForgotPasswordRequest
from services.grpc_connector import get_grpc_stub


class AuthRouter():
    def __init__(self):
        self.router = APIRouter(prefix="/auth", tags=["Authentication"])

        @self.router.post("/register")
        async def register(request: RegistrationRequest, grpc_stub=Depends(get_grpc_stub)) -> JSONResponse:
            """
            Register new

            Parameters:
            - `request`: `RegistrationRequest` object containing client data.

            Returns:
            - `JSONResponse` object containing token.
            """
            try:
                response: auth_pb2.RegistrationResponse = grpc_stub.Registration(
                    auth_pb2.RegistrationRequest(**request.__dict__)
                )

                res = JSONResponse(
                    status_code=status.HTTP_201_CREATED,
                    content={"token": response.token},
                )

                res.set_cookie(
                    key="JWToken",
                    value=response.token,
                    httponly=True,
                )

                return res

            except grpc.RpcError as e:
                self.__handle_grpc_exceptions(e)

            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=e,
                )

        @self.router.post("/login")
        async def login(request: LoginRequest, grpc_stub=Depends(get_grpc_stub)) -> dict:
            """
            Login

            Parameters:
            - `request`: `LoginRequest` object containing client data.

            Returns:
            - `JSONResponse` object containing token.
            """
            try:
                response: auth_pb2.RegistrationResponse = grpc_stub.Login(
                    auth_pb2.LoginRequest(**request.__dict__)
                )

                res = JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={"token": response.token},
                )

                res.set_cookie(
                    key="JWToken",
                    value=response.token,
                    httponly=True
                )

                return res

            except grpc.RpcError as e:
                self.__handle_grpc_exceptions(e)

            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=e,
                )

        @self.router.post("/forgot-password")
        async def forgot_password(request: ForgotPasswordRequest, grpc_stub=Depends(get_grpc_stub)) -> dict:
            """
            Forgot password

            Parameters:
            - `request`: `ForgotPasswordRequest` object containing client data.

            Returns:
            - `JSONResponse` object containing token.
            """
            try:
                response: auth_pb2.RegistrationResponse = grpc_stub.ForgotPassword(
                    auth_pb2.ForgotPasswordRequest(**request.__dict__)
                )

                return {"token": response.token}

            except grpc.RpcError as e:
                self.__handle_grpc_exceptions(e)

            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=e,
                )

        @self.router.post("/change-password", dependencies=[Depends(JWTBearer())])
        async def change_password(request: ChangePasswordRequest, grpc_stub=Depends(get_grpc_stub)) -> dict:
            """
            Change password

            Parameters:
            - `request`: `ChangePasswordRequest` object containing client data.

            Returns:
            - `JSONResponse` object containing token.
            """
            try:
                grpc_stub.ChangePassword(
                    auth_pb2.ChangePasswordRequest(**request.__dict__)
                )

                return {"message": "Password changed"}

            except grpc.RpcError as e:
                self.__handle_grpc_exceptions(e)

            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=e,
                )
                
        @self.router.get("/verify_jwt", dependencies=[Depends(JWTBearer())])
        async def verify_jwt() -> str:
            """
            Verify jwt

            Parameters:
            - no params.

            Returns:
            - string.
            """
            return "JWT successed verified"
                

    def __handle_grpc_exceptions(self, e: grpc.RpcError):

        match e.code():
            case grpc.StatusCode.INVALID_ARGUMENT:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=e.details(),
                )
            case grpc.StatusCode.UNAUTHENTICATED:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=e.details(),
                )
            case grpc.StatusCode.PERMISSION_DENIED:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=e.details(),
                )
            case grpc.StatusCode.NOT_FOUND:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=e.details(),
                )
            case  grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=e.details(),
                )
            case _:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=e.details(),
                )
