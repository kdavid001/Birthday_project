# 🎉 Departmental Birthday Email Automation

This project automates the process of sending personalized birthday emails to students or staff members in a university department. It uses a cleaned dataset, custom email templates, and cloud-based scheduling through GitHub Actions and Google Cloud services.

## 📌 Features

- Automated daily birthday checks
- Personalized email messages
- Dataset preprocessing and cleanup
- Cloud-based deployment via GitHub Actions
- Secure email authentication using Google Cloud credentials

## 🧑‍💻 Technologies Used

- **Python** – Core programming logic
- **Pandas** – Data handling and filtering
- **SMTP (smtplib)** – Email sending
- **GitHub Actions** – Workflow automation
- **Google Cloud Platform** – Secure credential handling

## 📂 Project Structure
```
├── data/
│   └── birthdays.csv
├── email_templates/
│   └── birthday_template.html
├── .github/
│   └── workflows/
│       └── birthday_email.yml
├── main.py
├── credentials.json
├── README.md
```
## ⚙️ How It Works

1. The script reads a CSV file containing names, birthdays, and email addresses.
2. It checks daily for any birthdays that match the current date.
3. A personalized email is generated and sent to the recipient.
4. GitHub Actions runs the script daily using a cron job.
5. Google Cloud is used to securely manage credentials (for Gmail or any mail provider).

## 🚀 Setup Instructions

### 1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/department-birthday-email.git
   cd department-birthday-email
   ```

### 2.	Install Dependencies
```
pip install pandas
pip install requirements.txt
```
### 📂 3. Add Your Dataset

- Place your cleaned CSV file in the `data/` folder.  
- Ensure it includes columns like: `Name`, `Email`, `Birthday` (in `YYYY-MM-DD` format).

### 🔐 4. Set Up Google Cloud Credentials

- Follow the instructions [here](https://developers.google.com/workspace/guides/create-credentials) to generate OAuth 2.0 credentials.  
- Save the file as `credentials.json` in your project root directory.

### ⚙️ 5. Configure GitHub Workflow

- Modify the `.yaml` file in `.github/workflows/` to set your preferred schedule and define secrets (e.g., email credentials, OAuth tokens).

### 🚀 6. Push to GitHub

- Push your code to a **private** or **public** GitHub repository to trigger the workflow automation.


🔐 Security Notes

	•	Never upload your credentials.json file to a public repository.
	•	Use GitHub secrets to store sensitive data for cloud deployment.

💡 Acknowledgements

This project builds upon a birthday email script developed earlier, now expanded for departmental use with cloud-based automation.

📫 Contact

Feel free to reach out to me via korededavid03@gmail.com | Github --> kdavid001 if you have any questions or suggestions.
