import os

directory = 'FOLDER_PATH'
files = os.listdir(directory)
for file in files:
    if (file[(len(file)-3):]=='ini'):
        print(file)
    else:
        try:
            os.remove(('C:/Users/Riccardo/Downloads/'+file))
            print("file rimosso :", file)

        except:
            print("problema con la rimozione file")
