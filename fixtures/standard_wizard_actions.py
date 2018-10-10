__author__ = 'pzqa'


class StandardWizard:
    def __init__(self, app):
        self.app = app

    def add_standard_volume(self):
        wd = self.app.wd
        wd.find_element_by_id("print_europe").click()
        self.wait_loading()

    def wait_loading(self):
        wd = self.app.wd
        wait = self.app.wait
        by = self.app.by
        ec = self.app.ec
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))

    def add_document(self, pdf):
        wd = self.app.wd
        wd.find_element_by_name("file-input").send_keys(pdf)
        self.wait_loading()

    def set_volume_options(self, checkout):
        self.change_selector_value(selector="//div[2]/div/div/div[2]/div/div/div/div",
                                   value=checkout.content_color)
        self.change_selector_value(selector="//div[2]/div/div[2]/div/div",
                                   value=checkout.binding)
        self.change_selector_value(selector="//div[2]/div/div[3]/div/div",
                                   value=checkout.cover_color)
        self.change_field_value(field="//input[@class='large-input']", value=checkout.vol_title)
        self.wait_loading()

    def change_field_value(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_xpath(field).click()
            wd.find_element_by_xpath(field).clear()
            wd.find_element_by_xpath(field).send_keys(value)
            wd.find_element_by_xpath('//body').click()
            self.wait_loading()

    def change_selector_value(self, selector, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_xpath(selector).click()
            wd.find_element_by_xpath("//div[@value='%s']" % value).click()
            self.wait_loading()

    def mark_standard_checkboxes(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label").click()
        wd.find_element_by_xpath("//label/span").click()
