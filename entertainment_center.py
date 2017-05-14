import media
import fresh_tomatoes

xXx = media.Movie("xXx"
                  ,"https://upload.wikimedia.org/wikipedia/commons/8/85/XXx_Return_of_Xander_Cage.jpg"
                  ,"superman"
                  ,"https://www.youtube.com/watch?v=yIoFjJ0JURI")
#print(xXx.title)

A_Dog_Purpose = media.Movie("A_Dog_Purpose"
                ,"https://upload.wikimedia.org/wikipedia/commons/0/00/A_Dog_Purpose.jpg"
                ,"AAAAAAAAAAa dog"
                ,"https://www.youtube.com/watch?v=yIoFjJ0JURI")
#print(A_Dog_Purpose.poster_image_url)

movies = [xXx, A_Dog_Purpose]
fresh_tomatoes.open_movies_page(movies)
