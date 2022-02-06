# P001_RealEstate_Insights

_If you prefer to read in english, please [click here](https://github.com/marianaborgal/P001_RealEstate_Insights/blob/main/README.md)_

Esse repositório contém códigos da análise do portfólio de uma empresa imbobiliária.<br>
Todas as informações abaixo são fictícias. 

#### Projeto 001 - Real Estate Insights:
Os objetivos desse projeto são:
* Realizar a análise exploratória de dados nas propriedades disponíveis no conjunto de dados.
* Determinar quais propriedades deveriam ser compradas de acordo com os critérios do negócio.
* Desenvolver um [dashboard](https://p001-realstate-insights.herokuapp.com/) online que possa ser acessado pelo CEO através de um celular ou computador.
<br>

---
## 1. Problema do Negócio
O modelo de negócios da House Rocket consiste na compra e revenda de imóveis por meio de uma plataforma digital. O cientista de dados é responsável por desenvolver um dashboard online para que o CEO da empresa tenha uma visão geral dos imóveis disponíveis que possam fazer parte do portfólio da House Rocket em King County (EUA).<br>

<br>O [dashboard](https://p001-realstate-insights.herokuapp.com/) deve conter:
   * Quais propriedades a empresa deve comprar.
   * Uma visualização de mapa com propriedades disponíveis.
   * Uma visualização de tabela com filtros de atributos.
   * Lucro esperado de cada propriedade. <br> <br>


**_Exemplo visual disponível no dashboard:_**

<img src="https://user-images.githubusercontent.com/77681284/152690550-fc5b1c2e-6cf6-4bb5-ae7d-0b19b936ac0d.png"/>


## 2. Business Results
Com base nos critérios de negócios, dos 21.436 imóveis disponíveis, 10.707 podem ser comprados pela House Rocket e podem resultar em um lucro de US$1,2B. <br>
Valor Máximo Investido: US$ 4.163.721.410,00<br>
Valor máximo Retornado: US$ 5.412.837.833,00<br>
Lucro Máximo Esperado: US$ 1.249.116.423,00<br>

Resultando em uma receita bruta de 30,0%.
<br><br>

## 3. Business Assumptions
* Os dados disponíveis são apenas de maio de 2014 a maio de 2015.
* Propriedades com número de quartos desproporcionais com área de estar interior foram excluídos, assumindo que era um erro de input nos dados.
* Estações do ano:<br>
   * Primavera começa em 21 de Março<br>
   * Verão começa em 21 de Junho<br>
   * Outuno começa em 23 de Setembro<br>
   * Inverno começa em 21 de Dezembro<br>
* Business criteria to determine wether a property should be bought are:
   * Property must have a 'condition' equals or bigger than 3.
   * Property price must be below or equal the median price on the region (zipcode)
* As variáveis originais do conjuto de dados são:<br>

Variável | Definição
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
10. Dashboard deploy on [Heroku](https://p001-realestate-insights.herokuapp.com/)
<br>

## 5. Top 4 Data Insights
1. Properties built with basements decreased after the 80s
2. Almost 60% of the properties became available during summer/spring.
3. 50% of properties that should be bought are in a 15km radius from the lake.
4. Properties selected to be bought in a 15km radius from lake correspond to 60% of expected profit.
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
* Python from Zero to DS lessons on [Youtube](https://www.youtube.com/watch?v=1xXK_z9M6yk&list=PLZlkyCIi8bMprZgBsFopRQMG_Kj1IA1WG&ab_channel=SejaUmDataScientist)
* Blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/)
* Dataset House Sales in King County (USA) from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
* Variables meaning on [Kaggle discussion](https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885)
* <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

![home](https://user-images.githubusercontent.com/77681284/117519523-439a7900-af7a-11eb-8cf0-4900c78737e4.png)


