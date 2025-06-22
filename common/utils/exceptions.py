from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    def __init__(self, result_code, detail, status_code=400):
        self.result_code = result_code
        self.status_code = status_code
        super().__init__(detail=detail)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        result_code = getattr(exc, 'result_code', response.status_code)

        if hasattr(exc, 'detail'):
            if isinstance(exc.detail, (dict, list)):
                result_msg = exc.detail
            else: 
                result_msg = str(exc.detail)
        else:
            result_msg = str(exc)


        response.data = {
            "resultCode": result_code,
            "resultMsg": result_msg,
            "data": None
        }

    return response