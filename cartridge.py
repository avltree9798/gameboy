from config import (
    CARTRIDGE_TYPE,
    DESTINATION,
    GAMEBOY_CARTRIDGE_TYPE,
    GAMEBOY_DESTINATION,
    GAMEBOY_TITLE_START,
    GAMEBOY_TITLE_END,
    GAMEBOY_LICENSEE_START,
    GAMEBOY_LICENSEE_END,
    GAMEBOY_RAM_SIZE,
    GAMEBOY_ROM_SIZE,
    RAM_BANKS,
    ROM_BANKS,
    LICENSEE
)


class Cartridge:
    filename: str
    title: str
    type: str
    rom_size: int
    ram_size: int
    lic_code: str
    version: str
    buffer: str

    def __init__(self, filename: str) -> None:
        self.filename = filename
        with open(self.filename, 'rb') as f:
            self.buffer = f.read()
        start = GAMEBOY_TITLE_START
        end = GAMEBOY_TITLE_END
        self.title = self.buffer[start:end].decode().replace('\x00', '')
        start = GAMEBOY_LICENSEE_START
        end = GAMEBOY_LICENSEE_END
        self.licensee_code = self.buffer[start:end]
        self.type_code = self.buffer[GAMEBOY_CARTRIDGE_TYPE]
        self.destination_code = self.buffer[GAMEBOY_DESTINATION]
        self.rom_size = self.buffer[GAMEBOY_ROM_SIZE]
        self.ram_size = self.buffer[GAMEBOY_RAM_SIZE]
        self.licensee = LICENSEE[self.licensee_code]
        self.type = CARTRIDGE_TYPE[self.type_code]
        self.destination = DESTINATION[self.destination_code]
        self.rom_bank = ROM_BANKS[self.rom_size]
        self.ram_bank = RAM_BANKS[self.ram_size]
        print("HIHI")

    def __repr__(self) -> str:
        return f'<Cartridge: title={self.title} destination={self.destination} type={self.type} bytes={len(self.buffer)} RAM banks={self.ram_bank} ROM banks={self.rom_bank}>'  # noqa: E501
