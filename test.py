import homework6_tpp5217

c = homework6_tpp5217.load_corpus("brown-corpus.txt")
t = homework6_tpp5217.Tagger(c)
s = "I am waiting to reply".split()
print(t.most_probable_tags(s))
print(t.viterbi_tags(s))








# import csv
# with open("./actors.csv","r") as actor_file:
#     actors=list(csv.reader(actor_file,dialect="excel"))
# with open("./directors.csv","r") as actor_file:
#     directors=list(csv.reader(actor_file,dialect="excel"))
#
# with open("./genres.csv","r") as actor_file:
#     genres=list(csv.reader(actor_file,dialect="excel"))
#
# with open("./actor_relations.csv","r") as actor_file:
#     actor_rel=list(csv.reader(actor_file,dialect="excel"))
#
# with open("./genre_relations.csv","r") as actor_file:
#     genre_rel=list(csv.reader(actor_file,dialect="excel"))
#
# actor_counter=int(max(actors[1:],key=lambda x:int(x[0]))[0])+1
# director_counter=int(max(directors[1:],key=lambda x:int(x[0]))[0])+1
# show_counter=0
# genre_counter=int(max(genres[1:],key=lambda x:int(x[0]))[0])+1
#
# tv_shows=[["showID","title","year","directorID","rating","seasons"]]
# with open("./tv.csv","r") as file:
#     obj=list(csv.reader(file,dialect="excel"))
#     x=0
#     for row in obj:
#         if x==0:
#             x += 1
#             continue
#         x+=1
#         # actor
#         actors_id_list=[]
#         row_actors=row[4].split(",")
#
#         for actor in row_actors:
#             actor_id = -1
#             fname=""
#             lname=""
#             name=actor.split()
#             if len(name)>2:
#                 fname=name[0].strip()
#                 lname=name[2].strip()
#             else:
#                 fname=name[0].strip()
#                 lname=name[1].strip()
#
#             for i in actors:
#                 if i[1]==fname and i[2]==lname:
#                     actor_id=i[0]
#                     break
#             if int(actor_id)<0:
#                 temp=[]
#                 temp.append(str(actor_counter))
#                 temp.append(fname)
#                 temp.append(lname)
#                 actors.append(temp)
#                 actor_id=actor_counter
#                 actor_counter+=1
#
#             actors_id_list.append(actor_id)
#         # director
#         name=row[3].split()
#         fname=""
#         lname=""
#         if len(name)>2:
#             fname=name[0].strip()
#             lname=name[2].strip()
#         else:
#             fname = name[0].strip()
#             lname = name[1].strip()
#
#         director_id=-1
#         for i in directors:
#             if i[1]==fname and i[2]==lname:
#                 director_id=i[0]
#                 break
#         if int(director_id)<0:
#             temp=[]
#             temp.append(str(director_counter))
#             temp.append(fname)
#             temp.append(lname)
#             directors.append(temp)
#             director_id=director_counter
#             director_counter+=1
#
# #         genre
#         genre_id_list=[]
#         row_genres=row[2].split(",")
#         for genre in row_genres:
#             genre=genre.strip()
#             genre_id=-1
#             for i in genres:
#                 if i[1]==genre:
#                     genre_id=i[0]
#             if int(genre_id)<0:
#                 temp=[]
#                 temp.append(str(genre_counter))
#                 temp.append(genre)
#                 genres.append(temp)
#                 genre_id=genre_counter
#                 genre_counter+=1
#             genre_id_list.append(genre_id)
#
#         #       actor_relation
#         for i in actors_id_list:
#             temp=[]
#             temp.append(str(show_counter))
#             temp.append("0")
#             temp.append(str(i))
#             actor_rel.append(temp)
# #         genre relation
#         for i in genre_id_list:
#             temp=[]
#             temp.append(str(show_counter))
#             temp.append("0")
#             temp.append(str(i))
#             genre_rel.append(temp)
#
# #         tv shows
#         tv_shows.append([str(show_counter),row[1],row[5],str(director_id),row[7],row[6]])
#         show_counter+=1
#
# with open("actors.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(actors)
#
# with open("directors.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(directors)
#
# with open("genres.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(genres)
#
# with open("actor_relations.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(actor_rel)
#
# with open("genre_relations.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(genre_rel)
#
# with open("tv_shows.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(tv_shows)





# actors=[["actorID","fname","lname"]]
# directors=[["directorID","fname","lname"]]
# movies=[["movieID","title","year","directorID","rating","duration"]]
# genres=[["genreID","genre"]]
# genre_rel=[["id","type","genreID"]]
# actor_rel=[["id","type","actorID"]]
# actor_counter=0
# director_counter=0
# movies_counter=0
# genre_counter=0
# with open("./new.csv","r") as file:
#     obj=list(csv.reader(file,dialect="excel"))
#     x=0
#     for row in obj:
#         if x==0:
#             x += 1
#             continue
#         x+=1
#         # actor
#         actors_id_list=[]
#         row_actors=row[4].split(",")
#         # filtering
#         end=0
#         for i in row_actors:
#             name=i.split()
#             if len(name)<2:
#                 end=1
#                 break
#         if end:
#             continue
#
#         # filtering
#         if len(row[3].split())<2:
#             continue
#
#         for actor in row_actors:
#             actor_id = -1
#             fname=""
#             lname=""
#             name=actor.split()
#             if len(name)>2:
#                 fname=name[0].strip()
#                 lname=name[2].strip()
#             else:
#                 fname=name[0].strip()
#                 lname=name[1].strip()
#
#             for i in actors:
#                 if i[1]==fname and i[2]==lname:
#                     actor_id=i[0]
#                     break
#             if int(actor_id)<0:
#                 temp=[]
#                 temp.append(str(actor_counter))
#                 temp.append(fname)
#                 temp.append(lname)
#                 actors.append(temp)
#                 actor_id=actor_counter
#                 actor_counter+=1
#
#             actors_id_list.append(actor_id)
#         # director
#         name=row[3].split()
#         fname=""
#         lname=""
#         if len(name)>2:
#             fname=name[0].strip()
#             lname=name[2].strip()
#         else:
#             fname = name[0].strip()
#             lname = name[1].strip()
#
#         director_id=-1
#         for i in directors:
#             if i[1]==fname and i[2]==lname:
#                 director_id=i[0]
#                 break
#         if int(director_id)<0:
#             temp=[]
#             temp.append(str(director_counter))
#             temp.append(fname)
#             temp.append(lname)
#             directors.append(temp)
#             director_id=director_counter
#             director_counter+=1
#
# #         genre
#         genre_id_list=[]
#         row_genres=row[2].split(",")
#         for genre in row_genres:
#             genre=genre.strip()
#             genre_id=-1
#             for i in genres:
#                 if i[1]==genre:
#                     genre_id=i[0]
#             if int(genre_id)<0:
#                 temp=[]
#                 temp.append(str(genre_counter))
#                 temp.append(genre)
#                 genres.append(temp)
#                 genre_id=genre_counter
#                 genre_counter+=1
#             genre_id_list.append(genre_id)
#
#         #       actor_relation
#         for i in actors_id_list:
#             temp=[]
#             temp.append(str(movies_counter))
#             temp.append("1")
#             temp.append(str(i))
#             actor_rel.append(temp)
# #         genre relation
#         for i in genre_id_list:
#             temp=[]
#             temp.append(str(movies_counter))
#             temp.append("1")
#             temp.append(str(i))
#             genre_rel.append(temp)
#
# #         movies
#         movies.append([str(movies_counter),row[1],row[5],str(director_id),row[7],row[6]])
#         movies_counter+=1
#


# with open("movies.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(movies)
#
# with open("actors.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(actors)
#
# with open("directors.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(directors)
#
# with open("genres.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(genres)
#
# with open("actor_relations.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(actor_rel)
#
# with open("genre_relations.csv","w") as file:
#     obj=csv.writer(file,dialect="excel")
#     obj.writerows(genre_rel)











