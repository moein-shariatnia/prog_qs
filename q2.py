def main(s):
    deletions = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    print(main("AAABBB"))