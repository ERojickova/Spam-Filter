import email
import re
from corpus import Corpus

def printHeader(separator, numberOfSeparators, text):
    '''Prints a header with a specific string in the terminal'''
    for _ in range(numberOfSeparators):
        print(separator, end='')
    print(f" {text} ", end='')
    for _ in range(numberOfSeparators):
        print(separator, end='')
    print()

def read_classification_from_file(path):
    dict = {}
    with open(path, encoding='utf-8') as file:
        for line in file:
            line = line.split()
            dict[line[0]] = line[1]
    return dict

def printCleanedEmail(email):
    printHeader('=', 20, email[0])

    m = email.message_from_string(email[1])
    
    printHeader('-', 10, "body start")
    if(m.is_multipart()):
        for subBody in m.get_payload():
            print(removeTags(subBody.get_payload()))
    else:
        print(removeTags(m.get_payload()))
        
    printHeader('-', 10, "body end")

def removeTags(msg):
    '''Removes the html tags and unnecessary enters from a string using regex'''
    msg = re.sub('<[^<]+?>', '', msg)
    msg = re.sub('\n+', '\n', msg)
    return msg


            
if __name__ == "__main__":
    corpus1 = Corpus("./1")
    emailGenerator = corpus1.email()
    
    for email in emailGenerator:
        printCleanedEmail(email)
    