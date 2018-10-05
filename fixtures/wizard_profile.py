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
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
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
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
