class PTPLayer():
    def __init__(self):
        self.messageType = b'\x0b'
        self.versionPtp = b'\x02'
        self.messageLength = b'\x00\x40'
        self.domainNumber = b'\x00'
        self.minorSdoID = b'\x00'
        self.flags = b'\x00\x04'
        self.CorrectionField = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        self.messageTypeSpecific = b'\x00\x00\x00\x00'
        self.clockIdentity = b'\x00\x0d\xa8\xff\xfe\x16\x17\xb1'
        self.surcePortID = b'\x00\x0a'
        self.sequenceID = b'\x01\x89'
        self.controlField = b'\x05'
        self.logMessagePeriod = b'\xfd'
        self.originTimeStampSeconds = b'\x00\x00\x63\x60\x3a\xa6'
        self.originTimeStampNanoSeconds = b'\x29\x70\xa7\xf4'
        self.originCurrentUTCOffset = b'\x00\x25'
        self.PrecisionTimeProtocol = b'\x00'
        self.priority = b'\x01'
        self.grandmasterClockClass = b'\x06'
        self.grandmasterClockAccuracy = b'\x20'
        self.grandmasterClockVariance = b'\xff\xff'
        self.priority2 = b'\x01'
        self.grandmasterClockIdentity = b'\x00\x0d\xa8\xff\xfe\x16\x17\xb1'
        self.localStepsRemoved = b'\x00\x00'
        self.TimeSource = b'\x20'

    def pack_message(self):
        # TODO: this should be packed struct based on HW architecture endianness see
        # https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
        message = self.messageType + self.versionPtp + self.messageLength + self.domainNumber + self.minorSdoID + \
            self.flags + self.CorrectionField + self.messageTypeSpecific + self.clockIdentity + self.surcePortID + \
            self.sequenceID + self.controlField + self.logMessagePeriod + self.originTimeStampSeconds + \
            self.originTimeStampNanoSeconds + self.originCurrentUTCOffset + self.PrecisionTimeProtocol + self.priority + \
            self.grandmasterClockClass + self.grandmasterClockAccuracy + self.grandmasterClockVariance + self.priority2 + \
            self.grandmasterClockIdentity + self.localStepsRemoved + self.TimeSource
        return message


class PTPAnnounce(PTPLayer):
    def __init__(self):
        super().__init__()
        self.messageType = b'\x0b'
        self.messageLength = b'\x00\x40'
        self.flags = b'\x00\x04'
        self.controlField = b'\x05'


class PTPFollow_Up(PTPLayer):
    def __init__(self):
        super().__init__()
        self.messageType = b'\x08'
        self.messageLength = b'\x00\x2c'
        self.flags = b'\x00\x00'
        self.controlField = b'\x02'


class PTPSync(PTPLayer):
    def __init__(self):
        super().__init__()
        self.messageType = b'\x00'
        self.messageLength = b'\x00\x2c'
        self.flags = b'\x02\x00'
        self.controlField = b'\x00'


