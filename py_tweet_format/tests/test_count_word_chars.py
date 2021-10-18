from py_tweet_format import count_word_chars

def test_word_chars_string():
	assert( count_word_chars( "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23 ) == 26 )

def test_word_chars_http():
	assert( count_word_chars( "http://www.github.org", 23 ) == 23 )
	assert( count_word_chars( "https://www.github.org", 23 ) == 23 )

def test_word_chars_tld():
	assert( count_word_chars( "github.org", 23 ) == 23 )
