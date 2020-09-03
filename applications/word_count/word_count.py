def word_count(s):
    # Your code here
    word_count_dict = {}
    ignored_characters = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    for character in ignored_characters:
        if character in s:
            s = s.replace(character, '')
    s = s.lower().split()
    for string in s:
        if string in word_count_dict.keys():
            word_count_dict[string] += 1
        else:
            word_count_dict[string] = 1
    
    return word_count_dict
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))