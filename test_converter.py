#!/usr/bin/env python3
"""
Test script for the Currency Converter application.
This script tests the core functionality without requiring the web interface.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from currency_converter import CurrencyConverter

def test_currency_converter():
    """Test the currency converter functionality."""
    print("🧪 Testing Currency Converter...")
    print("=" * 50)
    
    # Initialize converter
    converter = CurrencyConverter()
    
    # Test 1: Get supported currencies
    print("\n1. Testing supported currencies...")
    currencies = converter.get_supported_currencies()
    print(f"✅ Found {len(currencies)} supported currencies")
    
    # Test 2: Test a simple conversion
    print("\n2. Testing USD to EUR conversion...")
    try:
        result = converter.convert_currency(100, 'USD', 'EUR')
        if result is not None:
            formatted_from = converter.format_currency(100, 'USD')
            formatted_to = converter.format_currency(result, 'EUR')
            print(f"✅ {formatted_from} = {formatted_to}")
        else:
            print("❌ Conversion failed")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
    
    # Test 3: Test invalid currency
    print("\n3. Testing invalid currency...")
    result = converter.convert_currency(100, 'INVALID', 'EUR')
    if result is None:
        print("✅ Correctly rejected invalid currency")
    else:
        print("❌ Should have rejected invalid currency")
    
    # Test 4: Test negative amount
    print("\n4. Testing negative amount...")
    result = converter.convert_currency(-100, 'USD', 'EUR')
    if result is None:
        print("✅ Correctly rejected negative amount")
    else:
        print("❌ Should have rejected negative amount")
    
    # Test 5: Test currency formatting
    print("\n5. Testing currency formatting...")
    test_cases = [
        (100, 'USD', '$100.00'),
        (1000, 'EUR', '€1,000.00'),
        (1000000, 'JPY', '¥1,000,000'),
        (1234.56, 'GBP', '£1,234.56')
    ]
    
    for amount, currency, expected in test_cases:
        formatted = converter.format_currency(amount, currency)
        if formatted == expected:
            print(f"✅ {amount} {currency} formats as {formatted}")
        else:
            print(f"❌ {amount} {currency} formats as {formatted}, expected {expected}")
    
    print("\n" + "=" * 50)
    print("🎉 Testing completed!")

if __name__ == "__main__":
    test_currency_converter()
