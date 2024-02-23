from collections import defaultdict

termids = {}
docids = {}
doc_info = defaultdict()
terms_info1 = {}
hashmap={}

def initalize_maps():
    with open("C:/Users/Mansoor/Downloads/Compressed/Documents/termids.txt", 'r', encoding="utf8") as file:
        for x in file.read().split('\n'):
            if len(x)> 0:
                global termids
                termids[x.split('/')[0]] = int(x.split('/')[1])
                global hashamp
                hashmap[int(x.split('/')[1])] = defaultdict(list)
                global terms_info1
                terms_info1[int(x.split('/')[1])] = defaultdict(list)

    with open("C:/Users/Mansoor/Downloads/Compressed/Documents/docids.txt", 'r', encoding="utf8") as file:
              for x in file.read().split('\n'):
                   if len(x) > 0:
                        global docids
                        global doc_info
                        docids[x.split('/')[1]]  = int(x.split('/')[0])
                        doc_info[int(x.split('/')[0])] = [0 for m in range(2)]

    with open("C:/Users/Mansoor/Downloads/Compressed/Documents/doc_index.txt", 'r',encoding="utf8") as file:
         for x in file.read().split('\n'):
              if len(x) > 0:
                lst = x.split(' ')
                did = int(lst[0])
                tid = int(lst[1])
                try:
                    pos = [int(n) for y, n in enumerate(lst) if y > 1 and n != ""]
                except:
                     print(lst)
                     input()
                hashmap[tid][did] = [0 for b in range(2)]
                hashmap[tid][did][0] = len(pos) #total occurences in doc
                hashmap[tid][did][1] = pos
                try:
                 doc_info[did][0] += 1 #distinct term count
                 doc_info[did][1] += len(pos) #total terms count
                except:
                    print(did)
                    print(doc_info)
                    input()

    with open("C:/Users/Mansoor/Downloads/Compressed/Documents/term_info.txt", "r") as f:
        for line in f.read().split('\n'):
            lst = line.split('/')

            if lst[0] != '':
                termid = int(lst[0])
                terms_info1[termid] = [0, 0, 0]  # initialize the dictionary with empty values
                terms_info1[termid][0] = lst[3] # 0 index is holding the number of documents holding the term
                terms_info1[termid][1] = lst[2] # index 1 is holding the frequency of the term in the corpus
                terms_info1[termid][2] = lst[1] # index 2 is holding the term offset

def term(term):
    tid = termids[term]
    print("TERM: ", term)
    print("TERMID: ", termids[term])
    print("Term frequency in corpus: ", terms_info1[tid][1])
    print("Number of documents containing term: ",terms_info1[tid][0])
    print("Inverted list offset: ",terms_info1[tid][2])

def doc(doc):
    dt = docids[doc]
    print("Listing for document: ",doc)
    print("doc id:", docids[doc])
    print("total terms in this doc: ", doc_info[dt][1])
    print("total distinct terms in doc: ", doc_info[dt][0])

def term_doc(term,doc):
    td = termids[term]
    dt = docids[doc]
    print("doc: ", doc)
    print("term: ", term)
    print("term id: " , td)
    print("doc id: ", dt)
    print("term frequency in doc: ", hashmap[td][dt][0])
    print("term positions in doc: ", hashmap[td][dt][1])

#take console input for 3 functions above
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--doc", help="Document name")
    parser.add_argument("-t", "--term", help="Term name")
    parser.add_argument("-td", "--term_doc", help="Term and Document name")
    args = parser.parse_args()
    
    if args.doc and args.term:
        term_doc(args.term, args.doc)
    elif args.doc:
        doc(args.doc)
    elif args.term:
        term(args.term)
    else:
        print("Please provide at least one argument")


initalize_maps()
if __name__ == "__main__":
    main()              