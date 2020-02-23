f1 = open("doc1.txt", 'r')
f2 = open("doc2.txt", 'r')

words1 = f1.read().lower().split()[:]
words2 = f2.read().lower().split()[:]
words = set(words1) & set(words2)

with open('outfile.txt', 'w') as output:
    for word in words:
        output.write('{} sözü yüklənən faylda {} dəfə, yoxlanan faylda isə {} dəfədir.\n'.format(word, words1.count(word), words2.count(word)))
