__author__ = 'pzqa'


class Stripe:
    def __init__(self, card_number, month_year, cvc, cc_zip_code):
        self.card_number = card_number
        self.month_year = month_year
        self.cvc = cvc
        self.cc_zip_code = cc_zip_code


class WizardProfile:
    def __init__(self, title=None, country=None, vorname=None, name=None, priv_email=None, address=None,
                 house_number=None, phone=None, addit_address=None, city=None, zip_code=None):
        self.title = title
        self.country = country
        self.vorname = vorname
        self.name = name
        self.priv_email = priv_email
        self.address = address
        self.house_number = house_number
        self.phone = phone
        self.addit_address = addit_address
        self.city = city
        self.zip_code = zip_code


class VolumeOptions:
    def __init__(self, content_color=None, binding=None, cover_color=None, vol_title=None):
        self.content_color = content_color
        self.binding = binding
        self.cover_color = cover_color
        self.vol_title = vol_title
