import png


def ttpf():
    global data
    
    startingvar = input().split(' ')
    
    if startingvar[1] == '-w':

        dire = startingvar[2]
        
        data = ()
        
        with open(dire,"r") as f:
            data = f.read

        options = []

        for item in startingvar:
            if startingvar.index(item) > 2:
                options.append(item)



        f = open("test.png", 'wb')
        
        im = png.Writer(greyscale=True,width=3840,height=2160,background=(1,))

        im.write(f, [range(1,256),
                    range(1,256),
                    range(1,256)])

        f.close()
    if startingvar[1] == '-r':
        print("reading")
        
    else: ttpf()
    
ttpf()
print(data)