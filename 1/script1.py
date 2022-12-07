
def main ():
    with open('data.txt', 'r') as f:
        listlist = [[]]
        for line in f:
            if not line.startswith('\n'):
                listlist[-1].append(int(line))
            else:
                listlist.append([])


    print(max([sum(inner) for inner in listlist]))


if __name__ == '__main__':
    main()
