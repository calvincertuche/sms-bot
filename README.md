# sms-bot

This sms-bot does an analysis of an inbound message to find keywords which trigger a response. The keywords in this version are 'pizza' and 'ice cream'.  

## Requirements

- Flask 
- Ngrok
- Python 3.6+
- Telnyx Python SDK

## Installation

1. **Download:** Download the application code by clicking on Code -> Download ZIP. For ease, unzip the sms-bot folder and move it to your desktop. 

2. **Flask:** Next, you'll need a framework that will allow you to handle HTTP requests. That's where [Flask](https://pypi.org/project/Flask/) comes in. In you terminal, execute the following:

   ```pip install flask```

3. **ngrok:** In order to get HTTP requests to our application you'll need a tunneling service. I recommend ngrok. Ngrok allows you to expose your local server (Flask) to the internet. In our case, it will allow you to receive webhooks from inbound messages and tunnel it to our application. Instructions on how to download ngrok can be found [here](https://ngrok.com/download). Once you've downloaded ngrok, move the unzipped ngrok file into the sms-bot folder on your desktop. 

4. **Packages//Modules:** The following modules will be required to run this application. The installation commands are listed below. Run those in your temrinal:
   
   - Telnyx Python 

## Usage

- `incognito` - Open an incognito window with [Google](https://www.google.com/).

## Credits

Thank those who helped make this possible.
