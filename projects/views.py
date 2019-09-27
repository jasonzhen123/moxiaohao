from django.http import HttpResponse,JsonResponse
from django.views import View
from django.shortcuts import render
# Create your views here.


class IndexView(View):
    """
    index主页类视图
    """
    # def get(self, request):
    #     # get请求
    #     #return HttpResponse("<h1>GET请求：Hello, python测开大佬们！</h1>")
    #     datas = [
    #         {
    #             'project_name':'前程贷项目',
    #             'leader': '可优',
    #             'app_name': 'P2P平台应用',
    #         },
    #         {
    #             'project_name': '探索火星项目',
    #             'leader': '优优',
    #             'app_name': '吊炸天应用',
    #         },
    #         {
    #             'project_name': '无比牛逼的项目',
    #             'leader': '可可',
    #             'app_name': '神秘应用',
    #         }
    #     ]
    #     return render(request, 'index.html',locals())

    # def get(self, request):
    #
    #     return HttpResponse("<h1>GET请求：Hello, python测开大佬们！</h1>")
    def get(self, request, pk):
        datas = {
            "name":"keyou",
            "age" : "16"
        }
        # HttpResponse第一个参数往往为响应体内容
        #return HttpResponse("<h1>GET请求：Hello, python测开大佬们！</h1>")
        return JsonResponse(data=datas)


    def post(self, request):
        import json

        one_str = request.body.decode("utf-8")
        print(type(request.body))
        print(type(one_str))
        one_dict = json.loads(one_str)
        print(type(one_dict))
        print(one_dict["name"])

        return HttpResponse("<h1>POST请求：Hello, python测开大佬们！</h1>")

    def delete(self ,request):
        return HttpResponse("<h1>delete请求：Hello, python测开大佬们！</h1>")

    def put(self ,request):
        return HttpResponse("<h1>put请求：Hello, python测开大佬们！</h1>")


# 函数视图
def index(request):
    """
    函数视图
    :param request: request是HttpResponse对象，包含前端用户的所有请求信息
    :return: 必须返回一个HttpResponse对象或者子对象
    """
    if request.method == "GET":
        return HttpResponse("<h1>GET请求：Hello, python测开大佬们！</h1>")
    elif request.method == "POST":
        return HttpResponse("<h1>POST请求：Hello, python测开大佬们！</h1>")
    else:
        return HttpResponse("<h1>Hello, python测开大佬们！</h1>")



