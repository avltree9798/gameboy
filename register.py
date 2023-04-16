class Register:
    Z_FLAG: int = 0x80
    N_FLAG: int = 0x40
    H_FLAG: int = 0x20
    C_FLAG: int = 0x10

    A: int = 0x00
    B: int = 0x00
    C: int = 0x00
    D: int = 0x00
    E: int = 0x00
    F: int = 0x00
    H: int = 0x00
    L: int = 0x00
    PC: int = 0x00
    SP: int = 0x00

    def set_AF(self, word: int):
        self.A = (word >> 8) & 0xFF
        self.F = word & 0xF0

    def set_BC(self, word: int):
        self.B = (word >> 8) & 0xFF
        self.C = word & 0xF0

    def set_DE(self, word: int):
        self.D = (word >> 8) & 0xFF
        self.C = word & 0xF0

    def set_HL(self, word: int):
        self.H = (word >> 8) & 0xFF
        self.L = word & 0xF0

    def get_AF(self) -> int:
        return ((self.A << 8) + self.F) & 0xFFF0

    def get_BC(self) -> int:
        return (self.B << 8) + self.C

    def get_DE(self) -> int:
        return (self.D << 8) + self.E

    def get_HL(self) -> int:
        return (self.H << 8) + self.L

    def is_z_flag_set(self) -> bool:
        return self.F & self.Z_FLAG == self.Z_FLAG

    def is_n_flag_set(self) -> bool:
        return self.F & self.N_FLAG == self.N_FLAG

    def is_c_flag_set(self) -> bool:
        return self.F & self.C_FLAG == self.C_FLAG

    def is_h_flag_set(self) -> bool:
        return self.F & self.H_FLAG == self.H_FLAG

    def set_z_flag(self):
        self.F |= self.Z_FLAG

    def reset_z_flag(self):
        self.F &= self.Z_FLAG ^ 0xFF

    def set_n_flag(self):
        self.F |= self.N_FLAG

    def reset_n_flag(self):
        self.F &= self.N_FLAG ^ 0xFF

    def set_c_flag(self):
        self.F |= self.C_FLAG

    def reset_c_flag(self):
        self.F &= self.C_FLAG ^ 0xFF

    def set_h_flag(self):
        self.F |= self.H_FLAG

    def reset_h_flag(self):
        self.F &= self.H_FLAG ^ 0xFF
