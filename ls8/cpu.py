"""CPU functionality."""

import sys

###  INVENTORY OF FILES ###

# cpu.py - CPU class and methods
# ls8.py - Instatiation of CPU class,
#   CPU.load() and CPU.run() methods

### Needs to be implemented or removed: ##
# DAY 1:
#  X properties in CPU class
#  X ram_read()
#  X ram_write()
#  X run()
#  X HLT
#  X LDI
#  X PRN

# DAY 2:
# remove hardcoded programs
# implement load()
# MUL

# DAY 3:
# Clean up run()
# System Stack

# DAY 4:
# implement CALL and RET
# Subroutine Calls


############################
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.pc = 0
        self.ram = [0] * 256
        # TEMP until full implementation
        self.cmds = {
            "LDI": 0b10000010,
            "PRN": 0b01000111,
            "HLT": 0b00000001
        }

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def run(self):
        """Run the CPU."""
        prog_count = self.pc
        is_cpu_running = True
        while is_cpu_running is True:
            instruct_reg = self.ram[prog_count]
            arg_A = self.ram[prog_count + 1]
            arg_B = self.ram[prog_count + 2]
            if instruct_reg == self.cmds["LDI"]:
                self.reg[arg_A] = arg_B
                prog_count += 3
            elif instruct_reg == self.cmds["PRN"]:
                print(self.reg[arg_A])
                prog_count += 2
            elif instruct_reg == self.cmds["HLT"]:
                is_cpu_running = False
            else:
                print("Error!")
                sys.exit(1)
