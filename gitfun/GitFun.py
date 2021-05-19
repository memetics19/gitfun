import subprocess


def constants(url:str,m:str,b:str) -> str:
    cmd_remote = "git remote add origin {0}".format(url)
    cmd_commit = "git commit -m {0}".format(m)
    cmd_branch = "git checkout -b {0}".format(b)
    cmd_push = "git push origin {0}".format(b)
    return cmd_remote,cmd_push,cmd_branch,cmd_commit

def init_push(cmd_remote,cmd_commit) -> str:
    """

    :param url:str, required
    The url is passed to add a remote repo link for the git
    :return:
    str  subprocess.run("git push --set-upstream origin master ")
    which pushes all the changes to repo
    """

    print(subprocess.getoutput("git init"))
    subprocess.getoutput(cmd_remote)
    print(subprocess.getoutput("git add ."))
    try:
        if m == type(str):
            subprocess.getoutput(cmd_commit)
        elif m != type(str):
            subprocess.getoutput("git commit -m initial commit")
    except Exception as ex:
        print(ex)
    return subprocess.getoutput("git push --set-upstream origin master ")


def status():
    return subprocess.getoutput("git status")


def push_branch(cmd_commit,cmd_branch) -> str:
    try:
        subprocess.getoutput(cmd_branch)
        subprocess.getoutput("git add .")
        subprocess.getoutput(cmd_commit)
        subprocess.getoutput("git push origin {0}").fomart(push_branch)

    except Exception as ex:
        print(ex)
