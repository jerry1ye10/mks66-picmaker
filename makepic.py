cols = 500 #number of columns(up to down) and measured left to right
rows = 500#number of rows(left to right) and measured up to down
max = 255

imageString = ''#declaration of image String
def header(f):#outputs the header
    f.write('p3\n')#first line of image file
    f.write(str(cols) + ' ' + str(rows) + '\n') #second line of image file(following <column#> <row#>)
    f.write(str(max) + '\n')

def genImage(f):
    for c in range(cols):
        #print(c)
        for r in range(rows):
            r = 0
            g = 0
            b = 0
            f.write(str(r) + ' ' + str(g) + ' ' + str(b) + '\t')
        f.write('\n')
f = open("pic.ppm","w")#opens image file that will be written in
header(f)
genImage(f)
f.close()#closes file
