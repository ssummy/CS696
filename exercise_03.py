"""
exercise_03
2/8/2018

For this Exercise you will write one definition that will take in the name of a
directory as a string, and return a dictionary containing every sequence in every FASTA file where
the sequence header is the key and the DNA sequences are values.

Your definition will be tested with improperly formatted FASTA files and should handle the following cases:
    1) If there are extra new line characters, or empty lines, your program should still process sequences normally
    2) If a duplicate header exists between two entries your definition should check to see if the sequences are the same
        * If the headers and sequences are identical, your program should print a message that "a duplicate entry exists
          for <header>" and continue normally.
        * If the only the headers match, you should print a message that "duplicate headers with non-identical
          sequences were found for <header>" and neither entry should be added in the dictionary.
          (your print statements don't need to be identical to what I have written here)
    3) If a file in the directory is not a fasta file, your program should not open it.
    4) If a sequence contains characters that are not A, C, G, or T, then it should not be added to the dictionary.

If your program is working correctly, the dictionary should only contain the 4 "good sequence"s in the test folder.


The following syntax may be helpful:

# deleting from a dictionary
del my_dictionary[key]

# printing and formatting a string
x = 'my_variable'
print('Error related to variable: {}'.format(x))

# checking your final dictionary by printing out key, value pairs
for key, value in my_dictionary.items():
    print('Key is: {}\tValue is: {}'.format(key, value))

"""

import os
import re

def fasta_folder_to_dict(folder_path):
    """
    Constructs a dictionary of all of the FASTA formatted entries from a folder containing FASTA files.
    :param folder_path: string
    :return: dictionary
    """

    keys = []
    values = []
    pastkeys = []

    # loops through each fasta file, skipping files with a different ending
    for file in os.listdir(folder_path):
        if(not file.endswith(".fasta")):
            continue
        f = open(folder_path + '//' + file)
        #str1 is our next potential value in the dictionary
        str1 = ""
        line = f.readline()
        if(keys.__contains__(line)):
            # save this line as a potential key
            potkey = line
            line = f.readline().strip()
            if values.__contains__(line):
                continue
            # remove the duplicate
            keys.remove(potkey)
        keys.append(line.strip())
        line = f.readline()
        str1 = line.strip()
        while (line):
            if (line.startswith(">")):
                ####
                if(str1.strip().startswith('>')):
                    line = str1
                    str1 = f.readline().strip()
                if (str1.strip() == ''):
                    keys.pop()#######################
                    #keys.append(line.strip())
                    str1 = f.readline().strip()
                    continue
                if(len(values) < len(keys)):
                    values.append(str1.strip())
                    str1 = ""######################
                if (keys.__contains__(line.strip()) or pastkeys.__contains__(line)):
                    # save this line as a potential key
                    potkey = line.strip()
                    line = f.readline().strip()
                    while (line and not line.startswith(">")):
                        str1 += line.strip()
                        line = f.readline().strip()
                    if values.__contains__(str1):
                        str1 = f.readline().strip()
                        nextline = f.readline().strip()
                        while (not nextline.startswith(">")):
                            str1 += nextline.strip()
                            nextline = f.readline().strip()
                        keys.append(line)###################
                        line = nextline
                        continue
                    # remove the duplicate
                    ind = keys.index(potkey)
                    values.pop(ind)
                    keys.pop(ind)
                    #add to 'seen' list
                    pastkeys.append(potkey)
                    str1 = f.readline().strip()
                    continue
                keys.append(line.strip())
                line = f.readline()
                continue
            else:
                str1 += line.strip()
            line = f.readline()
        values.append(str1.strip())
        str1 = ""

    proind  = []
    for val in range(0, len(keys)):
        matchObj = re.search("[^ACTG]", values[val])
        if matchObj:
            proind.append(val)
    keys = [keys[x] for x in range(0, len(keys)) if x not in proind]
    values = [values[x] for x in range(0, len(values)) if x not in proind]
    return dict(zip(keys, values))

def main():
    rfolder = fasta_folder_to_dict('C:\\Users\stesu\OneDrive\Documents\Spring2018\BIO\\test_files')#\\tricky_fasta.fasta')
    quitter = 0

if __name__ == "__main__":
    main()