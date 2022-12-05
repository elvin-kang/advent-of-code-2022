from collections import deque

class Cargo:
    """Use 1-based index input"""
    def __init__(self, cargo):
        self.cargo = cargo  # [deque()]

    def move(self, count, src, dest):
        src_col, dest_col = src - 1, dest - 1

        if count > len(self.cargo[src_col]):
            raise IndexError("Pop from empty stack")

        queue = deque()

        for _ in range(count):
            crate = self.cargo[src_col].pop()
            queue.appendleft(crate)
        
        for item in queue:
            self.cargo[dest_col].append(item)

    def get_top_of_cargo(self):
        return "".join(stack[-1] for stack in self.cargo)

    def __repr__(self):
        return "Cargo Class\n" + str(self.cargo)


def read_cargo(fin):
    line = fin.readline()
    length = len(line)
    num_stacks = (length - 3) // 4 + 1

    cargo = [deque() for _ in range(num_stacks)]

    while line != "\n":
        for stack_index, crate_index in enumerate(range(1, length, 4)):
            if line[crate_index].isnumeric() or line[crate_index] == ' ':
                continue
            cargo[stack_index].appendleft(line[crate_index])

        line = fin.readline()

    return cargo


with open('input.txt', 'r') as fin:
    cargo_input = read_cargo(fin)
    cargo = Cargo(cargo_input)

    for line in fin:
        movement = line.split()
        amount, src_col, dest_col = map(int, (movement[1], movement[3], movement[5]))
        cargo.move(amount, src_col, dest_col)
    
    print(cargo.get_top_of_cargo())
    

# Maintain Crago as row-ordering -> Rotate cargo clockwise 90 degrees
# and maintain each row as a stack.
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 