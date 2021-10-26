# ✨ Live tweet sentiment analysis [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
A live Twitter sentiment analyzer using Tweepy, HuggingFace Transformers, and Streamlit that helps to find the live sentiment of tweeples(people who tweet are called as tweeples) on some celebrity or any event like, say, COVID at this moment?

## Installation:
***pip install -r requirements.txt*** will install the necessary dependencies

## Usage:
Run the command : ***streamlit run main.py*** and it will launch the webapp at http://localhost:8501 in your default browser.

![Animation](https://user-images.githubusercontent.com/29462447/138943063-796d7fea-ddab-46cc-93bf-d195d30edc42.gif)

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build --tag live_tweet_sentiment_app .
```
4. Run the docker:
```
docker run --publish 8000:8080 --detach --name bb live_tweet_sentiment_app
```

This will launch the dockerized app. Navigate to ***localhost:8000*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
