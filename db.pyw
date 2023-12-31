def check_login(u,p):
    read1=open("./txts/password.txt")
    passwords=read1.readlines();
    read2=open("./txts/username.txt")
    usernames=read2.readlines();
    u=u+'\n'
    p=p+'\n'
    read1.close()
    read2.close()
    if u in usernames and p in passwords and usernames.index(u)==passwords.index(p):
        return True
    return False


def add_login(u,p):
    read1=open("./txts/password.txt","a")
    read2=open("./txts/username.txt","a")
    read1.write(p)
    read1.write('\n')
    read2.write(u)
    read2.write('\n')
    read1.close()
    read2.close()