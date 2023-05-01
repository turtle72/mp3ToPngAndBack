import png


def ttpf():
    startingvar = input().split(' ')
    
    f = open("test.png", 'wb')

    dire = startingvar[1]

    options = []

    for item in startingvar:
        if startingvar.index(item) > 1:
            options.append(item)

    im = png.Writer(greyscale=True,width=256,height=3)

    im.write(f, [range(256),
                 range(256),
                 range(256)])

    f.close()
ttpf()