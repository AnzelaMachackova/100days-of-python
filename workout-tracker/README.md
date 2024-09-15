# Exercise Data Logger Script

## Purpose
This Python script interacts with an exercise API to fetch user-inputted exercise data and logs it into Google Sheets with date and time stamps.

## Features
- **Fetch Exercise Data**: Prompts the user to enter exercise activities and fetches related data like duration and calories burned.
- **Log Data in Google Sheets**: Authenticates with Google Sheets using a service account and appends fetched data to a sheet.

## Usage
Before running the script, ensure all dependencies are installed and the service account JSON key file is properly configured. 

### Setup
1. Install necessary Python libraries:
   ```bash
   pip install requests gspread google-auth
   ```
2. Make sure you have `appinfo.py` configured with the appropriate constants (APP_ID, API_KEY, etc.).
3. The `JSON_KEYFILE` should be set up with your Google service account credentials.

### Running the Script
Execute the script from your command line:
```bash
python main.py
```
This will prompt you to enter the exercises you did, fetch the relevant data, and update the designated Google Sheet.

## Prerequisites
- **Python**: Install Python on your system.
- **Google Cloud Setup**: Ensure that the Google Sheets API is enabled and the service account has edit permissions on the target Google Sheet.
- **Environment Setup**: Store sensitive keys and identifiers in `appinfo.py`.

## File Structure
- **main.py**: Main script file.
- **appinfo.py**: Contains constants like API keys and identifiers.

## Support
For troubleshooting, refer to the documentation of the libraries and APIs used:
- [Requests](https://docs.python-requests.org/en/latest/)
- [gspread](https://docs.gspread.org/en/latest/)
- [Google Cloud Documentation](https://cloud.google.com/docs)
