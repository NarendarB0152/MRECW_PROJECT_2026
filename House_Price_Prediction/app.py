import streamlit as st
import util

def main():
    st.set_page_config(
        page_title="Bangalore House Price Prediction",
        page_icon="🏠",
        layout="centered"
    )

    st.title("🏠 Bangalore House Price Prediction")
    st.markdown("Enter the details of the house you want to buy, and we'll estimate its price!")

    # Load artifacts once
    if 'artifacts_loaded' not in st.session_state:
        util.load_saved_artifacts()
        st.session_state['artifacts_loaded'] = True
        
    locations = util.get_location_names()
    
    # Input Form
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            total_sqft = st.number_input("Total Square Feet", min_value=100.0, max_value=100000.0, value=1000.0, step=100.0)
            bhk = st.number_input("BHK (Bedrooms)", min_value=1, max_value=20, value=2, step=1)
            
        with col2:
            location = st.selectbox("Location", locations)
            bath = st.number_input("Bathrooms", min_value=1, max_value=20, value=2, step=1)
            
        submit_button = st.form_submit_button("Estimate Price")

    if submit_button:
        try:
            price = util.get_estimated_price(location, total_sqft, bhk, bath)
            st.success(f"🏡 **Estimated Price:** {price} Lakhs")
        except Exception as e:
            st.error(f"Error predicting price: {e}")

if __name__ == "__main__":
    main()
