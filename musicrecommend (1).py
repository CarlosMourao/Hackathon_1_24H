
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
#DATAFRAME IMPORT & SUBSETS
spotify_compact = pd.read_csv('c:/py/spotify_clean.csv')

#VIBES
#chill = spotify_compact[(spotify_compact['energy'] < 0.71) & (spotify_compact['danceability'] > 0.55) & (spotify_compact['danceability'] < 0.75)]

#energetic_and_upbeat = spotify_compact[(spotify_compact['energy'] > 0.71) & (spotify_compact['danceability'] > 0.66)]

#feelgood = spotify_compact[(spotify_compact['energy'] > 0.57) & (spotify_compact['energy'] < 0.83)]

#cozy_evening = spotify_compact[(spotify_compact['energy'] < 0.71) & (spotify_compact['danceability'] < 0.66)]

#cheerful_and_fun = spotify_compact[(spotify_compact['energy'] > 0.71) & (spotify_compact['danceability'] > 0.55)]

#friday_night_fever = spotify_compact[(spotify_compact['energy'] > 0.71) & (spotify_compact['danceability'] > 0.66)]

#friendly_and_calm = spotify_compact[(spotify_compact['danceability'] < 0.75) & (spotify_compact['danceability'] > 0.55)]

####IMAGE LINKS SECTION ##########
sideheadimage = Image.open('c:/py/small.png')
maintitleimage = Image.open('c:/py/header.jpg')
###### END IMAGE LINKS SECTION ##############

##### MAIN PAGE SECTION#######################

st.title('Ambience© - The perfect sound for every situation.')

st.image(maintitleimage)

st.write("We know how hard it is to find the perfect music for the atmosphere you need. Let us help! Please just give us some clues of the music you need, and we'll set up a playlist for you!")

############END MAIN PAGE SECTION############33

year = st.sidebar.slider('Please choose a decade', min_value = 1960, max_value = 2020, value=1960, step=10)

#st.sidebar.subheader('Which mood you need?')

vibe = st.sidebar.selectbox('Choose a vibe!',('Chill', 'Energetic', 'Feel Good', 'Cozy Evening', 'Cheerfull and Fun', 'Friday Night Fever', 'Friendly and Calm'))

#st.sidebar.subheader("Where will it play?")

venue = st.sidebar.selectbox('Where to play it?',('Restaurant', 'Night Club', 'Street Bar', 'Tea House'))

#DANGEROUS ZONE - EDITING COP

#if st.sidebar.button('Play'):
#    st.subheader('Put these songs on:')
#    st.write(spotify_compact[spotify_compact.decade == year])

year_subset = spotify_compact
vibe_subset = spotify_compact
venue_subset = spotify_compact

if st.sidebar.button('Click & Scroll'):
    st.subheader('Put these songs on:')
    year_subset = spotify_compact[spotify_compact.decade == year]
    if vibe == 'Chill':
        vibe_subset = year_subset[(year_subset['energy'] < 0.71) & (year_subset['danceability'] > 0.55) & (year_subset['danceability'] < 0.75)]
    elif vibe == 'Energetic':
        vibe_subset = year_subset[(year_subset['energy'] > 0.71) & (year_subset['danceability'] > 0.66)]
    elif vibe == 'Feel Good':
        vibe_subset = year_subset[(year_subset['energy'] > 0.57) & (year_subset['energy'] < 0.83)]
    elif vibe == 'Cozy Evening':
        vibe_subset = year_subset[(year_subset['energy'] < 0.71) & (year_subset['danceability'] < 0.66)]
    elif vibe == 'Cheerfull and Fun':
        vibe_subset = year_subset[(year_subset['energy'] > 0.71) & (year_subset['danceability'] > 0.55)]
    elif vibe == 'Friday Night Fever':
        vibe_subset = year_subset[(year_subset['energy'] > 0.71) & (year_subset['danceability'] > 0.66)]
    elif vibe == 'Friendly and Calm':
        vibe_subset = year_subset[(year_subset['danceability'] < 0.75) & (year_subset['danceability'] > 0.55)]
    st.write(vibe_subset.head(10))

st.sidebar.image(sideheadimage, use_column_width = "always")

#END SIDEBAR SECTION#
