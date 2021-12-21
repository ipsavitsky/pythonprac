import sys
import struct

try:
    data = struct.unpack("4sI4s4sIHHIIHH4sI", sys.stdin.buffer.read(44))
    # print(data)
except struct.error:
    print("NO")
else:
    if data[0] == b'RIFF' and data[2] == b'WAVE' and data[3] == b'fmt ':
        print(f'Size={data[1]}, Type={data[5]}, Channels={data[6]}, Rate={data[7]}, Bits={data[10]}, Data size={data[12]}')
    else:
        print("NO")

