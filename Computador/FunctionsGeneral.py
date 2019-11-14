import json

class LanguagePacket:
    def __init__(self, Archive="LanguagePacket.json"):
        self.NameLanguagePack = Archive
    def DictLanguage (self):
        PackLang = open(self.NameLanguagePack, 'r', encoding='UTF-8')
        UseLanguage=json.loads(PackLang.read())
        PackLang.close()
        return UseLanguage

class FunctionsGeneral:
    def __init__(self):
        pass
    def DateFormate(self, Date):
        Day = int(Date[0:2])
        Month = int(Date[3:5])+1
        year = int(Date[6:])
        if(Month>12):
            Month = 1
            year+=1
        if(Day<10):
            day = '0'+str(Day)
        else:
            day = str(Day)
        if(Month<10):
            month = '0'+str(Month)
        else:
            month = str(Month)
        return (day+'/'+month+'/'+str(year))