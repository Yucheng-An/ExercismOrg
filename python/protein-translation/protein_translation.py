def proteins(strand):
    DICT = {"AUG": "Methionine",
            "UUU": "Phenylalanine",
            "UUC": "Phenylalanine",
            "UUA": "Leucine",
            "UUG": "Leucine",
            "UCU": "Serine",
            "UCC": "Serine",
            "UCA": "Serine",
            "UCG": "Serine",
            "UAU": "Tyrosine",
            "UAC": "Tyrosine",
            "UGU": "Cysteine",
            "UGC": "Cysteine",
            "UGG": "Tryptophan",
            "UAA": "STOP",
            "UAG": "STOP",
            "UGA": "STOP"
            }
    counter = 0
    checker = ""
    res = []
    for i in strand:
        checker += i
        counter += 1
        if counter == 3:
            if DICT[checker] == "STOP":
                break
            res.append(DICT[checker])
            checker = ""
            counter = 0
    return res

