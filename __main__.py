import npyscreen
from formation import NewFormation

class Content(object):
    HOST="localhost"
    PORT="6000"
    FORMATION="4-4-2"

class Main(npyscreen.FormWithMenus):
    def create(self):
        self.keypress_timeout = 1
        self.host = self.add(npyscreen.TitleText, name="Host:")
        self.port = self.add(npyscreen.TitleText, name="Port:")

        self.add(npyscreen.FixedText, name=" ", editable=False)

        self.formation = self.add(npyscreen.TitleText, name="Formation:")

        mainMenu = self.add_menu(name="New", shortcut="n")
        mainMenu.addItemsFromList([
            ("New Formation", self.newFormation)
        ])

    def onStart(self):
        self.host.set_value(self.parentApp.CONTENT.HOST)
        self.port.set_value(self.parentApp.CONTENT.PORT)

    def while_waiting(self):
        pass
    
    def newFormation(self):
        self.parentApp.setNextForm("NewFormation")
        self.editing = False
        self.parentApp.switchFormNow()

class App(npyscreen.NPSAppManaged):
    CONTENT=Content()
    def onStart(self):
        self.registerForm("MAIN", Main(name="Baile de Monique TUI"))
        self.registerForm("NewFormation", NewFormation(name="New Formation"))

MyApp = App()
MyApp.run()