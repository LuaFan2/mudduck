from server.assets.manager import Assets
from server.forms.form import Form


class StartupForm(Form):

    Name = "StartupForm"

    def OnCommand(self, client, cmd):
        if cmd == 'hello':
            print("Hi")

    def Invoke(self, client):
        client.send(Assets.getstring("welcome_text"))
