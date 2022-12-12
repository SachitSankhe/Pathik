import jwt
from rest_framework.response import Response
from datetime import datetime, timedelta


def login_required(view_function):
    def wrap(request, *args, **kwargs):
        jwt_token = request.headers.get('Authorization')
        if jwt_token is None:
            return Response(status=401)
        try:
            jwt_token = jwt_token.split()[1]
            # print(jwt_token)
            request.user = jwt.decode(
                jwt_token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return Response(status=403)
        except:
            return Response(status=500)
        return view_function(request, *args, **kwargs)
    return wrap
