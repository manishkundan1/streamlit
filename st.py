import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
#to run this file  "python -m streamlit run st.py"

df=yf.download('SBIN.NS')

# 1. st.title(): Adds a title to your web app.
st.title("My Streamlit App")

# 2. st.sidebar(): Creates a sidebar for additional controls or information.
with st.sidebar:
    st.title("Sidebar Title")
    # Add other elements to the sidebar

# 3. st.text() and st.markdown(): Display text or Markdown content.

st.text("This is a simple text.")
st.markdown("## This is a Markdown title")

# 4.st.header(), st.subheader(), and st.write(): Display headers, subheaders, and general text.

st.header("Header")
st.subheader("Subheader")
st.write("This is a general text.")

# 5. st.image(): Display an image.
from PIL import Image
image = Image.open("image.jpg")
st.image(image, caption="Example Image", use_column_width=True)

# 6.  st.dataframe() and st.table(): Display dataframes or tables.
import pandas as pd
df = pd.DataFrame({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
st.dataframe(df)
# or
st.table(df)

# 7. st.plotly_chart() and st.altair_chart(): Display interactive charts.
#import plotly.express as px
#fig = px.scatter(df, x="Column 1", y="Column 2")
#st.plotly_chart(fig)

# 8 st.pyplot(): Display a Matplotlib plot.

import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
st.pyplot()

#9.st.selectbox(), st.multiselect(), st.radio(), and st.slider(): Create interactive widgets for user input.
selected_option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])

selected_option = st.multiselect("Choose an option", ["Option 1", "Option 2", "Option 3"])

# st.button(): Create a clickable button.
if st.button("Click me"):
    st.write("Button clicked!")

#  st.checkbox() and st.radio(): Create a checkbox or a radio button.


if st.checkbox("Show data"):
    st.dataframe(df)

selected_radio = st.radio("Select an option", ["Option A", "Option B"])

# st.text_input() and st.number_input(): Get user input as text or numeric values.

user_input = st.text_input("Enter your name", "John Doe")
user_age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)

#st.text_area(): Get multiline text input.

user_comment = st.text_area("Enter your comments", "Type here...")

# st.file_uploader(): Upload files.

uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])

# st.date_input() and st.time_input(): Get date and time input.

selected_date = st.date_input("Select a date")
selected_time = st.time_input("Select a time")

# st.empty(): Create a placeholder to dynamically update content.


placeholder = st.empty()
# Update placeholder content dynamically
placeholder.text("New content")

# st.warning(), st.error(), and st.success(): Display warning, error, or success messages.

st.warning("This is a warning message.")
st.error("An error occurred.")
st.success("Task completed successfully!")

#  st.latex(): Render LaTeX equations.

st.latex(r'\int_{a}^{b} x^2 dx')

# st.color_picker(): Select a color.

selected_color = st.color_picker("Choose a color", "#00f")

# st.video(): Display a video.

st.video("path/to/video.mp4")
st.audio("path/to/audio.mp3")

# st.write() with unsafe_allow_html=True: Allow rendering HTML content.
st.write("<h1 style='color: blue;'>This is HTML content</h1>", unsafe_allow_html=True)

st.balloons()




