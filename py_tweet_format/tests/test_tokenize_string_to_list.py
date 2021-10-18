from py_tweet_format import tokenize_string_to_list

def test_tokenize_string_to_list():
	assert( tokenize_string_to_list( "word more words" ) == [ "word", " ", "more", " ", "words" ] )
