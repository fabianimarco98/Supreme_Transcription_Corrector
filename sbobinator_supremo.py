import json
import os
import base64

def load_dict_from_json(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)
    
def save_dict_to_json(words_to_replace, json_path):
    with open(json_path, 'w') as f:
        json.dump(words_to_replace, f, indent=4)

def convert_text(text, words_to_replace):
    words = text.split()
    corrected_text = []
    for word in words:
        if word in words_to_replace:
            corrected_text.append(words_to_replace[word])
        else:
            corrected_text.append(word)
    return ' '.join(corrected_text)

def convert_file(input_file, output_file, words_to_replace):
    with open(input_file, 'r', encoding='utf-8') as f:
        input_text = f.read()
    output_text = convert_text(input_text, words_to_replace)
    with open(output_file, 'w') as f:
        f.write(output_text)

def update_dict(words_to_replace, word, replacement):
    if word not in words_to_replace:
        words_to_replace[word] = replacement
        print("Word added successfully!")
    else:
        print("Word already present in the dictionary!")

def main():
    json_path = input("Enter the path of the JSON file: ")
    words_to_replace = load_dict_from_json(json_path)

    x = True
    while x:
        choice = int(input("1. Convert text?\n2. Add word to dictionary?\n3. Delete word from dictionary?\n4. Exit\nChoice: "))
        if choice == 1:
            input_file = input("Enter the path of the input file: ")
            output_file = input("Enter the path of the output file: ")
            convert_file(input_file, output_file, words_to_replace)
            print("File converted successfully!")
        elif choice == 2:
            word = input("Enter word to replace: ")
            replacement = input("Enter replacement word: ")
            update_dict(words_to_replace, word, replacement)
            save_dict_to_json(words_to_replace, json_path)
        elif choice == 3:
            word = input("Enter word to delete: ")
            if word in words_to_replace:
                del words_to_replace[word]
                print("Word deleted successfully!")
                save_dict_to_json(words_to_replace, json_path)
            else:
                choice2 = input("Word not present in the dictionary!\nDo you want to add it (Y/N)?: ")
                if choice2.capitalize() == "Y":
                    replacement = input("Enter replacement word: ")
                    update_dict(words_to_replace, word, replacement)
                    save_dict_to_json(words_to_replace, json_path)
        elif choice == 4:
            print("Exiting...")
            x = False

if __name__ == "__main__":
    main()
