import homework6_tpp5217
import time

c=homework6_tpp5217.load_corpus("./brown-corpus.txt")

t=homework6_tpp5217.Tagger(c)
s = "I saw the play".split()
start=time.time()
print(t.most_probable_tags(s))
print(t.viterbi_tags(s))
end=time.time()
print(end-start)
