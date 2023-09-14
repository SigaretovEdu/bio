import json
from operator import itemgetter

file = "allignment.json"

with open(file, 'r') as f:
    data = json.load(f)['BlastOutput2']

d = dict()
top10 = dict()

for i in range(len(data)):
    hits = data[i]['report']['results']['search']['hits']
    max_identity = 0
    sciname = ""
    hits_list = []

    for j in range(len(hits)):
        tmp = hits[j]['hsps'][0]['identity']
        hits_list.append((tmp, hits[j]['description'][0]['sciname']))
        if tmp > max_identity:
            max_identity = tmp
            sciname = hits[j]['description'][0]['sciname']
    
    if sciname in d.keys():
        d[sciname] += 1
    else:
        d[sciname] = 1

    print(i + 1, sciname, sep="\t")

    hits_list.sort(key = lambda x: x[1])
    for i in range(min(len(hits_list), 10)):
        if hits_list[i][1] in top10:
            top10[hits_list[i][1]] += 1
        else:
            top10[hits_list[i][1]] = 1

print()
for k, v in sorted(d.items(), key=itemgetter(1), reverse=True):
    if k != "":
        print(f"{k:<30}{v:>5}%")


print()
print("TOP 10\n")
for k, v in sorted(top10.items(), key=itemgetter(1), reverse=True):
    if k != "":
        print(f"{k:<35}{v:>5}")
