# =====================================================================
# ============= TENTATIVA DE MULTIPLOS FILTROS
# =====================================================================

# === creating filters
        f_decision = st.checkbox('Check to see properties suggested to be purchased.')
        f_zipcode = st.multiselect('Select zipcodes', data['zipcode'].sort_values(ascending=True).unique())
        f_id = st.multiselect('Select property ID', data['id'].sort_values(ascending=True).unique())

# === filtering data # improve filtering
        if f_decision:
            f_data = f_data[f_data['decision']==1]
            if (f_zipcode != []) & (f_id != []):
                f_data = f_data.loc[((f_data['zipcode'].isin(f_zipcode)) & (f_data['id'].isin(f_id))), :]
            elif (f_zipcode != []) & (f_id == []):
                f_data = f_data.loc[(f_data['zipcode'].isin(f_zipcode)), :]
            elif (f_zipcode == []) & (f_id != []):
                f_data = f_data.loc[(f_data['id'].isin(f_id)), :]
            else:
                f_data = f_data.copy()
        else:
            f_data = f_data
            if (f_zipcode!=[]) & (f_id!=[]):
                f_data = f_data.loc[ ( (f_data['zipcode'].isin(f_zipcode)) & (f_data['id'].isin(f_id)) ), :]
            elif (f_zipcode!=[]) & (f_id==[]):
                f_data = f_data.loc[ (f_data['zipcode'].isin(f_zipcode)), :]
            elif (f_zipcode==[]) & (f_id!=[]):
                f_data = f_data.loc[ (f_data['id'].isin(f_id)), :]
            else:
                f_data = f_data.copy()

        st.dataframe(f_data)

# =====================================================================
# =====================================================================
# =====================================================================

portfolio_density(data, geofile):
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
        t = folium.map.Layer('test')
        dfmap.add_child(t)
        dfmap.add_child(folium.map.LayerControl('topright', collapsed=True))

        folium_static(dfmap)



    exp_density.write("")
    exp_density.write("*End of portfolio density view*")
    exp_density.write("")

    return None


    # ===========================

st.title("Portfolio density map")
exp_density = st.beta_expander(
    "Click here to expand and see the portfolio concentration map by location and expected profit.")

with exp_density:
    exp_filters = st.beta_expander("Click here to expand filters")
    exp_density.write("")
    exp_density.write("*End of portfolio density view*")
    exp_density.write("")
    with exp_filters:
        # creating filters

        st.subheader("This checkbox filters the properties which fulfill business requirements.")
        f_decision = st.checkbox('Check to see properties suggested to be purchased.')
        if f_decision:
            data = data[data['decision'] == 1]
            st.write('There are', data.shape[0], 'properties available according to previously agreed criteria.')
        else:
            data = data.copy()
            st.write('*Note: All properties available are been shown. You can check the box above to filter.*')
        # f_dist_fromlake # create filter to select radius from lake,
        # show message of expected profit within the radius selected
        # show message of correspondent overall profit (15% of all profit. ex:)
        f_zipcode = st.multiselect('Select zipcodes', data['zipcode'].sort_values(ascending=True).unique())
        f_id = st.multiselect('Select property ID', data['id'].sort_values(ascending=true).unique())

    c1, c2 = st.beta_columns((1, 1))

    f_decision = st.checkbox('Check to see properties suggested to be purchased.')
    if f_decision:
        data = data[data['decision'] == 1]
        st.write('There are', data.shape[0], 'properties available according to previously agreed criteria.')
    else:
        data = data.copy()
        st.write('*Note: All properties available are been shown. You can check the box above to filter.*')

    c1.header("**Map**")
    with c1:

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

        folium_static(dfmap)

    c2.header("Properties Information")
    with c2:
        st.subheader("The table below presents the main properties attributes."

return None