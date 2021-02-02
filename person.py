
import requests

def get_random_person():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()


def get_next_person(user):
    person = get_random_person()

    while person in user['name']:
        person = get_random_person()
    return person
    


    