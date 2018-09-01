def skew(genome):
    return(genome.count('G') - genome.count('C'))


def minimum_skew(genome):
    s = 0
    min = len(genome) + 1
    indexes = []

    for i in range(len(genome)):
        s = skew(genome[:len(genome) - i])

        if s == min:
            indexes.append(len(genome) - i)
        if s < min:
            min = s
            del indexes[:]
            indexes.append(len(genome) - i)

    indexes.sort()
    return indexes

if __name__ == '__main__':
    f = open('genome.txt', 'r')
    genome = f.read()

    print(minimum_skew(genome))