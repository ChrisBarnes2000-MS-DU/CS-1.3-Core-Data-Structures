import re

def tokenize(text):
    # print("--Text--\n", text, "\n")
    no_punc_text = remove_punctuation(text)
    sentences = split_by_sentence(no_punc_text)
    start = add_start(sentences)
    end = add_stop(start)
    propper = end
    # for line in propper:
        # print(line)
    tokens = split_on_whitespace(propper)
    return tokens

def remove_punctuation(text):
    no_punc_text = re.sub('[,()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    # print("--No Punctuation--\n", no_punc_text, "\n")
    return no_punc_text

def split_by_sentence(text):
    # print("--Split by line--")
    sentences = re.split(r'\.(?:\s)+', text)
    return sentences

def add_start(sentences):
    for i, sentence in enumerate(sentences):
        sentences[i] = re.sub(r'^', "[START] ", sentence)
    return sentences

def add_stop(sentences):
    for i, sentence in enumerate(sentences):
        sentences[i] = re.sub(r'$', " [STOP]", sentence)
    return sentences

def split_on_whitespace(sentences):
    tokens = []
    for sentence in sentences:
        tokens += re.split(r'\s+', sentence)
    # print("\n--Tokens--\n", tokens)
    return tokens

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
    else:
        print('No source text filename given as argument')
