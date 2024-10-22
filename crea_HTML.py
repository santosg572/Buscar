import sys

def Busca(ss=''):
 k=0
 for s in ss:
  if s == ' ':
   k = k+1
  else:
   break
 return ss[k:]

file = sys.argv[1]

fileO = file+'.html'
fil = open(fileO, 'w')

fileI = file+'.dat'
filo = open(fileI, 'r')
datos = filo.readlines()
filo.close()

fil.write('<!DOCTYPE html>\n')
fil.write('<html>\n')
fil.write('<body>\n')
text = 'text'
k = 1

for ss in datos:
 ss = ss.replace('\n','')
 if (len(ss) > 0):
  ss = Busca(ss)
  print(ss) 
  if ss[:3] == 'htt':
   ss1 = '<p><a href=' + ss + '>'+ text + str(k) + '</a></p>\n'
   fil.write(ss1)
  else:
   ss1 = '<p>' + ss + '</p>\n'
   fil.write(ss1)
  k = k+1

fil.write('</body>\n')
fil.write('</html>\n')
fil.close()



