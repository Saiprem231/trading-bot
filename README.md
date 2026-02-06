# Binance Futures Testnet Trading Bot

---

## 📌 Project Overview

This project is a Python-based CLI Trading Bot that places MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).

The application demonstrates:
- Clean project structure
- Binance Futures Testnet API integration
- CLI-based user input
- Logging of requests and responses
- Proper error handling and validation

⚠ This bot works only on Binance Testnet (No real money involved).

---

## 🧱 Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── trading_bot.log
```

---

## ⚙ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/Saiprem231/trading-bot.git
cd trading_bot
```

---

### 2️⃣ Install Dependencies

Make sure Python 3.x is installed.

```
pip install -r requirements.txt
```

---

### 3️⃣ Create Binance Testnet Account

Register here:

```
https://testnet.binancefuture.com
```

Generate:
- API Key  
- Secret Key  

---

### 4️⃣ Set Environment Variables

#### Windows (PowerShell)

```
setx BINANCE_API_KEY "your_api_key_here"
setx BINANCE_API_SECRET "your_secret_key_here"
```

Restart terminal after setting.

---

## ▶ Running the Bot

---

### 🟢 MARKET Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### 🔵 LIMIT Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000
```

---

## 🧾 Sample Output

```
===== ORDER REQUEST SUMMARY =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

✅ ORDER SUCCESS
```

---

## 📊 Logging

Logs are saved in:

```
trading_bot.log
```

Logs include:
- Order request data
- API responses
- Error messages
- Success confirmations

---

## 📌 Assumptions

- Binance Futures Testnet is used (not live trading)
- API keys must be set as environment variables
- Internet connection required

Note:  
Binance Futures Testnet may sometimes return limited response fields.  
Order execution is still confirmed through successful API call and logging.

---

## 📦 Requirements

Main libraries used:
- python-binance  
- python-dotenv  
- requests  

(Exact versions are inside requirements.txt)

---

## ⚠ Disclaimer

This project is for educational and testing purposes only.  
Do not use this bot for real trading without proper risk management and security review.

---

## 👨‍💻 Author

Saiprem  
Python Developer
