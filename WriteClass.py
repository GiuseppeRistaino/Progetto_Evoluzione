import os
import os.path
import BuildPath
import Parser

DIR_CLASS="num_Class\\"

def writeNumClass(fileparsed):
    file = open(fileparsed, 'r')
    filename=projectname+'-class.txt'
    complete=os.path.join(BuildPath.create_directory(projectPath,DIR_CLASS),filename)
    fileRes=open(complete,'w')
    ClassList = []
    for line in file:
        elem = line.split("|")
        ClassName1 = elem[1].split(".")[0].strip()
        ClassName2 = elem[3].split(".")[0].strip()
        if ClassName1 not in ClassList:
            ClassList.append(ClassName1)
        if ClassName2 not in ClassList:
            ClassList.append(ClassName2)


    for elem in ClassList:
        fileRes.write(elem+"\n")

projectList = os.listdir(BuildPath.ROOT_PATH)

for project in projectList:
    projectPath = BuildPath.ROOT_PATH + project +"\\"
    dir=projectPath+Parser.DIR_PARSED
    fileparsed = os.listdir(dir)
    for file in fileparsed:
        projectname = file.split("-parsed")[0].strip()
        print(projectname)

        writeNumClass(dir+"\\"+file)