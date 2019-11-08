from FunctionsGeneral import LanguagePacket
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class InitScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class DDHMApp(App):
    Text = LanguagePacket()
    LanguageTex = Text.DictLanguage()
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InitScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == '__main__':
    DDHMApp().run()