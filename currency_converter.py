import requests
import json
import logging
import time
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple, List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CurrencyConverter:
    """
    A currency converter that uses the ExchangeRate-API to get real-time exchange rates.
    """
    
    def __init__(self):
        self.base_url = "https://api.exchangerate-api.com/v4/latest"
        # Historical data provider (no key required)
        self.history_base_url = "https://api.exchangerate-api.com/v4/timeseries"
        self.api_key = os.getenv('EXCHANGE_RATE_API_KEY')  # Optional API key for higher limits
        self.session = requests.Session()
        # Cache: base_currency -> (fetched_at_unix, payload)
        self.cache_ttl_seconds = int(os.getenv('RATES_CACHE_TTL', '3600'))
        self._rates_cache: Dict[str, Tuple[float, Dict]] = {}
        # Logger
        self.logger = logging.getLogger(__name__)

        self.supported_currencies = {
            'USD': 'US Dollar',
            'EUR': 'Euro',
            'GBP': 'British Pound',
            'JPY': 'Japanese Yen',
            'CAD': 'Canadian Dollar',
            'AUD': 'Australian Dollar',
            'CHF': 'Swiss Franc',
            'CNY': 'Chinese Yuan',
            'INR': 'Indian Rupee',
            'BRL': 'Brazilian Real',
            'MXN': 'Mexican Peso',
            'KRW': 'South Korean Won',
            'SGD': 'Singapore Dollar',
            'NZD': 'New Zealand Dollar',
            'SEK': 'Swedish Krona',
            'NOK': 'Norwegian Krone',
            'DKK': 'Danish Krone',
            'PLN': 'Polish Złoty',
            'CZK': 'Czech Koruna',
            'HUF': 'Hungarian Forint'
        }
    
    def get_exchange_rates(self, base_currency: str) -> Optional[Dict]:
        """
        Fetch exchange rates for a given base currency.
        
        Args:
            base_currency (str): The base currency code (e.g., 'USD')
            
        Returns:
            Optional[Dict]: Exchange rates data or None if request fails
        """
        base_currency = base_currency.upper()

        # Serve from cache if fresh
        cached = self._rates_cache.get(base_currency)
        now = time.time()
        if cached:
            fetched_at, payload = cached
            if now - fetched_at < self.cache_ttl_seconds:
                return payload

        try:
            url = f"{self.base_url}/{base_currency}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Cache on success
            self._rates_cache[base_currency] = (now, data)
            return data
        except requests.RequestException as e:
            self.logger.warning(
                "exchange_rates_fetch_error",
                extra={"base_currency": base_currency, "error": str(e)}
            )
            # Fallback to stale cache if present
            if cached:
                self.logger.info("using_stale_rates_cache", extra={"base_currency": base_currency})
                return cached[1]
            return None
        except json.JSONDecodeError as e:
            self.logger.error(
                "exchange_rates_json_decode_error",
                extra={"base_currency": base_currency, "error": str(e)}
            )
            return None
    
    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> Optional[float]:
        """
        Convert an amount from one currency to another.
        
        Args:
            amount (float): The amount to convert
            from_currency (str): Source currency code
            to_currency (str): Target currency code
            
        Returns:
            Optional[float]: Converted amount or None if conversion fails
        """
        # Validate input
        if amount <= 0:
            self.logger.info("invalid_amount", extra={"amount": amount})
            return None

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        # Same-currency short-circuit
        if from_currency == to_currency:
            return round(float(amount), 2)

        if from_currency not in self.supported_currencies:
            self.logger.info("unsupported_source_currency", extra={"from_currency": from_currency})
            return None

        if to_currency not in self.supported_currencies:
            self.logger.info("unsupported_target_currency", extra={"to_currency": to_currency})
            return None

        # Get exchange rates
        rates_data = self.get_exchange_rates(from_currency)
        if not rates_data:
            return None

        rates = rates_data.get('rates', {})
        if to_currency not in rates:
            self.logger.info("missing_exchange_rate", extra={"to_currency": to_currency})
            return None

        # Perform conversion
        exchange_rate = rates[to_currency]
        converted_amount = amount * exchange_rate

        return round(converted_amount, 2)
    
    def get_supported_currencies(self) -> Dict[str, str]:
        """
        Get a dictionary of supported currencies.
        
        Returns:
            Dict[str, str]: Currency codes and their full names
        """
        return self.supported_currencies.copy()
    
    def format_currency(self, amount: float, currency_code: str) -> str:
        """
        Format currency amount with proper symbol and formatting.
        
        Args:
            amount (float): The amount to format
            currency_code (str): The currency code
            
        Returns:
            str: Formatted currency string
        """
        currency_symbols = {
            'USD': '$',
            'EUR': '€',
            'GBP': '£',
            'JPY': '¥',
            'CAD': 'C$',
            'AUD': 'A$',
            'CHF': 'CHF',
            'CNY': '¥',
            'INR': '₹',
            'BRL': 'R$',
            'MXN': '$',
            'KRW': '₩',
            'SGD': 'S$',
            'NZD': 'NZ$',
            'SEK': 'kr',
            'NOK': 'kr',
            'DKK': 'kr',
            'PLN': 'zł',
            'CZK': 'Kč',
            'HUF': 'Ft'
        }
        
        symbol = currency_symbols.get(currency_code, currency_code)
        
        # Special formatting for different currencies
        if currency_code in ['JPY', 'KRW']:
            return f"{symbol}{amount:,.0f}"
        else:
            return f"{symbol}{amount:,.2f}"

    def get_historical_rates(self, from_currency: str, to_currency: str, days: int = 30) -> Optional[Tuple[List[str], List[float]]]:
        """
        Fetch historical exchange rates for the given currency pair.
        For now, returns simulated data since free historical APIs are unreliable.
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.supported_currencies or to_currency not in self.supported_currencies:
            return None

        try:
            # Get current rate first
            current_rates = self.get_exchange_rates(from_currency)
            if not current_rates or to_currency not in current_rates.get('rates', {}):
                return None
            
            current_rate = current_rates['rates'][to_currency]
            
            # Generate simulated historical data with some variation
            import random
            dates = []
            rates = []
            base_date = datetime.utcnow().date()
            
            for i in range(days):
                date = base_date - timedelta(days=days - 1 - i)
                dates.append(date.isoformat())
                
                # Add some realistic variation (±5%)
                variation = random.uniform(-0.05, 0.05)
                rate = current_rate * (1 + variation)
                rates.append(round(rate, 4))
            
            return dates, rates
            
        except Exception as e:
            self.logger.warning(
                "historical_rates_fetch_error",
                extra={
                    "from_currency": from_currency,
                    "to_currency": to_currency,
                    "days": days,
                    "error": str(e),
                },
            )
            return None


def main():
    """
    Command-line interface for the currency converter.
    """
    converter = CurrencyConverter()
    
    print("=== Currency Converter ===")
    print("Supported currencies:")
    for code, name in converter.supported_currencies.items():
        print(f"  {code}: {name}")
    print()
    
    while True:
        try:
            # Get user input
            amount = float(input("Enter amount: "))
            from_currency = input("From currency (e.g., USD): ").upper()
            to_currency = input("To currency (e.g., EUR): ").upper()
            
            # Perform conversion
            result = converter.convert_currency(amount, from_currency, to_currency)
            
            if result is not None:
                formatted_from = converter.format_currency(amount, from_currency)
                formatted_to = converter.format_currency(result, to_currency)
                print(f"\n{formatted_from} = {formatted_to}")
            else:
                print("Conversion failed. Please check your input and try again.")
            
            # Ask if user wants to continue
            continue_conversion = input("\nConvert another amount? (y/n): ").lower()
            if continue_conversion != 'y':
                break
                
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
