import streamlit as st
import json
import requests



st.title("Productionizing the Pipeline")

menu = ["Home", "Login", "API2","API3 & API4","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
     st.subheader("Home")

elif choice == "Login":
    st.subheader("Login Section ")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox("Login"):
        if password=='12345':
            st.success("Logged in as {}".format(username))

            # Connecting with API Gateway to invoke lambda functions
            # #API 1
            st.subheader("API1 - Scraping Data")
            scrape_data = st.text_input("Enter the url to scrape data")
            get_url = scrape_data

            if scrape_data:
                gateway_url1 = 'https://7bbv59k23f.execute-api.us-east-1.amazonaws.com/Test1/webscrape'
                #convert into json format
                json_payload1 = json.dumps({ "url": get_url})
                response1 = requests.post(gateway_url1, data=json_payload1)

                data1 = response1.json()
                display_data1 = st.json(data1)

        else:
            st.warning("Incorrect Username/Passwrod")
#API2
elif choice == "API2":
    st.subheader("API2 - Named Entity Recognition ")
    gateway_url2 = 'https://sjys10yiqj.execute-api.us-east-1.amazonaws.com/dev/entitiesdetection'
    # convert into json format
    json_payload2 = json.dumps({'key': 'ScrapedFolder/webscrape.txt', 'decision': 'Hello'})
    response2 = requests.post(gateway_url2, data=json_payload2)

    data2 = response2.json()
    display_data2 = st.json(data2)

#API 3 & API4
elif choice == "API3 & API4":
    st.subheader("API3 & API4 - Anonymization & De-Anonymization Entities")

    radio_list = st.radio(
        "How do u wanna view your data?",
        ('Masked View', 'De-identify View'))

    if radio_list == 'Masked View':
        st.write('Your data is masked')


        gateway_url3 = 'https://sjys10yiqj.execute-api.us-east-1.amazonaws.com/dev/dataanonymization'

        json_payload3 = json.dumps({ 'filelocation': 'ScrapedFolder/webscrape.txt', 'decision':'anonymize'})

        response3 = requests.post(gateway_url3, data=json_payload3)

        data3 = response3.json()
        display_data3 = st.text_area(data3)


    else:
        st.write('Your data is not masked')

        gateway_url4 = 'https://sjys10yiqj.execute-api.us-east-1.amazonaws.com/dev/dataanonymization'

        json_payload4 = json.dumps({ 'filelocation': 'ScrapedFolder/webscrape.txt', 'decision': 'deidentify'})

        response4 = requests.post(gateway_url4, data=json_payload4)

        data4 = response4.json()
        display_data4 = st.text_area(data4)


elif choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("SignUp"):
        st.success("You have successfully created a valid account")
        st.info("Go to Login Menu to Login")

