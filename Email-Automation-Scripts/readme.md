
```markdown
# Email Automation Script

This Python script automates the process of sending emails using SMTP (Simple Mail Transfer Protocol). You can use this script to send emails programmatically from your Python application.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone [<repository-url>](https://github.com/sandeepmvd18/Python-Automation-Scripts.git)
cd Email-Automation-Scripts
```

### 2. Configure Email Settings

#### For Gmail:
- SMTP Server: smtp.gmail.com
- Port: 587
- Enable Less Secure Apps Access: [Learn More](https://support.google.com/accounts/answer/6010255)

#### For Office 365:
- SMTP Server: smtp.office365.com
- Port: 587
- Enable SMTP Authentication: [Learn More](https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission)

### 3. Update Script
Open `email_automation.py` and replace the following placeholders with your email credentials:

```python
sender_email = 'your_email@gmail.com'  # Replace with your email address
sender_password ='your_password'  # Replace with your email password or app password
```

### 4. Run the Script
Execute the script by running the following command in your terminal:

```bash
python3 email_automation.py
```

## Usage
Once the script is executed, it will send an email to the specified recipient with the subject and message provided in the script.

## Support
For any issues or questions, please open an issue in the [issue tracker](https://github.com/sandeepmvd18/Python-Automation-Scripts.git/issues).


