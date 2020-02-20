import npyscreen

class NewFormation(npyscreen.SplitForm):
    def create(self):
        defender = self.add(npyscreen.TitleText, name="Defender:")
        midfield = self.add(npyscreen.TitleText, name="Midfield:")
        striker = self.add(npyscreen.TitleText, name="Striker:")
        self.draw_line_at = 5
        self.add(npyscreen.FixedText, name=" ", editable=False)
        self.add(npyscreen.TitleFilenameCombo, name="Load Player:", value_changed_callback=self.loadPlayer)

    def loadPlayer (self):
        pass

    def on_cancel(self):
        self.editing = False
        self.parentApp.switchFormPrevious()