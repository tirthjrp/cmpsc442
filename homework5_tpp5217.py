############################################################
# CMPSC442: Homework 5
############################################################

student_name = "Tirth Patel"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import email
import os
from math import log,exp
############################################################
# Section 1: Spam Filter
############################################################

def load_tokens(email_path):
    tokens=[]
    with open(email_path,"r") as file:
        message= email.message_from_file(file)
    for line in email.iterators.body_line_iterator(message):
        tokens+=line.split()
    return tokens


def log_probs(email_paths, smoothing):
    d={}
    for path in email_paths:
        tokens=load_tokens(path)
        for token in tokens:
            if token in d:
                d[token]+=1
            else:
                d[token]=1
    total=sum(d.values())
    for token in d:
        d[token]=log((d[token]+smoothing)/(total+smoothing*(len(d)+1)))

    d["<UNK>"]=log(smoothing/(total+smoothing*(len(d)+1)))
    return d




class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir, smoothing):
        spam_paths=os.listdir(spam_dir)
        ham_paths=os.listdir(ham_dir)
        for i in range(len(spam_paths)):
            spam_paths[i]=os.path.join(spam_dir,spam_paths[i])
        for i in range(len(ham_paths)):
            ham_paths[i]=os.path.join(ham_dir,ham_paths[i])
        self.ham_prob=log(len(ham_paths)/(len(ham_paths)+len(spam_paths)))
        self.spam_prob=log(len(spam_paths)/(len(spam_paths)+len(ham_paths)))
        self.ham_tokens_prob=log_probs(ham_paths,smoothing)
        self.spam_tokens_prob=log_probs(spam_paths,smoothing)

    
    def is_spam(self, email_path):
        tokens=load_tokens(email_path)
        prob_ham_e=0
        prob_spam_e=0
        for i in tokens:
            if i in self.ham_tokens_prob:
                prob_ham_e+=self.ham_tokens_prob[i]
            else:
                prob_ham_e+=self.ham_tokens_prob["<UNK>"]
            if i in self.spam_tokens_prob:
                prob_spam_e+=self.spam_tokens_prob[i]
            else:
                prob_spam_e+=self.spam_tokens_prob["<UNK>"]
        prob_ham_e+=self.ham_prob
        prob_spam_e+=self.spam_prob
        return prob_spam_e>prob_ham_e



    def most_indicative_spam(self, n):
        ind_values=[]
        for i in self.spam_tokens_prob:
            if i in self.ham_tokens_prob:
                temp=log(exp(1)**(self.ham_tokens_prob[i]+self.ham_prob)+exp(1)**(self.spam_tokens_prob[i]+self.spam_prob))
                value=self.spam_tokens_prob[i] -temp;
                ind_values.append((i,value))
        ind_values.sort(key=lambda x: x[1], reverse=True)
        return list(map(lambda x:x[0],ind_values))[:n]


    def most_indicative_ham(self, n):
        ind_values = []
        for i in self.spam_tokens_prob:
            if i in self.ham_tokens_prob:
                temp = log(exp(1) ** (self.ham_tokens_prob[i] + self.ham_prob) + exp(1) ** (self.spam_tokens_prob[i] + self.spam_prob))
                value = self.ham_tokens_prob[i] - temp
                ind_values.append((i, value))
        ind_values.sort(key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], ind_values))[:n]

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
It took me 4 hours to complete.
"""

feedback_question_2 = """
I found taking the log of probabilities and then solving the equation a bit challenging.
"""

feedback_question_3 = """
I liked implementing the overall project. I don't think there is need to change anything.
"""
