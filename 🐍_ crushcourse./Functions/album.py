def make_album(artist_name,album_title,album_year = None,track_no = None):
	"""describing a music album"""
	#,album_year = None,track_no = None
	album_details = {}
	album_details['Artist_name'] = artist_name
	album_details['Album_title'] = album_title
	if album_year:
		album_details['Album_year'] = album_year
	if track_no:
		album_details['Track_no'] = track_no
	return album_details
album = make_album(artist_name = 'Eminem',album_title = 'Encore')
print(album)
album = make_album(artist_name = 'Chris Brown',album_title = 'Breezy')
print(album)
album = make_album(artist_name = 'Fireboy',album_title = 'Playboy')
print(album)
print()
print()
album = make_album(artist_name = 'Eminem',album_title = 'Encore',album_year = 2003,track_no=14)
print(album)