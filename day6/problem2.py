def get_first_unique_fourteen(signal):
    for i in range(len(signal) - 4):
        cur = set(signal[i:i+14])
        if len(cur) == 14:
            return i+14
    
    raise ValueError("No such sequence found")
        


with open('input.txt', 'r') as fin:
    signal = fin.readline().strip()

print(get_first_unique_fourteen(signal))