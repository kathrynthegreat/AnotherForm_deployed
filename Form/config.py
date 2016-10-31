import os
import logging

#http://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/
logging.basicConfig(level=logging.INFO)

DB_URL = os.environ["DATABASE_URL"]