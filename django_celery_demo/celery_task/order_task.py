from celery_task.celery import app

import time
@app.task
def order_add(x,y):
    time.sleep(1)
    return x+y