# Day 1:
"""
Beej Computer Emulator
​
Software that pretends to be hardware
​
Turing Complete--it can solve any problem for which there is an algorithm.
"""
​
"""
Memory--like a big array
​
"Index into the memory array" == "address" == "pointer"
"""
​
import sys
​
#memory = [0] * 256  # RAM
​
PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3    # SAVE_REG R1,37   register[1] = 37
PRINT_REG = 4   # PRINT_REG R1     print(register[1])
ADD = 5
​
memory = [
	SAVE_REG, # SAVE_REG R1,37
	1,  # <-- index into the register array
	99, # <-- value that we want to store there
	SAVE_REG,
	2,  # <-- index into the register array
	11, # <-- value that we want to store there
	ADD, # ADD R1, R2  register[1] += register[2]
	1,
	2,
	PRINT_REG,
	1,
	PRINT_BEEJ,
	HALT,
]
​
register = [0] * 8 # 8 general-purpose registers, like variables, R0, R1, R2 .. R7
​
pc = 0  # Program Counter, index of the current instruction
running = True
​
while running:
	ir = memory[pc]  # Instruction register
​
	if ir == PRINT_BEEJ:
		print("Beej!")
		pc += 1
​
	elif ir == SAVE_REG:
		reg_num = memory[pc + 1]
		value = memory[pc + 2]
		register[reg_num] = value
		pc += 3
​
	elif ir == PRINT_REG:
		reg_num = memory[pc + 1]
		print(register[reg_num])
		pc += 2
​
	elif ir == ADD:
		reg_num1 = memory[pc + 1]
		reg_num2 = memory[pc + 2]
		register[reg_num1] += register[reg_num2]
		pc += 3
​
	elif ir == HALT:
		running = False
		pc += 1
​
	else:
		print(f'Unknown instruction {ir} at address {pc}')
		sys.exit(1)

# Day 2:
## EM w Load Support:

Memory--like a big array
​
"Index into the memory array" == "address" == "pointer"
"""
​
import sys
​
PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3    # SAVE_REG R1,37   register[1] = 37
PRINT_REG = 4   # PRINT_REG R1     print(register[1])
ADD = 5
​
memory = [0] * 256
​
register = [0] * 8 # 8 general-purpose registers, like variables, R0, R1, R2 .. R7
​
# -- Load program --
filename = sys.argv[1]
​
# TODO: error checking on sys.argv
​
with open(filename) as f:
	for address, line in enumerate(f):
​
		line = line.split("#")
​
		try:
			v = int(line[0], 10)
		except ValueError:
			continue
​
		memory[address] = v
​
# -- Run loop --
​
pc = 0  # Program Counter, index of the current instruction
running = True
​
while running:
	ir = memory[pc]  # Instruction register
​
	if ir == PRINT_BEEJ:
		print("Beej!")
		pc += 1
​
	elif ir == SAVE_REG:
		reg_num = memory[pc + 1]
		value = memory[pc + 2]
		register[reg_num] = value
		pc += 3
​
	elif ir == PRINT_REG:
		reg_num = memory[pc + 1]
		print(register[reg_num])
		pc += 2
​
	elif ir == ADD:
		reg_num1 = memory[pc + 1]
		reg_num2 = memory[pc + 2]
		register[reg_num1] += register[reg_num2]
		pc += 3
​
	elif ir == HALT:
		running = False
		pc += 1
​
	else:
		print(f'Unknown instruction {ir} at address {pc}')
		sys.exit(1)

# Branch Tables
# (AKA Dispatch Tables)
​
def fun1(x, y):
	print(f"fun1 {x} {y}")
​
def fun2(x, y):
	print(f"fun2 {x} {y}")
​
def fun3(x, y):
	print(f"fun3 {x} {y}")
​
def fun4(x, y):
	print(f"fun4 {x} {y}")
​
def call_fun(n, x=None, y=None):
	"""
	if n == 1:
		fun1(x, y)
	elif n == 2:
		fun2(x, y)
	elif n == 3:
		fun3(x, y)
	elif n == 4:
		fun4(x, y)
	"""
​
	branch_table = {
		1: fun1,
		2: fun2,
		3: fun3,
		4: fun4,
		5: lambda x, y: print(f"lambda {x} {y}")
	}
​
	#f = branch_table[n]
	#f(x, y)
	branch_table[n](x, y)
​
call_fun(2, 99, 100)
call_fun(3, 2, 3)
call_fun(5, 33,44)

# Bitwise:
Bitwise Operations
------------------
Review: Boolean
if x < 10 or x > 2:
    print("foo")
x = 0
if False: 
    print("foo")
A   B    A and B
----------------
F   F       F
T   F       F
F   T       F
T   T       T
A   B    A or B
----------------
F   F       F
T   F       T
F   T       T
T   T       T
Bitwise:
A   B     A & B   Bitwise AND
----------------
0   0       0
1   0       0
0   1       0
1   1       1
A   B     A | B   Bitwise OR
----------------
0   0       0
1   0       1
0   1       1
1   1       1
  11001100
& 11110000   AND Mask
----------
  11000000
In general:
* You can use AND to clear (set to 0) bits
* You can use OR to set (set to 1) bits
Shifting
--------
Moving all bits in a number left or right.
   111001
   011100 
   001110 
   000111
   000011
Base 10, Decimal analogy:
      vv
    12345678
    23456780
    34567800
    03456780
    00345678
    00034567
    00003456
    00000345
    00000034
          ^^
      vv
    12345678
 d& 00990000  First AND
 -----------
    00340000  Then shift
    00034000
    00003400
    00000340
    00000034
       vv
ir = 0b10000010
     vv
     10000010
   & 11000000
   ----------
     10000000
     ^^
     00000010
           ^^
num_operands = (ir & 0b11000000) >> 6
how_far_to_move_pc = num_operands + 1
pc += how_far_to_move_pc
LDI R1,R2
