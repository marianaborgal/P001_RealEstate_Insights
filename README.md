# P001_RealState_Insights
_NOTE: This project is on going_ <br>
Insights from a real state portfolio analysis.

![home](https://user-images.githubusercontent.com/77681284/117519523-439a7900-af7a-11eb-8cf0-4900c78737e4.png)

This repository contains codes for the porfolio analysis of a real satate company. <br>
All information below is fictional.

#### Project 001 - Real State Insights:
The objetive of this project is to develop a online dashboard to the company's CEO so that a few data analysis can be made by him/her instantaneously.

---
## 1. Business Problem
House Rocket business model consists of purchasing and reselling properties through a digital platform. The data scientist is in charge to develop a online dashboard that can be acessed by the CEO from a mobile or computer with informations of properties available in King County (USA).<br>
The dashboard must contain:
* Report with suggested properties to purchase with recommended value
* Report with suggested properties to sale with recommended value
* Other insights for the company
    * xxxx _on going_
    * Data overview - general iformations about the database
    * Prorpeties by zipcode - informations about the properties grouped by zipcode
    * Portfolio density map - a map view with the database distribution 
    * Properties price by timeline - properties price by year built or by date sold, and properties price distribution 
    * Properties distribution by main attributes - properties distribution by number of bedrooms, bathrooms, floors, and by wether the property has or not a water view.
    * Personalized data and map view - a section to choose attributes and see both dataframe and map distribution of these properties.
    * xxxx _on going_

## 2. Business Results
_on going_

## 3. Business Assumptions
* The data available is only from May 2014 to May 2015.
* Seasons of the year:<br>
      * Spring starts on March 21st<br>
      * Summer starts on June 21st<br>
      * Fall starts on September 23rd<br>
      * Winter starts on December 21d<br>
* The variables goes as follows:<br>

Variable | Definition
------------ | -------------
|id | Unique ID for each property available|
|date | Date that the property was available|
|price | Sale price of each property |
|bedrooms | Number of bedrooms|
|bathrooms | Number of bathrooms, where .5 accounts for a room with a toilet but no shower, and .75 or ¾ bath is a bathroom that contains one sink, one toilet and either a shower or a bath.|
|sqft_living | Square footage of the apartments interior living space|
|sqft_lot | Square footage of the land space|
|floors | Number of floors|
|waterfront | A dummy variable for whether the apartment was overlooking the waterfront or not|
|view | An index from 0 to 4 of how good the view of the property was|
|condition | An index from 1 to 5 on the condition of the apartment|
|grade | An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above | The square footage of the interior housing space that is above ground level|
|sqft_basement | The square footage of the interior housing space that is below ground level|
|yr_built | The year the property was initially built|
|yr_renovated | The year of the property’s last renovation|
|zipcode | What zipcode area the property is in|
|lat | Lattitude|
|long | Longitude|
|sqft_living15 | The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15 | The square footage of the land lots of the nearest 15 neighbors|

<br>

## 4. Solution Strategy
* xxxx _on going_
1. Understanding the business model
2. Understanding the business problem
3. Collecting the data
4. Data Description
5. Feature Engineering
6. Data Filtering
7. Exploratory Data Analysis
8. Insights Conclusion
9. Dashboard deploy on [Heroku](xxx)
* xxxx _on going_

## 5. Top 3 Data Insights
1. x
2. x
3. x

## 6. Conclusion
The objective of this project was to create a online dashboard to House Rocket's CEO. Deploying the dashboard on Heroku platforms provides the CEO acess from anywhere facilitating both pre-arrange or costumized data visualization.

## 7. Next Steps
* xxxx _on going_


----
**References:**
* Python from Zero to DS lessons on [Youtube](https://www.youtube.com/watch?v=1xXK_z9M6yk&list=PLZlkyCIi8bMprZgBsFopRQMG_Kj1IA1WG&ab_channel=SejaUmDataScientist)
* Blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/)
* Dataset House Sales in King County (USA) from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
* Variables meaning on [Kaggle discussion](https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885)
* <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
