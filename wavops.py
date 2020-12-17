import wave
import struct

def wav_write(array, name):
    sound = wave.open(name, 'w')

    sound.setnchannels(1)
    sound.setsampwidth(2)
    sound.setframerate(48000)

    arr = []
    for x in array:
        arr.append(int(round(x*32000)))

    BinStr = struct.pack( str(len(array))+'h', *arr)

    sound.writeframes(BinStr)
    sound.close()