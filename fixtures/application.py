from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from fixtures.standard_wizard_actions import StandardWizard
__author__ = 'pzqa'


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wait = WebDriverWait
        self.ec = ec
        self.by = By
        self.wizard = StandardWizard(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://staging.pluspeter.com/")
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def set_profile(self, checkout):
        wd = self.wd
        wd.find_element_by_xpath("//a[@class='letter-file']").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_id("title_input").click()
        wd.find_element_by_xpath("//div[@value='%s']" % checkout.title).click()
        wd.find_element_by_xpath("(//div[@id='title_input'])[2]").click()
        wd.find_element_by_xpath("//div[@value='%s']" % checkout.country).click()
        wd.find_element_by_id("vorname").click()
        wd.find_element_by_id("vorname").clear()
        wd.find_element_by_id("vorname").send_keys(checkout.name)
        wd.find_element_by_id("name").click()
        wd.find_element_by_id("name").clear()
        wd.find_element_by_id("name").send_keys(checkout.surname)
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(checkout.priv_email)
        wd.find_element_by_id("Handynummer").click()
        wd.find_element_by_id("Handynummer").clear()
        wd.find_element_by_id("Handynummer").send_keys(checkout.phone)
        wd.find_element_by_id("Adresse").clear()
        wd.find_element_by_id("Adresse").send_keys(checkout.address)
        wd.find_element_by_id("Hausnummer").clear()
        wd.find_element_by_id("Hausnummer").send_keys(checkout.house_number)
        wd.find_element_by_id("Zusatz").clear()
        wd.find_element_by_id("Zusatz").send_keys(checkout.addit_address)
        wd.find_element_by_id("Stadt").clear()
        wd.find_element_by_id("Stadt").send_keys(checkout.city)
        wd.find_element_by_id("zip_code").clear()
        wd.find_element_by_id("zip_code").send_keys(checkout.zip_code)
        wd.find_element_by_id("wizard_profile_update_btn").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def cc_checkout(self, checkout):
        wd = self.wd
        wd.find_element_by_xpath("//div[2]/label/span").click()
        wd.find_element_by_id("paypalPayment").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        WebDriverWait(wd, 60).until(ec.frame_to_be_available_and_switch_to_it('stripe_checkout_app'))
        wd.find_element_by_xpath("//input[@placeholder='Card number']").click()
        wd.find_element_by_xpath("//input[@placeholder='Card number']").send_keys(checkout.card_number)
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").click()
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys(checkout.month_year)
        wd.find_element_by_xpath("//input[@placeholder='CVC']").click()
        wd.find_element_by_xpath("//input[@placeholder='CVC']").send_keys(checkout.cvc)
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").click()
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").send_keys(checkout.cc_zip_code)
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.switch_to.default_content()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def close_success_page(self):
        wd = self.wd
        WebDriverWait(wd, 60).until(ec.visibility_of_element_located((By.XPATH, "//main/div/a/img"))).click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def destroy(self):
        self.wd.quit()
