import homework6_tpp5217
import time

c=homework6_tpp5217.load_corpus("./brown-corpus.txt")
start=time.time()
t=homework6_tpp5217.Tagger(c)
print(t.most_probable_tags(["The", "blue", "bird", "sings"]))
end=time.time()
print(end-start)
