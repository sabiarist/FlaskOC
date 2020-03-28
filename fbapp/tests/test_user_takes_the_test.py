from flask_testing import LiveServerTestCase
from selenium import webdriver

from fbapp import app
from fbapp import models


class TestUserTakesTheTest(LiveServerTestCase):
    def test_user_login(self):
        self.driver.get(self.get_server_url())
        assert self.driver.current_url == 'http://127.0.0.1:8943'

    def create_app(self):
        app.config.from_object('fbapp.tests.config')
        return app

    def setUp(self) -> None:
        self.driver = webdriver.firefox
        models.init_db()

    def tearDown(self) -> None:
        self.driver.quit()


