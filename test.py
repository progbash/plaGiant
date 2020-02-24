f1 = open("doc1.txt", 'r')
f2 = open("doc2.txt", 'r')

# words1 = f1.read().lower().split()[0:5]
# words2 = f2.read().lower().split()[0:5]
# words = set(words1) & set(words2)

f1_words = f1.read().lower().split()[0:5]
f2_words = f2.read().lower().split()
joined_docs = set(f1_words) & set(f2_words)

for i in range(len(f2_words) - 5):
    for j in range(len(f2_words)):
        if(j-i==5):
            words2 = f2_words[i:j]
            if(f1_words == words2):
                print(f1_words)
                print("Detected !")
            else:
                pass
        else:
            pass

# with open('outfile.txt', 'w') as output:
#     for word in words:
#         output.write('{} sözü yüklənən faylda {} dəfə, yoxlanan faylda isə {} dəfədir.\n'.format(word, words1.count(word), words2.count(word)))
