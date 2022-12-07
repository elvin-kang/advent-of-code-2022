class File:
    TOTAL_DISK_SPACE = 70000000
    THRESHOLD = 30000000

    def __init__(self, size, name, is_dir=False, parent=None):
        self.size = size
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = {}


    def calculate_sum(self, limit=100000):
        if not self.is_dir:
            return 0

        current_size = self.calculate_dir_size()
        total = 0 if current_size > limit else current_size

        for child in self.children.values():
            if child.is_dir:
                total += child.calculate_sum(limit)

        return total


    def calculate_dir_size(self):
        if not self.is_dir:
            return self.size
        else:
            file_sizes_in_current_dir = 0
            for child in self.children.values():
                if child.is_dir:
                    file_sizes_in_current_dir += child.calculate_dir_size()
                else:
                    file_sizes_in_current_dir += child.size
            
            return file_sizes_in_current_dir


    def find_directory_to_delete(self):
        current_size = self.calculate_dir_size()
        directory_sizes = self.get_all_directory_sizes()
        unused = self.TOTAL_DISK_SPACE - current_size

        smallest = float('inf')

        for size in directory_sizes:
            if unused + size >= self.THRESHOLD:
                smallest = min(smallest, size)

        return smallest


    def get_all_directory_sizes(self):
        result = []

        if not self.is_dir:
            return result

        result.append(self.calculate_dir_size())

        for child in self.children.values():
            if child.is_dir:
                result += child.get_all_directory_sizes()

        return result


    def get_description(self):
        if self.is_dir:
            return "(dir)"
        else:
            return f"(file, size={self.size})"


    def print_filetree(self, indent=""):
        print(f"{indent}- {self.name} {self.get_description()}")
        for child in self.children.values():
            child.print_filetree(indent + "  ")


    def __repr__(self):
        return f"File(name={self.name}, size={self.size}, is_dir={self.is_dir}, children={self.children}))"


def find_node(root, name):
    if root.name == name:
        return root

    for child_name, child in root.children.items():
        if child_name == name:
            return child

        find_node(child, name)

    raise FileNotFoundError("File not found!")

cur_dir = "/"

root = File(-1, "/", True)
cur = root
stack = ["/"]

with open('input.txt', 'r') as fin:
    for line in fin:
        terminal = line.strip().split()
        if terminal[0] == "$":
            cmd = terminal[1]
            if cmd == "cd":
                cur_dir = terminal[2]  # filename
                if cur_dir == "/":
                    cur = root
                    stack = ["/"]
                else:
                    name = terminal[2]  # filename
                    if name == "..":
                        stack.pop()
                        print(stack)
                        root.print_filetree()
                        cur = cur.parent
                    else:
                        stack.append(name)
                        cur = cur.children[name]
            elif cmd == "ls":
                listing = True
            else:
                raise ValueError("Invalid command")
        else:
            if terminal[0] == "dir":
                new_dir = File(-1, terminal[1], is_dir=True, parent=cur)
                cur.children[terminal[1]] = new_dir
            elif terminal[0].isnumeric():
                new_file = File(int(terminal[0]), terminal[1], False)
                cur.children[terminal[1]] = new_file
            else:
                raise ValueError("Invalid input")

# root.print_filetree()
# print()
# print(root.calculate_sum())

print(root.find_directory_to_delete())