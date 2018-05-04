class DnaStrand:
    def __init__(self, strand_string):
        self.StrandString = strand_string

class DnaStrandComparer:
    def __init__(self, strand_one, strand_two):
        self.StrandOne = strand_one
        self.StrandTwo = strand_two
        self.HammingDistance = 0

    def calculate_hamming_distance(self):
        if len(self.StrandOne.StrandString) != len(self.StrandTwo.StrandString):
            raise ValueError("The two strings of DNA are not of equal length. Hamming distance can only be calculated "
                             "with DNA strands of equal length.")
        else:
            for iterator in range(len(self.StrandOne.StrandString)):
                strand_one_letter = self.StrandOne.StrandString[iterator]
                strand_two_letter = self.StrandTwo.StrandString[iterator]
                if strand_one_letter != strand_two_letter:
                    self.HammingDistance += 1


def distance(strand_a, strand_b):
    strand_one = DnaStrand(strand_a)
    strand_two = DnaStrand(strand_b)
    strand_comparer = DnaStrandComparer(strand_one, strand_two)
    strand_comparer.calculate_hamming_distance()
    return strand_comparer.HammingDistance
