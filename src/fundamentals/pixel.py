""" this is the subclass of abstractphone """
from abstractphone import AbstractPhone


class Pixel(AbstractPhone):
    @property
    def screen_size(self):
        return 5.5

    @property
    def os_type(self):
        return 'Android 13'
