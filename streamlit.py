import streamlit as st
import numpy as np
import pickle

# Cargar el modelo entrenado
model = pickle.load(open('model.pkl', 'rb'))

def main():
    st.title('Mi Aplicación de Predicción')

    # Sidebar con instrucciones o información adicional
    st.sidebar.header('Instrucciones')
    st.sidebar.markdown('Complete los siguientes campos y haga clic en "Predecir" para obtener la predicción.')

    # Obtener las características de entrada del usuario
    init_features = get_user_input()

    # Realizar la predicción cuando se hace clic en el botón
    if st.button('Predecir'):
        prediction = make_prediction(init_features)
        st.success(f'Clase Predicha: {prediction}')

def get_user_input():
    # Crear campos de entrada para las características
    feature1 = st.number_input('Ingrese Feature 1', value=0.0)
    feature2 = st.number_input('Ingrese Feature 2', value=0.0)
    feature3 = st.number_input('Ingrese Feature 3', value=0.0)

    # Devolver las características como una lista
    return [feature1, feature2, feature3]

def make_prediction(features):
    # Convertir las características a un array de NumPy
    final_features = np.array(features).reshape(1, -1)

    # Hacer la predicción utilizando el modelo cargado
    prediction = model.predict(final_features)[0]
    return prediction

if __name__ == '__main__':
    main()
