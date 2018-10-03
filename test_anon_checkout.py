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
        wd.get("https://staging.pluspeter.com/")
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_id("print_europe").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_name("file-input").send_keys("E:\\Code\\Test data\\25.pdf")
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_css_selector("div.profil-select.select-search-input.div-as-input").click()
        wd.find_element_by_xpath("//div[@value='1c']").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//div[2]/div/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@value='punched']").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//div[2]/div/div[3]/div/div").click()
        wd.find_element_by_xpath("//div[@value='green']").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_css_selector("input.large-input").click()
        wd.find_element_by_css_selector("input.large-input").clear()
        wd.find_element_by_css_selector("input.large-input").send_keys("Stan-dard )by( }{b0t!][")
        wd.find_element_by_xpath('//body').click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//a[@class='letter-file']").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_id("title_input").click()
        wd.find_element_by_xpath("//div[@value='m']").click()
        wd.find_element_by_xpath("(//div[@id='title_input'])[2]").click()
        wd.find_element_by_xpath("//div[@value='de']").click()
        wd.find_element_by_id("vorname").click()
        wd.find_element_by_id("vorname").clear()
        wd.find_element_by_id("vorname").send_keys("Adalbert")
        wd.find_element_by_id("name").click()
        wd.find_element_by_id("name").clear()
        wd.find_element_by_id("name").send_keys("Hoffmann")
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("adal95@hotmal.com.de")
        wd.find_element_by_id("Handynummer").click()
        wd.find_element_by_id("Handynummer").clear()
        wd.find_element_by_id("Handynummer").send_keys("004911234567890")
        wd.find_element_by_id("Adresse").clear()
        wd.find_element_by_id("Adresse").send_keys("Mainstrasse")
        wd.find_element_by_id("Hausnummer").clear()
        wd.find_element_by_id("Hausnummer").send_keys("2311")
        wd.find_element_by_id("Zusatz").clear()
        wd.find_element_by_id("Zusatz").send_keys("45-Y/T")
        wd.find_element_by_id("Stadt").clear()
        wd.find_element_by_id("Stadt").send_keys("Berlin")
        wd.find_element_by_id("zip_code").clear()
        wd.find_element_by_id("zip_code").send_keys("13512")
        wd.find_element_by_id("wizard_profile_update_btn").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_css_selector("label").click()
        wd.find_element_by_xpath("//label/span").click()
        wd.find_element_by_xpath("//div[2]/label/span").click()
        wd.find_element_by_id("paypalPayment").click()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        WebDriverWait(wd, 60).until(ec.frame_to_be_available_and_switch_to_it('stripe_checkout_app'))
        wd.find_element_by_xpath("//input[@placeholder='Card number']").click()
        wd.find_element_by_xpath("//input[@placeholder='Card number']").send_keys("4242 4242 4242 4242")
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").click()
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys("02 / 23")
        wd.find_element_by_xpath("//input[@placeholder='CVC']").click()
        wd.find_element_by_xpath("//input[@placeholder='CVC']").send_keys("132")
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").click()
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").send_keys("3454")
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.switch_to.default_content()
        WebDriverWait(wd, 60).until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='loading_box']")))
        WebDriverWait(wd, 60).until(ec.visibility_of_element_located((By.XPATH, "//main/div/a/img"))).click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
