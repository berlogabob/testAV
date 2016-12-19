#'''
s = open("testo.dat").read()
s = s.replace(',', '.')
#s = s.replace('\n', ', ')
s = s.replace('    ', '\t')
sstr = s.replace('\r', '')
f = open("testo.dat", 'w')
f.write(s)
f.close()


#'''


lines = open('testo.dat').readlines()
print lines
#open('testo.dat', 'w').writelines(lines[])

