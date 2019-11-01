from miniboa import TelnetServer

from server.system.MudServer import MudServer


class Server:

    def run(self):
        server = MudServer()

        telnet_server = TelnetServer(port=7777,
                                     address='',
                                     on_connect=server.on_connect,
                                     on_disconnect=server.on_disconnect,
                                     timeout=.05)

        while server.SERVER_RUN:
            telnet_server.poll()
            server.kick_idle()
            server.process_clients()
