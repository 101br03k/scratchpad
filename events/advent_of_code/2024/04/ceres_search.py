#start met py .\ceres_search.py input
import sys
data={}
startlist=[]
startlist2=[]
with open(sys.argv[1]) as f:
  for y,line in enumerate(f.read().splitlines()):
    for x,val in enumerate(line.rstrip('\n')):
      data[(x,y)] = val
      if val == "X":
        startlist.append((x,y))
      if val == "A":
        startlist2.append((x,y))

vectors = []
for xv in range(3):
  for yv in range(3):
    vectors.append((xv-1,yv-1))
vectors.remove((0,0))
vectors2 = []

part1=0
xmas="XMAS"
for s in startlist:
   for v in vectors:
      try:
        for i in range(1,4):
          if data[(s[0]+v[0]*i,s[1]+v[1]*i)]!=xmas[i]: 
            break
        else:
          part1 += 1
      except KeyError:
        pass
print(part1)

part2=0
vectors2=[(1,1),(-1,1),(-1,-1),(1,-1)]
for s in startlist2:
   for i in ["MMSS", "MSSM", "SSMM", "SMMS"]:
      try:
        for j in range(4): 
          if data[(s[0]+vectors2[j][0],s[1]+vectors2[j][1])]!=i[j]:
            break
        else: 
           part2 += 1
        continue
      except KeyError:
        pass
print(part2)
