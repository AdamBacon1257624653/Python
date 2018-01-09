import struct

data = struct.pack("!H5sb3sb", 1, b"hello", 0, b"hei", 0)

recv_data = struct.unpack("!Hs", data[:3])
print("%c%c" % ('h', 'e'))
print(recv_data)
