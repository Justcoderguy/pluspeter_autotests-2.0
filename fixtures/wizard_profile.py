__author__ = 'pzqa'


class WizardProfile:
    def __init__(self, app):
        self.app = app

    def set(self, checkout):
        wd = self.app.wd
        wait = self.app.wait
        by = self.app.by
        ec = self.app.ec
        wd.find_element_by_xpath("//a[@class='letter-file']").click()
        self.wait_loading(by, ec, wait)
        self.change_selector_value(selector="title_list", value=checkout.title)
        self.change_selector_value(selector="country_list", value=checkout.country)
        self.change_field_value(field="vorname", value=checkout.vorname)
        self.change_field_value(field="name", value=checkout.name)
        self.change_field_value(field="email", value=checkout.priv_email)
        self.change_field_value(field="Handynummer", value=checkout.phone)
        self.change_field_value(field="Adresse", value=checkout.address)
        self.change_field_value(field="Hausnummer", value=checkout.house_number)
        self.change_field_value(field="Zusatz", value=checkout.addit_address)
        self.change_field_value(field="Stadt", value=checkout.city)
        self.change_field_value(field="zip_code", value=checkout.zip_code)
        wd.find_element_by_id("wizard_profile_update_btn").click()
        self.wait_loading(by, ec, wait)

    def change_field_value(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_id(field).click()
            wd.find_element_by_id(field).clear()
            wd.find_element_by_id(field).send_keys(value)

    def change_selector_value(self, selector, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_id(selector).click()
            wd.find_element_by_xpath("//div[@value='%s']" % value).click()

    def wait_loading(self, by, ec, wait):
        wd = self.app.wd
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
