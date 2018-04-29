from enum import Enum


class RnaCharacter(Enum):
    A = "A"
    C = "C"
    G = "G"
    U = "U"


class DnaCharacter(Enum):
    A = "A"
    C = "C"
    G = "G"
    T = "T"


class DnaRnaCouple:
    def __init__(self, dna_character):
        self.PassedDnaCharacter = dna_character.upper()
        self.DnaCharacter = ''
        self.RnaCharacter = ''
        self.enumerate_dna_character()
        self.enumerate_rna_character()

    def enumerate_dna_character(self):
        if self.PassedDnaCharacter == "A":
            self.DnaCharacter = DnaCharacter.A
        elif self.PassedDnaCharacter == "C":
            self.DnaCharacter = DnaCharacter.C
        elif self.PassedDnaCharacter == "G":
            self.DnaCharacter = DnaCharacter.G
        elif self.PassedDnaCharacter == "T":
            self.DnaCharacter = DnaCharacter.T
        else:
            raise ValueError("Unknown DNA type")

    def enumerate_rna_character(self):
        if self.DnaCharacter == DnaCharacter.G:
            self.RnaCharacter = RnaCharacter.C
        if self.DnaCharacter == DnaCharacter.C:
            self.RnaCharacter = RnaCharacter.G
        if self.DnaCharacter == DnaCharacter.T:
            self.RnaCharacter = RnaCharacter.A
        if self.DnaCharacter == DnaCharacter.A:
            self.RnaCharacter = RnaCharacter.U


def to_rna(dna_strand):
    if isinstance(dna_strand, str):
        rna_strand = ""

        for dna_iterator in dna_strand:
            dna_rna_couple = DnaRnaCouple(dna_iterator)
            rna_strand += dna_rna_couple.RnaCharacter.value

        return rna_strand

    else:
        raise ValueError("dna_strand is not a string")
