
import os
import pytest
from tasks.celery import app


@pytest.fixture(scope="module")
def celery_app(request):
    app.conf.update(CELERY_ALWAYS_EAGER=True)

    return app
