import requests
import streamlit as st


def sendsms(number,message):
    url= 'https://www.fast2sms.com/dev/bulkV2'

    querystring = {"authorization":"gM8NKjXoG4xYFakQTpHJWL3AndOebS60uZcDs9UIRqP71zChw2DGEdlje7ZyRX068s12ahFmiKNp4gqz",
                   #"sender_id":"FAKE",
                   "message":message,
                   "route":"v3",
                   "numbers":number}
    headers = {"cache-control":"no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    global dic
    dic = response.text
    return dic




def main():
    st.title("Send SMS")
    
if __name__=='__main__':
        main()
        
numbers = st.text_input("Enter Mobile No")

message = st.text_input('Enter your message here.')

if st.button("Send SMS"):    
    sendsms(numbers,message)
    st.write(dic)
