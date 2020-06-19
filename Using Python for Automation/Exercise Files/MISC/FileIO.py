f = open('inputFile.txt' , 'r')
pf = open('PassFile.txt', 'w')
ff = open("FailFile.txt", 'w')
count = 0

for  line in f: 
    line_split = line.split()
    if line_split[2] == "P":
        pf.write(line)
    else:
        ff.write(line)
  
f.close()
pf.close()
ff.close()

