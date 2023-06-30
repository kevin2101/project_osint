import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter



# Remplacez les valeurs ci-dessous par vos propres clés et jetons d'accès Twitter
consumer_key = "fMxBoczQWDTp1cJ40XY4XBaMU"
consumer_secret = "UVHSYTTBSwAElPguKJ3l5jwu1xbukYgNm7BmhZgXGyqFy3MdN8"
access_token = "2467414650-nDLsaFQSZovoFqDyCaUQPklwGzsjpH1eqhHHz6D"
access_token_secret = "FAhAEbEuWcA9GOhYn4IjQC5dccEAW7BWo4vNTw7EXjyLZ"

# Authentification à l'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Demander à l'utilisateur de saisir des mots clés pour le hashtag
mots_cles = input("Entrez les mots clés pour le hashtag : ")


# Collecte des tweets avec le hashtag spécifié
tweets = api.search_tweets(q=mots_cles) #count=10)

# Affichage des tweets
#for tweet in tweets:
#    print("---")
#    print("Auteur :", tweet.user.screen_name)
#    print("Contenu :", tweet.text)

#hashtags = []
#for tweet in tweets:
#    for hashtag in tweet.entities["hashtags"]:
#        hashtags.append(hashtag["text"])

# Compter le nombre d'occurrences de chaque hashtag
#occurrences = Counter(hashtags)

# Afficher les hashtags les plus courants et le nombre d'occurrences de chaque hashtag
#for hashtag, occurrence in occurrences.most_common(10):
#    print(hashtag + ": " + str(occurrence))

#trends_result = api.get_place_trends(23424819) # WOEID pour la France

#for trend in trends_result[0]["trends"][:10]:
#    print(trend["name"], trend["tweet_volume"])

# Saisie de l'ID de la localisation (WOEID)
woeid = 23424819  # WOEID pour la France

# Récupération des tendances pour la localisation spécifiée
trends = api.get_place_trends(id=woeid)

# Affichage des tendances
print("Tendances en France :")
for index, trend in enumerate(trends[0]['trends'], start=1):
    print(f"{index}. {trend['name']}")

# Saisie du choix du hashtag
choice = int(input("Sélectionnez le numéro du hashtag : "))

# Vérification de la validité du choix
if 1 <= choice <= len(trends[0]['trends']):
    selected_trend = trends[0]['trends'][choice - 1]
    hashtag = selected_trend['name']
    print(f"\nUtilisateurs ayant publié le hashtag '{hashtag}' :")

    # Récupération des tweets avec le hashtag spécifié
    tweets = tweepy.Cursor(api.search_tweets, q=hashtag, tweet_mode="extended").items(10)

    # Affichage des utilisateurs ayant publié le hashtag
    for tweet in tweets:
        print("---")
        print("Auteur :", tweet.user.screen_name)
        print("Contenu :", tweet.full_text)
else:
    print("Choix invalide. Veuillez sélectionner un numéro de hashtag valide.")