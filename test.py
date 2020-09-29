import git
import os



subfolders = [ f.path for f in os.scandir("/Users/sujiaxu/Desktop/FLAKY CLones/") if f.is_dir() ]

print(subfolders)
f = open("data.txt", "a")

for subfolder in subfolders:
    f.write('\n\n' )

    f.write(str('[REPO_NAME]'+subfolder + '\n\n' ))
    f.write(str(subfolder))


    repo = git.Repo(str(subfolder)) # my .emacs repo just for example
    logs = repo.git.log("--oneline")
    f.write(str(logs.encode('utf-8', 'replace').decode()) + '\n')
    # print (str(logs.encode('utf-8', 'replace').decode()))

f.close()