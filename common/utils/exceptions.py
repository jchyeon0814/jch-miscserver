from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    def __init__(self, result_code, detail, status_code=400):
        self.result_code = result_code
        self.status_code = status_code
        super().__init__(detail=detail)
