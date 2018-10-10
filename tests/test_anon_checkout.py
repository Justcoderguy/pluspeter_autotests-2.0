# -*- coding: utf-8 -*-
from models.checkout import Stripe, WizardProfile, VolumeOptions


def test_anon_checkout_default_volume_options(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions())
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="4242424242424242", month_year="0223", cvc="132", cc_zip_code="3454"))
    app.close_success_page()


def test_anon_checkout(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color="1c", binding="punched",
                                                cover_color="green", vol_title="Stan-dard )by( }{b0t!]["))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()
