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

st.title("Resumo do próposito da ferramenta")
st.header("Resumo do próposito da ferramenta")
st.subheader("subheader ashduahsdas")
st.write("write asmdasmola")
st.write("")
st.write("")

# =================================================
# =============== HELPER FUNCTIONS ================
# =================================================

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

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
    exp_density = st.beta_expander("Click here to expand and see the portfolio on a density map by location and expected profit.")

    with exp_density:
        st.write("Map is colored according to *expected profit* range.")
        st.write("Properties are grouped by density.")
        st.write("You can click on a number to zoom in.")

        # creating filter
        st.subheader("Properties")
        st.write("This checkbox filters the properties according to previously agreed criteria.")
        f_decision = st.checkbox('Check to see properties suggested to be purchased.')
        if f_decision:
            data = data[data['decision']==1]
            st.write('There are', data.shape[0], 'properties fulfilling the requirements')
        else:
            data = data.copy()
            st.write('*All properties available are been shown.*')

        # defining map dataframe
        dfmap = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                           default_zoom_start=15)

        # grouping properties for dfmpap
        make_cluster = MarkerCluster().add_to(dfmap)

        for name, row in data.iterrows():
            folium.Marker([row['lat'], row['long']],
                          popup = 'Available on {0} for {1}. Selling price suggestion is {2}, resulting on an expected profit of {3}.'.format(
                              row['date'], row['buying_price'], row['selling_price_suggestion'],
                              row['expected_profit'])).add_to(make_cluster)

        # coloring map area
        df_geofile = geofile[geofile['ZIP'].isin(data['zipcode'].tolist())]
        folium.features.Choropleth(data=data, geo_data=df_geofile, columns=['zipcode', 'expected_profit'],
                                   key_on='feature.properties.ZIP',
                                   fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
                                   legend_name='Expected Profit').add_to(dfmap)

        # adding layer details
        #folium.map.Layer('test').add_to(dfmap)
        folium.LayerControl('topright', collapsed=True).add_to(dfmap)

        folium_static(dfmap)



    exp_density.write("")
    exp_density.write("*End of portfolio density view*")
    exp_density.write("")

    return None

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
