## Applicant Portal
This is an App that allows applicants to register and submit an application for a fictional business. 

## Technical Stack
Python, Django, SQLite, CSS, HTML5

## Running the Application
To run this application locally, clone this repository and run the following commands from the project directory - applicant_portal

Apply db migrations:

`python manage.py migrate`

Run django server:

`python manage.py runserver`

The landing page of the application can then be accessed at the URL:

`http://localhost:8000/applicant_portal/`

### Applicant Registration and Application tracking
#### http://localhost:8000/applicant_portal/
* An applicant can submit a new application or track an existing application by email.
* A returning applicant is validated based on email and phone number.
* Applicant sessions are managed based on email using Django's session support.
* Backend validation errors are communicated via Django's message support.


## To Do
1. Add unit tests
