import streamlit as st
import pandas    as pd
import geopandas
import folium

from streamlit_folium  import folium_static
from folium.plugins    import MarkerCluster


# =================================================
# ================== PAGE SET UP ==================
# =================================================

# page titles
st.set_page_config(page_title="HR Insights", page_icon="📊",
                   layout="wide")  # initial_sidebar_state = "expanded"
st.title("*House Rocket Company*")
st.header("*Welcome to House Rocket Data Analysis*")



# =================================================
# =============== HELPER FUNCTIONS ================
# =================================================

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    # drop duplicates

    return data

@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile

def set_features(data):
    # create columns as needed

    return data

def data_overview(data):
    st.title("Data Overview")
    exp_data = st.beta_expander("Click here to expand and see the dataset general information")

    with exp_data:
        st.subheader("Data Dimensions")
        st.write("Number of Registers:", data.shape[0])
        st.write("Number of Attributes:", data.shape[1])

        st.subheader("Time Interval")
        st.write("", data['date'].min())
        st.write("", data['date'].max())

        # c1, c2 = exp_data.beta_columns((1, 1))
        #
        # with c1:
        #     st.subheader("Data Dimensions")
        #     st.write("Number of Registers:", data.shape[0])
        #     st.write("Number of Attributes:", data.shape[1])
        #
        #     st.write("\n\n\n")
        #
        #     st.subheader("Time Interval")
        #     st.write("", data['date'].min())
        #     st.write("", data['date'].max())
        #
        # with c2:
        #     st.subheader("Data Types")
        #     df = pd.DataFrame(data.dtypes.reset_index())
        #     df.columns = ['attributes', 'data types']
        #     st.dataframe(df)

    exp_data.write("")
    exp_data.write("*End of data overview*")
    exp_data.write("")

    return None

def portfolio_density(data, geofile):
    st.title("Portfolio density map")
    exp_density = st.beta_expander("Click here to expand and see the portfolio concentration map by location and expected profit.")

    with exp_density:

        data = data.head(100) # testing

        st.subheader("Select filters below")

        # creating filters
        st.write("**Decision:** This checkbox filters the properties according to previously agreed criteria.")
        f_decision = st.checkbox('Check to see properties suggested to be purchased.')
        f_zipcode = st.multiselect('Select zipcodes', data['zipcode'].sort_values(ascending=True).unique())

        c1, c2 = st.beta_columns((1,1))

        c1.subheader("Properties distribution")
        with c1:
            st.write("Map is colored according to *expected profit* range.")

            if (f_decision==True) & (f_zipcode!=[]):
                data = data[(data['decision'] == 1) & (data['zipcode'].isin(f_zipcode))]
            elif (f_decision==True) & (f_zipcode==[]):
                data = data[data['decision'] == 1]
            elif (f_decision==False) & (f_zipcode!=[]):
                data = data[(data['decision'] == 0) & (data['zipcode'].isin(f_zipcode))]
            else:
                data = data.copy()
                st.write('*All properties available are been shown.*')

            # defining map dataframe
            dfmap = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                               default_zoom_start=15)

            # grouping properties for dfmpap
            make_cluster = MarkerCluster().add_to(dfmap)

            for index, row in data.iterrows():
                folium.Marker([row['lat'], row['long']],
                              popup='Available since {0} for US$ {1}.'
                                    '\nSelling price suggestion is US$ {2}, resulting on an expected profit of US$ {3}.'
                                    '\nZipcode: {4}'
                                    '\nProperty ID: {5}'.format(
                                  row['date'], row['buying_price'], row['selling_price_suggestion'],
                                  row['expected_profit'], row['zipcode'], row['id'])).add_to(make_cluster)

            # coloring map area
            df_geofile = geofile[geofile['ZIP'].isin(data['zipcode'].tolist())]
            folium.features.Choropleth(data=data, geo_data=df_geofile, columns=['zipcode', 'expected_profit'],
                                       key_on='feature.properties.ZIP',
                                       fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
                                       legend_name='Expected Profit').add_to(dfmap)

            dfmap.add_child(folium.map.LayerControl('topright', collapsed=True))  # improve it later

            # adding layer details
            t = folium.map.Layer('test')
            dfmap.add_child(t)
            dfmap.add_child(folium.map.LayerControl('topright', collapsed=True))

            folium_static(dfmap)

            st.write("You can click on a number to zoom in.")



        c2.subheader("Properties Information")
        with c2:
            st.write("The table below presents the main properties attributes.")
            #f_id = st.multiselect('Select property ID', data['id'].sort_values(ascending=True).unique())

            st.dataframe(data[['id', 'zipcode', 'buying_price', 'expected_profit', 'decision']])
            # add id filter
            # printar soma do expected profit dos dados filtrados
            st.write("The expected profit for the properties filtered is US$ ")

    exp_density.write("")
    exp_density.write("")
    exp_density.write("*End of portfolio density view*")
    exp_density.write("")

    return None

def new (data):

    st.title("New")
    exp_new = st.beta_expander('click')
    with exp_new:
        f = data
        st.dataframe(f)

    exp_new.write("")
    exp_new.write("*End of view*")
    exp_new.write("")
    return None

def new_2 (data):

    st.title("New")
    exp_new_2 = st.beta_expander('click')
    with exp_new_2:
        f = data
        st.dataframe(f)

    exp_new_2.write("")
    exp_new_2.write("*End of view*")
    exp_new_2.write("")

    return None


# def new_2 (data):
#
#     st.title("New")
#     exp_new_2 = st.beta_expander('click')
#     with exp_new_2:
#         f = data
#         st.dataframe(f)
#
#     exp_new_2.write("")
#     exp_new_2.write("*End of view*")
#     exp_new_2.write("")
#
#     return None


# =================================================
# ================ MAIN FUNCTION ==================
# =================================================

if __name__ == '__main__':
    # ====== DATA EXTRACTION
    data = get_data('../datasets/processed/house_rocket.csv')
    geofile_raw = get_geofile('https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson')

    data = set_features(data)

    data_overview(data)

    portfolio_density(data, geofile_raw)

    new(data)

    new_2(data)



st.title("Resumo do próposito da ferramenta")
st.markdown("Resumo do próposito da ferramenta")
st.header("Resumo do próposito da ferramenta")
st.subheader("subheader ashduahsdas")
st.write("write asmdasmola")
st.write("")
st.write("")