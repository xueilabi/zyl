from django.shortcuts import render,HttpResponse

# Create your views here.
from celery_task.user_task import user_add
def index(request):
    result = user_add.delay(8,9)
    return HttpResponse(result.id)


def check_result(request):
    res=request.GET.get('id')
    from celery.result import AsyncResult
    from celery_task.celery import app
    async = AsyncResult(id=res, app=app)
    if async.successful():
        # 取出它return的值
        result = async.get()
        print(result)
        return HttpResponse('ok')
