GAMEBOY_TITLE_START = 0x134
GAMEBOY_TITLE_END = 0x143
GAMEBOY_LICENSEE_START = 0x144
GAMEBOY_LICENSEE_END = 0x145
GAMEBOY_CARTRIDGE_TYPE = 0x147
GAMEBOY_DESTINATION = 0x14a
GAMEBOY_ROM_SIZE = 0x148
GAMEBOY_RAM_SIZE = 0x149

LICENSEE = {
    b'\x00': 'None',
    b'\x01': 'Nintendo R&D1',
    b'\x08': 'Capcom',
    b'\x13': 'Electronic Arts',
    b'\x18': 'Hudson Soft',
    b'\x19': 'b-ai',
    b'\x20': 'kss',
    b'\x22': 'pow',
    b'\x24': 'PCM Complete',
    b'\x25': 'san-x',
    b'\x28': 'Kemco Japan',
    b'\x29': 'seta',
    b'\x30': 'Viacom',
    b'\x31': 'Nintendo',
    b'\x32': 'Bandai',
    b'\x33': 'Ocean/Acclaim',
    b'\x34': 'Konami',
    b'\x35': 'Hector',
    b'\x37': 'Taito',
    b'\x38': 'Hudson',
    b'\x39': 'Banpresto',
    b'\x41': 'Ubi Soft',
    b'\x42': 'Atlus',
    b'\x44': 'Malibu',
    b'\x46': 'angel',
    b'\x47': 'Bullet-Proof',
    b'\x49': 'irem',
    b'\x50': 'Absolute',
    b'\x51': 'Acclaim',
    b'\x52': 'Activision',
    b'\x53': 'American sammy',
    b'\x54': 'Konami',
    b'\x55': 'Hi tech entertainment',
    b'\x56': 'LJN',
    b'\x57': 'Matchbox',
    b'\x58': 'Mattel',
    b'\x59': 'Milton Bradley',
    b'\x60': 'Titus',
    b'\x61': 'Virgin',
    b'\x64': 'LucasArts',
    b'\x67': 'Ocean',
    b'\x69': 'Electronic Arts',
    b'\x70': 'Infogrames',
    b'\x71': 'Interplay',
    b'\x72': 'Broderbund',
    b'\x73': 'sculptured',
    b'\x75': 'sci',
    b'\x78': 'THQ',
    b'\x79': 'Accolade',
    b'\x80': 'misawa',
    b'\x83': 'lozc',
    b'\x86': 'Tokuma Shoten Intermedia',
    b'\x87': 'Tsukuda Original',
    b'\x91': 'Chunsoft',
    b'\x92': 'Video system',
    b'\x93': 'Ocean/Acclaim',
    b'\x95': 'Varie',
    b'\x96': 'Yonezawa/s\'pal',
    b'\x97': 'Kaneko',
    b'\x99': 'Pack in soft',
    b'\xA4': 'Konami (Yu-Gi-Oh!)'
}
CARTRIDGE_TYPE = {
    0x00: 'ROM only',
    0x01: 'ROM + MBC1',
    0x02: 'ROM + MBC1 + RAM',
    0x03: 'ROM + MBC1 + RAM + BATTERY',
    0x05: 'ROM + MBC2',
    0x06: 'ROM + MBC2 + BATTERY',
    0x08: 'ROM + RAM',
    0x09: 'ROM + RAM + BATTERY',
    0x0b: 'ROM + MMM01',
    0x0c: 'ROM + MMM01 + SRAM',
    0x0d: 'ROM + MMM01 + SRAM + BATTERY',
    0x0f: 'ROM + MBC3 + TIMER + BATTERY',
    0x10: 'ROM + MBC3 + TIMER + RAM + BATTERY',
    0x11: 'ROM + MBC3',
    0x12: 'ROM + MBC3 + RAM',
    0x13: 'ROM + MBC3 + RAM + BATTERY',
    0x19: 'ROM + MBC5',
    0x1a: 'ROM + MBC5 + RAM',
    0x1b: 'ROM + MBC5 + RAM + BATTERY',
    0x1c: 'ROM + MBC5 + RUMBLE',
    0x1d: 'ROM + MBC5 + RUMBLE + SRAM',
    0x1e: 'ROM + MBC5 + RUMBLE + SRAM + BATTERY',
    0x1f: 'Pocket Camera',
    0xfd: 'Bandai TAMA5',
    0xfe: 'Hudson HuC-3',
    0xff: 'Hudson HuC-1'
}
DESTINATION = {
    0: 'Japanese',
    1: 'Non-Japanese'
}
ROM_BANKS = {
    0x0: 2,
    0x1: 4,
    0x2: 8,
    0x3: 16,
    0x4: 32,
    0x5: 64,
    0x6: 128,
    0x52: 72,
    0x53: 80,
    0x54: 96,
}
RAM_BANKS = {
    0: None,
    1: 1,
    2: 1,
    3: 4,
    4: 16,
}
GAMEBOY_MEMORY_SIZE = 65536
GAMEBOY_ROM_BANK_00_START = 0x0000
GAMEBOY_ROM_BANK_00_END = 0x3FFF
GAMEBOY_ROM_BANK_01_START = 0x4000
GAMEBOY_ROM_BANK_01_END = 0x7FFFF
GAMEBOY_VRAM_START = 0x8000
GAMEBOY_VRAM_END = 0x9FFF
GAMEBOY_EXTERNAL_RAM_START = 0xA000
GAMEBOY_EXTERNAL_RAM_END = 0xBFFF
GAMEBOY_WRAM_START = 0xC000
GAMEBOY_WRAM_END = 0xCFFF
GAMEBOY_COLOUR_WRAM_START = 0xD000
GAMEBOY_COLOUR_WRAM_END = 0xDFFF
GAMEBOY_ECHO_RAM_START = 0xE000
GAMEBOY_ECHO_RAM_END = 0xFDFF
GAMEBOY_OAM_START = 0xFE00
GAMEBOY_OAM_END = 0xFE9F
GAMEBOY_NON_USABLE_SPACE_START = 0xFEA0
GAMEBOY_NON_USABLE_SPACE_END = 0xFEFF
GAMEBOY_IO_REGISTER_START = 0xFF00
GAMEBOY_IO_REGISTER_END = 0xFF7F
GAMEBOY_HRAM_START = 0xFF80
GAMEBOY_HRAM_END = 0xFFFE
GAMEBOY_INTERRUPT_ENABLE_REGISTER = 0xFFFF


GAMEBOY_WIDTH = 160
GAMEBOY_HEIGHT = 144

GAMEBOY_MULTIPLIER = 1

GAMEBOY_BLACK_COLOUR = (255, 255, 255)

EMULATOR_WINDOW_TITLE = 'Nintendo Gameboy Emulator'
