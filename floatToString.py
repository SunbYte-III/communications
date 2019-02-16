import struct
import binascii

def float_to_string(n):
    return binascii.unhexlify('%x' % int(format(struct.unpack('!I', struct.pack('!f', n))[0], '032b'),2))
