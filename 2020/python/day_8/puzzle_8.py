import re
from typing import List

with open("./day_8/data.txt") as f:
    instructions = f.read().splitlines()


def execute(instructions: List[str]):
    acc = 0
    ip = 0
    visited_ip = set()

    while ip < len(instructions):
        if ip in visited_ip:
            return acc, False

        instruction = instructions[ip]
        visited_ip.add(ip)

        op, param = instruction.split()
        param = int(param)

        if op == 'jmp':
            ip += param
            continue

        if op == 'acc':
            acc += param
        elif op == 'nop':
            pass
        else:
            raise RuntimeError()
        
        ip += 1

    return acc, True


result, _ = execute(instructions)
print('Accumulator after loop detection', result)


def execute_repair(instructions: List[str]):
    index = 0
    acc, success = execute(instructions)

    while not success:
        # Change back modified instruction
        if index > 0:
            instruction = instructions[index]
            if 'jmp' in instruction:
                instructions[index] = instruction.replace('jmp', 'nop')
            elif 'nop' in instruction:
                instructions[index] = instruction.replace('nop', 'jmp')

        index, instruction = next(
            (index, instruction) for index, instruction in enumerate(instructions[index+1:], index + 1)
            if 'jmp' in instruction or 'nop' in instruction
        )

        if 'jmp' in instruction:
            instructions[index] = instruction.replace('jmp', 'nop')
        elif 'nop' in instruction:
            instructions[index] = instruction.replace('nop', 'jmp')

        acc, success = execute(instructions)

    return acc


result = execute_repair(instructions)
print('Accumulator after loop fix', result)