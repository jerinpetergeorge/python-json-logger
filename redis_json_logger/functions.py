from datetime import datetime


def get_current_time_iso(fmt):
    return datetime.now().strftime(fmt)
