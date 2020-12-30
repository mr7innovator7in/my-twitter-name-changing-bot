import tweepy
api_key = '6ywz7k7gwFrT5btrcAodOlwBa'
api_secret_key = 'ch34ohAxW6tHgZWPAKlDr3FOH5e7NhjL4KByJ5hm5e1GRYCCJT'
access_token = '1339936871091081221-3IXURJ1G0HpLzoMijGqVQMeQoHzJW5'
secret_access_token = '9g8NIOn5fPKPgTEPQ4TyRRBZm0z0lrH1q8XYueyrrGg0q'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth)
import time
while True: # to make this forever
  user= api.get_user('blabla21932776')
  follower = user.followers_count
  api.update_profile(name = f'bla bla {follower} followers')
  print(f'bla bla {follower} followers')
  time.sleep(60) #this process takes 60s to update (limitation) 
