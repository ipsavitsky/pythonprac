import sys, struct
wav_contents = sys.stdin.buffer.read()
r = struct.unpack('4ci12chhi5cc4ci', wav_contents)
print(r)
