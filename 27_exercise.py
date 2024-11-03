"""A file called hashtags.txt containing hashtags related to sport is
attached to the exercise:
#sport #fitness #training #motivation #gym #sports #workout #fit #football
#love #in #lifestyle #running #like #bodybuilding #healthy #instagram
#health #soccer #follow • #nature #fun #healthylifestyle #muscle öbhfyp
#fashion #fitfam #gymlife ffphotoofthed Spicoftheday #exercise ömma
#sportlife #boxing #athlete #bike #basketball #happy öde
               Implement a function called cleanhashtags( ) that takes three
arguments:
• input file - filename containing hashtags
• output file - filename to which the hashtags should be saved
• length - the maximum length of the hashtag
The '#' sign is not included in the length of the hashtag. For example, the
hashtag '»gym' has a length of 3.
The clean_hashtags( ) function loads a file called input file and does some
hashtag cleanup. The function extracts hashtags up to length characters long
and also removes duplicates. It then  saves the alphabetically sorted
hashtags to a file called output_file, saving each hashtag in a new line.
"""


def clean_hashtag(input_file, output_file, length):
    with open(input_file, "r") as file:
        hashtags = file.read().split()
        short_hashtags = [hashtag for hashtag in hashtags if len(hashtag) <= (length + 1)]
        # Sort and remove duplicates
        short_hashtags = sorted(set(short_hashtags))

        with open(output_file, "w") as file2:
            for hashtag in short_hashtags:
                file2.write(hashtag + "\n")


print(clean_hashtag("hashtag_input.txt", "hashtag_output.txt", 4))
