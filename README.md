# Project-3-Twitter-Sentiment-Analysis

## Dataset : https://www.kaggle.com/datasets/kazanova/sentiment140

## Objective: 
The project aims to perform sentiment analysis on a dataset of tweets obtained from Twitter. Sentiment analysis involves determining the sentiment expressed in each tweet, categorizing them as either positive, negative, or neutral. The goal is to gain insights into the sentiment distribution and identify significant features contributing to sentiment predictions.

# 1. Data Exploration:
•	The dataset was loaded from a CSV file containing columns such as "target," "id," "date," "flag," "user," and "text."
•	Basic information about the dataset was displayed, including the data types and the presence of any missing values.

![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/787ff809-dd94-444d-8966-78d3eef766a4)
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/220dfe63-3b56-4712-af8a-c97ece565cd8)


 
 
# 2. Data Cleaning:
•	Missing values were checked, and any NaN values were handled appropriately.
•	Duplicate rows were removed from the dataset.
•	Unnecessary columns ("id," "flag," "user") were dropped.
# 3. Text Preprocessing:
•	Text data underwent preprocessing steps, including the removal of special characters, links, and conversion to lowercase.
•	Tokenization and removal of stopwords were performed using NLTK.
•	Lemmatization was applied to reduce words to their base or root form.
# 4. Exploratory Data Analysis (EDA):
•	Visualizations were created to understand the sentiment distribution, tweet length distribution, and word clouds for positive and negative sentiments.
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/e689c314-f54b-4f24-ab3c-9ff30f919efe)
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/fe95e5a9-c867-4559-b12f-ee29155e1157)


 
 
# 5. Sentiment Distribution:
•	The sentiment distribution was visualized after mapping numerical target values to sentiment labels (Negative, Neutral, Positive).
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/6af8cd96-0505-453c-b65d-50dc4588c004)
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/0673d153-e4e0-475c-adb7-6f8880506ba8)


 
 
# 6. Word Frequency Analysis:
•	Word frequency bar charts were created for both positive and negative sentiments, displaying the most common words.
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/fc6fc010-7dd9-4e23-a770-ebb76b25c014)

 
# 7. Temporal Analysis:
•	Additional time-related features, such as day of the week and hour of the day, were extracted.
•	Sentiment variation over days of the week and by hour of the day was visualized.
 ![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/4dd1a5ab-670d-4b54-942a-ce775a54a500)

# 8. Sentiment Prediction Model:
•	A sentiment prediction model was built using a Random Forest Classifier with TF-IDF vectorization.
•	The model's performance was evaluated using metrics such as accuracy, classification report, and confusion matrix.
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/8a0a8028-ec24-4037-bb5d-713ef2d55363)
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/b06fb2ef-ebee-4822-b755-66daa9d2f419)


 
 
# 9. Feature Importance:
•	Feature importance analysis was conducted to identify the most significant words or phrases contributing to sentiment predictions.
•	The top 20 important features were visualized using bar charts.
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/b6f5ebd0-52d8-4d6b-aa11-e773ce6d36ad)

 
# 10. User Interface:- A simple user interface was developed for users to input custom text for sentiment analysis. - Sentiment prediction results were showcased in a user-friendly manner.
![image](https://github.com/Vinod-Ghanchi/Project-3-Twitter-Sentiment-Analysis/assets/80514865/236e4dd0-35ba-43ef-936d-ca69a1062bcf)


 

