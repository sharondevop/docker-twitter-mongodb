# docker-twitter-mongodb

### Description
A simple Python script to save tweets to a MongoDB using the Twitter Streaming API.

### Prerequisites
You need the following Python packages:
* tweepy
* pymongo

To use the Twitter API you need your personal consumer key, consumer secret, access token and acces token secret. You can get it from the [Twitter Application Management](https://apps.twitter.com)

### Usage
Put in **set-var.sh** the API keys 
export it to environment-variable and run docker-compose:

` . set-var.sh && docker-compose up`

To view the messages use mongo-express after the stack is ready:
http://localhost:8081


