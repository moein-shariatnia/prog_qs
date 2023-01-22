# version 1
def main_1(string, n):
    output = ''
    while True:
        if len(output) >= n:
            break
        output += string
    output = output[:n]
    return sum([1 for char in output if char == 'a'])

# version 2
def main_2(string, n):
    output = 0
    initial_a_count = sum([1 for char in string if char == 'a'])
    str_len = len(string)
    repeats = n // str_len
    residue = n % str_len
    output += repeats * initial_a_count
    residue_str = string[:residue]
    residue_a_count = sum([1 for char in residue_str if char == 'a'])
    return output + residue_a_count
    

if __name__ == '__main__':
    print(main_1('aba', 10))
    print(main_2('aba', 10))
    
        