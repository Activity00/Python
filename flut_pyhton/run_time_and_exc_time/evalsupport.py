print('<100> evalsupport module start')


def deco_alpha(cls):
    print('<200> deco_alpha')

    def inner_1(self):
        print('<300> deco_alpha inner_1')

    cls.method_y = inner_1
    return cls

# BEGIN META_ALPEPH


class MetaAleph(type):
    print('<400> MetaAleph body')

    def __init__(cls, name, bases, dict):
        print('<500> MetaAleph body')

        def inner_2(self):
            print('<600> MetaAleph.__init__:inner_2')

        cls.method_z = inner_2


# END META_ALEPH

print('<700> evasupport module end')
