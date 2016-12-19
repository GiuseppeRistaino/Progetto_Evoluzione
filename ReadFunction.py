file = open("parsed.txt", 'r')
fileRes = open("classList.txt", 'w')
functionList = []

for line in file:
    elem = line.split("|")
    if elem[1].__contains__("."):
        function1 = elem[1].split(".")[1].strip()
        if function1 not in functionList:
            functionList.append(function1)
    if elem[3].__contains__("."):
        function2= elem[3].split(".")[1].strip()
        if function2 not in functionList:
            functionList.append(function2)

print("Numero di funzioni :" +str(len(functionList)))