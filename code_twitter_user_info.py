import tweepy
import pandas as pd
import matplotlib.pyplot as plt


class TwitterOps:
    def __init__(self, consumer_key = " ",
                 consumer_secret = " ",
                 access_token = " ",
                 access_token_secret = " "):        
        print("\n\n>>>>>>>>>>>>>>>> YOOOOOOOOOOOOOOOOO!!!!!!")
        # Remplacez les valeurs ci-dessous par vos propres clés et jetons d'accès Twitter
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        

    def get_user_info(self, username):
        # Authentification à l'API Twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        # Ask user for Twitter username
        username = username

        # Get user object
        try:
            user = api.get_user(screen_name=username)
            user_info = {
            "name": user.name,
            "followers": user.followers_count,
            "friends": user.friends_count,
            "location": user.location,
            "description": user.description,
            "status": user.statuses_count,
            "created": user.created_at,
        }
        except Exception as e:
            user_info = None

        return user_info
    

    def get_user_tweets(self, username):
        # Authentification à l'API Twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        # Ask user for Twitter username
        username = username

        # Get user object
        try:
            # Collecte des hashtags populaires
            print("\nHashtags populaires récents :")
            tweets = api.user_timeline(screen_name=username, count=20)
            hashtags = []
            all_tweets = []
            for tweet in tweets:
            
                for hashtag in tweet.entities.get("hashtags"):
                    hashtags.append(hashtag["text"])
                    hashtags = list(set(hashtags))
                    if hashtags:
                        print(", ".join(hashtags))
                    else:
                        print("Aucun hashtag trouvé.")
                curr_tweet =  {
                    "created_date" : tweet.created_at,
                    "text" : tweet.text
                }
                all_tweets.append(curr_tweet)
            
            result = {
                "tweets": all_tweets,
                "hashtags": hashtags
            }
            return result
        except Exception as e:
            print('piiiiiiiiiimmmmmmmmm!!!!!!!')
            result = None

        return result



    

    #         # Collecte des mentions d'utilisateurs
    #         print("\nMentions d'utilisateurs récentes :")
    #         mentions = []
    #         for tweet in tweets:
    #             for mention in tweet.entities.get("user_mentions"):
    #                 mentions.append(mention["screen_name"])
    #         mentions = list(set(mentions))
    #         print(", ".join(mentions))

    #         # Collecte des URL partagées
    #         print("\nURL partagées récemment :")
    #         urls = []
    #         for tweet in tweets:
    #             for url in tweet.entities.get("urls"):
    #                 urls.append(url["expanded_url"])
    #         urls = list(set(urls))
    #         print("\n".join(urls))

    #         # Collecte des followers
    #         print("\nFollowers :")
    #         followers = []
    #         for page in tweepy.Cursor(api.followers, screen_name=username).pages():
    #             followers.extend(page)
    #         for follower in followers:
    #             print(follower.screen_name)

    #         # Collecte des personnes suivies
    #         print("\nPersonnes suivies :")
    #         following = []
    #         for page in tweepy.Cursor(api.friends, screen_name=username).pages():
    #             following.extend(page)
    #         for followee in following:
    #             print(followee.screen_name)

            #except tweepy.error.TweepError as e:
            #print("Une erreur s'est produite :", str(e))

    # Saisie du nom d'utilisateur
    #username = input("Entrez le nom d'utilisateur Twitter : ")

    # Appel de la fonction pour collecter les données de l'utilisateur
    #collect_user_data(username)