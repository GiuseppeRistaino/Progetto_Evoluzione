import WriteClass
import BuildPath
import os


def calcIndex(file1,file2):
    release1=set(file1)
    release2=set(file2)

    unionClass=release1.union(release2)
    interClass=release1.intersection(release2)
    print("Classi tot:"+str(len(unionClass)))
    print("Classi inter:"+str(len(interClass)))
    if (len(release2-release1)>0):
        print("Classi aggiunte:"+str(len(release2-release1)))
    else:
        print("Classi rimosse="+str(len(release1-release2)))

listFile=[]
projectList = os.listdir(BuildPath.ROOT_PATH)
for project in projectList:
    projectPath = BuildPath.ROOT_PATH + project +"\\"
    dir=projectPath+WriteClass.DIR_CLASS
    fileparsed = os.listdir(dir)
    numFile=0
    while numFile<len(fileparsed):
        if numFile+1<len(fileparsed):
            calcIndex(fileparsed[numFile],fileparsed[numFile+1])
        numFile+=1

