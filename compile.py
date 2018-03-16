output_file = open("output.txt", 'wr')

a = 0
while a < 1000:
    a = a + 1
    b = "{}.txt".format(a)
    data = open(b, 'r').read()
    data = data.replace('ObjectID = ', 'CreateDynamicObject(').replace('\nX = ', ',').replace('\nY = ', ',').replace('\nZ = ', ',').replace('\nRX = ', ',').replace('\nRY = ', ',').replace('\nRZ = ', ',').replace('\nVW = ', ',').replace('\nInterior = ', ',').replace('\n[End]', ');')
    output_file.write(data)

