import streamlit as st
import pandas as pd
import numpy as np

import csv
from enum import Enum
import time

from rich import print
from rich.pretty import pprint
from rich.progress import track, Progress

import Joist_and_Plank as jp
import pandas as pd
from O86 import O86_20 as O86
from Section import Section

#dummy = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur auctor varius sodales. Donec et pellentesque tellus. Ut eu pharetra nisi. Aliquam a turpis tempus, posuere mauris et, vulputate purus. Sed in dui dolor. Suspendisse potenti. Quisque euismod ultrices pulvinar. In elementum felis vitae elit vulputate finibus. Vivamus velit lectus, sagittis at urna ac, semper auctor lacus. Nullam bibendum velit eu orci rhoncus feugiat. Nam malesuada ultrices eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam vitae malesuada dolor. Duis non metus vitae eros aliquam semper placerat sed nisl. In vestibulum eget lectus et lacinia. Praesent libero nulla, pulvinar sit amet tortor a, eleifend elementum ex.\nSed iaculis vulputate nisl, nec convallis mi. Aliquam porttitor viverra mauris, nec congue neque venenatis sit amet. Quisque in massa a tortor consequat pharetra ac sit amet arcu. Morbi venenatis ante lorem, vel posuere arcu tempus in. Praesent congue molestie felis, ut ornare magna fringilla nec. Sed condimentum nisi et leo interdum cursus. Mauris pretium tellus ac ex imperdiet, vel sodales tortor tincidunt. Nullam et sem vel lectus congue tincidunt in sit amet leo. Phasellus egestas dolor nec iaculis tempor. Nullam aliquet, lectus a pharetra semper, lacus mauris iaculis magna, id aliquet massa purus eget nibh. Morbi molestie tellus non diam fringilla, at laoreet nunc hendrerit. Phasellus luctus tincidunt metus.\n\nPraesent efficitur ullamcorper hendrerit. In sit amet ullamcorper purus. Suspendisse augue nisl, laoreet in finibus eu, sollicitudin at ligula. Sed quis libero placerat mauris ultricies suscipit. Etiam ullamcorper laoreet risus a scelerisque. Etiam porta sem vel malesuada malesuada. Nullam nec ligula nulla. Nullam rutrum tellus eget lorem gravida tincidunt. Suspendisse sit amet ipsum non purus dignissim pulvinar ut sit amet risus. Fusce tristique luctus quam. Sed eget pellentesque magna. Sed vel magna rhoncus, posuere sapien id, dapibus mauris. Proin elit augue, suscipit auctor mi vel, aliquet fringilla nunc. Nulla facilisi.\n\nNunc eget tincidunt massa. In vel felis et mi consequat facilisis quis vel augue. Praesent varius urna sit amet luctus ultricies. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse vitae urna ante. Suspendisse ac eros sit amet elit lacinia sodales in ac dui. Morbi ipsum est, sodales sit amet orci ac, cursus fermentum ipsum. Donec vestibulum, purus at semper ultricies, diam massa tincidunt augue, quis feugiat lacus sapien et nunc. Nam pellentesque dignissim leo, nec gravida orci tempus in. Morbi tempus dolor enim, vitae fermentum metus suscipit sit amet. Fusce eu massa sagittis, efficitur ex imperdiet, cursus diam. Duis bibendum id risus ut vulputate. Suspendisse in ultrices nibh, in imperdiet ipsum. Nunc sed arcu vel massa finibus fringilla. Vestibulum id sodales nunc.\n\nVestibulum auctor, nunc a auctor ultrices, felis neque tincidunt ipsum, vel tincidunt velit velit id urna. Phasellus lobortis enim nec erat blandit, nec vehicula quam commodo. Nam ut risus mauris. Nunc felis lorem, iaculis fringilla arcu id, tristique varius mauris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae egestas felis, vel aliquet tortor. Nam dignissim metus tortor, et egestas magna sagittis vel. Praesent rhoncus, sapien vitae posuere tincidunt, ligula urna varius arcu, in facilisis lectus leo id ipsum. Donec porttitor pellentesque eros in elementum. Proin tincidunt nec justo eu tempus. Etiam volutpat accumsan dolor, non lobortis lacus placerat in."

csv_filename = 'Joist_and_Plank.csv'
jp_dict = {}
species_list = []   

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

col1, col2 = st.columns(2)

def Get_Materials(csv_filename: str, species: str) -> pd.DataFrame:
    if species == "SPF No2":
        type = 'Spruce-Pine-Fir'
        grade = 'No1/No2'
    else:
        type = 'Douglas Fir-Larch'
        grade = 'No1/No2'
    with open(csv_filename, mode ='r')as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            temp = {}
            for key, value in lines.items():
                try:
                    x = float(value)
                except:
                    x = value
                temp[key] = x
            new_jp = jp.Joist_and_Plank(**temp)
            species_list.append(new_jp.name) 
            jp_dict[new_jp.name] = new_jp
            df = pd.read_csv(csv_filename)# , index_col="Species")
            new_df = df.loc[df['Species'] == type]
            return new_df
        
with st.sidebar:
    with st.expander('Project Information'):
        project_numer = st.text_input("Project Number")
        project_name = st.text_input("Project Name")
        project_adress = st.text_input("Address")
        enigneer = st.text_input("Engineer")

    with st.expander('Loads'):
        st.header("Roof Loads", divider=True)
        dl_roof = st.text_input("Roof Dead Load", 0.75)
        ll_roof = st.text_input("Roof Live Load", 0.0)
        sl_roof = st.text_input("Roof Snow Load", 2.0)
        st.header("Floor Loads", divider=True)
        dl_floor = st.text_input("Floor Dead Load", 3.6)
        ll_floor = st.text_input("Floor Live Load", 1.9)
        st.header("Wall Loads", divider=True)
        sw_wall = st.text_input("Wall Self Weight", 0.56)

    with st.expander('Wall Info'):
        n_floors = st.text_input("Number of Floors", 6)
        roof_trib = st.text_input("Roof Trib Width", 610)
        floor_trib = st.text_input("Floor Trib Width", 6)
        floor_list = []

    with st.expander('Materials'):
        material = st.radio(
            "Select Wood Species and Grade",
            ['SPF No2', 'D. Fir No2'], 
            captions=['Spruce-Pine-Fir No2','Douglas Fir-Larch No2']
        )
        if material == 'SPF No2':
            df = Get_Materials(csv_filename, 'SPF No2')
        else:
            df = Get_Materials(csv_filename, 'D. Fir No2') 
        
with col1:
    st.header("Wood Properties")
    st.dataframe(df)
    st.header("Floor Loads")
    for i in range(int(n_floors)):
        if i ==0:
            name = 'Roof'
        else:
            name = f"Level-{int(n_floors)-i+1}"
        floor_list.append({'name': name, 'h': 3.0, 'DL': 0.0, 'LL': 0.0, 'SL': 0.0})
    loads_df = pd.DataFrame(floor_list)
    edited_df = loads_df
    st.data_editor(edited_df)
    st.header("Origonal DF")
    st.dataframe(loads_df)

with col2:
    floor = st.selectbox("Select Floor", edited_df['name'])
    new_df = edited_df.loc[edited_df['name'] == floor]
    st.dataframe(new_df)