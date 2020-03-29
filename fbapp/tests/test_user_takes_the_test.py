from flask_testing import LiveServerTestCase
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

from .. import app
from .. import models


class TestUserTakesTheTest(LiveServerTestCase):
    def test_user_login(self):
        self.driver.get(self.get_server_url())
        self.clicks_on_Login()
        self.sees_login_page()
        assert self.driver.current_url == 'http://localhost:8943/'

    def create_app(self):
        app.config.from_object('fbapp.tests.config')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Firefox()
        models.init_db()
        self.wait = ui.WebDriverWait(self.driver, 1000)

    def gel_el(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def clicks_on_Login(self):
        # element contenant l'iframe
        button = self.get_el(".fb-login-button")
        # Attente du cahrgement de l'iframe
        self.wait.until(lambda driver: self.driver.find_element_by_tag_name("iframe").is_displayed())
        # Clique sur l'element
        ActionChains(self.driver).click(button).perform()

    def sees_login_page(self):
        # On attend d'avoir plus d'une fenêtre ouverte.
        self.wait.until(lambda driver: len(self.driver.window_handles) > 1)
        # switch_to permet de changer de fenêtre.
        # window_handles renvoie une liste contenant toutes les fenêtres ouvertes
        # par ordre d'ouverture.
        # La fenêtre d'authentification étant la dernière ouverte,
        # c'est la dernière de la liste.
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # On attend que la page ait fini de charger.
        self.wait.until(lambda driver: self.get_el('#email'))
        assert self.driver.current_url.startswith('https://www.facebook.com/login.php')  # <3 Python

    def tearDown(self):
        self.driver.quit()