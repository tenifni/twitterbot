import tweepy
import random
import os

 # NOW, create a file in the same mani file called "secret.txt": consumer key, consumer secret, acess token, acess secret. [direct copy and paste].

#opens secret.txt file
with open ("secret.txt") as f: 	
	secrets = f.realines ()
	#secrets = [consumer key, consumer secret, access token, access secret] ---an array
f.close() #closes the file


#get/set Twitter authorization information from secret array
#REMEMBER to remove newline characters: "\n"
CONSUMER_KEY=secret[0].rstrip('\n') #sets the consumer_key to the first element in the array
CONSUMER_SECRET=secrets[1].rstrip('\n') #removes newline character from b/c API does not expect enter line in secret.txt
ACCESS_TOKEN = secrets[2].rstrip('\n')
ACCESS_SECRET=secrets[3].rstrip('\n')


#Give your access info to Tweepy so that you can access the Twitter API
#Otherwise your Tweepy API calls will be rejected :<
auth =tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) #set auth. OAuthHandler function belongs to tweepy, and we put in the parameters
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET) #adding this ACCESS-thingy info to auth. Essentially, paring [consumer_key/secret with access_token/secret]
api = tweepy.API(auth); #access our API and abstract it to a single variable by calling tweepy.api(auth).
#Now we've got our tweepy api access!
#Now, we can do our stuff- getting images, quotes, & posting...


#Build list of tweets! (check out github for building more complex tweetlist)
tweetlist = [
"Physics puns are no joke. It's a relatively dark matter",
"The universe was cold, before it mattered",
"What does a subatomic duck sound like?  QUARK!"]

#Set up a shortcut to your image directory so you have esay access to it later
##We first need to store images in a seperate folder called "img". 
##In order to access these, we set imgdir = to os. get the stuff in this "img/" directory/folder
imgdir= os.listdir("img/") 


#Tweeting! this is the tweet API call!
#Tweepy has function called api.update_with_media 
#that lets you make a new tweet with a photo and text.
#time.sleep(10) means there will be a 10s break between each tweet.
for tweet in tweetlist:
	api_update_media("img/"+random.choice(imgdir),tweet)
	
	#for every tweet it the tweetlist (there are 3), api_update_media--will post a tweet and an iamge.
	#Take our image: "img/"+[random.choice(imgdir)--randomly picks an img from the imgdir directory]. 
	#Take a tweet from the tweelist: tweet.

