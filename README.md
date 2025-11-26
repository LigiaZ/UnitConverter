# UnitConverter
Unit converter project with my husband
The sweeetest! 
## Description
A web-based unit converter built with Python and Streamlit. Converts between various units in temperature, length, volume, and weight categories.

## Features

### Temperature Conversions
- **Celsius ↔ Fahrenheit**: Convert between Celsius and Fahrenheit temperature scales
- **Celsius ↔ Kelvin**: Convert between Celsius and Kelvin temperature scales
- **Formula examples**: 
  - Fahrenheit = (Celsius × 9/5) + 32
  - Kelvin = Celsius + 273.15

### Length Conversions
- **Kilometers ↔ Miles**: Convert between metric and imperial distance units
- **Kilometers → Yards**: Convert kilometers to yards (1 km = 1093.61 yards)
- **Meters → Feet**: Convert metric length to imperial feet (1 m = 3.28084 feet)
- **Conversion factors**:
  - 1 kilometer = 0.621371 miles
  - 1 kilometer = 1093.61 yards
  - 1 meter = 3.28084 feet

### Volume Conversions
- **Milliliters → Ounces**: Convert liquid volume from metric to US ounces
- **Liters → Gallons**: Convert larger volumes from liters to US gallons
- **Conversion factors**:
  - 1 milliliter = 0.033814 US fluid ounces
  - 1 liter = 0.264172 US gallons

### Weight Conversions
- **Grams → Ounces**: Convert weight from metric grams to imperial ounces
- **Kilograms → Pounds**: Convert weight from kilograms to pounds
- **Conversion factors**:
  - 1 gram = 0.035274 ounces
  - 1 kilogram = 2.20462 pounds

### User Interface
- Clean, intuitive interface with dropdown selection for categories and units
- Real-time conversion calculations
- Custom color scheme with Tea & Romance palette
- Responsive design suitable for web browsers
- Clear input validation and error handling

## Setup and Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   streamlit run app.py
   ```

3. Open your browser to the URL provided by Streamlit (usually http://localhost:8501)