# -*- coding: utf-8 -*-
from models.checkout import Stripe, WizardProfile, VolumeOptions


def test_multi_spiral_blue(app):
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


def test_multi_spiral_green(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(cover_color="green"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_spiral_purple(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(cover_color="purple"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_spiral_red(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(cover_color="red"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_spiral_yellow(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(cover_color="yellow"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_spiral_dark_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(cover_color="dark_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_spiral_light_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(cover_color="light_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_punched_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(binding='punched', cover_color="blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_punched_green(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(binding='punched', cover_color="green"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_punched_purple(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(binding='punched', cover_color="purple"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_punched_red(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(binding='punched', cover_color="red"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_punched_yellow(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(binding='punched', cover_color="yellow"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_punched_dark_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(binding='punched', cover_color="dark_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_multi_punched_light_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(binding='punched', cover_color="light_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_spiral_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', cover_color="blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_spiral_green(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', cover_color="green"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_spiral_purple(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', cover_color="purple"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_spiral_red(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', cover_color="red"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_spiral_yellow(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', cover_color="yellow"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_spiral_dark_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', cover_color="dark_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_spiral_light_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', cover_color="light_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_punched_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', binding='punched', cover_color="blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_punched_green(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', binding='punched', cover_color="green"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_punched_purple(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', binding='punched', cover_color="purple"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_punched_red(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', binding='punched', cover_color="red"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_punched_yellow(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', binding='punched', cover_color="yellow"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_punched_dark_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', binding='punched', cover_color="dark_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()


def test_bw_punched_light_blue(app):
    app.open_home_page()
    app.wizard.add_standard_volume()
    app.wizard.add_document(pdf="C:\\Users\\pzakharevich\\Desktop\\"
                            "Image attachments\\Testdata\\25.pdf")
    app.wizard.set_volume_options(VolumeOptions(content_color='1c', binding='punched', cover_color="light_blue"))
    app.wizard_profile.set(WizardProfile(title="m", country="de", vorname="Adalbert", name="Hoffmann",
                                         priv_email="adal95@hotmal.com.de", address="Mainstrasse",
                                         house_number="2311", phone="004911234567890", addit_address="45-Y/T",
                                         city="Berlin", zip_code="13512"))
    app.wizard.mark_standard_checkboxes()
    app.stripe.checkout(Stripe(card_number="5555555555554444", month_year="0124", cvc="456", cc_zip_code="12790"))
    app.close_success_page()
