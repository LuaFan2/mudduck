import os
import sys

from server.forms.form import Form

FORMS = []

class FormsManager:

    def LoadForms(self):
        ss = os.listdir('server/forms/forms')
        sys.path.insert(0, 'server/forms/forms')

        for s in ss:
            __import__(os.path.splitext(s)[0], None, None, [''])
        print(Form.__subclasses__())
        for form in Form.__subclasses__():  # так как Plugin произведен от object, мы используем __subclasses__, чтобы найти все плагины, произведенные от этого класса
            f = form()  # Создаем экземпляр
            FORMS.append(f)
            f.OnLoad()  # Вызываем событие загруки этого плагина
