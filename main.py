def main():
    with open("books/frankenstein.txt") as f:        
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")       
    #print(file_contents)
    count(file_contents)
    print()
    wordCount(file_contents)
    print("--- End report ---") 

def count(s):
    words = s.split()
    word_count = len(words)
    print(str(word_count) + " words found in the document")
    return word_count

def wordCount(s):
    lowered_string = s.lower()
    my_dict = {}
    for char in lowered_string:
        if(char in my_dict):
            my_dict[char] = my_dict[char] +1
        else:
            my_dict[char] = 1

    list_of_dicts = [{'character': key, 'value': value} for key, value in my_dict.items()]
    list_of_dicts.sort(key=lambda x: x['value'], reverse=True)
    for dictionary in list_of_dicts:
        character = dictionary['character']
        value = dictionary['value']
        if character.isalpha():
            print("The " + character + " character was found " + str(value) + " times")

main()