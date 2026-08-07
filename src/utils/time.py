from datetime import datetime

def get_greetings():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else: return "Good night"


def get_current_date():
    date = datetime.now()
    current_date = date.strftime("%A, %B %d, %Y")
    return current_date

def get_current_time():
    time = datetime.now()
    current_time = time.strftime("%I:%M %p")
    return current_time