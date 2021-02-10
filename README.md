# sms-bot

This sms-bot does an analysis of an inbound message to find keywords which trigger a response. The keywords in this version are 'pizza' and 'ice cream'.  

## Requirements

- Flask 
- Ngrok
- Python 3.6+
- Telnyx Python SDK

## Installation

1. First, download the code by clicking on Code -> Download ZIP. Unzip the sms-bot folder and move it to your desktop. 

2. Next, you'll need to install [Flask](https://pypi.org/project/Flask/). Flask is a framework that will allow to handle HTTP requests. Think of it as a local server.

   ```pip install flask```

3. You'll need a tunneling tool next. I recommend ngrok. ngrok allows you to expose your local server (Flask) to the internet. In our case, it will allow you to receive webhooks from inbound messages to the app. Instructions on how to download ngrok can be found [here](https://ngrok.com/download). Once you followed the instructions to download ngrok, move the unzipped ngrok file into the sms-bot folder on your dekstop. 

3. Start up the server with your code by navigating to the sms-bot folder on your desktop then execute the following command:

   ``` python app.py ```
   
   You should see a version of the following:
   
   ```* Serving Flask app "app" (lazy loading)
      * Environment: production
        WARNING: This is a development server. Do not use it in a production deployment.
        Use a production WSGI server instead.
      * Debug mode: off
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) ```

4. Activate your ngrok tunnel. While in your sms-bot, execute the following command:
   
   ```./ngrok http 5000```
   
5. 

## Usage

- `incognito` - Open an incognito window with [Google](https://www.google.com/).

## Credits

Thank those who helped make this possible.
