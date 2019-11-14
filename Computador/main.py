from FunctionsGeneral import LanguagePacket
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

Constructor_Borders = 1
class DBscreen(Screen):
    def NextButton(self):
        DDHMapp.Screens.current = 'UserCreator'

class CreateUser(Screen):
    def nextbutton(self):
        DDHMapp.Screens.current = 'LoginPage'
    def previousbutton(self):
        DDHMapp.Screens.current = 'DBscreen'
class LoginPage(Screen):
    pass

class Home(Screen):
    pass

class Transactions(Screen):
    pass

class DDHMapp(App):
    Text = LanguagePacket()
    LanguageTex = Text.DictLanguage()
    Languagetext = 'Portuguese'
    Screens = ScreenManager()
    def build(self):
        self.load_kv('DDHM.kv')
        self.Screens.add_widget(DBscreen(name='DBscreen'))
        self.Screens.add_widget(CreateUser(name='UserCreator'))
        self.Screens.add_widget(LoginPage(name='LoginPage'))
        #Screens.add_widget(Home(name='Home'))
        return self.Screens
    def next_page(self, code):
        code()


if __name__ == '__main__':
    DDHMapp().run() 
