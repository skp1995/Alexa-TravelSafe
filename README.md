# TravelSafe-with-Alexa

### This project won the Sunhacks18 MLH Hackathon in 'best alexa skill' category
## Inspiration

37,461 fatal road accidents are reported in the US for the year 2016 alone. From the data, we got from Department of Transportation, few highways are more accident prone than others. We wanted to build a service that alerts the drivers on such highways through easily accessible and non-distracting medium by using Alexa (which now being adopted by mainstream automakers in the US )

## What it does

Upon user asking about the current location details while he is on road, Alexa device responds with a safety rating for the road, Currently, it classifies the road into either of, safe, accident-prone - caution advised, Dangerous road - extreme caution advised.

## How we built it

Since Alexa does not have access to user's GPS data, We have developed an android app that resides on user's mobile and updates the user location of periodically.

To save the user's location and respond to request from Alexa (lambda function) we have a Django server to handle the Http request and response.

Once the mobile device performs a check-in to our server with GPS coordinates, with the help of google maps API, we are able to get the highway name we are on. We then used machine learning to classify the road into its safety rating.

we have used logistic regression with no. of accidents reported on the road, Length of the road (to normalize the data), DUI reports, the degree of fatality of the accident to give a score to the road/highway. We then split the distribution into three ranges to get the category

## Challenges we ran into

Deciding what features of the dataset we want to use and their respective weight for classification.

Data collection and cleaning

Alexa was a new skill for our team

## Accomplishments that we're proud of


Our logistic regression model was able to classify the data into correct categories within a reasonable test error.

We have found some of the extremely accident-prone roads in the united states

Learning Alexa skill development was very interesting and we see how a good idea can positively impact people with Alexa

## What we learned


Alexa skill development Google maps API for location related queries Benefits of having a smart assistant in cars

What's next for TravelSafe
We want to consider the weather data like visibility, precipitation, and temperature to see how it will affect the safety of the road

In case of an accident, we would like our service to notify emergency services (assuming cars with Alexa give it access to car information - ex if airbags are deployed)

full-featured android and iOS application to allow people without Alexa enabled cars to access our service.

## Built With


python, 
android, 
alexa, 
machine-learning, 
django, 
java, 
scikit-learn, 
pandas
