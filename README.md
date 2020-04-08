# <img src="/uploads/6aa59d6cfe7082f28fddd51caf52b729/Logo.png"  width="250">

This is a group project for the course TDT4145 Programvareutvikling.
The goal of this course is to immerse in Agile Methodology, and develop crucial skills in cooperation, project planning and source-code management. This includes learning
to use Git and using Git-repository manager GitLab.

Our job is to create a knit platform for our product owner. This platform is a community where
knitters and business owners can meet. This web application will allow users to create arrangements, challenges,
advertisement and share thoughts through a feed. Knitters will be able to participate in challenges and arrangements
created by companies.

## Demo

An example of the application:

<img src="/uploads/50ea564f02a60604089dae480dbad7bc/Skjermbilde_2020-04-08_kl._00.54.28.png"  width="50%">

When logged in you will have access to a variety of functions.

For a more detailed guide on how to use the application, refer to our Wiki page:

[Link to User Manual](documentation)

## Technology/framework
#### Built with:
* [Django](https://www.djangoproject.com): Python framework
* [Bootstrap](https://getbootstrap.com): CSS framework
* [SQLite](https://www.sqlite.org/index.html): Database

## Requirements

To run the project, you must have Python 3.8 or later and Pip installed.

## Installation

You should use virtual environment like [VirtualEnv](https://virtualenv.pypa.io/en/latest/installation.html) to isolate Python projects. This may help to prevent problems in the future.

To activate VirtualEnv:

```sh
$ source /venv/bin/activate
```


1. Use any IDE that supports Python and clone: 

    ```
    https://gitlab.stud.idi.ntnu.no/tdt4140-2020/13.git
    ```

    Or use Git to clone:

    ```sh
     $ git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/13.git
    ```

2. Install required packages:

    ```sh
     $ pip install -r requirements.txt
    ```

3. Apply migrations:

    ```sh
     $ python manage.py migrate
    ```

   > You may have to change directory to PU13 before using the command over.
   > `$ cd PU13`.
4. Run project:

    ```sh
     $ python manage.py runserver
    ```
    
    Use a web browser and visit your development server: `http://127.0.0.1:8000/`

## Tests

Tests in Django are written using the unittest module which is built-in to the Python standard library.

The project is integrated with CI to validate and test code after every push and merge. 
This will make it easy to catch bugs and errors in the development cycle, ensuring that all the code deployed to production is working correctly.
It is possible to check the status and rerun the pipeline under *GitLab --> CI/CD --> Pipelines*

The tests can also be ran with the command:

```sh
 $ python manage.py test
```

## Team Members
* Andreas Torgersen
* Elise Almestad
* Mai Tran
* Vivi Svendsen
* William H. Le
* Anders Lyholm Limi

## License
NTNU © PU13