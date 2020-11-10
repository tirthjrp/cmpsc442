import homework5_tpp5217
sf = homework5_tpp5217.SpamFilter("homework5_data/train/spam","homework5_data/train/ham", 1e-5)
print(sf.most_indicative_spam(5))
# paths = ["homework5_data/train/ham/ham%d" % i for i in range(1, 11)]
# p = homework5_tpp5217.log_probs(paths, 1e-5)
# print(p["the"])
# sf = homework5_tpp5217.SpamFilter("homework5_data/train/spam","homework5_data/train/ham", 1e-5)
# for i in range(1,11):
#     print(sf.is_spam("homework5_data/train/spam/spam%d" % i))








