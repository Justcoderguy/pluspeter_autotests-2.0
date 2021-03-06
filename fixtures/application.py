from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from fixtures.standard_wizard_actions import StandardWizard
from fixtures.stripe import Stripe
from fixtures.wizard_profile import WizardProfile
__author__ = 'pzqa'


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wait = WebDriverWait
        self.ec = ec
        self.by = By
        self.wizard = StandardWizard(self)
        self.stripe = Stripe(self)
        self.wizard_profile = WizardProfile(self)

    def open_home_page(self):
        wd = self.wd
        if not (len(wd.find_elements_by_xpath("//a[contains(text(),'Registrieren')]")) > 0):
            wd.get("https://staging.pluspeter.com/")
        self.wait_loading()

    def close_success_page(self):
        wd = self.wd
        WebDriverWait(wd, 60).until(ec.visibility_of_element_located((By.XPATH, "//main/div/a/img"))).click()
        self.wait_loading()
        WebDriverWait(wd, 60).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='packages']")))

    def wait_loading(self):
        wd = self.wd
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def destroy(self):
        self.wd.quit()
