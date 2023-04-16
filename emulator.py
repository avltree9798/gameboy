from cartridge import Cartridge
from config import (
    EMULATOR_WINDOW_TITLE,
    GAMEBOY_BLACK_COLOUR,
    GAMEBOY_HEIGHT,
    GAMEBOY_MULTIPLIER,
    GAMEBOY_WIDTH
)
from processor import Processor
import pygame
import time


class Emulator:
    processor: Processor

    def __init__(self) -> None:
        self.processor = Processor()
        self.running = False
        self.paused = False
        self.ticks = 0
        self.cartridge = None
        pygame.init()
        self.screen = pygame.display.set_mode(
            [
                GAMEBOY_WIDTH * GAMEBOY_MULTIPLIER,
                GAMEBOY_HEIGHT * GAMEBOY_MULTIPLIER
            ]
        )
        pygame.display.set_caption(f'{EMULATOR_WINDOW_TITLE}')

    def render(self):
        self.screen.fill(GAMEBOY_BLACK_COLOUR)
        pygame.display.flip()

    def handle_event(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYUP:
                    pass
                case pygame.KEYDOWN:
                    pass

    def load(self, cartridge: Cartridge):
        self.cartridge = cartridge
        boot_rom = None
        with open('bios.rom', 'rb') as f:
            boot_rom = f.read()
        self.processor.memory.load(boot_rom, 0x0000)
        self.processor.memory.load(
            self.cartridge.buffer,
            0x0000,
            start=0x0100,
            end=0x4000
        )
        with open('logs.txt', 'w') as f:
            f.write(str(self.processor.memory.memory))
        print(self.processor.memory.read_word(0x30))
        exit()

    def run(self):
        assert isinstance(self.cartridge, Cartridge)
        self.running = True
        while self.running:
            if self.paused:
                time.sleep(10 / 1000)
                continue

            self.handle_event()
            self.render()
            self.processor.exec(1)
            self.processor.register
            self.ticks += 1

        pygame.quit()
