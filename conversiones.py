import streamlit as st

# Título y autor de la app
st.title("App de Conversiones")
st.write("Esta app fue elaborada por Cesar Augusto Ospina Muñoz.")

# Menú desplegable para seleccionar el tipo de conversión
conversion_seleccionada = st.sidebar.selectbox("Seleccione el tipo de conversión:",
                                               ["Conversiones de temperatura", "Conversiones de longitud",
                                                "Conversiones de peso/masa", "Conversiones de volumen",
                                                "Conversiones de tiempo", "Conversiones de velocidad",
                                                "Conversiones de área", "Conversiones de energía",
                                                "Conversiones de presión", "Conversiones de tamaño de datos"])

# Mostrar el tipo de conversión seleccionado
st.sidebar.write(f"Ha seleccionado: {conversion_seleccionada}")

# Realizar conversiones de temperatura
if conversion_seleccionada == "Conversiones de temperatura":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Celsius a Fahrenheit", "Fahrenheit a Celsius",
                                    "Celsius a Kelvin", "Kelvin a Celsius"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Celsius a Fahrenheit":
        valor_convertido = (valor_original * 9/5) + 32
        st.write(f"{valor_original} °C equivale a {valor_convertido} °F")
    elif tipo_conversion == "Fahrenheit a Celsius":
        valor_convertido = (valor_original - 32) * 5/9
        st.write(f"{valor_original} °F equivale a {valor_convertido} °C")
    elif tipo_conversion == "Celsius a Kelvin":
        valor_convertido = valor_original + 273.15
        st.write(f"{valor_original} °C equivale a {valor_convertido} K")
    elif tipo_conversion == "Kelvin a Celsius":
        valor_convertido = valor_original - 273.15
        st.write(f"{valor_original} K equivale a {valor_convertido} °C")
