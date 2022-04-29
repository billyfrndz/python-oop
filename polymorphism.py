class Manusia(object):
    nama = None

    def __init__(self, nama) -> None:
        self.nama = nama

    def makan(self):
        print('{} makan nasi'.format(self.nama))
        
class ManusiaMilenial(Manusia):
    email = None
    __password = None

    def set_email(self, email):
        self.email = email

    def set_pass(self, password):
        self.__password = password

    def __samarkan_password(self):
        return self.__password.replace('a,', '*')

    def info(self):
        print('nama={}, email={}, pass={}'.format(self.nama, self.email, self.__samarkan_password()))

class Programmer(ManusiaMilenial):
    def info(self):
        print('nama={}/ email={}'.format(self.nama, self.email))

class Influencer(ManusiaMilenial):
    def info(self):
        print('nama={}: email={}'.format(self.nama, self.email))

manusiamilenial = ManusiaMilenial('Billy')
manusiamilenial.set_email('bill.fernandez@gmail.com')
manusiamilenial.set_pass('rahasia')
manusiamilenial.info()

programmer = Programmer('Eka')
programmer.set_email('bill.fernandez@gmail.com')
programmer.set_pass('rahasia')
programmer.info()

influencer = Influencer('Eka')
influencer.set_email('bella.fernandez@gmail.com')
influencer.set_pass('rahasia')
influencer.info()