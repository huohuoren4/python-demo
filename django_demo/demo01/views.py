from django.http import JsonResponse


def home(req):
    data = {
        "name": "往昔",
        "subject": {
            "password": "123456w中文乱码"
        }
    }
    # 响应 json 格式的数据, 防止中文乱码
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
