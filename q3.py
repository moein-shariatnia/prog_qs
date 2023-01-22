
def main(array):
    pos_item = list(enumerate(array))
    pos_item = sorted(pos_item, key=lambda x: x[1])
    seen = {i: 0 for i in range(len(array))}
    
    output = 0
    for i in range(len(array)):
        if seen[i] or pos_item[i][0] == i: continue
 
        rotation = 0
        j = i
        while not seen[j]:
            seen[j] += 1
            j = pos_item[j][0]
            rotation += 1
 
        if rotation > 0:
            output += (rotation - 1)
 
    return output

if __name__ == '__main__':
    array = [7, 1, 3, 2, 4, 5, 6]
    print(main(array))