import streamlit as sl
import pandas as pd
import matplotlib.pyplot as plt

from io import BytesIO
import base64


def roundIt(val):
    return round(val, 2)

def pieChart_Genres():
    
    movies = pd.read_csv("MovieMasterData.csv")
    # print(movies.head(2))

    comedy = 0 
    action = 0
    crime = 0
    romance = 0
    thriller = 0
    animation = 0
    drama = 0

    for i in movies["Genre"]:        
        if "Comedy" in i:
            comedy+=1
        if "Drama" in i:
            drama+=1
        if "Romance" in i:
            romance+=1
        if "Animation" in i:
            animation+=1
        if "Thriller" in i:
            thriller+=1
        if "Action" in i:
            action+=1
        if "Crime" in i:
            crime+=1

    total = action + animation + comedy + crime + romance + drama + thriller
    percentageConst = 100/total

    data = [action, animation, comedy , crime , romance , drama , thriller]
    labels = ['Comedy', 'Action', 'Animation', 'Thriller', 'Drama', 'Romance', 'Crime']
    colors = ['#BBD500', '#2C2255', '#75B7FD','#555555', '#FF8A00', '#737373', '#FF8A00', '#FFE600']

    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, colors= colors)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image = base64.b64encode(buffer.getvalue()).decode()
    sl.image(f"data:image/png;base64,{image}")



sl.header("Analytics")
sl.subheader("Here you get what your business does!")
sl.write("This is DataScience Demo App")
sl.markdown("Partner For Growing Business")

sl.write("-----------------------------------------------------------------------")

sl.write(pieChart_Genres())