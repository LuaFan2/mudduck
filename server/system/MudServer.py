from server.forms.manager import FORMS, FormsManager


def broadcast(self, msg):
    for client in self.clients:
        client.send(msg)


class MudServer:

    def __init__(self):
        self.timeout = 300
        self.clients = []
        self.SERVER_RUN = True

        FormsManager.LoadForms(FormsManager())

    def on_connect(self, client):
        self.clients.append(client)

    def on_disconnect(self, client):
        self.clients.remove(client)

    def process_commands(self, client):
        global SERVER_RUN
        cmd = client.get_command().lower()

        for f in FORMS:
            f.OnCommand(client, cmd)

    def process_clients(self):
        for client in self.clients:
            if client.active and client.cmd_ready:
                self.process_commands(client)

    def kick_idle(self):
        """
        Looks for idle clients and disconnects them by setting active to False.
        """
        # Who hasn't been typing?
        for client in self.clients:
            if client.idle() > self.timeout:
                client.active = False
