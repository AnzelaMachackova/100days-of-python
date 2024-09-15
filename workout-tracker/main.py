from appinfo import APP_ID, API_KEY, WEIGHT_KG, HEIGHT_CM, AGE, JSON_KEYFILE, SPREADSHEET_ID, EXERCISE_ENDPOINT
import requests
from google.oauth2 import service_account
import gspread
import datetime

def get_exercise_data():
    exercise_text = input("Tell me which exercises you did: ")
    parameters = {
        "query": exercise_text,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
    result = response.json()
    exercises_data = []

    # Extract data from the response
    for exercise in result['exercises']:
        name = exercise['name']
        duration_min = exercise['duration_min']
        nf_calories = exercise['nf_calories']
        
        # Get the current date and time
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        exercises_data.append([date_str, time_str, name, duration_min, nf_calories])

    return exercises_data


def authenticate_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    try:
        credentials = service_account.Credentials.from_service_account_file(JSON_KEYFILE, scopes=scope)
        print("Authenticated with Google Sheets successfully.")
        client = gspread.authorize(credentials)
        return client
    except Exception as e:
        print(f"Error authenticating with Google Sheets: {e}")

def update_google_sheet(data):
    try:
        client = authenticate_google_sheets()
        sheet = client.open_by_key(SPREADSHEET_ID).sheet1  
        
        # Append data to the next available empty row
        for row in data:
            sheet.append_row(row)
        print("Data written to Google Sheet successfully.")

    except Exception as e:
        print(f"Error updating Google Sheet: {e}")

if __name__ == '__main__':
    data_to_write = get_exercise_data()
    update_google_sheet(data_to_write)