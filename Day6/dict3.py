movie ={}

movie['title']="The GodFather"
movie['director']="FOrd"
movie['year']=1972
movie['rating']=9.3
# Adding list into dict
movie['actors']=['Marlon','Al Pacino','James']
# Adding dict into dict (nested dict)
movie['other_Details']={'runTime':175,
                        "language":'English',
                        "Director":"Raja mouli"}

print(movie['other_Details']['Director'])


