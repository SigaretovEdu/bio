qu = "GAGAGGAGCCATGCCTAGAGTGGGATGGGCCATTGTTCATCTTCTGGCCCCTGTTGTCTGCATGTAACTTAATACCACAACCAGGCATAGGGGAAAGATT"

with open("short.fasta", 'w') as f:
    while len(qu) > 0:
        f.write(f">fragment_{len(qu)}\n")
        f.write(qu + '\n')
        qu = qu[:-1]
