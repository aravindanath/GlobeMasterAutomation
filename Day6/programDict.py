# Using dict to store movie records

movie = {'title':"The GodFather",
         "director":"Ford",
         'year':1972,
         'rating':8.8}
print(type(movie))


print(movie['year'])

movie['rating']=(movie['rating'])/2
print(movie['rating'])