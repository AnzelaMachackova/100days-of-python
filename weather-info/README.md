# Weather Report Emailer Script

## Purpose
This script fetches the current day's weather information, specifically average temperature and sunshine duration, and emails this summary to a specified recipient.

## Features
- **Fetch Weather Data**: Retrieves weather data from an API for a specific location.
- **Generate Email Message**: Formats the fetched weather data into a readable message.
- **Send Email**: Sends the formatted message via email to a predefined recipient.

## Usage
Ensure Python, `requests`, and `smtplib` libraries are installed on your system. Configure the `data.json` file with your email credentials and recipient's email address before running the script.

### Setup
1. Install required libraries if not already installed:
   ```bash
   pip install requests
   ```
2. Create a `data.json` file in the same directory as the script with the following structure:
   ```json
   {
     "my_email": "your_email@example.com",
     "password": "your_password",
     "recipient_mail": "recipient@example.com"
   }
   ```

### Running the Script
Execute the script from the command line:
```bash
python main.py
```

## Prerequisites
- **Python**: Python must be installed on your system.
- **Libraries**: `requests` for HTTP requests and `smtplib` for email functionality.
- **Configuration**: User credentials and recipient's email must be correctly set up in `data.json`.

## File Structure
- **main.py**: Main script handling the fetching of weather data, email message generation, and sending the email.
- **data.json**: Contains sensitive information such as the user's email and password.

## Notes
Ensure all sensitive information in `data.json` is securely managed. Use environment variables or secure vaults in production environments.

## Support
For additional information on the API used for weather data, refer to [Open-Meteo API documentation](https://api.open-meteo.com/).
