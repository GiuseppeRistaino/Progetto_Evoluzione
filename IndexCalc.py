import WriteClass
import BuildPath
import os


def calcIndex(file1,file2,filewrite):

    release1=set(open(file1,'r'))
    release2=set(open(file2,'r'))

    filewrite.write("###########################################\n")
    filewrite.write("Indici di "+file1.__str__()+" "+file2.__str__()+" :\n")
    unionClass=release1.union(release2)
    interClass=release1.intersection(release2)
    filewrite.write("Classi totali tra le due release="+str(len(unionClass))+"\n")
    filewrite.write("Intersezione tra le classi delle due release:"+str(len(interClass))+"\n")
    filewrite.write("Mt=" + str(len(release1)) + "\n")
    filewrite.write("Mt2=" + str(len(release2)) + "\n")
    filewrite.write("Fa="+str(len(release2-interClass))+"\n")
    filewrite.write("Fd="+str(len(release1-interClass))+"\n")


listFile=[]
dirIndex="dirIndex\\"
projectList = os.listdir(BuildPath.ROOT_PATH)
for project in projectList:
    projectPath = BuildPath.ROOT_PATH + project +"\\"
    dir=projectPath+WriteClass.DIR_CLASS
    path_dirindex=BuildPath.create_directory(projectPath,dirIndex)
    fileparsed = os.listdir(dir)
    fileIndex=BuildPath.create_file(path_dirindex,"fileIndex.txt")
    numFile=0
    while numFile<len(fileparsed):
        if numFile+1<len(fileparsed):

            calcIndex(dir+fileparsed[numFile],dir+fileparsed[numFile+1],fileIndex)

        numFile+=1

