import subprocess as sp

vl = sp.check_output(['cinder', 'list']).split('\n')
lines = vl[3:-2]
for i in xrange(len(lines)):
    lines[i] = lines[i].split('|')[1].strip()

f = open('names', 'w')
for l in lines:
    f.write('%s\n' % l)
