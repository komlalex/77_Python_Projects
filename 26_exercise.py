"""A file called hashtags.txt containing hashtags related to sport is
attached to the exercise:
#sport #fitness #training #motivation #gym #sports #workout #fit #football
#love #in #lifestyle #running #like #bodybuilding #healthy #instagram
#health #soccer #follow • #nature #fun #healthylifestyle #muscle öbhfyp
#fashion #fitfam #gymlife ffphotoofthed Spicoftheday #exercise ömma
#sportlife #boxing #athlete #bike #basketball #happy öde
             Implement a function called clean_hashtags() that loads the
included hashtags.txt file and does some cleanup. Extract hashtags up to 4
characters long. The '#' sign is not included in the length of the hashtag.
For example, the hashtag '#gym’ has a length of 3.
Also take care to remove duplicates, if any. Then return the alphabetically
sorted hashtags as a list.
In response, call clean_hashtags( ) function and print the result to the
console.
"""


def clean_hashtags():
    try:

        fh = open("hashtags.txt")
        content = fh.read()
        hashtags = content.split()
        short_hashtags = [hashtag for hashtag in hashtags if len(hashtag) <= 5]
        return short_hashtags

    except IOError:
        raise IOError("Error loading file")


print(clean_hashtags())
