import os,fnmatch
def findFile(filename,releasepath):
    filesearch=None
    for path,dirs,files in os.walk(os.path.abspath(releasepath)):
        for filename in fnmatch.filter(files,filename):
            filesearch=os.path.join(path,filename)
    return filesearch


