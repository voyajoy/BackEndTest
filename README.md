## Coding Challenge

In order to be considered for this position, you must complete the following steps. 

*Note: This task should take no longer than 1-2 hours at the most.*


### Prerequisites

- Please note that this will require some basic knowledge and/or the ability to learn of the following:
       - Python
       - [Django](http://expressjs.com/)
       - Git
       - [Docker](http://www.docker.com/)
       - [Celery](http://www.celeryproject.org/) (or any task queue)
       - Any type of DB of your choosing

- You will need to have the following installed to complete this task
       - Python
       - [Docker](http://www.docker.com/)

## Task

1. Fork this repository
2. Create a *source* folder to contain your code. 
3. In the *source* directory, please create an Django app that accomplishes the following:
    - Connect to the [Github API](http://developer.github.com/)
    - Find the [nodejs/node](https://github.com/nodejs/node) repository
    - Find the most recent commits (choose at least 25 or more of the commits)
    - Write a task that syncs the recent commits to your database and have it run every hour
    - Create API routes that displays the synced commits by author and can mark them read/unread. 
4. Dockerize your application by writing a docker.yml file and test it by running the container locally.
5. Commit and Push your code to your new repository
6. Send us a pull request, we will review your code and get back to you

### Tests

Create the following unit tests with the testing framework of your choice:

  1.  Verify the API work as intended 

## Once Complete
1. Commit and Push your code to your new repository
2. Send us a pull request, we will review your code and get back to you

### Notes
- You are free to write and modularize code any way you like just as long as you follow the requirements
- 4 spaces for indentation! No tabs!
- If you don't know how to do something, Google is your friend!