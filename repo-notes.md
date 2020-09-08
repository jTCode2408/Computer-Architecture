FILES/FOLDERS:
-LS8-spec.md
  --FULL range specs about microcomputer being built/used
    TOPICS:
    -Registers
    -Internal Registers
    -Flags
    -Memory
    -Stack
    -Interrupts(for stretch ONLY)
    -Interrupt numbers(Stretch)
    -Power on State
    -Execution Sequence(!!!Important)
    -Instruction Layout
    -Instruction Set(Glossary!!!!!)
    --Glossary full terms, explanation of instructions

-L:S8-cheatsheet.md
  --This document is non-authoritative. In cases where it differs from the spec, the spec is correct.

-FAQ.md
  --Frequently asked questions/answers
    -Contents:

-LS8(folder)
  --Readme for project(8 bit cpu w/8 bit memory addressing)
    *8 bits, 256 bytes total, computes to 255
    -Implemenation
    -Steps(all week)
  --cpu.py
  -LDI=load immediate(store val in register, save_reg from class)
  -R0=(register# save reg from class)
  -PRN=PRint numberic val in reg(print_reg from class)
  -HLT=Halt, cpu exits emulator(from class)
    -trace fn(prints out state of cpu, good for debugging in run())
  --ls8.py(main)
    -run() here. 
    --needs to read the memory address that's stored in register PC, and store that result in IR, the Instruction Register(can be local variable in run())







