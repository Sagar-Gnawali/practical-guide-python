'''
 Write a Python program that initialises a variable with text from a tweet (or any other social
media post that uses hashtags in text). The program should count how many hashtags (“#”) that
tweet contains. For extra points, a hashtag alone with no content is not a valid hashtag, such as
“My # of followers is too low.” Instead, valid hashtags should be followed by a string of content, such
as “Great #coding session tonight at #bppuniversity.”
'''
def countHashTag(tweet):
    track=False
    for wrds in tweet.split():
        if wrds.startswith('#') and len(wrds)>1:
            track=True
            # track.append(wrds)
    if(track):
        return {"Text":tweet,"Hashtags":tweet.count("#")}
    return {"Text":"Not a valid hashtag","Hashtags":0}

print(countHashTag("This is to #s  #msl"))