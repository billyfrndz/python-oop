class Manusia(object):
    nama = None

    def __init__(self, nama) -> None:
        self.nama = nama

    def makan(self):
        print('{} makan nasi'.format(self.nama))

programmer = Manusia('Eka')
programmer.makan()

programmer = Manusia('Putra')
programmer.makan()

programmer = Manusia('Putri')
programmer.makan()