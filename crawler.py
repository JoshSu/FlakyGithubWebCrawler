

import urllib.request
import json


#
# def getAllcommits(owner, repo):
#     url = 'https://api.github.com/repos/' + str(owner) + '/' + str(repo)+ '/' + 'commits'
#     print(url)
#     content = urllib.request.urlopen(url).read()
#     print(content)
#     jsonContent = json.loads(content)
#     retList = []
#     for i in range(0, len(jsonContent)):
#         retList.append(jsonContent[i]['sha'])
#     return (url,retList)
#
# def getCommitMessagesForThisRepo(url, commitSHAListForThisRepo):
#
#     for sha in commitSHAListForThisRepo:
#         newURL = str(url) +str('/')+ str(sha)
#         content = urllib.request.urlopen(newURL).read()
#         jsonContent = json.loads(content)
#         message = jsonContent['commit']['message']
#         print(message)

def getRepoAndAuthorForTable():
    file1 = open('URLs.txt', 'r')
    Lines = file1.readlines()
    ret = []
    for line in Lines:
        # print(line)
        # print( line[0: len(line) - 1])

        ret.append(line[0: len(line) - 1] + '.git')

    f = open("demofile2.txt", "a")
    for line in ret:
        f.write(line + '\n')
    f.close()

    print(ret)

getRepoAndAuthorForTable()
# auth = "curl -u joshsu https://api.github.com/user"
# urllib.request.urlretrieve(auth)
#
# getRepoAndAuthorForTable()
# url, commitSHAListForThisRepo = getAllcommits('numpy', 'numpy')
# getCommitMessagesForThisRepo(url, commitSHAListForThisRepo)


# contents = urllib.request.urlopen("https://api.github.com/repos/numpy/numpy/commits/6525ed58f1757092d73f33ee8717be2b5988c3e8").read()
# realcontent = json.loads(contents)
#
#
#
#
# print(realcontent['commit']['message'])

# curl -u joshsu https://api.github.com/user