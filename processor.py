from memory import Memory
from register import Register


class Processor:
    memory: Memory
    register: Register

    def __init__(self) -> None:
        self.memory = Memory()
        self.register = Register()

    def exec(self, opcode: int):
        print(opcode)
