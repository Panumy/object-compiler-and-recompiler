output_file = open("output.txt", 'r')
num = 1
for line in output_file:
    f = "{}.txt".format(num)
    newf = open(f,'w')
    s = line.replace('CreateDynamicObject(', '').replace(');','')
    s = s.strip().split(',')
    sa = "ObjectID = {}\nX = {}\nY = {}\nZ = {}\nRX = {}\nRY = {}\nRZ = {}\nVW = {}\nInterior = {}\n[End]".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8])
    newf.write(sa)
    num = num + 1
