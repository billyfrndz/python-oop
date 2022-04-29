class Manusia(object):
    nama = None

    def __init__(self, nama) -> None:
        self.nama = nama

    def makan(self):
        print('{} makan nasi'.format(self.nama))
        
class ManusiaMilenial(Manusia):
    email = None

    def set_email(self, email):
        self.email = email

    def info(self):
        print('nama={}, email={}'.format(self.nama, self.email))

programmer = ManusiaMilenial('Eka')
programmer.set_email('bill.fernandez@gmail.com')
programmer.info()

dokter = ManusiaMilenial('Putra')
dokter.set_email('bill.fernandez@gmail.com')
dokter.info()

petani = ManusiaMilenial('Putri')
petani.set_email('bill.fernandez@gmail.com')
petani.info()