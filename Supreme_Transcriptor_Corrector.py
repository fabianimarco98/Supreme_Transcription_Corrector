import json
import os

def convert_sbv_to_txt(sbv_file_path):
    # Check if the .sbv file exists
    if not os.path.exists(sbv_file_path):
        print("The specified .sbv file does not exist.")
        return None
    
    # Read the content of the .sbv file
    with open(sbv_file_path, 'r', encoding='utf-8') as f:
        sbv_lines = f.readlines()

    # Remove lines containing timestamps
    filtered_lines = [line for line in sbv_lines if not line.strip().startswith('0:')]   
    # Join the remaining lines to form the .txt content
    txt_content = ' '.join(filtered_lines)

    # Ask the user for the output directory
    output_dir = input("Insert the output directory: ")
    if not os.path.exists(output_dir):
        print("The specified output directory does not exist.")
        return None
    
    # Modify the file extension for the .txt output file
    txt_file_name = os.path.splitext(os.path.basename(sbv_file_path))[0] + ".txt"
    txt_file_path = os.path.join(output_dir, txt_file_name)

    # Write the content to the .txt output file
    with open(txt_file_path, 'w', encoding='utf-8') as f:
        f.write(txt_content)
    print(f"Conversion from {sbv_file_path} to {txt_file_path} completed successfully.")
    return txt_file_path


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
        choice = int(input("0. Convert .sbv to .txt\n1. Convert text?\n2. Add word to dictionary?\n3. Delete word from dictionary?\n4. Exit\nChoice: "))
        if choice == 0:
            input_file = input("Enter the path of the .sbv file to convert in .txt: ")
            convert_sbv_to_txt(input_file)
        if choice == 1:
            input_file = input("Enter the path of the input .txt file: ")
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
