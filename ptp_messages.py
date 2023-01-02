ptp_messageType = b'\x0b'
ptp_versionPtp = b'\x02'
ptp_messageLength = b'\x00\x40'
ptp_domainNumber = b'\x00'
ptp_minorSdoID = b'\x00'
ptp_LI_61 = b'\x00\x04'
ptp_CorrectionField = b'\x00\x00\x00\x00\x00\x00\x00\x00'
ptp_messageTypeSpecific = b'\x00\x00\x00\x00'
ptp_clockIdentity = b'\x00\x0d\xa8\xff\xfe\xf16\xf17\xb1'
ptp_surcePortID = b'\x00\x0a'
ptp_sequenceID = b'\x01\x89'
ptp_controlField = b'\x05'
ptp_logMessagePeriod = b'\xfd'
ptp_originTimeStampSeconds = b'\x00\x00\x63\x60\x3a\xa6'
ptp_originTimeStampNanoSeconds = b'\x29\x70\xa7\xf4'
ptp_originCurrentUTCOffset = b'\x00\x25'
ptp_PrecisionTimeProtocol = b'\x00'
ptp_priority = b'\x01'
ptp_grandmasterClockClass = b'\x06'
ptp_grandmasterClockAccuracy = b'\x20'
ptp_grandmasterClockVariance = b'\xff\xff'
ptp_priority2 = b'\x01'
ptp_grandmasterClockIdentity = b'\x00\x0d\xa8\xff\xfe\x16\x17\xb1'
ptp_localStepsRemoved = b'\x00\x00'
ptp_TimeSource = b'\x20'

# TODO: this should be packed struct based on HW architecture endianness see
# https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
ptp_announce = ptp_messageType + ptp_versionPtp + ptp_messageLength + ptp_domainNumber + ptp_minorSdoID + \
    ptp_LI_61 + ptp_CorrectionField + ptp_messageTypeSpecific + ptp_clockIdentity + ptp_surcePortID + \
    ptp_sequenceID + ptp_controlField + ptp_logMessagePeriod + ptp_originTimeStampSeconds + \
    ptp_originTimeStampNanoSeconds + ptp_originCurrentUTCOffset + ptp_PrecisionTimeProtocol + ptp_priority + \
    ptp_grandmasterClockClass + ptp_grandmasterClockAccuracy + ptp_grandmasterClockVariance + ptp_priority2 + \
    ptp_grandmasterClockIdentity + ptp_localStepsRemoved + ptp_TimeSource