#---------------------------------------------------
#PART THREE: Not so fast, yet another Flask Tutorial

AnotherForm_deployed
#---------------------------------------------------



This is yet another Flask tutorial in the world, but...I don't jump from hello world to deployment. My aim was to explain the hidden brain of flask a bit more pedantically for newbies and none software developers. 

This code belongs to the tutorial katya_flask_tutorial https://github.com/kathrynthegreat/katya_flask_tutorial

Part One uses: https://github.com/kathrynthegreat/katya_flask_tutorial/tree/master/1.AnotherForm_as_module

Part Two uses: https://github.com/kathrynthegreat/katya_flask_tutorial/tree/master/2.AnotherForm_as_package

Part Three uses: https://github.com/kathrynthegreat/anotherform_deployed

The app is deployed to: https://salty-cove-96240.herokuapp.com/

In this section we will deploy this small but not simple app to Heroku. A number of steps (more detailed list is in steps.txt) to do this are infront of us:
-Creating a config.py file to pull global vars connecting to Heroku db instance

-Setting up an account, app, and DB on Heroku 

-Creating Procfile to tell Heroku how to run stuff

-Creating pgsql files to create tables

-Replacing db connections with those on Heroku

-Spin up a DB on Heroku

-For the purposes of live Python meetup tutorial December 17, 2016, we'll be going through these step-by-step.


#Here's what our new file structure looks like now locally, which will get pushed to Git and automatically deployed to Heroku:

```
AnotherForm_deployed
├── .gitignore              # So that we don't commit compiled files or our environment passwords
├── Procfile                # Use the Procfile to tell Heroku how to run various pieces of your app
├── .env                    # So that we don't commit compiled files or our environment passwords
├── README.md               # This will be how to test/run the app & have basic info
├── requirements.txt        # These are the dependencies that you need to install for the app to run
├── runtime.txt        	  # Tells Heroku to run in python 3.5.2
├── run.py  				 # Runs the app!
├── test.csv                # sample csv to load
├──  Form/                  # Everything our app includes is inside this folder
│   ├──  __init__.py        # App-wide setup. Called by `run.py`
│   ├──  config.py          # Configuration Files. i.e. Login related things. Pulls from .env
│   ├──  views.py           # All the view routes
│   ├──  database_helper.py # All the view routes
│   ├──  setup.py           # Folder for any data we might want to use
│   ├──  templates/         # HTML files go here
│   │   ├──  index.html     # JavaScript & HTML
│   ├──  scripts/           # Postgres database creation scripts 
│   │   ├──  test.pgsql     # Test pgsql
```

-The cat.jpg, steps.tex, and README.md are anciallary to the app

