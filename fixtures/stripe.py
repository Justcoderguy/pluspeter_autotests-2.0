__author__ = 'pzqa'


class Stripe:
    def __init__(self, app):
        self.app = app

    def checkout(self, checkout):
        wd = self.app.wd
        wait = self.app.wait
        by = self.app.by
        ec = self.app.ec
        wd.find_element_by_xpath("//div[2]/label/span").click()
        wd.find_element_by_id("paypalPayment").click()
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
        wait(wd, 60).until(ec.frame_to_be_available_and_switch_to_it('stripe_checkout_app'))
        wd.find_element_by_xpath("//input[@placeholder='Card number']").click()
        wd.find_element_by_xpath("//input[@placeholder='Card number']").send_keys(checkout.card_number)
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").click()
        wd.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys(checkout.month_year)
        wd.find_element_by_xpath("//input[@placeholder='CVC']").click()
        wd.find_element_by_xpath("//input[@placeholder='CVC']").send_keys(checkout.cvc)
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").click()
        wd.find_element_by_xpath("//input[@placeholder='ZIP Code']").send_keys(checkout.cc_zip_code)
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.switch_to.default_content()
        wait(wd, 60).until(ec.invisibility_of_element_located((by.XPATH, "//div[@class='loading_box']")))
