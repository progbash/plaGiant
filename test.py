f1 = open("doc1.txt", 'r')
f2 = open("doc2.txt", 'r')

f1_words = f1.read().lower().split()[11:16]
f2_words = f2.read().lower().split()
joined_docs = set(f1_words) & set(f2_words)

for i in range(len(f2_words) - 4):
    for j in range(len(f2_words)+1):
        if(j-i==5):
            words2 = f2_words[i:j]
            if(f1_words == words2):
                print(f1_words)
                print("Detected !")
            else:
                pass
        else:
            pass
    
