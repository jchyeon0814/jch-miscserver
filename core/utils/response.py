from rest_framework.views import exception_handler
from rest_framework.renderers import JSONRenderer

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

class CustomJSONRenderer(JSONRenderer):
    def get_indent(self, *args, **kwargs):
        return None

    def render(self, data, accepted_media_type=None, renderer_context=None):

        if isinstance(data, dict) and set(data.keys()) >= {"resultCode", "resultMsg", "data"}:
            return super().render(data, accepted_media_type, renderer_context=renderer_context)

        # ensure_ascii=False 옵션을 명시적으로 지정(get_default_renderer_context)
        return super().render({
            "resultCode": 0,
            "resultMsg": "success",
            "data": data
        }, accepted_media_type, renderer_context=renderer_context)

    # ASCII 코드 문자열의 이스케이프 처리 방지 -> 저장 또는 전송 시 utf-8로 지정해서 사용해야 함
    def get_default_renderer_context(self):
        context = super().get_default_renderer_context()
        context['json_dumps_params'] = {'ensure_ascii': False}
        return context
    