def sentence_no_duplicate(sentence):
    words = sentence.split(' ')
    new_words = []
    for w in words :
        if w not in new_words :
            new_words.append(w)

    print(' '.join(new_words))



sentence_no_duplicate("My name name name is is Ahmed ahmed")