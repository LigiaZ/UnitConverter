import streamlit as st

# Custom CSS for styling
st.markdown("""
<style>
body {
    background-color: #f9f1f0; /* ivory */
    color: #663635; /* marsala */
}
.stApp {
    background-color: #f9f1f0;
}
h1, h2, h3 {
    color: #663635;
}
.stButton>button {
    background-color: #e1999f; /* rosewater */
    color: #663635;
    border: none;
    border-radius: 5px;
}
.stSelectbox, .stNumberInput {
    background-color: #deb3ad; /* dusty-rose */
    color: #663635;
}
.stTextInput {
    background-color: #deb3ad;
    color: #663635;
}
</style>
""", unsafe_allow_html=True)

st.title("Unit Converter")
st.write("Welcome to the Unit Converter app! Choose a category and start converting units.")

# Unit conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def km_to_yards(km):
    return km * 1093.61

def meters_to_feet(m):
    return m * 3.28084

def ml_to_ounces(ml):
    return ml * 0.033814

def liters_to_gallons(l):
    return l * 0.264172

def grams_to_ounces(g):
    return g * 0.035274

def kg_to_pounds(kg):
    return kg * 2.20462

def check_temperature(celsius):
    if not isinstance(celsius, (int, float)):
        return "Invalid input: temperature must be a number."
    if celsius > 30:
        return "It's too hot! 🔥"
    elif celsius < 0:
        return "It's too cold! ❄️"
    else:
        return "The temperature is comfortable."

def temp_to_color(temp, min_temp=-100, max_temp=100):
    # Normalize temperature to 0-1
    norm = (temp - min_temp) / (max_temp - min_temp)
    norm = max(0, min(1, norm))  # Clamp to [0, 1]
    # Hue from 240° (blue) to 0° (red)
    hue = 240 - (240 * norm)
    # Saturation 100%, Lightness 50%
    return f"hsl({hue:.0f}, 100%, 50%)"

def display_temperature_gradient(temp_celsius):
    min_temp = -100
    max_temp = 100
    # Calculate position as percentage from left (0% = cold, 100% = hot)
    position = ((temp_celsius - min_temp) / (max_temp - min_temp)) * 100
    position = max(0, min(100, position))  # Clamp
    
    # HTML for horizontal gradient bar with marker
    gradient_html = f"""
    <div style="margin-top: 20px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
            <span>-100°C (Cold)</span>
            <span>100°C (Hot)</span>
        </div>
        <div style="height: 30px; width: 100%; background: linear-gradient(to right, #00BFFF, #00FF00, #FFFF00, #FF0000); position: relative; border-radius: 15px; border: 1px solid #ccc;">
            <div style="position: absolute; left: {position:.1f}%; top: -5px; width: 4px; height: 40px; background: black; transform: translateX(-50%); border: 1px solid white;"></div>
        </div>
        <div style="text-align: center; margin-top: 10px; font-weight: bold;">
            Current: {temp_celsius:.1f}°C
        </div>
    </div>
    """
    st.markdown(gradient_html, unsafe_allow_html=True)

# Categories and units
categories = {
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Length": ["Kilometers", "Miles", "Yards", "Meters", "Feet"],
    "Volume": ["Milliliters", "Ounces", "Liters", "Gallons"],
    "Weight": ["Grams", "Ounces", "Kilograms", "Pounds"]
}

# Conversion logic
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return celsius_to_fahrenheit(value)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return fahrenheit_to_celsius(value)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return celsius_to_kelvin(value)
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return kelvin_to_celsius(value)
        else:
            return value  # Same unit
    elif category == "Length":
        if from_unit == "Kilometers" and to_unit == "Miles":
            return km_to_miles(value)
        elif from_unit == "Miles" and to_unit == "Kilometers":
            return miles_to_km(value)
        elif from_unit == "Kilometers" and to_unit == "Yards":
            return km_to_yards(value)
        elif from_unit == "Meters" and to_unit == "Feet":
            return meters_to_feet(value)
        else:
            return value
    elif category == "Volume":
        if from_unit == "Milliliters" and to_unit == "Ounces":
            return ml_to_ounces(value)
        elif from_unit == "Liters" and to_unit == "Gallons":
            return liters_to_gallons(value)
        else:
            return value
    elif category == "Weight":
        if from_unit == "Grams" and to_unit == "Ounces":
            return grams_to_ounces(value)
        elif from_unit == "Kilograms" and to_unit == "Pounds":
            return kg_to_pounds(value)
        else:
            return value
    return value

# UI
category = st.selectbox("Select Category", list(categories.keys()))

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", categories[category])
with col2:
    to_unit = st.selectbox("To Unit", categories[category])

value = st.number_input("Enter Value", value=0.0)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    if category == "Temperature" and to_unit == "Celsius":
        message = check_temperature(result)
        st.info(message)
        display_temperature_gradient(result)