def to_rna(dna_strand):
    rna = ''
    if len(dna_strand) == 0:
        return rna
    for i in range(0, len(dna_strand)):
        if dna_strand[i] == "G":
            rna = rna + 'C'
        elif dna_strand[i] == "C":
            rna = rna + 'G'
        elif dna_strand[i] == "T":
            rna = rna + 'A'
        else:
            rna = rna + 'U'
    return rna
