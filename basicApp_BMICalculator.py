# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt


# data = {'City': ['New York', 'Chicago', 'San Francisco', 'Boston', 'Seattle'],
#         'Population': [8623000, 2700000, 883305, 692600, 769714]}

# # Create a pandas DataFrame from the data
# df = pd.DataFrame(data)

# # Set the index to the 'City' column
# df.set_index('City', inplace=True)

# # Create a bar chart using the DataFrame and matplotlib
# fig, ax = plt.subplots()
# df.plot(kind='bar', ax=ax)

# # Set the y-axis to integers of interval 200
# ax.set_yticks(range(0, max(df['Population'])+1, 200))

# # Set the x-axis and y-axis labels
# plt.xlabel('City')
# plt.ylabel('Population')

# # Render the chart using Streamlit
# st.pyplot(fig)


# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
				('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
	# take height input in centimeters
	height = st.number_input('Centimeters')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Enter some value of height")

elif(status == 'meters'):
	# take height input in meters
	height = st.number_input('Meters')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Enter some value of height")

else:
	# take height input in feet
	height = st.number_input('Feet')

	# 1 meter = 3.28
	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

	# print the BMI INDEX
	st.text("Your BMI Index is {}.".format(bmi))

	# give the interpretation of BMI index
	if(bmi < 16):
		st.error("You are Extremely Underweight")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("You are Underweight")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Healthy")
	elif(bmi >= 25 and bmi < 30):
		st.warning("Overweight")
	elif(bmi >= 30):
		st.error("Extremely Overweight")
