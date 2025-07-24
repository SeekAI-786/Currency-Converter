# 💱 Currency Converter GUI App

A simple desktop application built using Python and Tkinter that lets you convert between major world currencies in real time using [RapidAPI's Currency Converter API](https://rapidapi.com/).

---

## 🖥️ Features

- ✅ Real-time currency conversion
- ✅ Supports 13 major currencies
- ✅ Clean and interactive Tkinter GUI
- ✅ Displays currency symbols (₹, $, €, ₨, etc.)
- ✅ Utilizes **RapidAPI** for live exchange rate data

---

## 🛠 Technologies Used

- **Python 3.7+**
- **Tkinter** (standard GUI library)
- **Pillow** (for image handling)
- **Requests** (to fetch API data)
- **RapidAPI** (for exchange rates)

---

## ⚙️ Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter
Install required dependencies:

bash
Copy
Edit
pip install pillow requests
🧩 tkinter comes pre-installed with most Python distributions. If it doesn’t work, reinstall Python and ensure you check the “tcl/tk” option during installation.

Run the app:

bash
Copy
Edit
python currency_converter.py
🔑 API Key Setup
This project uses the Currency Converter API from RapidAPI.

Go to RapidAPI and sign in / sign up.

Search for Currency Converter API and subscribe to a free plan.

Copy your X-RapidAPI-Key.

Open the script and replace the following section with your actual key:

python
Copy
Edit
headers = {
    "X-RapidAPI-Key": "your-api-key-here",
    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}
🌐 Supported Currencies
The app supports conversion between the following currencies:

Code	Currency Name	Symbol
USD	US Dollar	$
PKR	Pakistani Rupee	₨
EUR	Euro	€
INR	Indian Rupee	₹
TRY	Turkish Lira	₺
CAD	Canadian Dollar	CAD
GBP	British Pound	£
CNY	Chinese Yuan	¥
SAR	Saudi Riyal	SR
AUD	Australian Dollar	AUD
HKD	Hong Kong Dollar	HK $
AED	UAE Dirham	د.إ
IQD	Iraqi Dinar	ع.د
IRR	Iranian Rial	﷼

📸 UI Preview
(Add a screenshot or GIF of your GUI here)
Example:

📬 Contributing
Have an idea to improve the app or want to add more currencies?
Feel free to fork the repo, submit a pull request, or open an issue!
