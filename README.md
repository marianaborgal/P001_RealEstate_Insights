# P001_RealEstate_Insights

<i>Se quiser ler sobre esse projeto em português, [clique aqui](https://github.com/marianaborgal/P001_RealEstate_Insights/blob/main/Readme_EmPortugu%C3%AAs.md).</i>


This repository contains codes for the porfolio analysis of a real estate company. <br>
All information below is fictional.

#### Project 001 - Real Estate Insights
The objetives of this project are:
* Perform exploratory data analysis on properties available on dataset.
* Determine which properties should be bouth according to business criteria.
* Develop a online [dashboard](https://p001-realestate-insights.herokuapp.com/) that can be acessed by the CEO from a mobile or computer.
<br>

## 1. Business Problem
House Rocket business model consists of purchasing and reselling properties through a digital platform. The data scientist is in charge to develop a online dashboard so that the company's CEO can have an overview of properties available to became part of House Rocket portfolio in King County (USA).<br>

The [dashboard](https://p001-realestate-insights.herokuapp.com/) must contain:
   * Which properties the company should buy.
   * A map view with properties available.
   * A table view with attributes filters.
   * Expected profit of each property.<br><br>


**_Dashboard screenshot exemple:_**

<img src="https://user-images.githubusercontent.com/77681284/152690550-fc5b1c2e-6cf6-4bb5-ae7d-0b19b936ac0d.png"/>


<!-- <img src="https://user-images.githubusercontent.com/77681284/117519523-439a7900-af7a-11eb-8cf0-4900c78737e4.png" alt="image" width="200" align="right"/>
<img src="https://user-images.githubusercontent.com/77681284/152690450-089c6833-edbe-4eb2-bfa6-261973611e3a.png" alt="dashboard screenshot" width="300"  align="right"/> -->

## 2. Business Results
There are 21,436 available properties. Based on business criteria, 10,707 should be bought by House Rocket resulting on a US$1,2B profit.<br>
Maximum Value Invested: US$4,163,721,410.00<br>
Maximum Value Returned: US$5,412,837,833.00<br>
Maximum Expected Profit: US$1,249,116,423.00<br>

This results on a 30.0 % gross revenue.
<br><br>

## 3. Business Assumptions
* The data available is only from May 2014 to May 2015.
* Properties with bedrooms disproportional with interior living squarefoot were deleted, assuming it was a input error.
* Seasons of the year:<br>
   * Spring starts on March 21st<br>
   * Summer starts on June 21st<br>
   * Fall starts on September 23rd<br>
   * Winter starts on December 21d<br>
* Business criteria to determine wether a property should be bought are:
   * Property must have a 'condition' equals or bigger than 3.
   * Property price must be below or equal the median price on the region (zipcode)

* The variables on original dataset goes as follows:<br>

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

* Variables created during the project development goes as follow:

Variable | Definition
------------ | -------------
| decision | wether a property should be bought |
| median_price_zipcode | median price of zipcode region |
| selling_price_suggestion | 30% more on buying price, if property should be bought |
| expected_profit | difference between buying price and selling price suggestion  |
| dist_fromlake | distance from the center of Evergreen Point Floating Bridge |
| season | season property became available |
| med_autumn | median price from properties available during autumn  |
| med_spring | median price from properties available during spring |
| med_summer | median price from properties available during summer |
| med_winter | median price from properties available during winter |
| season_to_sell | in which season property should be sold |

<br>

## 4. Solution Strategy
1. Understanding the business model
2. Understanding the business problem
3. Collecting the data
4. Data Description
5. Data Filtering
6. Feature Engineering
8. Exploratory Data Analysis
9. Insights Conclusion
10. Dashboard deploy on [Heroku](https://p001-reale-insights.herokuapp.com/)
<br>

## 5. Top 3 Data Insights
1. The number of properties built with basements decreased after the 80s.
2. Almost 60% of the properties became available during summer/spring.
3. Properties selected to be bought in a 15km radius from lake correspond to 60% of expected profit.
<br>

## 6. Conclusion
The objective of this project was to create a online dashboard to House Rocket's CEO. Deploying the dashboard on Heroku platforms provided the CEO acess from anywhere facilitating data visualization and business decisions.
<br><br>

## 7. Next Steps
* Determine which season of the year would be the best to execute a sale.
* Get more address data to fill NAs.
* Expand this methodology to other regions that House Rocket operates.
<br>

---
## References:
* Dataset House Sales in King County (USA) from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
* Variables meaning on [Kaggle discussion](https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885)
* <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
* Python from Zero to DS lessons on [Youtube](https://www.youtube.com/watch?v=1xXK_z9M6yk&list=PLZlkyCIi8bMprZgBsFopRQMG_Kj1IA1WG&ab_channel=SejaUmDataScientist)
* Blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/)
