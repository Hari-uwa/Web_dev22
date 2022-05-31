import os
from os import os_getenv
from app import create_app

config_name = os_getenv("FLASK_ENV")
app = create_app(config_name)

if __name__ == "__main__":
    app.run()