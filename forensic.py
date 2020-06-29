suspects = {"Eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
            "Larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
            "Matej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
            "Miha": ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}

with open("dna.txt", "r") as dna_file:
        dna = dna_file.read()

for thief in suspects:
    arrest = True
    for x in suspects[thief]:
        if x not in dna:
            arrest = False
            break
    else:
            print(thief)
