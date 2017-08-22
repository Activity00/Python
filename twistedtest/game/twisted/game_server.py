import argparse
import os
import sys

from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.web.resource import Resource
from twisted.web.server import Site

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


def main(args):
    from texas.game.threads.server_info_report_thread import ServerInfoReportThread
    from texas.game.twisted.factory import TexasFactory
    from texas.game.web_views.views import Api, CreateRoom
    
    factory = TexasFactory()

    endpoint = TCP4ServerEndpoint(reactor, args['game_port'])
    endpoint.listen(factory)
     

    class Debugger(Resource):
        isLeaf = True

        def __init__(self, factory):
            self.factory = factory
            super(Debugger, self).__init__()

        def render_GET(self, request):
            return '<html><body><form method="POST" target="_blank"><p><textarea name="q"></textarea></p><p><input type="submit" value="Submit" /></p></form></body></html>'.encode()

        def render_POST(self, request):
            import json # NOQA
            try:
                result = eval(request.args[b'q'][0].decode())
                return str(result).encode()
            except:
                return 'error'.encode()

    site = Site(Debugger(factory))
    endpoint = TCP4ServerEndpoint(reactor, args['debug_port'])
    endpoint.listen(site)

    api_site = Site(Api(factory))
    endpoint = TCP4ServerEndpoint(reactor, args['web_port'])
    endpoint.listen(api_site)

    # t = CheckThread(factory.room_dict)
    # t.setDaemon(True)
    # t.start()
    
    # 服务器信息汇报进程，把服务器信息写到redis去，每5秒刷新一次
    server_info_report_thread = ServerInfoReportThread(args, factory)
    server_info_report_thread.setDaemon(True)
    server_info_report_thread.start()

    reactor.run()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "texas.settings")
 
    import django
    django.setup()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('server_name')
    parser.add_argument('server_ip')
    parser.add_argument('-m', '--max_room_count', default=200, type=int, help='max room count supported', metavar='N')
    parser.add_argument('-g', '--game_port', default=8007, type=int, help='port for play game', metavar='PORT')
    parser.add_argument('-w', '--web_port', default=8008, type=int, help='port for server control', metavar='PORT')
    parser.add_argument('-d', '--debug_port', default=8009, type=int, help='port for debug', metavar='PORT')
    args = vars(parser.parse_args())

    main(args)
