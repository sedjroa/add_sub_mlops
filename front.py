import streamlit as st
import requests

# Frontend configurations
st.set_page_config(page_title="calc", page_icon="➕", layout="wide")
st.header(body="Fun pour faire des calculs", 
          divider="green", 
          width='stretch')

# Frontend columns definition
left, right = st.columns(2)

# Left column code
with left:
    with st.form("calc_form"):
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input(label="Entrez un nombre",
                    value=None,
                    placeholder="Entrer A")
        with col2:
            b = st.number_input(label="Entrez un nombre",
                    value=None,
                    placeholder="Entrer B")
        
        operation = st.selectbox(label="Operation", options=("Addition","Soustraction"))
        submit = st.form_submit_button('Calculer')

# Right column code
with right:
    # Test if user clicked submit button
    if submit:
        # Tests if A and B are provided
        if a and b:
            ops = "add" if operation == "Addition" else "sub"
            url = f"http://127.0.0.1:8000/{ops}?a={a}&b={b}"

            try:
                response = requests.get(url=url)
                if response.status_code == 200:
                    resultat = response.json()
                    st.success(f"Votre {resultat['operation']} donne: {resultat['result']} ")
                    # Link to view metrics
                    st.markdown("Consultez les [métriques de l'API](http://localhost:8000/metrics)")
                    # Link to view backend functions documentation and testing available
                    st.markdown("Voir la [documentation](http://localhost:8000/docs)")
                else:
                    # Error of requesting backend FastAPI
                    st.error(f"Error  {response.status_code}")
                
            except Exception as e:
                st.error(f"{e}")

        # If at least A or B is misssing
        else:
            st.warning("Valeur A et/ou B manquante")