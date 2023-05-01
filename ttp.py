import png
from main import startingvar

dire = startingvar[1]

options = []

for item in startingvar:
    if startingvar.index(item) > 1:
        options.append(item)
print(options)
