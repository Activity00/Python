from pydispatch import dispatcher

SIGNAL = 'my-first-signal'


def handle_event(sender, aaa):
    print(f'xxx:{sender}{aaa}')


dispatcher.connect(handle_event, signal=SIGNAL, sender=dispatcher.Any)

first_sender = object()
second_sender = {}

if __name__ == '__main__':
    dispatcher.send(signal=SIGNAL, sender=first_sender, aaa=123)
    dispatcher.send(signal=SIGNAL, sender=second_sender, aaa=332)
