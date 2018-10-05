__author__ = 'pzqa'


class StandardWizard:
    def __init__(self, app):
        self.app = app

    def add_standard_volume(self):
        wd = self.app.wd
        wait = self.app.wait
        by = self.app.by
        ec = self.app.ec
        wd.find_element_by_id("print_europe").click()
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))

    def add_document(self, pdf):
        wd = self.app.wd
        wait = self.app.wait
        by = self.app.by
        ec = self.app.ec
        wd.find_element_by_name("file-input").send_keys(pdf)
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))

    def set_volume_options(self, checkout):
        wd = self.app.wd
        wait = self.app.wait
        by = self.app.by
        ec = self.app.ec
        wd.find_element_by_css_selector("div.profil-select.select-search-input.div-as-input").click()
        wd.find_element_by_xpath("//div[@value='%s']" % checkout.content_color).click()
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//div[2]/div/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@value='%s']" % checkout.binding).click()
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_xpath("//div[2]/div/div[3]/div/div").click()
        wd.find_element_by_xpath("//div[@value='%s']" % checkout.cover_color).click()
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
        wd.find_element_by_css_selector("input.large-input").click()
        wd.find_element_by_css_selector("input.large-input").clear()
        wd.find_element_by_css_selector("input.large-input").send_keys(checkout.vol_title)
        wd.find_element_by_xpath('//body').click()
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))

    def mark_standard_checkboxes(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label").click()
        wd.find_element_by_xpath("//label/span").click()
