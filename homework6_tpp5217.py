############################################################
# CMPSC 442: Homework 6
############################################################

student_name = "Tirth Patel"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.



############################################################
# Section 1: Hidden Markov Models
############################################################

def load_corpus(path):
    with open(path,"r") as file:
        result=[]
        for line in file:
            l=[]
            for j in line.split():
                l.append(tuple(j.split("=")))
            result.append(l)
    return result

class Tagger(object):

    def __init__(self, sentences):
        self.l_tags=["NOUN","VERB","ADJ","ADV","PRON","DET","ADP","NUM","CONJ","PRT",".","X"]
        self.d_tags={"NOUN":0,"VERB":1,"ADJ":2,"ADV":3,"PRON":4,"DET":5,"ADP":6,"NUM":7,"CONJ":8,"PRT":9,".":10,"X":11}
        tags_init_count={}
        tags_total_count={}
        vocab={}
        l = [[0 for j in range(len(self.l_tags))] for i in range(len(self.l_tags))]
        for sen in sentences:
            for i in range(len(sen)):
                if sen[i][0] in vocab:
                    vocab[sen[i][0]][self.d_tags[sen[i][1]]]+=1
                else:
                    temp=[0 for i in range(len(self.l_tags))]
                    temp[self.d_tags[sen[i][1]]]=1
                    vocab[sen[i][0]] = temp

                if i<(len(sen)-1):
                    l[self.d_tags[sen[i][1]]][self.d_tags[sen[i+1][1]]]+=1
                tag = sen[i][1]
                if i==0:
                    if tag in tags_init_count:
                        tags_init_count[tag]+=1
                    else:
                        tags_init_count[tag]=1
                if tag in tags_total_count:
                    tags_total_count[tag]+=1
                else:
                    tags_total_count[tag] = 1

        for tag in self.l_tags:
            if tag in tags_init_count:
                tags_init_count[tag]=(tags_init_count[tag]+1)/(len(sentences)+len(self.l_tags))
            else:
                tags_init_count[tag]=1/(len(sentences)+len(self.l_tags))

            if tag not in tags_total_count:
                tags_total_count[tag]=0

        for i in range(len(l)):
            for j in range(len(l[i])):
                l[i][j]=(l[i][j]+1)/(tags_total_count[self.l_tags[i]]+len(self.l_tags))

        for word in vocab:
            for i in range(len(self.l_tags)):
                vocab[word][i]=(vocab[word][i]+1)/(tags_total_count[self.l_tags[i]]+len(vocab))

        self.tags_init_prob=tags_init_count
        self.transition_prob=l
        self.emission_prob=vocab

    def most_probable_tags(self, tokens):
        result=[]
        for i in tokens:
            max=0
            temp=-1
            for j in range(len(self.emission_prob[i])):
                if self.emission_prob[i][j]>=max:
                    max=self.emission_prob[i][j]
                    temp=j
            result.append(self.l_tags[temp])
        return result

    def viterbi_tags(self, tokens):
        pass

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""