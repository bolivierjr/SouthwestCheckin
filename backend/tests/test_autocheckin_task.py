import requests_mock
from tasks import autocheckin
from utils import RedisCache
from tests.responses import reservation_resp, checkin_get_resp, checkin_post_resp


redis_client = RedisCache().connect()


def test_autocheckin(celery_app):
    with requests_mock.Mocker(real_http=True) as mock:
        base_url = "https://mobile.southwest.com/api/"
        conf_number = "MR6D6N"
        params = "?first-name=John&last-name=Doe"

        mock.register_uri(
            "GET",
            f"{base_url}mobile-air-booking/v1/mobile-air-booking/page/view-reservation/{conf_number}{params}",
            json=reservation_resp
        )

        mock.register_uri(
            "GET",
            f"{base_url}mobile-air-operations/v1/mobile-air-operations/page/check-in/{conf_number}{params}",
            json=checkin_get_resp
        )

        mock.register_uri(
            "POST",
            f"{base_url}mobile-air-operations/v1/mobile-air-operations/page/check-in",
            json=checkin_post_resp
        )

        autocheckin.apply(args=["MR6D6N", "John", "Doe", []])

        assert redis_client.hget("MR6D6N", "messages") == []
