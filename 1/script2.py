
def main ():
    with open('data.txt', 'r') as f:
        listlist = [[]]
        for line in f:
            if not line.startswith('\n'):
                listlist[-1].append(int(line))
            else:
                listlist.append([])


    print(sum(sorted([sum(inner) for inner in listlist], reverse=True)[0:3]))


if __name__ == '__main__':
    main()
