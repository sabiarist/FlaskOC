import os

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

FB_APP_ID = 511455589474741

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10
SERVER_NAME = 'localhost:8943'

# Facebook test user
FB_USER_NAME = "Ellen"
FB_USER_PW = "YOLOYOLO"
FB_USER_EMAIL = "ellen_rmilrcp_page@tfbnw.net"
FB_USER_ID = 100018814390853
FB_USER_GENDER = 'female'
