from config.celery import celery_app

@celery_app.task
def generate_reports():
    pass