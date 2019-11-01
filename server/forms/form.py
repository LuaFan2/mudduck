class Form(object):
    Name = 'undefined'

    def OnLoad(self):
        print("Module | {} was loaded".format(self.Name))

    def OnCommand(self, client, cmd):
        pass

    def Invoke(self, client):
        pass