import unittest
import urllib2

from flask_testing import LiveServerTestCase
from selenium import webdriver

from app import create_app, db
from app.models import User

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Set test variables for test admin user
test_admin_username = "admin"
test_admin_password = "admin"

# Set test variables for test admin user 2
test_admin_username2 = "hello"
test_admin_password2 = "123"

class TestBase(LiveServerTestCase):

    def create_app(self):
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            # Specify the test database
                SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db'),
            # Change the port that the liveserver listens on
            LIVESERVER_PORT=5000
        )
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.get_server_url())

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        self.admin = User(username=test_admin_username,
                              password=test_admin_password,)

        self.admin2 = User(username=test_admin_username2,
                            password=test_admin_password2)

        # save users to database
        db.session.add(self.admin)
        db.session.add(self.admin2)
        db.session.commit()

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    unittest.main()
