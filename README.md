# sms-bot

This sms-bot does an analysis of an inbound message to find keywords which trigger a response. The keywords are 'pizza' and 'ice cream'.  

## Requirements

- Python 3.6+
- Flask 
- Ngrok

## Installation

1. **Download:** Download the application code by clicking on Code -> Download ZIP. For ease, unzip the sms-bot folder and move it to your desktop. 

2. **Flask:** Next, you'll need a framework that will allow you to handle HTTP requests. That's where [Flask](https://pypi.org/project/Flask/) comes in. In you terminal, execute the following:

```
pip install flask
```

3. **ngrok:** In order to get HTTP requests to our application you'll need a tunneling service. Ngrok allows you to expose your local server (Flask) to the internet. In our case, it will allow you to receive webhooks from inbound messages and tunnel it to our application. Instructions on how to download ngrok can be found [here](https://ngrok.com/download). Once you've downloaded ngrok, move the unzipped ngrok file into the sms-bot folder on your desktop. 

4. **Packages/Modules:** The following packages and modules will be required to run this application. In your terminal, exexcute the install for each:
   
Telnyx Python SDK
```
pip install telnyx
```
python-dotenv
```
pip install python-dotenv
```
urllib
```
pip install urllib3
```

## Setup

1. **ngrok:** In you terminal, navigate to the project root and launch ngrok with the following command:

``` 
./ngrok http 5000
```

   Port 5000 is the port defined in our enviroment variable. More on that shortly. Once ngrok is launched you will see a version of the following:
   
```
ngrok by @inconshreveable

Session Status                online
Account                       Calvin Certuche (Plan: Free)
Version                       2.3.35
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://cd21a04bc202.ngrok.io -> http://localhost:5000
Forwarding                    https://cd21a04bc202.ngrok.io -> http://localhost:5000                                                                                                                        
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                                         0       0       0.00    0.00    0.00    0.00
```

2. **Environment Variables:** Open the .env file from the project root:

       ```
       TELNYX_API_KEY="your_api_key"
       TELNYX_PUBLIC_KEY="your_public_key"
       BASE_URL=your_url
       PORT=5000
       ```    
       
   Your API Key and Public Key can be found in your Telnyx account dashboard under "API Keys". Assign your API Key and Public Key between the quotes in the .env        file. Grab the https forwarding address from step #1 and assign it to BASE_URL. Your .env should now resemble the following:

     ```
      TELNYX_API_KEY="KEY017789BB9F8028D3228A09981951BC12_hq8IhlQmu2KjFjDZO8pQwL"
      TELNYX_PUBLIC_KEY="/MagzNkLjrXor4pRuZpby+gRb44zb80hUOqx5cQScDg="
      BASE_URL=https://62ee4f1a6788.ngrok.io
      PORT=5000
               ``` 

   Save the .env file. 

3. **Telnyx Messaging Profile:** The final step requires that you set the 'Webhook URL' in your Messaging Profile to the same https forwarding address from ngrok. Your Messaging Profile can be found in your Telnyx account dashboard under Messaging > My Telnyx Messaging Profile > Inbound Settings. Paste in the URL under "Send a webhook to this URL:", append the URL with `/webhooks`, and hit save. **Important: be sure to append it the URL with `/webhooks` to properly tunnel it to your application when an inbound message is received. The resulting URL should look like: https://cd21a04bc202.ngrok.io/webhooks**

## Run Application 

Open a new tab in your terminal (remember, ngrok is still running) and start the application by navigating to the project root and executing the following:

``` python app.py ```

You should see a version of the following:

   ``` * Serving Flask app "app" (lazy loading)
       * Environment: production
         WARNING: This is a development server. Do not use it in a production deployment.
         Use a production WSGI server instead.
       * Debug mode: off
       * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)```

You're now ready to text your bot (Telnyx number). Give it a shot. Remember, the bot only likes pizza and ice cream. 
