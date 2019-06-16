from celery import Celery


app = Celery("worker", include=["tasks.autocheckin"])


if __name__ == "__main__":
    app.start()
