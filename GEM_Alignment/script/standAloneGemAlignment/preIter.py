import csv

def sumEle(key, map1, map2):
  tmp = map1[key]
  #try: tmp2 = map2[key]
  #except: tmp2 = [0,0,0,0,0,0]
  tmp2 = map2[key]
  tmp3 = []
  for i,x in enumerate(tmp):
    tmp3.extend([float(x)+float(tmp2[i])])
  return tmp3

gemAl = csv.reader(open('../ME11_initial_240322/out_CutNumber1.csv','r'))		#Starting alignment .csv
fitter = csv.reader(open('out_CutNumber1.csv','r'))		#The result from GE11.cpp alignment

gemAlMap = {}
fitterMap = {}
for l in gemAl:
  gemAlMap[l[0]] = l[1:-1]

for l in fitter:
  fitterMap[l[0]] = l[1:-1]

out = csv.writer(open("CRAFT2022_ME11Iter2_Align.csv",'w'))			#Output alignment .csv
for i in gemAlMap.keys():
  out.writerow([int(i)]+sumEle(i, gemAlMap, fitterMap))
  
