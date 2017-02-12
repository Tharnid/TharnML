count= 0
corpus_file = "/usr/share/dict/words"
with open( corpus_file ) as corpus:
    for line in corpus:
        word= line.strip()
        if len(word) == 10:
            count += 1
print( count )
