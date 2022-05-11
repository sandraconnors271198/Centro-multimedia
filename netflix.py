from pyflix2 import  NetflixAPIV1, User, NetflixError, EXPANDS, SORT_ORDER, RENTAL_HISTORY_TYPE
import sys

netflix = NetflixAPIV1( 'appname', 'key', 'shared_secret')
movies = netflix.title_autocomplete(sys.argv[1], filter='instant')
for title in movies['autocomplete']['title']:
    print (title)

user = netflix.get_user('use_id', 'access_token', 'access_token_secret')
reco = user.get_reccomendations()
for movie in reco['recommendations']:
    print (movie['title']['regular'])