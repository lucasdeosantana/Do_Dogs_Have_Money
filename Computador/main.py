from FunctionsGeneral import LanguagePacket
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

Constructor_Borders = 1
class InitScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class DDHMapp(App):
    Text = LanguagePacket()
    LanguageTex = Text.DictLanguage()
    Languagetext = 'Portuguese'
    def build(self):
        self.load_kv('DDHM.kv')
        sm = ScreenManager()
        sm.add_widget(InitScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == '__main__':
    DDHMapp().run() 