__author__ = 'RaccoonChad'

import pytumblr
from tumblr_keys import *

# authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret)

'''
Posts an image to your tumblr.
Make sure you point an image in your hard drive. Here, 'image.jpg' must be in the
same folder where your script is saved.
From yourBlogName.tumblr.com should just use 'yourBlogName'
The default state is set to "queue", to publish use "published"

client.create_text(
    'raccoonchad',
    state="published",
    tags=["testing", "ok"],
    title="Testing",
    body="testing123")
'''

client.info()
