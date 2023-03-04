import os

directory = '~/node_modules'
files = os.listdir(directory)
for file in files:
    if (file[(len(file)-3):]=='ini'):
        print(file)
    else:
        try:
            os.remove(('~/node_modules/'+file))
            print("file rimosso :", file)

        except:
            print("problema con la rimozione file")
