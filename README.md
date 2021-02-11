# sms-bot

This sms-bot does an analysis of an inbound message to find keywords which trigger a response. The keywords in this version are 'pizza' and 'ice cream'.  

## Requirements

- Python 3.6+
- Flask 
- Ngrok


## Installation

1. **Download:** Download the application code by clicking on Code -> Download ZIP. For ease, unzip the sms-bot folder and move it to your desktop. 

2. **Flask:** Next, you'll need a framework that will allow you to handle HTTP requests. That's where [Flask](https://pypi.org/project/Flask/) comes in. In you terminal, execute the following:

   ```pip install flask```

3. **ngrok:** In order to get HTTP requests to our application you'll need a tunneling service. Ngrok allows you to expose your local server (Flask) to the internet. In our case, it will allow you to receive webhooks from inbound messages and tunnel it to our application. Instructions on how to download ngrok can be found [here](https://ngrok.com/download). Once you've downloaded ngrok, move the unzipped ngrok file into the sms-bot folder on your desktop. 

4. **Packages/Modules:** The following packages and modules will be required to run this application. In your terminal, exexcute the install for each:
   
   - Telnyx Python SDK
   ``` pip install telnyx ```
   - python-dotenv
   ``` pip install python-dotenv ```
   - urllib
   ``` pip install urllib3 ```

## Setup

1. **ngrok:** In you terminal, navigate to the project root and launch ngrok with the following command:

   ``` ./ngrok http 5000 ```

   Port 5000 is the port defined in our enviroment variable. More on that shortly. Once ngrok is launched you will see a version of the following:
   
      ```ngrok by @inconshreveable

      Session Status                online
      Account                       Calvin Certuche (Plan: Free)
      Version                       2.3.35
      Region                        United States (us)
      Web Interface                 http://127.0.0.1:4040
      Forwarding                    http://cd21a04bc202.ngrok.io -> http://localhost:5000
      Forwarding                    https://cd21a04bc202.ngrok.io -> http://localhost:5000                                                                                                                        
      Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                                                   
                                    0       0       0.00    0.00    0.00    0.00```  
                                       
2. **Environment Variables:** The and fill in the TELNYX_API_KEY, TELNYX_PUBLIC_KEY, and BASE_URL with your own.

Your TELNYX_API_KEY and TELNYX_PUBLIC_KEY can be found in your Telnyx account dashboard under "Apie Keys".

The BASE_URL can be found from your started ngrok

save .env file 

3. **Telnyx Messaging Profile:** Set Webhook URL in your messaging profile to the https forwarding address from ngrok. append it with /webhooks to properly tunnel it to your application when and inbound message is received. 

## Run Application 

You already have your ngrok running. navigate to your project root. run 

``` python app.py ```

you should see the following :




that's it. send an inbound message.
