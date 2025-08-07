# 💱 Currency Converter

A modern, responsive currency converter application built with Python and Flask. Convert between 20+ currencies using real-time exchange rates from the ExchangeRate-API.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Heroku](https://img.shields.io/badge/Deployed%20on-Heroku-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌐 Live Demo

**[Try the Currency Converter Live!](https://your-currency-converter-app-bdf3aa5944f5.herokuapp.com/)**

## ✨ Features

- **Real-time Exchange Rates**: Get up-to-date currency conversion rates
- **20+ Supported Currencies**: Including USD, EUR, GBP, JPY, CAD, AUD, and more
- **Beautiful Web Interface**: Modern, responsive design with smooth animations
- **Dark Mode Toggle**: Switch between light and dark themes
- **Currency Swap Button**: Instantly swap between currencies
- **Command-line Interface**: Simple CLI for quick conversions
- **Error Handling**: Robust error handling for API failures and invalid inputs
- **Currency Formatting**: Proper currency symbols and formatting for each currency
- **Mobile Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Production Ready**: Deployed on Heroku with Gunicorn

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SohamPawgi15/currency-converter.git
   cd currency-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000` to use the web interface.

## 📖 Usage

### Web Interface

1. Enter the amount you want to convert
2. Select the source currency from the dropdown
3. Select the target currency from the dropdown
4. Click "Convert Currency" to see the result

#### 🌟 New Features:
- **🌙 Dark Mode**: Click the moon icon in the top-right to toggle dark/light theme
- **🔄 Swap Button**: Click the swap button between currency selectors to instantly reverse the conversion
- **💾 Persistent Settings**: Your theme preference is saved in your browser

### Command Line Interface

Run the command-line version for quick conversions:

```bash
python currency_converter.py
```

Example usage:
```
=== Currency Converter ===
Supported currencies:
  USD: US Dollar
  EUR: Euro
  GBP: British Pound
  ...

Enter amount: 100
From currency (e.g., USD): USD
To currency (e.g., EUR): EUR

$100.00 = €92.50
```

## 🛠️ API Integration

This project uses the [ExchangeRate-API](https://exchangerate-api.com/) for real-time exchange rates. The API is free to use and doesn't require an API key for basic usage.

### Optional API Key

For higher rate limits, you can add an API key:

1. Sign up at [ExchangeRate-API](https://exchangerate-api.com/)
2. Create a `.env` file in the project root:
   ```
   EXCHANGE_RATE_API_KEY=your_api_key_here
   ```

## 📁 Project Structure

```
currency-converter/
├── app.py                 # Flask web application
├── currency_converter.py  # Core conversion logic & CLI
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── test_converter.py     # Test suite
├── run.bat              # Windows launcher
├── run.sh               # Unix/Linux/Mac launcher
├── Procfile             # Heroku deployment
├── .python-version      # Python version specification
├── .gitignore           # Git ignore rules
├── templates/
│   └── index.html        # Web interface template
└── .env                  # Environment variables (optional)
```

## 🔧 Technical Details

### Core Components

- **CurrencyConverter Class**: Handles API calls and currency conversions
- **Flask Web App**: Provides RESTful API endpoints and serves the web interface
- **Modern UI**: Responsive design with CSS Grid and Flexbox
- **Error Handling**: Comprehensive error handling for network issues and invalid inputs

### Supported Currencies

- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)
- CHF (Swiss Franc)
- CNY (Chinese Yuan)
- INR (Indian Rupee)
- BRL (Brazilian Real)
- MXN (Mexican Peso)
- KRW (South Korean Won)
- SGD (Singapore Dollar)
- NZD (New Zealand Dollar)
- SEK (Swedish Krona)
- NOK (Norwegian Krone)
- DKK (Danish Krone)
- PLN (Polish Złoty)
- CZK (Czech Koruna)
- HUF (Hungarian Forint)

## 🧪 Testing

Test the application with different scenarios:

```bash
# Run the test suite
python test_converter.py

# Test web interface
python app.py
# Open http://localhost:5000

# Test command line interface
python currency_converter.py
```

## 🚀 Deployment

### Heroku Deployment

This app is configured for easy deployment on Heroku:

```bash
# Create Heroku app
heroku create your-app-name

# Deploy to Heroku
git push heroku master

# Open your app
heroku open
```

### Alternative Deployment Options

- **Render**: Use `render.yaml` configuration
- **Railway**: Direct GitHub integration
- **Vercel**: Static site deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [ExchangeRate-API](https://exchangerate-api.com/) for providing free exchange rate data
- Flask community for the excellent web framework
- All contributors and users of this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/SohamPawgi15/currency-converter/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

## 🎯 Learning Outcomes

This project demonstrates:
- **API Integration**: Real-world external service usage
- **Web Development**: Full-stack Flask application
- **Modern UI/UX**: Beautiful, responsive design
- **Error Handling**: Production-ready code
- **Testing**: Comprehensive test suite
- **Deployment**: Cloud deployment with Heroku
- **Version Control**: Professional Git workflow

---

**Built with ❤️ using Python and Flask**
