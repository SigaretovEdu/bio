import json

with open("last.json", 'r') as f:
    data = json.load(f)["BlastOutput2"]

for i in range(len(data)):
    hits = data[i]['report']['results']['search']['hits']
    evalue = 1000

    for j in range(len(hits)):
        tmp = float(hits[j]['hsps'][0]['evalue'])
        if tmp < evalue:
            evalue = tmp

    print(100 - i, evalue)
