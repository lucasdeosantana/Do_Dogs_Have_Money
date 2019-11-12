from FunctionsGeneral import LanguagePacket
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

Constructor_Borders = 1
class InitScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

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
    def build(self):
        self.load_kv('DDHM.kv')
        Screens = ScreenManager()
        Screens.add_widget(InitScreen(name='DBscreen'))
        Screens.add_widget(CreateUser(name='UserCreator'))
        Screens.add_widget(LoginPage(name='LoginPage'))
        Screens.add_widget(Home(name='Home'))
        return Screens


if __name__ == '__main__':
    DDHMapp().run() 
