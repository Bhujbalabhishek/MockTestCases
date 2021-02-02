
def let_down_gently(person):
    return "better luck next time"

def send_email(person):
    return "email sent"

def give_it_time(person):
    return "give some time to like"

def evaluate(person1, person2):
    if person1 in person2['likes']:
        send_email(person1)
        send_email(person2)
    elif person1 in person2['dislikes']:
        let_down_gently(person1)
    elif person1 not in person2['likes'] and person1 not in person2['dislikes']:
        give_it_time(person1)