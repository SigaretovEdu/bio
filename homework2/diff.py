l = []
with open("ribosomal_protein_S14.fasta") as f:
    lines = f.readlines()
    last = ''
    for line in lines:
        if line[0] == '>':
            l.append(last)
            last = ""
        else:
            last = last + line.replace('\n', '')

for item in l:
    print(item, end="\n\n")

for i in range(0, len(l)-1):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            print(i, j)