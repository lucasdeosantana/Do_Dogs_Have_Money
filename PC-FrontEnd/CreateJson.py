import json

TextLanguages={
                'Portuguese':{
                    "FirstNameWallet":"Minha Carteira"
                },
                'English':{
                    "FirstNameWallet":"My Wallet"
                }
            }
print(json.dumps(TextLanguages))
f=open("Alltext.json", "w")
f.write(json.dumps(TextLanguages))
f.close()
