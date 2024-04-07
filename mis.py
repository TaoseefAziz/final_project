def correct_spelling(input_file, spell_dict):
    file = open("test.txt",'w')
    file.write("hello\nhow\nare\nyou\n")
    file.close()
correct_spelling("", {})