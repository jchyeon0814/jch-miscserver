from json import JSONEncoder
import json
from rest_framework.response import Response
import logging

def api_response(data, result_code=0, result_msg="success"):
    
    response_data = {
        "resultCode": result_code, 
        "resultMsg": result_msg,
        "data": data
    }
    
    print(f"API 응답 생성 - 결과 코드: {result_code}, 메시지: {result_msg}, 데이터 개수: {len(data)}")
    
    return Response(response_data)