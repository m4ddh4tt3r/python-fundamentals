""" This (abstract) class is the base for subclasses """
from abc import ABC
from abc import abstractmethod


class AbstractPhone(ABC):
    @property
    @abstractmethod
    def screen_size(self):
        pass

    @property
    @abstractmethod
    def os_type(self):
        pass

    @property
    def has_print_scanner(self):
        """ a normal property within an abstract class """
        return True

    def make_call(self):
        """ this is a concrete method, which is a normal method """
        print(f'Phone unlocked using scanner {self.has_print_scanner}')
        print('Numbers dialed and call is made')


