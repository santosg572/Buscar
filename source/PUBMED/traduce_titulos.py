from deep_translator import GoogleTranslator

file = 'gifted_title.txt'

fil = open(file,'r')

datos = fil.readlines()

traductor = GoogleTranslator(source='en', target='es')

k = 1
for ss in datos:
  sst = ss
  ss = ss.replace('\n','')
  i = ss.find('-')
  ss = ss[i+1:]
  print(sst+'\n')
  if len(ss) > 10:
    ss2 = traductor.translate(ss)
    print(ss2+'\n')
