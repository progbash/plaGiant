import os
f1 = open("doc1.txt", 'r')
f2 = open("doc2.txt", 'r')
result = open("outfile.txt", 'w')
count, fives_count = 0, 0


f1_words = f1.read().lower().split()
f2_words = f2.read().lower().split()
joined_docs = set(f1_words) & set(f2_words)

def iterate():
    for i in range(len(f1_words) - 4):
        for j in range(len(f1_words)+1):
            if(j-i==5):
                words1 = f1_words[i:j]
                yield words1
            else:
                pass

for i in range(len(f2_words) - 4):
    for j in range(len(f2_words)+1):
        if(j-i==5):
            words2 = f2_words[i:j]
            for words1 in iterate():
                if(words1 == words2):
                    # print(words1)
                    # print("Detected in", os.path.basename(f2.name))
                    count+=1
                    result.write('{} hissəsi {} sənədində tapıldı.\n'.format(words1, os.path.basename(f2.name)))
                else:
                    pass
        else:
            pass

for words1 in iterate():
    fives_count+=1

print(fives_count)
percentage = count/fives_count
result.write('Plagiat faizi: {} %'.format(percentage))
    