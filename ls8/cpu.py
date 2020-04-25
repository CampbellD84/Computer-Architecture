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
# X remove hardcoded programs
# X implement load()
# X MUL

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
        # self.cmds = {
        #     "LDI": 0b10000010,
        #     "PRN": 0b01000111,
        #     "HLT": 0b00000001
        # }

    def load(self, name_of_file):
        """Load a program into memory."""
        try:
            address = 0
            with open(name_of_file) as f:
                for ln in f:
                    split_cmt = ln.split("#")
                    num_str = split_cmt[0].strip()

                    if num_str == '':
                        continue

                    num_val = int(num_str)
                    num_val = eval(f"0b{num_val}")
                    self.ram_write(address, num_val)
                    address += 1

        except FileNotFoundError:
            print(f'{sys.argv[0]}: could not find {sys.argv[1]}')
            sys.exit(1)

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
            instruct_reg = self.ram_read(prog_count)
            arg_A = self.ram_read(prog_count + 1)
            arg_B = self.ram_read(prog_count + 2)
            if instruct_reg == 0b10000010:
                self.reg[arg_A] = arg_B
                prog_count += 3
            elif instruct_reg == 0b01000111:
                print(self.reg[arg_A])
                prog_count += 2
            elif instruct_reg == 0b10100010:
                mult_result = self.reg[arg_A] * self.reg[arg_B]
                self.reg[arg_A] = mult_result
                prog_count += 3
            elif instruct_reg == 0b10100010:
                is_cpu_running = False
            else:
                # raise Exception(f"Instruction {instruct_reg} doesn't exist")
                sys.exit()
