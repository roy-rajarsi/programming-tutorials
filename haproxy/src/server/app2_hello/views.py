from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from typing import Optional


class Hello(APIView):

    def get(self, request: Request, format: Optional[str] = None) -> Response:
        print(f'>>>>>>>>>>>>>>>>>>>> Request received on {request.get_host()}:{request.get_port()} >>>>>>>>>>>>>>>>>>>>>\n')
        return Response(data=f'App2 - Hello from Application running on {request.get_port()}', status=HTTP_200_OK)
