s = open("10-10-3.CSV").read()
#s = s.replace(',', '.')
#s = s.replace('\n', ', ')
s = s.replace(',', '\t')
s = s.replace('.', ',')
f = open("10-10-3b.tsv", 'w')
f.write(s)
f.close()