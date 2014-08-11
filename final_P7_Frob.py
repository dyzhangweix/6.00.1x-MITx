class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    if atMe.myName()<newFrob.myName():
        pre = atMe
        while pre.getAfter()!=None and pre.getAfter().myName()<newFrob.myName():
            pre=pre.getAfter()
        newFrob.setAfter(pre.getAfter())
        newFrob.setBefore(pre)
        if pre.getAfter()!=None:
            pre.getAfter().setBefore(newFrob)
        pre.setAfter(newFrob)
    else:
        aft=atMe
        while aft.getBefore()!=None and aft.getBefore().myName()>newFrob.myName():
            aft=aft.getBefore()
        newFrob.setAfter(aft)
        newFrob.setBefore(aft.getBefore())
        if aft.getBefore()!=None:
            aft.getBefore().setAfter(newFrob)
        aft.setBefore(newFrob)
