import email
import re
from corpus import Corpus

def PrintHeader(separator, numberOfSeparators, text):
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

def clearMailPrint(msg):
    PrintHeader('=', 20, msg[0])

    m = email.message_from_string(msg[1])
    
    PrintHeader('-', 10, "body start")
    if(m.is_multipart()):
        for subBody in m.get_payload():
            print(removeTags(subBody.get_payload()))
    else:
        print(removeTags(m.get_payload()))
        
    PrintHeader('-', 10, "body end")

def removeTags(msg):
    msg = re.sub('<[^<]+?>', '', msg)
    msg = re.sub('\n\n+', '\n', msg)
    return msg


            
if __name__ == "__main__":
    c = Corpus("./1")
    a = c.email()



    msg = next(a)

    for msg in a:
        clearMailPrint(msg)
    