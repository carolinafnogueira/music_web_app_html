from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM artists')
        artists = []
        for row in rows:
            artist = Artist(row['id'], row['name'], row['genre'])
            artists.append(artist)
        return artists
    
    def create(self, artist):
        self.connection.execute(
            'INSERT INTO artists (name, genre) VALUES (%s, %s)',
            [artist.name, artist.genre]
        )
    
    def find(self, artist_id):
        self.connection.execute(
            'SELECT * FROM artists WHERE id = %s', [artist_id]
        )