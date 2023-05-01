

startingvar = input().split(' ')

options = []

for item in startingvar:
    if startingvar.index(item) > 1:
        options.append(item)


print(options)
