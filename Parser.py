import os
import re
import BuildPath

DIR_PARSED="dirParsed\\"

def printParsedDot(nodeToPackage, assNodes, fileName):
    file = open(fileName, 'a')
    for pair in assNodes:
        file.write(nodeToPackage[pair[0]][0])
        file.write("\t|\t")
        file.write(nodeToPackage[pair[0]][1])
        file.write("\t|\t")
        file.write(nodeToPackage[pair[1]][0])
        file.write("\t|\t")
        file.write(nodeToPackage[pair[1]][1])
        file.write("\n")


def getDotFiles(path):
    dotFiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(path)
                for name in files
                if name.endswith(".dot")
                ]
    for el in dotFiles:
        nodeToPackage = {}
        assNodes = []
        file = open(el, 'r')
        for line in file:
            packageName = re.search("label=\"(\w+\.)*", line)
            if packageName:
                methodName = re.search('\\l\w+(\.\w+)*"', line)
                nodeName = re.search("Node\d+", line)
                packageName = packageName.group().lstrip("label=\"").rstrip(".")
                methodName = methodName.group().lstrip('l').rstrip("\"")
                nodeToPackage[nodeName.group()] = [packageName, methodName]
                print(nodeToPackage[nodeName.group()])
            else:
                tmp=re.findall("Node\d+", line)
                if tmp:
                    assNodes.append(tmp)
                    print(assNodes)



        printParsedDot(nodeToPackage, assNodes,BuildPath.create_directory(projectPath,DIR_PARSED)+release +"-parsed.txt")


projectList = os.listdir(BuildPath.ROOT_PATH)

for project in projectList:
    projectPath = BuildPath.ROOT_PATH + project +"\\"
    releaseList = os.listdir(projectPath)
    for release in releaseList:
        if(release.__contains__(project)):
            finalPath = projectPath + release+"\\html"
            print(finalPath)
            getDotFiles(finalPath)

