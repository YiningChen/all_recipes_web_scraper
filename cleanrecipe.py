def main():
  fname = 'data.txt'
  newfname = 'cleandata.txt'
  data = open(fname,'r')
  newdata = open(newfname,'w')

  for line in data:
    values = line.strip('\n').split('\t')
    if len(values) > 1:
      for i in range (2,6):
        values[i] = values[i].strip('mg')
      newdata.write('\n')
      newdata.write('\t'.join(values))

  data.close()
  newdata.close()

main()
