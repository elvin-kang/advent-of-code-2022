def get_first_unique_four(signal):
    for i in range(len(signal) - 4):
        cur = {signal[i], signal[i+1], signal[i+2], signal[i+3]}
        if len(cur) == 4:
            return i+4
       
    
    raise ValueError("No such sequence found")
        


with open('input.txt', 'r') as fin:
    signal = fin.readline().strip()

print(get_first_unique_four(signal))