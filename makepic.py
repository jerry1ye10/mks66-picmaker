import random
cols = 750 #number of columns(up to down) and measured left to right
rows = 750#number of rows(left to right) and measured up to down
max = 255

imageString = ''#declaration of image String
def header(f):#outputs the header
    f.write('P3\n')#first line of image file JERRRRRRRRRRYYYYY  THIS IS P3 NOT p3
    f.write(str(cols) + ' ' + str(rows) + '\n') #second line of image file(following <column#> <row#>)
    f.write(str(max) + '\n')

def genImage(f):
    #color = 'red'
    for c in range(cols):
        #print(c)
        for r in range(rows):
            red = 0
            g = 0
            b = 0
            if random.randrange(10) == 5:
                red = random.randrange(255)
                g = random.randrange(255)
                b = random.randrange(255)
            if c <= 250:
                red = 255
            elif c <= 500:
                g = 255
            else:
                b = 255
            f.write(str(red) + ' ' + str(g) + ' ' + str(b) + ' ') # WHY ARE U USING \t instead of ' '
        f.write('\n')
f = open("pic.ppm","w")#opens image file that will be written in
header(f)
genImage(f)
f.close()#closes file
