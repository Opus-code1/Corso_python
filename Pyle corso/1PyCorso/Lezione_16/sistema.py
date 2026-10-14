# MANIPOLAZIONE DEL SISTEMA OPERATIVO
'''
os: Permette di interagire con i file system 
e altre funzionalità del sistema operativo

shutil: Shell-Utility -> Fornisce operazioni avanzate su file e directory

subprocess: Permette di eseguire i comandi del sistema e interagire 
anche con programmi esterni

pathlib: permette di manipolare i percorsi in una maniera molto orientata
'''
def opsys():
    # OS
    import os
    # ottenere il percorso file del nostro progetto getcwd()
    print(f"percorso file attuale-> {os.getcwd()}")

    # cambiare il percorso file chdir()
    os.chdir("C:/Users/avare/Desktop")
    print(f"percorso file attuale-> {os.getcwd()}")

    # elencare una directory listdir()
    files = os.listdir()
    print(files)

    # creare una directory mkdir()
    os.mkdir("eliminami")
    # rimuovere una directory rmdir()
    os.rmdir("eliminami")

    # verifica se esiste (file o cartella)
    if os.path.exists("AB"):
        pass#os.rmdir("AB")
    else:
        pass#os.mkdir("AB")
    if not os.path.exists("remove.txt"):
        file = open("remove.txt", "x")
        file.close()
    else:
        # Eliminare un FILE con os.remove()
        os.remove("remove.txt")

    # Creo la cartella e dentro la cartella creo un file
    # os.mkdir("prova")
    # file = open("C:/Users/avare/Desktop/prova/file.txt", "x")
    try:
        os.removedirs("prova")
    except Exception as r:
        print('Errore: ', r)

    # Vedere le statistiche su un file con os.stat()
    info = os.stat("A")
    print(info)

    # Unire i percorsi file os.path.join()
    percorso = os.path.join("prova", "BugFix.txt")
    print(percorso)

    # Cambiare il nome di un file/directory con os.rename()
    #            da    ->    a
    #os.rename("prova", "nuovo_nome")
    #os.rename("nuovo_nome", "prova")

    # Controllare se un percorso è un file con os.path.isfile()
    if os.path.isfile("BugFix.txt"):
        print("si")
    else:
        print("no")

    # Controllare se un percorso è una directory con os.path.isdir()
    if os.path.isdir("prova"):
        print("si")
    else:
        print("no")

    # Bloccare il programma con os.exit()
    '''
    x = 10
    while True:
        print(x)
        x -= 1
        os._exit(True)
    print("Finale")

    '''

def sh():
    import shutil
    import os
    # mi sposto sul desktop
    os.chdir("C:/Users/avare/Desktop")
    #---------------------------------
    # Copiare un file con shutil.copy() e con shutil.copy2() <- metadati
    shutil.copy("C:/Users/avare/Desktop/BugFix.txt", "C:/Users/avare/Desktop/nuovo.json")
    shutil.copy2("C:/Users/avare/Desktop/BugFix.txt", "C:/Users/avare/Desktop/nuovo.json")
    
    # Copiare il contenuto di una directory shutil.copytree()
    #shutil.copytree("nome_dir", "nuovo_nome_dir")
    
    # Spostare una directory o file con shutil.move()
    
    try:#          cosa -> dove
        shutil.move("due", "uno")
    except Exception as r:
        print(f'Errore: {r}')
    finally:
        if os.path.exists("uno"):
            # Rimuovere una cartella con shutil.rmtree()
            shutil.rmtree("uno")
        else:
            pass
    
    # Creare un archivio Zip con shutil.make_archive() : solo cartelle non i file
    #shutil.make_archive("nome_zip", "zip", "D")
    
    # Estrarre un archivio zip con shutil.unpack_archive()
    #shutil.unpack_archive("nome_zip.zip", "new")
    
    # Vedere lo spazio disponibile su un disco con shutil.disk_usage()
    spazio = shutil.disk_usage('/')
    print(spazio)
    
    # Cambiare i permessi di un file con shutil.chown()
    #shutil.chown("quale file.txt", user="quale utente")

def subp():
    import subprocess
    import os
    # mi sposto sul desktop
    os.chdir("C:/Users/avare/Desktop")
    
    # aprire un file o un software con subprocess.Popen()
    subprocess.Popen("notepad")
    # aprire un file con un software con subprocess.Popen()
    subprocess.Popen(["notepad", "BugFix.txt"])

def pathl():
    from pathlib import Path
    # creare un percorso con Path()
    percorso = Path("creare/il/percorso")
    print(percorso)
    
    # Creare una cartella
    #Path("nome cartella").mkdir()
    
    # Eliminare un file
    #Path("nome file.txt").unlink()
    
    # Possiamo ottenere l'estensione di un file
    #ext = Path("nome_file").suffix

def eserc_1():
    import os
    nome = input("Nome Cartella: ")
    if os.path.exists(nome):
        print("La cartella esiste")
        el = input("Eliminare?\ns/n\n-> ").lower()
        if el == "s":
            nome_e = input("Quale cartella vuoi eliminare?\n-> ")
            os.rmdir(nome_e)
        else:
            pass
    else:
        print("Cartella non esiste\nVuoi crearla?\ns/n")
        crea = input("-> ").lower()
        if crea == "s":
            nome_c = input("Come la vuoi chiamare?\n-> ")
            # creo la cartella
            os.mkdir(nome_c)
        else:
            pass
























