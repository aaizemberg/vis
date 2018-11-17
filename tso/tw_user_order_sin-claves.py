import sys
import pandas as pd
from TwitterSearch import *

if (len(sys.argv) == 2):
	pd.set_option('display.max_colwidth', -1)	

	col_names = ['screen_name', 'date', 'fav', 'retweet', 'text']
	df = pd.DataFrame(columns = col_names)

	user = sys.argv[1]
	try:
		tuo = TwitterUserOrder( user )
		tuo.arguments.update({'tweet_mode':'extended'})		

		ts = TwitterSearch(
			consumer_key = '****************************',
			consumer_secret = '****************************',	
			access_token = '****************************',
			access_token_secret = '****************************'
		)
		for tweet in ts.search_tweets_iterable(tuo):
			df = df.append({'screen_name': tweet["user"]["screen_name"],  'date' : tweet["created_at"], 'fav' : tweet["favorite_count"], 'retweet' : tweet["retweet_count"], 'text' : tweet["full_text"].replace("\n","<br>") }, ignore_index=True)
	except TwitterSearchException as e:
		print(e)
	df.to_csv('df_' + user + '.tsv', sep='\t', encoding='utf-8', index=False)
