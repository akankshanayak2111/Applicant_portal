import random, string, time, datetime
from .models import Applicant


APPLICATION_STATUS = ["applied", "quiz_started", "quiz_completed", "onboarding_requested", "onboarding_completed", "hired", "rejected"]
SERVICE_LOCATIONS = {'Atlanta':'GA', 'Scottdale' : 'GA', 'San Francisco': 'CA', 'San Jose': 'CA', 'Menlo Park' : 'CA','Denver': 'CO', 'Chicago': 'IL', 'Indianapolis' : 'IN', 'Cambridge': 'MA','New York' : 'NY' }


def get_random_first_name():
    return ''.join(random.choice(string.lowercase) for i in range(26))

def get_random_last_name():
    return ''.join(random.choice(string.lowercase) for i in range(26))

def get_random_email():
    return get_random_first_name() + get_random_last_name() +"@gmail.com"

def get_random_phone():
    return ''.join(["%s" % randint(0, 9) for num in range(0, 10)])

def generate_random_city():
	return random.choice(list(SERVICE_LOCATIONS.keys()))

def generate_random_date():
	start_date, end_date = datetime.date(2010, 1, 1), datetime.date(2017, 10, 31)
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start_date + timedelta(seconds=random_second)

def generate_random_appliation_status():
	return random.choice(APPLICATION_STATUS)




