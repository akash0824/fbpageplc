import fbpageplc
import json

pagename = "BPAmerica"
access_token = "EAACEdEose0cBADxgEpVqCpi1m2fdqoS2zfqonpoGzaqWgwZA9ZAkzmQ15zSWvmoYJuq29QZBXyvDnp5HiCyZAzw5RXR5pZCz5V7EZBnoVC9SnUWq75vf3XY7wUQIwBqltP4sfeOz7VS0g2l8WOpZA8e6rs4bZA1iEzOzfFX2kmded5L76wTZA3iUx4N5EftfDaHcZD"
stdate = "1 august 2017"
endate = "1 september 2017"

posts = fbpageplc.get_posts(pagename, access_token, stdate, endate)

likes = []
comments = []

for p in posts:
    post_id = p["id"]
    like = fbpageplc.get_likes(post_id, access_token)
    comment = fbpageplc.get_comments(post_id, access_token)

    likes.append(like)
    comments.append(comment)


with open(pagename + "_posts.json","w") as file:
    json.dump(posts, file)

with open(pagename + "_likes.json","w") as file:
    json.dump(likes, file)

with open(pagename + "_comments.json","w") as file:
    json.dump(comments, file)
