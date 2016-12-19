import os
import os.path

def writeNumClass(fileparsed):
    file = open(fileparsed, 'r')
    #pathdirClass = 'C:\\Users\\Utente\\Desktop\\Evoluzione_Manutenzione_SW\\dotParser\\dirClass\\'
    pathdirClass = 'classParsed\\'
    filename=projectname+'-class.txt'
    complete=os.path.join(pathdirClass,filename)
    fileRes=open(complete,'w')
    #print(pathdirClass);
    #dirparsed = os.listdir(pathdirClass)
    #fileRes = open(projectname+"-class.txt", 'a')
    ClassList = []
    for line in file:
        elem = line.split("|")
        ClassName1 = elem[1].split(".")[0].strip()
        ClassName2 = elem[3].split(".")[0].strip()
        if ClassName1 not in ClassList:
            ClassList.append(ClassName1)
        if ClassName2 not in ClassList:
            ClassList.append(ClassName2)
    # for e in ClassList:
    fileRes.write("Class number is: " + str(len(ClassList)) + "\n")
    for elem in ClassList:
        fileRes.write(elem+"\n")
dir="dirParsed"
fileparsed = os.listdir(dir)
for file in fileparsed:
    projectname = file.split("-parsed")[0].strip()
    print(projectname)
    writeNumClass(dir+"\\"+file)