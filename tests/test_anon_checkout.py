# -*- coding: utf-8 -*-
from selenium import webdriver
from models.checkout import Stripe, WizardProfile, VolumeOptions
import unittest
from fixtures.application import Application


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()
        self.wd = webdriver.Chrome()

    def test_untitled_test_case(self):
        self.app.open_home_page()
        self.app.add_standard_volume()
        self.app.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                                  "Image attachments\\Testdata\\25.pdf")
        self.app.set_volume_options(VolumeOptions(content_color="1c", binding="punched",
                                                  cover_color="green", vol_title="Stan-dard )by( }{b0t!]["))
        self.app.set_profile(WizardProfile(title="m", country="de", name="Adalbert", surname="Hoffmann",
                                           priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                           house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                           city="Berlin", zip_code="13512"))
        self.app.mark_standard_checkboxes()
        self.app.cc_checkout(Stripe(card_number="4242424242424242", month_year="0223", cvc="132", cc_zip_code="3454"))
        self.app.close_success_page()

    def tearDown(self):
        self.app.destroy()
