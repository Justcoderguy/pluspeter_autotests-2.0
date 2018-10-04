__author__ = 'pzqa'


class Stripe:
    def __init__(self, card_number, month_year, cvc, cc_zip_code):
        self.card_number = card_number
        self.month_year = month_year
        self.cvc = cvc
        self.cc_zip_code = cc_zip_code


class WizardProfile:
    def __init__(self, title, country, name, surname, priv_email, address,
                 house_number, phone, addit_address, city, zip_code):
        self.title = title
        self.country = country
        self.name = name
        self.surname = surname
        self.priv_email = priv_email
        self.address = address
        self.house_number = house_number
        self.phone = phone
        self.addit_address = addit_address
        self.city = city
        self.zip_code = zip_code


class VolumeOptions:
    def __init__(self, content_color, binding, cover_color, vol_title):
        self.content_color = content_color
        self.binding = binding
        self.cover_color = cover_color
        self.vol_title = vol_title
