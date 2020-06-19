"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] *256
        self.register =[0] *8
        self.pc =0
        
#Inside the CPU, there are two internal registers used for memory operations: 
 #mdr- data that was read/to write
 #mar- register address being read/written to

 #ram_read:ACCEPT ADDRESS TO READ-- and RETURNS VALUE @ address
 #ram_write:ACCEPT VALUE TO WRITE AND ADDRESS TO WRITE TO
    def ram_read(self, position):
        return self.ram[position]

    def ram_write(self, position, value):
        self.ram[position] =value


    def load(self):
        """Load a program into memory."""

        filename = f
        program = open(f"{filename}", "r")
        address = 0
        for line in program:
            if line[0] == "0" or line[0] == "1":
                command = line.split("#", 1)[0]
                self.ram[address] = int(command, 2)
                address += 1
    
        # For now, we've just hardcoded a program:

        #program = [
         #   # From print8.ls8
          #  0b10000010, # LDI R0,8
           # 0b00000000,
           # 0b00001000,
           # 0b01000111, # PRN R0
           # 0b00000000,
           # 0b00000001, # HLT
        #]

        #for instruction in program:
         #   self.ram[address] = instruction
          #  address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "MULT": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
#implement code to run
#read memory address
#store memory address in IR
##using ram_read(), read the bytes at PC+1 and PC+2 from RAM into variables operand_a and operand_b in case the instruction needs them.
#set instruction for what to do 
#set pc pointer to next instruction(depending how many bytes previous action took)
#LDI(set value of register to int)=3byte op?(register, value)
#HLT=1byte op
#PRN=2byte op?(get register, get value)
        HLT =0b00000001
        LDI =0b10000010
        PRN=0b01000111
        running =True


        while running:
            ir= self.ram_read(self.pc)
            operand_a=self.ram_read(self.pc+1)
            operand_b=self.ram_read(self.pc+2)

            if ir ==LDI:
                #LDI op:var, reg, value
                self.register[operand_a] =operand_b
                self.pc+=3
                
                #PRN op:
            elif ir == PRN:
                print(self.register[operand_a])
                self.pc+=2

            elif ir == HLT:
                running =False
                self.pc+1
                sys.exit(0)
            else:
                print(f'Unknown command {ir} at address {pc}')
                sys.exit(1)

