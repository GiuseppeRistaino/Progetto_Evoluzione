
import os

ROOT_PATH="ProjectAnalysis\\"

def create_directory(finalPath,nameDirectory):
    newpath=finalPath+nameDirectory
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath
