import os
import time
import sys
from .celery import app
from southwest.checkin import auto_checkin


@app.task(bind=True)
def autocheckin(self, confirmation, firstname, lastname, notifications=[]):
    try:
        auto_checkin(confirmation, firstname, lastname, notifications)
    except (SystemExit, Exception) as exc:
        print(exc)
