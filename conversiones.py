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
