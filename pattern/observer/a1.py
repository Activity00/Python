class Event(object):
    """
    抽象事件
    """

    def __init__(self, username, event_type):
        self._username = username
        self._event_type = event_type

    @property
    def username(self):
        return self._username

    @property
    def event_type(self):
        return self._event_type


class EventType(object):
    LEVEL_UP = None  # 角色升级


class LevelUpEvent(Event):
    """具体事件"""

    def __init__(self, username, event_type):
        super().__init__(username, event_type)


class EventListener(object):
    # 事件监听接口
    def handle_event(self, event):
        pass


class AttrChangeListener(EventListener):
    """具体事件监听器"""

    def handle_event(self, event):
        print(event.username, ':升级了，攻击力啥的上升了')


class SkillListener(EventListener):
    def handle_event(self, event):
        print(event.username, '技能也升级了')


class EventDispatcher:
    """事件分发接口"""

    def register_event(self, eventtype, eventlistener):
        pass

    def fire_event(self, event):
        pass


class CommonEventDispatcher(EventDispatcher):
    def register_event(self, eventtype, eventlistener):
        pass


'''未完待续'''
