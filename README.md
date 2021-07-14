# Bungalow Take Home Project for Backend Developer Role

## About This Project
This is a Django based assignment. We have created a base project for you to work from. 
You are free to vary from our original base if you would like to. We provide it with the intention of providing 
a common base for all candidates to work from and to hopefully save you a bit of time. 

If you need an introduction to Django, their docs are an excellent place to start: https://docs.djangoproject.com/en/3.2

We encourage you to use the Django Rest Framework for developing your API. This is a framework that we use extensively 
at Bungalow, and it provides some nice functionality out of the box. https://www.django-rest-framework.org/

## What to Build
We would like you to build an API that can be used to query some information about houses.
Sample data is provided in the `sample-data` folder.
We have provided the stub for a Django command to import the data. Finish writing this code.
You should use Django's ORM to model the data and store it in a local database.
Then, utilize the Django Rest Framework to provide an API to query the models.
A very basic API design here would simply return all of the data available.
You can choose to improve and refine this very basic API design, and we encourage you to do so.
This will give us an opportunity to see how you approach API design.
If you are running out of time, you can outline how you would have done things differently given more time.


## How Will This Be Evaluated
We will use this project as our basis for our evaluation of your coding skill level as it relates to our team.
To do this, we will review your code with an eye for the following:

- Design Choices - choice of functionality, readability, maintainability, extendability, appropriate use of language/framework features
- Does it work as outlined
- Testing - have you considered how you'd test your code?
- Documentation - have you provided context around decisions and assumptions that you have made?
- Polish - have you produced something that would be ready to go into a production system?
  if not, have you clearly stated what would be needed to get from where it is to that level of polish?

## Time Expectations
We know you are busy and likely have other commitments in your life, so we don't want to take too much of your time.
We don't expect you to spend more than 2 hours working on this project. That being said, if you choose to put more or
less time into it for whatever reason, that is your choice. Feel free to indicate in your notes below if you worked on
this for a different amount of time and we will keep that in mind while evaluating the project. You can also provide us
with additional context if you would like to. Additionally, we have left a spot below for you to note. If you have ideas 
for pieces that you would have done differently or additional things you would have implemented if you had more time, 
you can indicate those in your notes below as well, and we will use those as part of the evaluation. For example, if you 
would have tested more, you can describe the tests that you would have written, and just provide 1 or 2 actual implemented
tests.

## Public Forks
We encourage you to try this project without looking at the solutions others may have posted. This will give the most
honest representation of your abilities and skills. However, we also recognize that day-to-day programming often involves 
looking at solutions others have provided and iterating on them. Being able to pick out the best parts and truly 
understand them well enough to make good choices about what to copy and what to pass on by is a skill in and of itself. 
As such, if you do end up referencing someone else's work and building upon it, we ask that you note that as a comment. 
Provide a link to the source so we can see the original work and any modifications that you chose to make. 

## Setup Instructions
1. Fork this repository and clone to your local environment. If you make your fork private, 
1. Install a version of Python 3 if you do not already have one. We recommend Python 3.8 or newer.
1. You can use the built-in virtual environment creation within Python to create a sandboxed set of package installs. 
   If you already have a preferred method of virtualenv creation, feel free to proceed with your own method. 
   `python -m venv env`    
1. You will need to activate your virtual environment each time you want to work on your project. 
   Run the `activate` script within the `env/bin` folder that was generated.
1. We have provided a `requirements.txt` file you can use to install the necessary packages.
   With your virtualenv activated run: `pip install -r requirements.txt`
1. To run the django server run `python manage.py runserver`
1. To run the data import command run `python manage.py import_house_data`
1. You are now setup and ready to start coding. 


# Jean Ventura's Notes

## Instructions to run the project as a developer

- Assuming previous Setup Instructions were done

- From repository root, go to project root

        $ cd listings

- Run migrations

        $ python manage.py migrate

- Load data

        $ python manage.py import_house_data ../sample-data/data.csv

- Run tests

        $ python manage.py test

- Start server

        $ python manage.py runserver

- Go to endpoint

    http://localhost:8000/api/houses/

## Time Spent

| Task | Time (hours)  |
|---|---|
| Designing/Coding  | 2.0  |
| Documenting  | 0.5  |
| Total  | 2.5  |

## Assumptions

1. No authentication/authorization required
2. No automatic data schema or cleanup
3. No additional functionality outside of reading the data
4. Not expecting huge amounts of requests (since it not production ready)

Since there was no direct mention of any of the above in the instructions, the expectations given the time constraint and the inability to wait until the next day to send out an email asking for clarification, I decided to assume the above was not needed.

Under different circumstance I would ask for clarification of everything mentioned here in my notes.

## Next Steps

1. Schema/data cleanup
2. Add authorization/authentication (if required)
3. Better logging/auditing
4. Filtering
5. Caching
6. More tests

The current model definition is very generic and there's a lot that can be done to improve it, from naming conventions to data definitions. To comply with time requirements, couldn't dedicate as much time as I wanted to the initial data load.

### Features

1. Endpoint that provides data on houses: `/api/houses/`
2. Ability to paginate the endpoint using query parameters: `limit=50&offset=50`
3. Ability to migrate data from a CSV (backend only)

### Testing

Only added basic tests for the small amount of coding I had to do, since for such a simple requirement the Django REST Framework library provides almost all the functionality required.

More tests will be needed in order to add functionality (testing permissions, serialization, etc.).

### Anything else needed to make this production ready?

Application should be optimized for a continuous integration pipeline (automatic style checks and tests, dockerization).

Proper application and web servers should be used (uwsgi/NGINX).

Improve auditability (better logs).

## How to Use

On a browser:

- To view the first page using the API Browser:
    
    http://localhost:9000/api/houses/?format=json

- To view the first page in raw JSON format:

    http://localhost:9000/api/houses/?format=json

- To go to page 3 (amount of records per page is 50 by default):

    http://localhost:9000/api/houses/?offset=100

- To view 100 records per page (amount of records per page is 50 by default):

    http://localhost:9000/api/houses/?limit=100

- To go to page 3 when records per page is 100:

    http://localhost:9000/api/houses/?limit=100&offset=200
    
- Total records, next page and previous pages are available as keys.
