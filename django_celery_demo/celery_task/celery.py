from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
backend='redis://:123456@127.0.0.1:6379/1' #最后的0是指定的库
broker='redis://:123456@127.0.0.1:6379/0'
app = Celery('test',broker=broker,backend=backend,
             include=['celery_task.order_task',
                      'celery_task.user_task'
                      ])
#一定要指定一个名字，每次实例化都要起一个名字
# 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
#时区
app.conf.timezone = 'Asia/Shanghai'
#是否使用UTC
app.conf.enable_utf = False

app.conf.beat_schedule = {
    # 名字随意命名
    'add-every-10-seconds': {
        # 执行tasks1下的test_celery函数
        'task': 'celery_task.order_task.order_add',
        # 每隔2秒执行一次
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': timedelta(seconds=2),
        # 传递参数
        'args': (5,6)
    },
    # 'add-every-12-seconds': {
    #     'task': 'celery_task.order_task.order_add',
    #     # 每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     # 'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': (16, 16)
    # },
}