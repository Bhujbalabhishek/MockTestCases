from datetime import datetime

def get_now():
    return datetime.now()

def is_summer():
    month = get_now().month

    return month in [6, 7, 8]