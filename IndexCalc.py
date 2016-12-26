import WriteClass
import BuildPath
import FindFile
import os


def calcIndex(file1,file2, Fc, filewrite):

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
    filewrite.write("Fc="+str(Fc))


def diffClasses(release1, release2):

    numDiff = 0

    classListPath = projectPath + "num_Class\\"
    classList = os.listdir(classListPath)[numFile]

    fileClass = open(classListPath + classList, 'r')

    for line in fileClass:
        pureLine = line.strip()
        file1 = FindFile.findFile(pureLine + ".*", release1)
        file2 = FindFile.findFile(pureLine + ".*", release2)

        if file1 is not None and file2 is not None:
            with open(file1) as f:
                t1 = f.read().splitlines()
                t1s = set(t1)

            with open(file2) as f:
                t2 = f.read().splitlines()
                t2s = set(t2)

            findDiff = False

            print(file1)
            print(file2)
            # in file1 but not file2
            print("Only in file1")
            for diff in t1s - t2s:
                findDiff = True
                print(t1.index(diff), diff)

            if findDiff is False:
                # in file2 but not file1
                print("Only in file2")
                for diff in t2s - t1s:
                    findDiff = True
                    print(t2.index(diff), diff)

            if findDiff:
                numDiff += 1
        else:
            print("il file non è presente in entrambe le release")

    print(numDiff)
    return numDiff


listFile=[]
dirIndex="dirIndex\\"
projectList = os.listdir(BuildPath.ROOT_PATH)
for project in projectList:
    projectPath = BuildPath.ROOT_PATH + project +"\\"
    dir=projectPath+WriteClass.DIR_CLASS
    path_dirindex=BuildPath.create_directory(projectPath,dirIndex)
    fileparsed = os.listdir(dir)
    fileIndex=BuildPath.create_file(path_dirindex,"fileIndex.txt")

    releasePath = projectPath + "release\\"
    releaseList = os.listdir(releasePath)

    numFile=0
    while numFile<len(fileparsed):
        if numFile+1<len(fileparsed):
            Fc = diffClasses(releasePath + releaseList[numFile], releasePath + releaseList[numFile + 1])
            calcIndex(dir+fileparsed[numFile],dir+fileparsed[numFile+1], Fc, fileIndex)

        numFile+=1


