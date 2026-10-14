import os
import random

class FileManager:
    def create_file(self):
        """Crea un nuovo file."""
        file_name = input("Inserisci il nome del file: ")
        with open(file_name, 'w') as file:
            print("File creato con successo!")

    def read_file(self):
        """Legge il contenuto di un file esistente."""
        file_name = input("Inserisci il nome del file da leggere: ")
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                print("Contenuto del file:\n", content)
        except FileNotFoundError:
            print("Il file non esiste.")

    def delete_file(self):
        """Elimina un file esistente."""
        file_name = input("Inserisci il nome del file da eliminare: ")
        try:
            os.remove(file_name)
            print("File eliminato con successo!")
        except FileNotFoundError:
            print("Il file non esiste.")

    def rename_file(self):
        """Rinomina un file esistente."""
        old_name = input("Inserisci il vecchio nome del file: ")
        new_name = input("Inserisci il nuovo nome del file: ")
        try:
            os.rename(old_name, new_name)
            print("File rinominato con successo!")
        except FileNotFoundError:
            print("Il file non esiste.")

class FolderManager:
    def create_folder(self):
        """Crea una nuova cartella."""
        folder_name = input("Inserisci il nome della cartella: ")
        os.makedirs(folder_name)
        print("Cartella creata con successo!")

    def delete_folder(self):
        """Elimina una cartella esistente."""
        folder_name = input("Inserisci il nome della cartella da eliminare: ")
        try:
            os.rmdir(folder_name)
            print("Cartella eliminata con successo!")
        except FileNotFoundError:
            print("La cartella non esiste.")

    def rename_folder(self):
        """Rinomina una cartella esistente."""
        old_name = input("Inserisci il vecchio nome della cartella: ")
        new_name = input("Inserisci il nuovo nome della cartella: ")
        try:
            os.rename(old_name, new_name)
            print("Cartella rinominata con successo!")
        except FileNotFoundError:
            print("La cartella non esiste.")

class PasswordGenerator:
    def generate_passwords(self):
        """Genera una o più password casuali."""
        num_passwords = int(input("Quante password creare? "))
        length = int(input("Inserisci la lunghezza della password (minimo 8, massimo 999): "))
        
        # Lista di caratteri utilizzati per generare le password
        characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/")
        
        passwords = []

        # Genera le password
        for _ in range(num_passwords):
            password = ''.join(random.choice(characters) for _ in range(length))
            passwords.append(password)

        print("Password generate:")
        for password in passwords:
            print(password)

class Menu:
    def main_menu(self):
        """Stampa il menu principale."""
        print("1-File")
        print("2-Cartelle")
        print("3-Generatore di Password")
        print("4-Esci")

    def file_menu(self):
        """Stampa il menu delle operazioni sui file."""
        print("1-Crea il file")
        print("2-Leggi il file")
        print("3-Elimina il file")
        print("4-Rinomina il file")
        print("5-Torna al Menù")

    def folder_menu(self):
        """Stampa il menu delle operazioni sulle cartelle."""
        print("1-Crea la cartella")
        print("2-Elimina la cartella")
        print("3-Rinomina la cartella")
        print("4-Torna al Menù")

    def password_generator_menu(self):
        """Stampa il menu del generatore di password."""
        print("1-Quante password creare")
        print("2-Lunghezza della password (Minimo 8 massimo 999)")
        print("3-Torna al Menù")

def main():
    # Creazione delle istanze delle classi
    file_manager = FileManager()
    folder_manager = FolderManager()
    password_generator = PasswordGenerator()
    menu = Menu()

    while True:
        menu.main_menu()
        choice = input("Inserisci la tua scelta: ")

        if choice == '1':
            while True:
                menu.file_menu()
                file_choice = input("Inserisci la tua scelta: ")

                if file_choice == '1':
                    file_manager.create_file()
                elif file_choice == '2':
                    file_manager.read_file()
                elif file_choice == '3':
                    file_manager.delete_file()
                elif file_choice == '4':
                    file_manager.rename_file()
                elif file_choice == '5':
                    break
                else:
                    print("Scelta non valida. Riprova.")

        elif choice == '2':
            while True:
                menu.folder_menu()
                folder_choice = input("Inserisci la tua scelta: ")

                if folder_choice == '1':
                    folder_manager.create_folder()
                elif folder_choice == '2':
                    folder_manager.delete_folder()
                elif folder_choice == '3':
                    folder_manager.rename_folder()
                elif folder_choice == '4':
                    break
                else:
                    print("Scelta non valida. Riprova.")

        elif choice == '3':
            while True:
                menu.password_generator_menu()
                password_choice = input("Inserisci la tua scelta: ")

                if password_choice == '1':
                    password_generator.generate_passwords()
                elif password_choice == '2':
                    print("L'opzione di impostazione della lunghezza della password non è implementata in questo esempio.")
                elif password_choice == '3':
                    break
                else:
                    print("Scelta non valida. Riprova.")

        elif choice == '4':
            print("Programma Terminato!")
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
