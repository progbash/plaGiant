import glob
original = open("original.txt", 'r')
original_words = original.read().lower().split()
result = open("outfile2.txt", 'w')
found_count, fives_count = 0, 0

path = 'doc*.txt'

files = glob.glob(path)

def iterate():
    for i in range(len(original_words) - 4):
        for j in range(len(original_words)+1):
            if(j-i == 5):
                original_each_five = original_words[i:j]
                yield original_each_five
            else:
                pass


for each_file in files:
    other_docs = open(each_file, 'r')
    other_docs_words = other_docs.read().lower().split()
    print(other_docs_words)

    for i in range(len(other_docs_words) - 4):
        for j in range(len(other_docs_words)+1):
            if(j-i == 5):
                each_five_others = other_docs_words[i:j]
                for original_each_five in iterate():
                    if(original_each_five == each_five_others):
                        found_count += 1
                        result.write('{} hissəsi {} sənədində tapıldı.\n'.format(
                            original_each_five, each_file))
                    else:
                        pass
            else:
                pass

for original_each_five in iterate():
    fives_count += 1

print(found_count)
print(fives_count)

percentage = found_count/fives_count
result.write('Plagiat faizi: {}%'.format(round(percentage, 2)*100))
