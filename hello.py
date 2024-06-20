import datetime

def greet():
    now = datetime.datetime.now()
    current_hour = now.hour
    if 5 <= current_hour < 11:
        return "Good morning!"
    elif 11 <= current_hour < 13:
        return "Good noon!"
    elif 13 <= current_hour < 18:
        return "Good afternoon!"
    elif 18 <= current_hour < 21:
        return "Good evening!"
    else:
        return "Good night!"

print(
    '\n'.join(
        [
            "", 
            greet() + " I'm hanryi.", 
            "An independent developer in HZAU. ", 
            ""
        ]
    )
)