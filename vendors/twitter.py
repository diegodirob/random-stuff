import os
from typing import Optional

# pip install tweepy
from tweepy import OAuth1UserHandler, API

class Twitter:
    v1 = None
    v2 = None
    language = None
    account_mapper = {
        'account_key': {
            'consumer_key': os.environ.get('TWITTER_CONSUMER_KEY', 'dev_consumer_key'),
            'consumer_secret': os.environ.get('TWITTER_CONSUMER_SECRET', 'dev_consumer_secret'),
            'access_token_key': os.environ.get('TWITTER_ACCESS_TOKEN_KEY', 'dev_access_token_key'),
            'access_token_secret': os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', 'dev_access_token_secret'),
        }
    }
    max_tweets = os.environ.get('TWITTER_MAX_TWEETS', 100)

    def __init__(self, language: str):
        self.language = language
        self.v1_authenticate()
        # self.v2_authenticate()

    def v1_authenticate(self):
        # V1 Authentication
        keys = self.account_mapper[self.language]
        access_token, access_token_secret = keys.pop('access_token_key'), keys.pop('access_token_secret')
        auth = OAuth1UserHandler(access_token=access_token, access_token_secret=access_token_secret, **keys)
        self.v1 = API(auth)

        # If the authentication was successful, this should print the screen name / username of the account
        try:
            print('Successful Authentication', self.v1.verify_credentials().screen_name)
        except Exception as e:
            print('Failed authentication', str(e))

    # def v2_authenticate(self):
    #     # V2 Authentication
    #     self.v2 = Client(**self.account_mapper[self.language])

    def v1_get_users_tweets(self, username: str) -> dict:
        return self.v1.user_timeline(
            screen_name=username,
            count=self.max_tweets,
            include_rts=False,
            # since_id=
        )

    def v1_create_tweet(self, message: str, url: Optional[int] = None):
        self.v1.update_status(status=message, attachment_url=url)
