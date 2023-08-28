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

# Mostrar el tipo de conversión seleccionado en la barra lateral
st.sidebar.text(f"Ha seleccionado: {conversion_seleccionada}")

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

# Realizar conversiones de longitud
elif conversion_seleccionada == "Conversiones de longitud":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Pies a metros", "Metros a pies",
                                    "Pulgadas a centímetros", "Centímetros a pulgadas"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Pies a metros":
        valor_convertido = valor_original * 0.3048
        st.write(f"{valor_original} pies equivale a {valor_convertido} metros")
    elif tipo_conversion == "Metros a pies":
        valor_convertido = valor_original / 0.3048
        st.write(f"{valor_original} metros equivale a {valor_convertido} pies")
    elif tipo_conversion == "Pulgadas a centímetros":
        valor_convertido = valor_original * 2.54
        st.write(f"{valor_original} pulgadas equivale a {valor_convertido} centímetros")
    elif tipo_conversion == "Centímetros a pulgadas":
        valor_convertido = valor_original / 2.54
        st.write(f"{valor_original} centímetros equivale a {valor_convertido} pulgadas")

elif conversion_seleccionada == "Conversiones de peso/masa":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Libras a kilogramos", "Kilogramos a libras",
                                    "Onzas a gramos", "Gramos a onzas"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Libras a kilogramos":
        valor_convertido = valor_original * 0.453592
        st.write(f"{valor_original} libras equivale a {valor_convertido} kilogramos")
    elif tipo_conversion == "Kilogramos a libras":
        valor_convertido = valor_original / 0.453592
        st.write(f"{valor_original} kilogramos equivale a {valor_convertido} libras")
    elif tipo_conversion == "Onzas a gramos":
        valor_convertido = valor_original * 28.3495
        st.write(f"{valor_original} onzas equivale a {valor_convertido} gramos")
    elif tipo_conversion == "Gramos a onzas":
        valor_convertido = valor_original / 28.3495
        st.write(f"{valor_original} gramos equivale a {valor_convertido} onzas")

# Realizar conversiones de volumen
elif conversion_seleccionada == "Conversiones de volumen":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Galones a litros", "Litros a galones",
                                    "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Galones a litros":
        valor_convertido = valor_original * 3.78541
        st.write(f"{valor_original} galones equivale a {valor_convertido} litros")
    elif tipo_conversion == "Litros a galones":
        valor_convertido = valor_original / 3.78541
        st.write(f"{valor_original} litros equivale a {valor_convertido} galones")
    elif tipo_conversion == "Pulgadas cúbicas a centímetros cúbicos":
        valor_convertido = valor_original * 16.387
        st.write(f"{valor_original} pulgadas cúbicas equivale a {valor_convertido} centímetros cúbicos")
    elif tipo_conversion == "Centímetros cúbicos a pulgadas cúbicas":
        valor_convertido = valor_original / 16.387
        st.write(f"{valor_original} centímetros cúbicos equivale a {valor_convertido} pulgadas cúbicas")
# Realizar conversiones de tiempo
elif conversion_seleccionada == "Conversiones de tiempo":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Horas a minutos", "Minutos a segundos",
                                    "Días a horas", "Semanas a días"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Horas a minutos":
        valor_convertido = valor_original * 60
        st.write(f"{valor_original} horas equivale a {valor_convertido} minutos")
    elif tipo_conversion == "Minutos a segundos":
        valor_convertido = valor_original * 60
        st.write(f"{valor_original} minutos equivale a {valor_convertido} segundos")
    elif tipo_conversion == "Días a horas":
        valor_convertido = valor_original * 24
        st.write(f"{valor_original} días equivale a {valor_convertido} horas")
    elif tipo_conversion == "Semanas a días":
        valor_convertido = valor_original * 7
        st.write(f"{valor_original} semanas equivale a {valor_convertido} días")

# Realizar conversiones de velocidad
elif conversion_seleccionada == "Conversiones de velocidad":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo",
                                    "Nudos a millas por hora", "Metros por segundo a pies por segundo"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Millas por hora a kilómetros por hora":
        valor_convertido = valor_original * 1.60934
        st.write(f"{valor_original} millas por hora equivale a {valor_convertido} kilómetros por hora")
    elif tipo_conversion == "Kilómetros por hora a metros por segundo":
        valor_convertido = valor_original * 0.277778
        st.write(f"{valor_original} kilómetros por hora equivale a {valor_convertido} metros por segundo")
    elif tipo_conversion == "Nudos a millas por hora":
        valor_convertido = valor_original * 1.15078
        st.write(f"{valor_original} nudos equivale a {valor_convertido} millas por hora")
    elif tipo_conversion == "Metros por segundo a pies por segundo":
        valor_convertido = valor_original * 3.28084
        st.write(f"{valor_original} metros por segundo equivale a {valor_convertido} pies por segundo")

# Realizar conversiones de área
elif conversion_seleccionada == "Conversiones de área":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados",
                                    "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Metros cuadrados a pies cuadrados":
        valor_convertido = valor_original * 10.7639
        st.write(f"{valor_original} metros cuadrados equivale a {valor_convertido} pies cuadrados")
    elif tipo_conversion == "Pies cuadrados a metros cuadrados":
        valor_convertido = valor_original / 10.7639
        st.write(f"{valor_original} pies cuadrados equivale a {valor_convertido} metros cuadrados")
    elif tipo_conversion == "Kilómetros cuadrados a millas cuadradas":
        valor_convertido = valor_original * 0.386102
        st.write(f"{valor_original} kilómetros cuadrados equivale a {valor_convertido} millas cuadradas")
    elif tipo_conversion == "Millas cuadradas a kilómetros cuadrados":
        valor_convertido = valor_original / 0.386102
        st.write(f"{valor_original} millas cuadradas equivale a {valor_convertido} kilómetros cuadrados")


# Realizar conversiones de energía
elif conversion_seleccionada == "Conversiones de energía":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Julios a calorías", "Calorías a kilojulios",
                                    "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Julios a calorías":
        valor_convertido = valor_original * 0.239006
        st.write(f"{valor_original} julios equivale a {valor_convertido} calorías")
    elif tipo_conversion == "Calorías a kilojulios":
        valor_convertido = valor_original * 0.001
        st.write(f"{valor_original} calorías equivale a {valor_convertido} kilojulios")
    elif tipo_conversion == "Kilovatios-hora a megajulios":
        valor_convertido = valor_original * 1000
        st.write(f"{valor_original} kilovatios-hora equivale a {valor_convertido} megajulios")
    elif tipo_conversion == "Megajulios a kilovatios-hora":
        valor_convertido = valor_original * 0.001
        st.write(f"{valor_original} megajulios equivale a {valor_convertido} kilovatios-hora")
# Realizar conversiones de presión
elif conversion_seleccionada == "Conversiones de presión":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Pascales a atmósferas", "Atmósferas a pascales",
                                    "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Pascales a atmósferas":
        valor_convertido = valor_original * 9.8692e-6
        st.write(f"{valor_original} pascales equivale a {valor_convertido} atmósferas")
    elif tipo_conversion == "Atmósferas a pascales":
        valor_convertido = valor_original / 9.8692e-6
        st.write(f"{valor_original} atmósferas equivale a {valor_convertido} pascales")
    elif tipo_conversion == "Barras a libras por pulgada cuadrada":
        valor_convertido = valor_original * 14.5038
        st.write(f"{valor_original} bares equivale a {valor_convertido} libras por pulgada cuadrada")
    elif tipo_conversion == "Libras por pulgada cuadrada a bares":
        valor_convertido = valor_original / 14.5038
        st.write(f"{valor_original} libras por pulgada cuadrada equivale a {valor_convertido} bares")
# Realizar conversiones de tamaño de datos
elif conversion_seleccionada == "Conversiones de tamaño de datos":
    tipo_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                   ["Megabytes a gigabytes", "Gigabytes a terabytes",
                                    "Kilobytes a megabytes", "Terabytes a petabytes"])
    
    valor_original = st.number_input("Ingrese el valor a convertir:")
    
    if tipo_conversion == "Megabytes a gigabytes":
        valor_convertido = valor_original * 0.001
        st.write(f"{valor_original} megabytes equivale a {valor_convertido} gigabytes")
    elif tipo_conversion == "Gigabytes a terabytes":
        valor_convertido = valor_original * 0.001
        st.write(f"{valor_original} gigabytes equivale a {valor_convertido} terabytes")
    elif tipo_conversion == "Kilobytes a megabytes":
        valor_convertido = valor_original * 0.001
        st.write(f"{valor_original} kilobytes equivale a {valor_convertido} megabytes")
    elif tipo_conversion == "Terabytes a petabytes":
        valor_convertido = valor_original * 0.001
        st.write(f"{valor_original} terabytes equivale a {valor_convertido} petabytes")
