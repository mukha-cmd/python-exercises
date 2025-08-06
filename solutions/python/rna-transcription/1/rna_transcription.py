def to_rna(dna_strand):
    rna = ("")
    for letter in dna_strand:
        if letter == "A":
            rna += "U"
        if letter == "T":
            rna += "A"
        if letter == "C":
            rna += "G"
        if letter == "G":
            rna += "C"
    return rna
