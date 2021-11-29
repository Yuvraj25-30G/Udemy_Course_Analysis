#Created By;- Yuvraj Saxena(E20CSE307)
#and Aditya Kochar(E20CSE309)

# Note: install all the libraries before running the program

import io
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import streamlit as st
import altair as alt



st.set_page_config(page_title = "Course Dashboard",
				   page_icon = ":bar_chart:"
)


st.title("Udemy Courses Database")
st.caption("By: Yuvraj Saxena and Aditya Kochar")
st.markdown("##")

#*******ASSIGNMENT FUNCTIONS*****
def label_is_paid(row):
	if row['is_paid'] == "False" :
		return 1
	elif row['is_paid'] == "True" :
		return 1

def assign_sub_code(row):
	if row["subject"] == "Business Finance":
		return 1
	elif row["subject"] == "Graphic Design":
		return 1
	elif row["subject"] == "Musical Instruments":
		return 1
	elif row["subject"] == "Web Development":
		return 1

def assign_level_code(row):
	if row["level"] == "All Levels":
		return 1
	elif row["level"] == "Intermediate Level":
		return 1
	elif row["level"] == "Beginner Level":
		return 1
	elif row["level"] == "Expert Level":
		return 1
	elif row["level"] == "52":
		return 1
#load dataframe
st.subheader("Database")
df = pd.read_csv("udemy.csv")
df.insert(18,column = "is_paid_bin", value = 1)
df.insert(19,column = "year_bin", value = 1)
# df.apply (lambda row: label_is_paid(row), axis=1)
# df['is_paid_bin'] = df.apply (lambda row: label_is_paid(row), axis=1)

df['sub_code'] = df.apply (lambda row: assign_sub_code(row), axis=1)

df['level_code'] = df.apply (lambda row: assign_level_code(row), axis=1)
st.dataframe(df)
print(df)

#*******load sidebar******
st.sidebar.header("Filter from here")

subject = st.sidebar.multiselect(
	"Select Subject",
	options = df["subject"].unique(),
)

is_paid = st.sidebar.multiselect(
	"Select Paid",
	options = df["is_paid"].unique(),
	default = df["is_paid"].unique(),
)

year = st.sidebar.multiselect(
	"Select year of release",
	options = df["year"].unique(),
	default = df["year"].unique(),
)

level = st.sidebar.multiselect(
	"Select level",
	options = df["level"].unique(),
	default = df["level"].unique(),
)

#********displaying filtered database*********
df_selection = df.query(
	"subject == @subject & is_paid == @is_paid & year == @year & level == @level"
)
st.markdown("##")
st.subheader("Filtered Database")
st.markdown("##")
st.dataframe(df_selection)
sump = df_selection['profit'].sum()
# print(sump)
sums = df_selection['num_subscribers'].sum()
strsump = str(sump)
strsums = str(sums)
st.markdown("##")
# st.subheader("Some values")
st.markdown("Total Profit made (based on filtering) = "+strsump)
# st.markdown(sump)
st.markdown("Total number of subscribers made (based on filtering) = "+strsums)
# st.markdown(sums)
#main page
st.title("Course Dashboard")
st.markdown("##")

st.set_option('deprecation.showPyplotGlobalUse', False)
#all variables

#***********level vs number of lectures********
st.subheader("1. Course Levels vs Lectures and length")
x = df["level"]
y = df["num_lectures"]
plt.xlabel("Levels",fontsize = 12)
plt.ylabel("Number of Lectures",fontsize = 12)
bary = plt.bar(x,y)
print(bary)
st.pyplot()
st.markdown("This bar graph clearly depicts that beginner level has the most number of lectures and content duration as it should be because basics take most amount of time to learn")
st.markdown("##")

#**********Level Distri*********
st.subheader("2. Level Distribution Among all subjects")
pie_chart = px.pie(
	data_frame = df,
	values = 'level_code',
	names = 'level',
	color = 'level',
	labels = {"level": "The level"},
)
st.plotly_chart(pie_chart)
st.markdown("Creators generally made courses that are suitable for all levels of consumers")
st.markdown("##")
st.subheader("3. Subject Distribution")
st.markdown("##")

#********SUBJECT DISTRIBUTION*****
st.caption("Pie Chart")
pie_chart = px.pie(
	data_frame = df,
	values = 'sub_code',
	names = 'subject',
	color = 'subject',
	labels = {"subject": "The subject"},
)

st.plotly_chart(pie_chart)
st.markdown("Web development and Business FInance subjects were the most produced, however highly differ in popularity")
st.markdown("##")
#******Paid vs free courses distri
st.subheader("4. Paid vs Free Courses")
st.markdown("##")
st.markdown("Distribution Criteria: is paid?")
pie_chart = px.pie(
	data_frame = df,
	values = 'is_paid_bin',
	names = 'is_paid',
	color = 'is_paid',
	labels = {"subject": "The subject"},
)
st.markdown("There is a vast difference in the production of free against paid courses")
st.markdown("##")
#******Subscribers vs subjects*******
st.plotly_chart(pie_chart)
st.markdown("##")
st.subheader("5. Number of Subscribers vs Subjects")
st.markdown("##")
x = df["subject"]
y = df["num_subscribers"]
plt.xlabel("Subjects",fontsize = 12)
plt.ylabel("Number of Subscribers",fontsize = 12)
barc = plt.bar(x,y)
print(barc)
st.pyplot()
st.markdown("Clearly Web Development takes the lead in popularity by a very large margin")
st.markdown("##")

#********production over the years********
st.subheader("6. Course Production by the years")
st.markdown("##")
pie_chart = px.pie(
	data_frame = df,
	values = 'year_bin',
	names = 'year',
	color = 'year',
	labels = {"subject": "The subject"},
)

st.plotly_chart(pie_chart)
st.markdown("Recent years have been a great time to launch your own online courses")
st.markdown("##")

#*********CONCLUSION**********
st.subheader("Conclusions")
st.markdown("There were 2 areas which could be analyzed")
st.markdown("	1. Consumer recommendation")
st.markdown("Based on the previous conclusions we can say that:")
st.markdown("i. A consumer is most likely to take a Web Development course followed by a musical instrument course")
st.markdown("ii. New consumers don't mind if the courses are paid or free")
st.markdown("iii. Consumners are willing to spend a good amount of time by lectures on thier courses")
st.markdown("CONCLUSION 1: All these inferences can help us make a personalised course recommendation system. ")
st.markdown("	2. Production Aspect")
st.markdown("i. A creator should make web development courses as they are the most popular")
st.markdown("ii. Based on recent year distribution current time is the best to produce an online udemy course")
st.markdown("CONCLUSION 2: All these inferences can help a content creator make informed choice on the course they want to launch")
#1 Consumner recommendation
#2 Production for profit and subscribers

#******end*****
