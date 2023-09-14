import random

fasta_file = "GRCh38_latest_genomic.fna"
limit = 100
queries = []

with open(fasta_file, 'r') as f:
    f.readline()
    jump = random.randrange(200) + 1
    for i in range(jump):
        f.readline()
    line = ""
    while len(queries) < limit:
        line = line + f.readline().replace('\n', '')
        if 'N' in line or 'N' in line:
            last = 0
            for i in range(len(line)):
                if line[i] == 'n' or line[i] == 'N':
                    last = i
            line = line[last+1:]
        if len(line) >= 100:
            queries.append(line[:100])
            line = ""
            jump = random.randrange(200) + 1
            for i in range(jump):
                f.readline()

assert(len(queries) == limit)

with open("result.txt", 'w') as f:
    for i in range(limit):
        echo = ">sequence{}".format(i + 1)
        f.write(echo + '\n')
        f.write(queries[i].upper() + '\n')
