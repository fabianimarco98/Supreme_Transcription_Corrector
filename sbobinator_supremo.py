import json
import os
import base64

def load_dict_from_json(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)
    
def save_dict_to_json(words_to_replace, json_path):
    with open(json_path, 'w') as f:
        json.dump(words_to_replace, f,indent=4)

def convert_text(testo, words_to_replace):
    parole = testo.split()
    testo_con_parole_corrette = []
    for parola in parole:
        if parola in words_to_replace:
            testo_con_parole_corrette.append(words_to_replace[parola])
        else:
            testo_con_parole_corrette.append(parola)
    return ' '.join(testo_con_parole_corrette)

def converti_file(input_file, output_file, words_to_replace):
    with open(input_file, 'r', encoding='utf-8') as f:
        testo_input = f.read()
    testo_output = convert_text(testo_input, words_to_replace)
    with open(output_file, 'w') as f:
        f.write(testo_output)

def update_dict(words_to_replace, word, replacement):
    if word not in words_to_replace:
        words_to_replace[word] = replacement
        print("Parola aggiunta con successo!")
    else:
        print("Parola già presente nel dizionario!")

def main():
    json_path = input("Inserisci il percorso del file JSON: ")
    words_to_replace = load_dict_from_json(json_path)

    x = True
    while x:
        choice = int(input("1. Convertire testo?\n2. Aggiungere parola al dizionario?\n3. Eliminare parola dal dizionario?\n4.Uscita\nScelta:"))
        if choice == 1:
            input_file = input("Inserisci il percorso del file di input: ")
            output_file = input("Inserisci il percorso del file di output: ")
            converti_file(input_file, output_file, words_to_replace)
            print("File convertito con successo!")
        elif choice == 2:
            word = input("Inserisci parola da sostituire: ")
            replacement = input("Inserisci parola di sostituzione: ")
            update_dict(words_to_replace, word, replacement)
            save_dict_to_json(words_to_replace, json_path)
        elif choice == 3:
            word = input("inserisci parola da eliminare: ")
            if word in words_to_replace:
                del words_to_replace[word]
                print("Parola eliminata con successo!")
                save_dict_to_json(words_to_replace, json_path)
            else:
                choice2=input("Parola non presente nel dizionario!\n Vuoi aggiungerla (S/N)?: ")
                if choice2.capitalize()=="S":
                    replacement = input("Inserisci parola di sostituzione: ")
                    update_dict(words_to_replace, word, replacement)
                    save_dict_to_json(words_to_replace, json_path)
        elif choice ==4:
            print("Uscita...")
            x = False
if __name__ == "__main__":
    main()
