# PenMind


PenMind is a web application designed to improve mental well-being and help individuals track their progress in achieving better psychological health. It offers various features, including journaling, mood tracking, goal setting, task management, and progress tracker, all within a secure and user-friendly interface.

It is intended for individuals who want to enhance their mental well-being, whether they're dealing with conditions like anxiety or depression or simply aiming for personal growth and self-reflection.
## Table of Contents
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting Up Locally](#setting-up-locally)
  - [Running with Docker](#running-with-docker)
- [Running Tests](#running-tests)
## Screenshots
<img width="936" alt="Dashboard" src="https://github.com/Slim-Mejdoub/PenMind/assets/105583731/c378e255-0ec2-4fef-8c43-b15925813415">
<img width="935" alt="journaling" src="https://github.com/Slim-Mejdoub/PenMind/assets/105583731/c91ccbac-20b8-4a1f-8a33-209ad6a9a2ea">
<img width="941" alt="goals" src="https://github.com/Slim-Mejdoub/PenMind/assets/105583731/66419cd6-d10d-4f23-904b-8594ca1611a6">
<img width="943" alt="progress tracker" src="https://github.com/Slim-Mejdoub/PenMind/assets/105583731/5de28c57-956a-41ce-aec3-d9b260e2bb84">
<img width="792" alt="linechart" src="https://github.com/Slim-Mejdoub/PenMind/assets/105583731/1f135521-2aef-4707-9085-90d8547f12ae">
<img width="536" alt="Donut-chart" src="https://github.com/Slim-Mejdoub/PenMind/assets/105583731/3f4f8287-6f2b-446f-80d6-8843245f11b9">
<img width="752" alt="Bar-chart" src="https://github.com/Slim-Mejdoub/PenMind/assets/105583731/54475cce-5381-4e12-afa0-933adc593ae3">

## Getting Started

These instructions will guide you through setting up and running the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, make sure you have the following requirements:

- Python installed on your system.
- Docker and Docker Compose (if running with Docker).
### Setting Up Locally

 1- Clone the GitHub Repository:

 
 ```
  git clone https://github.com/Slim-Mejdoub/PenMind.git
  ```

 2- Change your working directory to the cloned repository:
```
  cd PenMind
  ```

 3- Create a Virtual Environment:

To isolate the project's dependencies from your system-wide Python packages, it is recommended to use a virtual environment. Follow these steps to create and activate a virtual environment:

Create a new virtual environment. You can replace venv with your preferred name for the environment:

```
  python -m venv venv
  ```

 4- Activate the virtual environment:
```
  .\venv\Scripts\activate
  ```

 5- Installing Project Dependencies:
Install the required project dependencies using pip and the provided requirements.txt file:
```
  pip install -r requirements.txt
  ```
 6-Running the Project:

Now that you have set up the virtual environment and installed the dependencies, you are ready to run the project. Use the following command to start the development server:
 ```
  python manage.py runserver
  ```
- Visit: [http://localhost:8000](http://localhost:8000)

- To stop the server, press `Ctrl + C`.

## Running with Docker
1. Clone the project:
```
  git clone https://github.com/Slim-Mejdoub/PenMind.git
  ```
2. Set up and activate the virtual environment (skip if already done):
```
  python -m venv venv
  ```
```
  .\venv\Scripts\activate
  ```
3. Install Project Dependencies:
```
  pip install -r requirements.txt
  ```
4. Exit the virtual environment:
```
  deactivate
  ```
5. Run Docker: 
```
  docker-compose up
  ```
6. Visit: [http://localhost:8000](http://localhost:8000)


## Running Tests
To run tests, follow these steps:
1. Update the Django settings in the `Journaling_web_app/settings.py` file. Change the current DATABASES setting to use SQLite:
 
```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
  ```

2. Delete all the migrations in the Endeavors and To_Do folders, except for the __init__.py file. You can do this manually or use the following commands:
```
  del Endeavors\migrations\0*.py
  ```
```
  del To_Do\migrations\0*.py
  ```

3. Create new database migrations
```
  python manage.py makemigrations
  ```
```
  python manage.py migrate
  ```

4. With your database now ready to store data locally, run the tests
```
  python manage.py test
  ```

The project is now set up, have fun with the PenMind application locally.


