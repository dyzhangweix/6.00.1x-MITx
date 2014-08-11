class NewsStory (object):
    def __init__(self, g, t, s, su, l):
        self.g=g
        self.t=t
        self.s=s
        self.su=su
        self.l=l
    def getGuid(self):
        return self.g
    def getTitle(self):
        return self.t
    def getSubject(self):
        return self.s
    def getSummary(self):
        return self.su
    def getLink(self):
        return self.l
        
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word=word
    def isWordIn(self, text):
        import string
        import re
        word=self.word.lower()
        text=re.sub('['+string.punctuation+']', " ",  text.lower()).split()
        return word in text
        
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
class NotTrigger(Trigger):
    def __init__(self, otherTrigger):
        self.otherTrigger=otherTrigger
    def evaluate(self, story):
        return not self.otherTrigger.evaluate(story)
        
class OrTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1=t1
        self.t2=t2
    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1=t1
        self.t2=t2
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase=phrase
    def isPhraseIn(self, text):
        return self.phrase in text
    def evaluate(self, story):
        if self.isPhraseIn(story.getTitle()) or self.isPhraseIn(story.getSubject()) or self.isPhraseIn(story.getSummary()):
            return True
        else:
            return False
            
def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    result = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                result.append(story)
                break
    return result
    
def makeTrigger(triggerMap, triggerType, params, name):
    if triggerType=='TITLE':
        triggerMap[name]=TitleTrigger(params[0])
    elif triggerType=='SUBJECT':
        triggerMap[name]=SubjectTrigger(params[0])
    elif triggerType=='SUMMARY':
        triggerMap[name]=SummaryTrigger(params[0])
    elif triggerType=='NOT':
        triggerMap[name]=NotTrigger(triggerMap[params[0]])
    elif triggerType=='AND':
        triggerMap[name]=AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType=='OR':
        triggerMap[name]=OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType=='PHRASE':
        triggerMap[name]=PhraseTrigger(' '.join(params))
    return triggerMap[name]
