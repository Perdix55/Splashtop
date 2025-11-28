# Splashtop SOS - App Store Redirect

A Streamlit app that automatically detects the user's mobile device (iOS or Android) and redirects them to the appropriate app store.

## Features

- 🔍 Automatic device detection (iOS/Android)
- 🔄 Automatic redirection to the correct app store
- 📱 Fallback links for manual selection
- 🎨 Clean, minimal interface

## App Store Links

- **iOS**: [Splashtop SOS on App Store](https://apps.apple.com/app/splashtop-sos/id1230853703)
- **Android**: [Splashtop SOS on Google Play](https://play.google.com/store/apps/details?id=com.splashtop.sos&pcampaignid=web_share)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

Run the Streamlit app locally:
```bash
streamlit run splashtop.py
```

## How It Works

The app uses JavaScript to detect the user's device by checking the `navigator.userAgent` string:
- **iOS devices**: Detects iPhone, iPad, or iPod
- **Android devices**: Detects Android user agents

Once detected, the app automatically redirects the user to the appropriate app store link.

## Deployment

This app can be deployed on:
- Streamlit Community Cloud
- Heroku
- Any platform that supports Streamlit applications

## License

This project is open source and available for use.

