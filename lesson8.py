class Project :

    def __init__(self,name,list):
        self.name=name
        self.list=list

class Task:

    def __init__(self,name,status,team):
     self.name=name
     self.team=team
     self.status


class TeamMember:

    def __init__(self,member,listTask):
        self.member=member
        self.listTask=listTask
tm1=TeamMember("sari",t2)
tm2=TeamMember("tamar",t1)
t1 = Task("clean",True,"tamar")
t2 = Task("hw",False,"sari")
p1=Project("wed",t1)
p2=Project("the",t2)