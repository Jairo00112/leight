from datetime import datetime
import config
try:
    from zoneinfo import ZoneInfo
except Exception:
    ZoneInfo = None


def app_now() -> datetime:
    """Return current datetime in application's configured timezone.

    Falls back to system local time if zoneinfo or the configured zone is not available.
    """
    if ZoneInfo is not None:
        try:
            tz = ZoneInfo(config.APP_TIMEZONE)
            return datetime.now(tz)
        except Exception:
            return datetime.now()
    return datetime.now()


def app_now_date():
    return app_now().date()


def app_now_time():
    return app_now().time()
