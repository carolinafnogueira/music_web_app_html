from lib.album_repository import AlbumRepository
from lib.album import Album

'''
When I call AlbumRepository #all
I get a list of all the albums objects
in the albums table
'''

def test_get_albums_names(db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1)
        ]
    
'''
When we call the method #get_artist_name on Album
we get a string representing the artist name
linked to the album id given
'''
def test_get_artist_name(db_connection):
    db_connection.seed('seeds/record_store.sql')
    repository = AlbumRepository(db_connection)
    artist = repository.get_artist_name(1)
    assert artist == 'Pixies'