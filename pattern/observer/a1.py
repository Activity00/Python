
class Event(object):
    '''
            抽象事件
    '''
    def __init__(self,username,eventType):
        self.username=username
        self.eventType=eventType
    @property
    def username(self):
        return self.username
    @property
    def eventType(self):
        return self.eventType

class EventType(object):
    LEVEL_UP=None#角色升级
    
class LevelUpEvent(Event):
    '''具体事件'''
    def __init__(self,username,eventType):
        super(LevelUpEvent,self).__init__(username, eventType)
    
class EventListener(object):
    #事件监听接口
    def handleEvent(self,event):
        pass
    
class AttrChangeListener(EventListener):
    '''具体事件监听器'''
    def handleEvent(self, event):
        print event.username,':升级了，攻击力啥的上升了'
class SkillListener(EventListener):
    def handleEvent(self, event):
        print event.username,'技能也升级了'

class EventDispatcher():
    '''事件分发接口'''
    def registerEvent(self,eventtype,eventlistener):
        pass
    def fireEvent(self,event):
        pass

class CommonEventDispatcher(EventDispatcher):
    def registerEvent(self, eventtype, eventlistener):
        pass
'''未完待续'''
