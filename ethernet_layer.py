class EthernetLayer():
    def __init__(self):
        self.destination = b'\x01\x1b\x19\x00\x00\x00'
        self.source = b'\x00\x0d\xa8\x16\x17\xb1'
        self.type = b'\x88\xf7'

    def pack_message(self):
        message = self.destination + self.source + self.type
        return message