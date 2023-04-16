from config import GAMEBOY_MEMORY_SIZE


class Memory:
    memory: list = [0x00 for _ in range(GAMEBOY_MEMORY_SIZE)]

    def load(self, data, offset, start=0, end=0xFFFF):
        for i in range(max(0, start), min(len(data), end)):
            self.memory[i + offset] = data[i]

    def read_byte(self, addr: int):
        return self.memory[addr]

    def read_word(self, addr: int):
        return (self.memory[addr] | (self.memory[addr + 1] << 8))

    def memdump(self):
        with open("memdump.hex", mode='wb') as f:
            f.write(str(self.memory))
