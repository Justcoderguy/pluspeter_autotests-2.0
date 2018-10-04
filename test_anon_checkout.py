# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.add_standard_volume(wd)
        self.add_document(wd)
        self.set_volume_options(wd)
        self.set_profile(wd)
        self.mark_standard_checkboxes(wd)
        self.cc_checkout(wd)
        self.close_checkout_success(wd)

    def close_checkout_success(self, wd):
        WebDriverWait(wd, 60).until(ec.visibility_of_element_located((By.XPATH, "//main/div/a/img"))).click()

    def cc_checkout(self, wd, card_number="4242424242424242", month_year="0223", cvc="132", zip_code="3454"):
        wd.find_element_by_xpath("//div[2]/label/span").click()
        wd.find_element_by_id("paypalPayment").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        WebDriverWait(wd, 60).until(ec.frame_to_be_available_and_switch_to_it('stripe_checkout_app'))
        wd.find_element_by_xpath("//input[@placeholder='Card number']").click()
        wd.find_element_by_xpath("//input[@placeholder='Card number']").send_keys(card_number)
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").click()
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys(month_year)
        wd.find_element_by_xpath("//input[@placeholder='CVC']").click()
        wd.find_element_by_xpath("//input[@placeholder='CVC']").send_keys(cvc)
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").click()
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").send_keys(zip_code)
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.switch_to.default_content()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def mark_standard_checkboxes(self, wd):
        wd.find_element_by_css_selector("label").click()
        wd.find_element_by_xpath("//label/span").click()

    def set_profile(self, wd, title="m", country="de", name="Adalbert", surname="Hoffmann",
                    priv_email="adal95@hotmal.com.de", phone="004911234567890", address="Mainstrasse",
                    house_number="2311", addit_address="45-Y/T", city="Berlin", zip_code="13512"):
        wd.find_element_by_xpath("//a[@class='letter-file']").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_id("title_input").click()
        wd.find_element_by_xpath("//div[@value='%s']" % title).click()
        wd.find_element_by_xpath("(//div[@id='title_input'])[2]").click()
        wd.find_element_by_xpath("//div[@value='%s']" % country).click()
        wd.find_element_by_id("vorname").click()
        wd.find_element_by_id("vorname").clear()
        wd.find_element_by_id("vorname").send_keys(name)
        wd.find_element_by_id("name").click()
        wd.find_element_by_id("name").clear()
        wd.find_element_by_id("name").send_keys(surname)
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(priv_email)
        wd.find_element_by_id("Handynummer").click()
        wd.find_element_by_id("Handynummer").clear()
        wd.find_element_by_id("Handynummer").send_keys(phone)
        wd.find_element_by_id("Adresse").clear()
        wd.find_element_by_id("Adresse").send_keys(address)
        wd.find_element_by_id("Hausnummer").clear()
        wd.find_element_by_id("Hausnummer").send_keys(house_number)
        wd.find_element_by_id("Zusatz").clear()
        wd.find_element_by_id("Zusatz").send_keys(addit_address)
        wd.find_element_by_id("Stadt").clear()
        wd.find_element_by_id("Stadt").send_keys(city)
        wd.find_element_by_id("zip_code").clear()
        wd.find_element_by_id("zip_code").send_keys(zip_code)
        wd.find_element_by_id("wizard_profile_update_btn").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def set_volume_options(self, wd, title="Stan-dard )by( }{b0t!][", content_color="1c",
                           binding="punched", cover_color="green", ):
        wd.find_element_by_css_selector("div.profil-select.select-search-input.div-as-input").click()
        wd.find_element_by_xpath("//div[@value='%s']" % content_color).click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//div[2]/div/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@value='%s']" % binding).click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//div[2]/div/div[3]/div/div").click()
        wd.find_element_by_xpath("//div[@value='%s']" % cover_color).click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_css_selector("input.large-input").click()
        wd.find_element_by_css_selector("input.large-input").clear()
        wd.find_element_by_css_selector("input.large-input").send_keys(title)
        wd.find_element_by_xpath('//body').click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def add_document(self, wd, pdf="C:\\Users\\pzakharevich\\Desktop\\"
                                   "Image attachments\\Testdata\\25.pdf"):
        wd.find_element_by_name("file-input").send_keys(pdf)
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def add_standard_volume(self, wd):
        wd.find_element_by_id("print_europe").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def open_home_page(self, wd):
        wd.get("https://staging.pluspeter.com/")
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
