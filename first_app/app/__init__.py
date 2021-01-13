import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA



"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
# appbuilder = AppBuilder(app, db.session, base_template='app.html')
appbuilder = AppBuilder(app, db.session)

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""
from . import views, models
from .devices.api import DevicesApi
from .jobs.api import JobsApi

appbuilder.add_api(DevicesApi)
appbuilder.add_api(JobsApi)



