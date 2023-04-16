from cartridge import Cartridge
from emulator import Emulator
import sys


def main():
    argc = len(sys.argv)
    argv = sys.argv
    if argc < 2:
        print(f'Usage: {argv[0]} ROM.gb')
        return -1

    cartridge = Cartridge(filename=argv[1])
    emulator = Emulator()
    emulator.load(cartridge)
    emulator.run()


if __name__ == "__main__":
    main()
