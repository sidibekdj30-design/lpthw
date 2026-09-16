# This imports the sys module
import sys

# This unpacks argv into script, encoding and error handler
script, input_encoding, error = sys.argv


# This defines a function that reads the file line by line
def main(language_file, encoding, errors):
    # This reads one line from the file
    line = language_file.readline()
    # This checks if the line is not empty
    if line:
        # This calls print_line to process the line
        print_line(line, encoding, errors)
        # This calls main again to read the next line
        return main(language_file, encoding, errors)

# This defines a function that encodes and decodes each line
def print_line(line, encoding, errors):
    # This removes spaces and \n from the line 
    next_lang = line.strip()
    # This converts the string to bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # This converts the bytes back to string
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # This prints both bytes and string
    print(raw_bytes, "<===>" , cooked_string)

# This opens languages.txt with utf-8 encoding
languages = open("languages.txt", encoding="utf-8")
# This calls main to start readingv the file
main(languages, input_encoding, error)