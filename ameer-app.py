# Short code
import tweepy
consumer_key = '6ywz7k7gwFrT5btrcAodOlwBa'
consumer_secret = 'ch34ohAxW6tHgZWPAKlDr3FOH5e7NhjL4KByJ5hm5e1GRYCCJT'
access_token = '1339936871091081221-3IXURJ1G0HpLzoMijGqVQMeQoHzJW5'
secret_access_token = '9g8NIOn5fPKPgTEPQ4TyRRBZm0z0lrH1q8XYueyrrGg0q'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_access_token)
api = tweepy.API(auth)
print('Everything is fine')

import time
while True:
  user = api.get_user('blabla21932776')
  f = user.followers_count
  api.update_profile(name=f'bla bla {f} Followers')
  print(f'bla bla{f} Followers')
  time.sleep(60)
