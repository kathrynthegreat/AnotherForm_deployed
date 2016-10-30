#-------------------------
PART THREE: AnotherFormcopy
#-------------------------

This is yet another Flask tutorial in the world, but...I don't jump from hello world to deployment. My aim was to explain the hidden brain of flask a bit more pedantically for newbies and none software developers. 

This code belongs to the the tutorial katya_flask_tutorial https://github.com/kathrynthegreat/katya_flask_tutorial
Part Two uses: https://github.com/kathrynthegreat/AnotherFormcopy

In this section we will deploy this small but not simple app to Heroku. A number of steps to do this are infront of us:
Creating Procfile to tell Heroku how to run stuff
Creating pgsql files to create tables
Replacing db connections with those on Heroku
Creating .env file so that your passwords are not on git like mine are :)
Creating a .gitignore so that the .env file doesn't get pushed to git
Creating a config.py file so that global vars are pulled from .env
Setting up an account, app, and DB on Heroku 

#Here's what our new file structure looks like now locally, which will get pushed to Git and automatically deployed to Heroku:

```
AnotherFormcopy.
├── .gitignore              # So that we don't commit compiled files or our environment passwords
├── Procfile                # Use the Procfile to tell Heroku how to run various pieces of your app
├── .env                    # So that we don't commit compiled files or our environment passwords
├── README.md               # This will be how to test/run the app & have basic info
├── requirements.txt        # These are the dependencies that you need to install for the app to run
├── run.py  				# Runs the app!
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

