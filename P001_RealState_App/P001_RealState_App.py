import streamlit            as st
import pandas               as pd
import plotly.graph_objects as go
import geopandas
import folium

from PIL import Image
from streamlit_folium  import folium_static
from folium.plugins    import MarkerCluster


# =================================================
# ================== PAGE SET UP ==================
# =================================================

# === page titles
st.set_page_config(page_title="HR Insights", page_icon="📊",
                   layout="wide")


st.markdown('*Additional information about House Rocket and this streamlit creator are by the end of this page.*')
st.write('')

c1, c2 = st.beta_columns((1,5))

# image
with c1:
    photo = Image.open('house.jpg')
    st.image(photo, width=250)

# headers
with c2:

    st.write('')
    HR_format = '<p style="font-family:sans-serif;' \
                   'color:#0000cc;' \
                   'font-size: 50px;' \
                   'font-weight: bold;' \
                   'font-style: italic;' \
                   'text-align: left;' \
                   '">House Rocket Company</p>'
    st.markdown(HR_format, unsafe_allow_html=True)

    welcome_format = '<p style="font-family:sans-serif;' \
                       'color:#0000cc;' \
                       'font-size: 25px;' \
                       'font-style: italic;' \
                       'text-align: left;' \
                       '">Welcome to House Rocket Data Report</p>'
    st.markdown(welcome_format, unsafe_allow_html=True)

# =================================================
# =============== HELPER FUNCTIONS ================
# =================================================

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    # data = data.head(1000) # filter data to edit faster

    data.style.format(formatter={('buying_price', 'median_price_zipcode',
                                  'selling_price_suggestion', 'expected_profit'): '{:,.2f}'})

    return data

@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile

def set_features(data):
    # create columns as needed

    return data

def data_information(data):
    st.title("Data Information")
    exp_data = st.beta_expander("Click here to expand and see the dataset general information", expanded=False)
    with exp_data:
        st.subheader("Data Dimensions")
        st.write("Number of Registers:", data.shape[0])
        st.write("Number of Attributes:", data.shape[1])

        st.subheader("Time Interval")
        st.write("", data['date'].min())
        st.write("", data['date'].max())

    exp_data.write("")
    exp_data.write("*End of data overview*")

    return None

def portfolio_density(data, geofile):
    st.title("Portfolio distribution map")
    exp_density = st.beta_expander("Click here to expand and see the portfolio concentration map by location and expected profit.", expanded=True)
    with exp_density:

        st.write('**The sum of expected profit is', 'US$ {:,.2f}'.format(data['expected_profit'].sum()),
                 'for all available properties on database according to previously agreed criteria.**')

        f_decision = st.checkbox('Check to see properties suggested to be purchased.')
        if f_decision:
            data = data[data['decision'] == 1]
            st.write('There are', data.shape[0], 'properties fulfilling the requirements')
        else:
            data = data.copy()
            st.write('*All properties available are been shown.*')


        c1, c2 = st.beta_columns((1, 1))

        c1.subheader('Properties distribution') # map
        with c1:

            # defining map dataframe
            dfmap = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                               default_zoom_start=15)

            # grouping properties for dfmpap
            make_cluster = MarkerCluster().add_to(dfmap)

            # '{:, .2f}'.format
            for index, row in data.iterrows():
                folium.Marker([row['lat'], row['long']],
                              popup='Available since {0} for US$ {1}.'
                                    '\nSelling price suggestion is US$ {2}, resulting on an expected profit of US$ {3}.'
                                    '\nZipcode: {4}'
                                    '\nProperty ID: {5}'
                                    .format(row['date'], row['buying_price'], row['selling_price_suggestion'],
                                            row['expected_profit'], row['zipcode'], row['id']))\
                              .add_to(make_cluster)

            # coloring map area
            df_geofile = geofile[geofile['ZIP'].isin(data['zipcode'].tolist())]
            folium.features.Choropleth(data=data, geo_data=df_geofile, columns=['zipcode', 'expected_profit'],
                                       key_on='feature.properties.ZIP',
                                       fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
                                       legend_name='Expected Profit').add_to(dfmap)

            folium_static(dfmap)

        c2.subheader('Properties Information') # table
        with c2:

            if f_decision:
                data = data[data['decision']==1]
            else:
                data = data.copy()

            table = data[['id', 'date', 'condition', 'zipcode', 'dist_fromlake',
                          'buying_price', 'median_price_zipcode', 'selling_price_suggestion', 'expected_profit' ]].copy()


            # table = go.Figure(data=[go.Table(
            #                                  header=dict(values=list(df.columns),
            #                                              align='center'),
            #                                  cells=dict(values=[df['id'], df['date'], df['condition'], df['zipcode'],
            #                                                     df['buying_price'], df['median_price_zipcode'], df['selling_price_suggestion'], df['expected_profit'],
            #                                                     df['dist_fromlake']],
            #                                             align='center') )
            #                         ] )
            #
            #
            # st.write(table)


            st.dataframe(table)
            st.write('*Properties with selected attributes:', '{:,}*'.format(table['id'].count()))


    exp_density.write("")
    exp_density.write("*End of distribution view*")

    return None

def profit_business_attributes(data):
    st.title("Estimated Profit - Business Attributes")
    exp_att_bus = st.beta_expander('Click here to expand and see estimated profit table according to business attributes', expanded=True)
    with exp_att_bus:

        # business data = b
        b = data[data['decision']==1][['id', 'date', 'condition', 'zipcode', 'dist_fromlake',
                                       'buying_price', 'median_price_zipcode', 'selling_price_suggestion', 'expected_profit',
                                       'yr_built', 'yr_renovated', 'neighbourhood',
                                       'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'sqft_above', 'sqft_basement']].copy()

        # ======= creating filters
        c1, c2, c3 = st.beta_columns((4,1,4))

        # filters: buying_price, expected_profit, dist_fromlake
        with c1:

            f_buying_price = st.slider('Select maximum price',
                                       int(b['buying_price'].min()),
                                       int(b['buying_price'].max()), key='price bus',
                                       value=int(b['buying_price'].max()))
            f_expected_profit = st.slider('Select maximum expected profit',
                                          int(b['expected_profit'].min()),
                                          int(b['expected_profit'].max()),
                                          value=int(b['expected_profit'].max()))
            f_dist_fromlake = st.slider('Select maximum distance from lake',
                                        int(b['dist_fromlake'].min()),
                                        int(b['dist_fromlake'].max()),
                                        value=int(b['dist_fromlake'].max()), step=2)

            # filtering business data = f_b
            f_b = b[(b['buying_price'] <= f_buying_price) &
                    (b['expected_profit'] <= f_expected_profit) &
                    (b['dist_fromlake'] <= f_dist_fromlake)]

        # filters: zipcode, id
        with c3:

            f_zipcode = st.multiselect('Type or select zipcodes',
                                       f_b['zipcode'].sort_values(ascending=True).unique())
            f_id = st.multiselect('Type or select properties ID',
                                  f_b['id'].sort_values(ascending=True).unique())

            # filtering business data = f_b2
            if (f_id != []) & (f_zipcode != []):
                f_b2 = f_b.loc[(f_b['id'].isin(f_id)) & (f_b['zipcode'].isin(f_zipcode)), :]
                # st.write('id and zipcode')
            elif (f_id != []) & (f_zipcode == []):
                f_b2 = f_b.loc[f_b['id'].isin(f_id), :]
                # st.write('id')
            elif (f_id == []) & (f_zipcode != []):
                f_b2 = f_b.loc[f_b['zipcode'].isin(f_zipcode), :]
                # st.write('zipcode')
            else:
                f_b2 = f_b.copy()
                # st.write('none')

        # ======= printing dataframe
        st.dataframe(f_b2)
        st.write('')
        st.write('**Properties with selected attributes:', '{:,}**'.format(f_b2['id'].count()))
        st.write('**Sum of expected profit for subset above:', 'US$ {:,.2f}**'.format(f_b2['expected_profit'].sum()))

    exp_att_bus.write("")
    exp_att_bus.write("*End of table view*")

    return None

def profit_properties_attributes(data):
    st.title("Estimated Profit - Properties Attributes")
    exp_att_prop = st.beta_expander('Click here to expand and see estimated profit table according to properties attributes', expanded=False)
    with exp_att_prop:

        # properties data = p
        p = data[data['decision']==1][['id', 'date', 'condition', 'zipcode', 'dist_fromlake',
                                       'buying_price', 'median_price_zipcode', 'selling_price_suggestion', 'expected_profit',
                                       'yr_built', 'yr_renovated', 'neighbourhood',
                                       'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'sqft_above', 'sqft_basement']].copy()

        # ======= creating filters
        c1, c2, c3 = st.beta_columns((1,2,2))

        # filters: bedrooms, bathrooms
        with c1:

            f_bedrooms = st.selectbox('Select maximum number of bedrooms',
                                      p['bedrooms'].sort_values(ascending=True).unique().tolist(), key='bedrooms')

            f_bathrooms = st.selectbox('Select maximum number of bathrooms',
                                      p['bathrooms'].sort_values(ascending=True).unique().tolist(), key='bathrooms')

        # filters: sqft_living, sqft_basement
        with c2:
            f_sqft_living = st.slider('Select maximum interior living space size',
                                      int(p['sqft_living'].min()),
                                      int(p['sqft_living'].max()),
                                      value=int(p['sqft_living'].max()), key='living')

            f_sqft_basement = st.slider('Select maximum basement size',
                                      int(p['sqft_basement'].min()),
                                      int(p['sqft_basement'].max()),
                                      value=int(p['sqft_basement'].max()), key='basement')

        # filters: yrbuilt, yrrenovated
        with c3:
            f_yrbuilt = st.slider('Select minimum year property was built',
                                  int(p['yr_built'].min()),
                                  int(p['yr_built'].max()),
                                  value=int(p['yr_built'].min()), key='yrbuilt')

            f_yrrenovated = st.slider('Select minimum year property was renovated',
                                  int(p['yr_renovated'].min()),
                                  int(p['yr_renovated'].max()),
                                  value=int(p['yr_renovated'].min()), key='yrrenovated')

        # filters: buying_price
        f_buying_price = st.slider('Select maximum price',
                                   int(p['buying_price'].min()),
                                   int(p['buying_price'].max()),
                                   value=int(p['buying_price'].max()), key='price prop')

        # ======= filtered properties data = f_p
        f_p = p[ (p['bedrooms']      <= f_bedrooms)  &
                 (p['bathrooms']     <= f_bathrooms) &
                 (p['sqft_living']   <= f_sqft_living ) &
                 (p['sqft_basement'] <= f_sqft_basement) &
                 (p['buying_price']  <= f_buying_price) &
                 (p['yr_built']      >= f_yrbuilt) &
                 (p['yr_renovated']  >= f_yrrenovated)      ]


        # ======= printing dataframe
        st.dataframe(f_p)
        st.write('**Properties with selected attributes:', '{:,}**'.format(f_p['id'].count()))
        st.write('**Sum of expected profit for subset above:', 'US$ {:,.2f}**'.format(f_p['expected_profit'].sum()))


    exp_att_prop.write("")
    exp_att_prop.write("*End of table view*")

    return None


# =================================================
# ================ MAIN FUNCTION ==================
# =================================================

if __name__ == '__main__':
    # ====== DATA EXTRACTION
    data = get_data('house_rocket.csv')

    geofile_raw = get_geofile('https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson')

    set_features(data)

    data_information(data)

    portfolio_density(data, geofile_raw)

    profit_business_attributes(data)

    profit_properties_attributes(data)


st.markdown('---')
st.markdown('---')

st.title('Additional Information')

st.header("Report Purpose:")

st.write('House Rocket business model consists of purchasing and reselling properties through a digital platform.')
st.write("This report was created by a request from House Rocket's CEO to visualize "
         "all properties available to be bought at King County, Seatle.")

st.write('')
st.markdown('This data visualization is part of **House Rocket Insights Project** made by **Mariana Borges**.')
st.markdown('You can read the business context and check the code for this streamlit on [github](https://github.com/marianaborgal/P001_RealState_Insights).')
st.markdown('Other Projects: [Portfolio](https://github.com/marianaborgal)')
st.markdown('Contact me: [LinkedIn](https://www.linkedin.com/in/marianaborgal/)')
