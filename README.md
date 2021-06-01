# Rimbaud2.0

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
  * [Routes](#model-classes)
* [Settings](#special-thanks)

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

<!-- GETTING STARTED -->
## Getting Started

Get a local copy up and running following these steps.

### Installation

1. Clone the repository :

    ```sh
    git clone https://github.com/Twizzle1997/Rimbaud2.0
    ```
    
2. Install the requirements : 
    ```sh
    pip install -r requirements.txt
    ```

<!-- USAGE EXAMPLES -->
## Usage

* Prepare and make the migrations to update your dataase.  
``` python manage.py makemigrations ```  
```python manage.py migrate```

* launch the server by running the command :  
``` python manage.py runserver  ```

* You may have to create super user ids running these commands :  
``` python manage.py createsuperuser ```

### Routes
* ```/``` all the current articles  
* ```/article/{id}``` body of the target article    
* ```/admin/login``` administration pannel to create and manage the articles  
* ```/search/{word}``` search articles by key word   
*
## Settings
Edit the settings in the [/app/settings.py](https://github.com/Twizzle1997/Rimbaud2.0/blob/main/rimbaud_project/app/settings.py) file.
