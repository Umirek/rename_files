# Umirek
# 05.01.2022
# rename file names so it fit´s into ondrive's name system
import os


def rename_files(files, path):
    # split the list of names
    for file in files:

        # check if the name could be a dir then the program checks this dir
        if os.path.isdir(path + os.sep + file):
            new_path = path + os.sep + file
            rename_files(os.listdir(new_path), new_path)

        # for each file we have to check every single character, so another for loop which gives us each char
        for character in file:
            old_file = file
            forbidden_char_detected = False
            # we need to check every forbidden character in the forbidden dictionary
            for forbidden_character in range(len(forbidden)):
                # when we found a forbiden character then we have to replace the forbidden character with the accepted one
                if forbidden[forbidden_character] == character:
                    file = file.replace(character, replace_char)
                    forbidden_char_detected = True
                # when we checked every character with the forbidden dictionary then we rename the file and if we had found a character which shouldn"t be used as a file name
                if forbidden[forbidden_character] == forbidden[list(forbidden.keys())[-1]] and forbidden_char_detected:
                    os.rename(path + os.sep + old_file, path + os.sep + file)


# character which microsoft does not allow
forbidden = {
    0: '"',
    1: "*",
    2: ":",
    3: "<",
    4: ">",
    5: "?",
    6: "/",
    7: "|",
    8: "\\",
    9: " ",
    10: "\\\\",

}
# character we want to replace
replace_char = "_"

# get main path for first the first init, after that the programm automatically search for all the other files and folders
main_path = input("Enter the main path :").strip()

# function takes two arguments: files (takes a list of file names of the dir)
# path (takes the mainpath from the user input)
rename_files(os.listdir(main_path), main_path)
