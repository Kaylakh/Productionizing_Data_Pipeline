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

        # Get Execution name to hit the masked api
        get_execution_name = st.text_input("Get execution name")
        if get_execution_name:
            gateway_arn_url1 = 'https://f22iih35uf.execute-api.us-east-1.amazonaws.com/prod'
            # convert into json format
            json_payload_arn1 = json.dumps(
                {"input": "{\"key\": \"ScrapedFolder/webscrape.txt\", \"decision\": \"anonymize\"}",
                 "name": get_execution_name,
                 "stateMachineArn": "arn:aws:states:us-east-1:284378271947:stateMachine:DataPipeline"})

            response_arn1 = requests.post(gateway_arn_url1, data=json_payload_arn1)

            data_arn1 = response_arn1.json()
            display_arn1 = st.text(data_arn1)

            # Text box to get the new arn to run annomyzie part
            get_arn = st.text_input("Get annomyize arn")
            arn1 = get_arn

            if get_arn:
                gateway_url3 = 'https://9jloofnms1.execute-api.us-east-1.amazonaws.com/dev/describeexecution'

                json_payload3 = json.dumps({
                    "executionArn": arn1,
                    "stateMachineArn": "arn:aws:states:us-east-1:284378271947:stateMachine:DataPipeline"})

                response3 = requests.post(gateway_url3, data=json_payload3)

                data3 = response3.json()
                display_data3 = st.json(data3)


    else:
        st.write('Your data is not masked')
        # Get Execution name to hit the masked api
        get_execution_name2 = st.text_input("Get execution name")
        if get_execution_name2:
            gateway_arn_url2 = 'https://f22iih35uf.execute-api.us-east-1.amazonaws.com/prod'
            # convert into json format
            json_payload_arn2 = json.dumps(
                {"input": "{\"key\": \"ScrapedFolder/webscrape.txt\", \"decision\": \"deidentify\"}",
                 "name": get_execution_name2,
                 "stateMachineArn": "arn:aws:states:us-east-1:284378271947:stateMachine:DataPipeline"})

            response_arn2 = requests.post(gateway_arn_url2, data=json_payload_arn2)

            data_arn2 = response_arn2.json()
            display_arn2 = st.text(data_arn2)

            # Text box to get the new arn to run annomyzie part
            get_arn2 = st.text_input("Get annomyize arn")
            arn2 = get_arn2

            if get_arn2:
                gateway_url4 = 'https://9jloofnms1.execute-api.us-east-1.amazonaws.com/dev/describeexecution'

                json_payload4 = json.dumps({
                    "executionArn": arn2,
                    "stateMachineArn": "arn:aws:states:us-east-1:284378271947:stateMachine:DataPipeline"})

                response4 = requests.post(gateway_url4, data=json_payload4)

                data4 = response4.json()
                display_data4 = st.json(data4)



elif choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("SignUp"):
        st.success("You have successfully created a valid account")
        st.info("Go to Login Menu to Login")

