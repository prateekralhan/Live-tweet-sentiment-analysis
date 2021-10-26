import streamlit as st
import tweepy as tw
import pandas as pd
from transformers import pipeline


consumer_key = 'BK5xNNZ9FdsG9LF0Oq95u8w7Q'
consumer_secret = 'QWFMttWdxY3OnxmztQt0aJUt23s7dpqMZZJM3FLvggWmsKMnzy'
access_token = '1047019704601194498-27mThjjrDqDBtOXdVSIyr44rcG2LcM'
access_token_secret = 'ttR1EWW4Yvees3uekd47DxdIvgf6lZbo7fPt38xAG0P7x'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
classifier = pipeline('sentiment-analysis')

st.title('✨Live Tweet Sentiment Analysis')
st.markdown('This app uses tweepy to get tweets from twitter based on the input name/phrase. It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis. The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.')

def run():

    with st.form(key='Enter name'):
        search_words = st.text_input('Enter the name for which you want to know the sentiment')
        number_of_tweets = st.number_input('Enter the number of latest tweets for which you want to know the sentiment(Maximum 50 tweets)', 0,50,10)
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        tweets =tw.Cursor(api.search_tweets,q=search_words,lang="en").items(number_of_tweets)
        tweet_list = [i.text for i in tweets]
        p = [i for i in classifier(tweet_list)]
        q=[p[i]['label'] for i in range(len(p))]
        df = pd.DataFrame(list(zip(tweet_list, q)),columns =['Latest '+str(number_of_tweets)+' Tweets'+' on '+search_words, 'sentiment'])
        st.write(df)

if __name__=='__main__':
    run()
