# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template, request, jsonify
import pandas as pd
from tinydb import TinyDB, Query

# METER DATOS DE LAS CRYPTO EN TINYDB

app = Flask(__name__)


db = TinyDB('crypto_db.json')

# Lista completa de criptomonedas con soporte de contratos inteligentes
crypto_data = [
    {'symbol': 'AAVE-USD', 'name': 'Aave', 'contract': 'Aave Smart Contract', 'volume': 320000, 'price': 82.37},
    {'symbol': 'ADA-USD', 'name': 'Cardano', 'contract': 'Plutus Smart Contract', 'volume': 5000000, 'price': 0.48},
    {'symbol': 'ALGO-USD', 'name': 'Algorand', 'contract': 'Algorand Smart Contract', 'volume': 1200000, 'price': 0.31},
    {'symbol': 'AVAX-USD', 'name': 'Avalanche', 'contract': 'Avalanche Smart Contract', 'volume': 400000, 'price': 17.24},
    {'symbol': 'BAT-USD', 'name': 'Basic Attention Token', 'contract': 'BAT Smart Contract', 'volume': 800000, 'price': 0.32},
    {'symbol': 'BNB-USD', 'name': 'Binance Coin', 'contract': 'Binance Smart Chain Contract', 'volume': 1500000, 'price': 212.75},
    {'symbol': 'ENJ-USD', 'name': 'Enjin Coin', 'contract': 'Enjin Smart Contract', 'volume': 250000, 'price': 0.44},
    {'symbol': 'EOS-USD', 'name': 'EOS', 'contract': 'EOSIO Smart Contract', 'volume': 950000, 'price': 0.98},
    {'symbol': 'ETC-USD', 'name': 'Ethereum Classic', 'contract': 'Ethereum Virtual Machine', 'volume': 2200000, 'price': 18.03},
    {'symbol': 'ETH-USD', 'name': 'Ethereum', 'contract': 'Ethereum Smart Contract', 'volume': 3000000, 'price': 1362.49},
    {'symbol': 'HBAR-USD', 'name': 'Hedera Hashgraph', 'contract': 'Hedera Smart Contract', 'volume': 2000000, 'price': 0.06},
    {'symbol': 'HT-USD', 'name': 'Huobi Token', 'contract': 'Huobi ECO Chain Smart Contract', 'volume': 800000, 'price': 4.67},
    {'symbol': 'KLAY-USD', 'name': 'Klaytn', 'contract': 'Klaytn Smart Contract', 'volume': 500000, 'price': 0.27},
    {'symbol': 'LINK-USD', 'name': 'Chainlink', 'contract': 'Chainlink Smart Contract', 'volume': 1300000, 'price': 7.11},
    {'symbol': 'MANA-USD', 'name': 'Decentraland', 'contract': 'Decentraland Smart Contract', 'volume': 1000000, 'price': 0.70},
    {'symbol': 'MATIC-USD', 'name': 'Polygon', 'contract': 'Polygon Smart Contract', 'volume': 3000000, 'price': 0.91},
    {'symbol': 'MKR-USD', 'name': 'Maker', 'contract': 'MakerDAO Smart Contract', 'volume': 60000, 'price': 1024.00},
    {'symbol': 'NEO-USD', 'name': 'NEO', 'contract': 'NEO Smart Contract', 'volume': 800000, 'price': 9.20},
    {'symbol': 'QTUM-USD', 'name': 'Qtum', 'contract': 'Qtum Smart Contract', 'volume': 700000, 'price': 2.12},
    {'symbol': 'SNX-USD', 'name': 'Synthetix', 'contract': 'Synthetix Smart Contract', 'volume': 300000, 'price': 2.22},
    {'symbol': 'THETA-USD', 'name': 'Theta Network', 'contract': 'Theta Smart Contract', 'volume': 1100000, 'price': 1.13},
    {'symbol': 'TRX-USD', 'name': 'TRON', 'contract': 'TRON Smart Contract', 'volume': 7000000, 'price': 0.07},
    {'symbol': 'USDC-USD', 'name': 'USD Coin', 'contract': 'USDC Smart Contract', 'volume': 4200000, 'price': 1},
    {'symbol': 'USDT-USD', 'name': 'Tether', 'contract': 'Tether Smart Contract', 'volume': 10000000, 'price': 1.00},
    {'symbol': 'VET-USD', 'name': 'VeChain', 'contract': 'VeChain Smart Contract', 'volume': 2000000, 'price': 0.03},
    {'symbol': 'WAVES-USD', 'name': 'Waves', 'contract': 'Waves Smart Contract', 'volume': 500000, 'price': 4.12},
    {'symbol': 'XLM-USD', 'name': 'Stellar Lumens', 'contract': 'Stellar Smart Contract', 'volume': 3000000, 'price': 0.13},
    {'symbol': 'XRP-USD', 'name': 'XRP', 'contract': 'XRP Ledger Smart Contract', 'volume': 9000000, 'price': 0.45},
    {'symbol': 'XTZ-USD', 'name': 'Tezos', 'contract': 'Tezos Smart Contract', 'volume': 1000000, 'price': 1.75},
    {'symbol': 'YFI-USD', 'name': 'yearn.finance', 'contract': 'Yearn Finance Smart Contract', 'volume': 15000, 'price': 8700.00},
    {'symbol': 'ZIL-USD', 'name': 'Zilliqa', 'contract': 'Zilliqa Smart Contract', 'volume': 2000000, 'price': 0.05},
    {'symbol': 'BCH-USD', 'name': 'Bitcoin Cash', 'contract': '', 'volume': 1500000, 'price': 120.25},
    {'symbol': 'BTC-USD', 'name': 'Bitcoin', 'contract': '', 'volume': 10000000, 'price': 19200.00},
    {'symbol': 'DASH-USD', 'name': 'Dash', 'contract': '', 'volume': 400000, 'price': 46.20},
    {'symbol': 'DCR-USD', 'name': 'Decred', 'contract': '', 'volume': 120000, 'price': 28.15},
    {'symbol': 'DOGE-USD', 'name': 'Dogecoin', 'contract': '', 'volume': 8000000, 'price': 0.065},
    {'symbol': 'FIL-USD', 'name': 'Filecoin', 'contract': '', 'volume': 500000, 'price': 5.77},
    {'symbol': 'KSM-USD', 'name': 'Kusama', 'contract': '', 'volume': 60000, 'price': 48.30},
    {'symbol': 'LTC-USD', 'name': 'Litecoin', 'contract': '', 'volume': 2000000, 'price': 53.20},
    {'symbol': 'XEM-USD', 'name': 'NEM', 'contract': '', 'volume': 1500000, 'price': 0.042},
    {'symbol': 'XMR-USD', 'name': 'Monero', 'contract': '', 'volume': 300000, 'price': 150.00},
    {'symbol': 'ZEC-USD', 'name': 'Zcash', 'contract': '', 'volume': 300000, 'price': 65.00}
]


if not db.all():
    db.insert_multiple(crypto_data)


crypto_names = {
    'AAVE-USD': 'Aave',
    'ADA-USD': 'Cardano',
    'ALGO-USD': 'Algorand',
    'AVAX-USD': 'Avalanche',
    'BAT-USD': 'Basic Attention Token',
    'BCH-USD': 'Bitcoin Cash',
    'BNB-USD': 'Binance Coin',
    'BTC-USD': 'Bitcoin',
    'DASH-USD': 'Dash',
    'DCR-USD': 'Decred',
    'DOGE-USD': 'Dogecoin',
    'ENJ-USD': 'Enjin Coin',
    'EOS-USD': 'EOS',
    'ETC-USD': 'Ethereum Classic',
    'ETH-USD': 'Ethereum',
    'FIL-USD': 'Filecoin',
    'HBAR-USD': 'Hedera Hashgraph',
    'HT-USD': 'Huobi Token',
    'KLAY-USD': 'Klaytn',
    'KSM-USD': 'Kusama',
    'LINK-USD': 'Chainlink',
    'LTC-USD': 'Litecoin',
    'MANA-USD': 'Decentraland',
    'MATIC-USD': 'Polygon',
    'MKR-USD': 'Maker',
    'NEO-USD': 'NEO',
    'QTUM-USD': 'Qtum',
    'SNX-USD': 'Synthetix',
    'THETA-USD': 'Theta Network',
    'TRX-USD': 'TRON',
    'USDC-USD': 'USD Coin',
    'USDT-USD': 'Tether',
    'VET-USD': 'VeChain',
    'WAVES-USD': 'Waves',
    'XEM-USD': 'NEM',
    'XLM-USD': 'Stellar Lumens',
    'XMR-USD': 'Monero',
    'XRP-USD': 'XRP',
    'XTZ-USD': 'Tezos',
    'YFI-USD': 'yearn.finance',
    'ZEC-USD': 'Zcash',
    'ZIL-USD': 'Zilliqa'
}

df = pd.DataFrame(list(crypto_names.items()), columns=['crypto', 'name'])



@app.route("/")
def index():
    return render_template("index.html", df = df, ids = list(range(len(df))))


@app.route("/cryptoinfo", methods=['GET', 'POST'])
def cryptoinfo():
    # Obtener el símbolo de la criptomoneda de los argumentos de la solicitud
    if request.method == 'GET':
        symbol = request.args.get("crypto")
    elif request.method == 'POST':
        data = request.get_json()  # Asegúrate de que el cliente envía JSON
        symbol = data.get("crypto")

    Crypto = Query()
    crypto_info = db.search(Crypto.symbol == symbol)

    if crypto_info:
        return jsonify({"message": f"Información de {symbol}: {crypto_info}"})
    else:
        return jsonify({"error": f"No se encontró información para {symbol}"}), 404
