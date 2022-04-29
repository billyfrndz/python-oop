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

programmer = ManusiaMilenial('Eka')
programmer.set_email('bill.fernandez@gmail.com')
programmer.set_pass('rahasia')
programmer.info()