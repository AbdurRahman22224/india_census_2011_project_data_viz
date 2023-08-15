import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
   page_title="India Census 2011 Data Vis",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)
df = pd.read_csv('india census.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')
list_of_states.insert(0, ' ')

st.sidebar.title('India Census 2011')

selected_state = st.sidebar.selectbox('Select a state', list_of_states, index=0)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.iloc[:, 5:]))

secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.iloc[:, 5:]))
graph = st.sidebar.selectbox('Select The Graph', ['Treemap', 'Sunburst'])


def click_button():
    st.session_state.clicked = True


def starting():
    st.title(':blue[_Data Visualization_]')
    st.text(f'Size represent {primary}')
    st.text(f'Color represents {secondary}')
    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=3.5,
                                size_max=25,
                                mapbox_style="carto-positron", width=1200, height=800, hover_name='District',
                                color_continuous_scale=px.colors.diverging.Temps, title='Overall India Detail Overview')

        st.plotly_chart(fig, use_container_width=True)
        if graph == 'Treemap':
            st.title(':blue[_Treemap_]')
            fig1 = px.treemap(df, path=[px.Constant('India'), 'State', 'District'], values='Population', width=1200,
                              height=800)
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.title(':blue[_Sunburst_]')
            st.latex(r'''
            \bullet\text{Double Click On State To View Specific State Completely}
            ''')
            st.markdown('''
            <style>
            .katex-html {
                text-align: left;
            }
            </style>''',
                        unsafe_allow_html=True
                        )

            fig2 = px.sunburst(df, path=[px.Constant('India'), 'State', 'District', 'Male', 'Female'],
                               values='Population', width=1400, height=1000, hover_name='District',
                               color='literacy_rate')
            st.plotly_chart(fig2, use_container_width=True)

    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                size_max=25,
                                mapbox_style="carto-positron", width=1200, height=800, hover_name='District',
                                color_continuous_scale=px.colors.diverging.Tealrose)

        st.plotly_chart(fig, use_container_width=True)

        if graph == 'Treemap':
            st.title(':blue[_Treemap_]')
            fig1 = px.treemap(df, path=[px.Constant('India'), 'State', 'District'], values='Population', width=1200,
                              height=800)
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.title(':blue[_Sunburst_]')
            st.latex(r'''
            \bullet\text{Double Click On State To View Specific State Completely                                                                               }
            ''')
            st.markdown('''
            <style>
            .katex-html {
                text-align: left;
            }
            </style>''',
                        unsafe_allow_html=True
                        )

            fig2 = px.sunburst(df, path=[px.Constant('India'), 'State', 'District', 'Male', 'Female'],
                               values='Population', width=1400, height=1000, hover_name='District',
                               color='literacy_rate')
            st.plotly_chart(fig2, use_container_width=True)


plot = st.sidebar.button('Plot Graph')

if plot:

    starting()
else:
    pass
