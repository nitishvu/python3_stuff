input_str = "catsanddog"
words_dict = ["cat","cats","and","sand","dog"]

def track(input_str,word_dict,sent):
    if len(input_str) == 0:
        print(sent)

    for i in range(len(input_str)):
        word = input_str[:i+1]
        if word in word_dict:
            sent.append(word)
            track(input_str[i+1:],word_dict,sent)
            sent.pop()

sent = []
track(input_str,words_dict,sent)
