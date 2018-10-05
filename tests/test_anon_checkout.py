# -*- coding: utf-8 -*-
from models.checkout import Stripe, WizardProfile, VolumeOptions
import pytest
from fixtures.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.open_home_page()
    app.add_standard_volume()
    app.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                         "Image attachments\\Testdata\\25.pdf")
    app.set_volume_options(VolumeOptions(content_color="1c", binding="punched",
                                         cover_color="green", vol_title="Stan-dard )by( }{b0t!]["))
    app.set_profile(WizardProfile(title="m", country="de", name="Adalbert", surname="Hoffmann",
                                  priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                  house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                  city="Berlin", zip_code="13512"))
    app.mark_standard_checkboxes()
    app.cc_checkout(Stripe(card_number="4242424242424242", month_year="0223", cvc="132", cc_zip_code="3454"))
    app.close_success_page()
