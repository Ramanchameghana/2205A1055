import streamlit as st

st.title("2205A21055. -PS6.")

# Function to calculate transformer efficiency and copper losses
def Tran_Eff(Rated_VA, CL, FCL, K, PF):
    # Calculate output power
    output_power = K * Rated_VA * PF
    
    # Calculate input power
    input_power = K * Rated_VA * PF + CL + K**2 * FCL
    
    # Calculate Efficiency
    Eff = (output_power / input_power) * 100  # Efficiency in percentage
    
    # Calculate Copper Losses at given load
    CUL = K**2 * FCL  # Copper Losses at load factor K
    
    return Eff, CUL

# Streamlit UI
def main():
    st.title("Transformer Efficiency and Copper Losses Calculator")
    
    # Input Fields
    Rated_VA = st.number_input("Enter Rated Power (VA)", min_value=1, step=1)
    CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0, step=1)
    FCL = st.number_input("Enter Full Load Copper Losses (FCL) in Watts", min_value=0, step=1)
    K = st.number_input("Enter Loading on Transformer (K)", min_value=0.0, max_value=1.0, step=0.01)
    PF = st.number_input("Enter Power Factor (PF)", min_value=0.0, max_value=1.0, step=0.01)
    
    # Create two columns, one for inputs and one for output
col1, col2 = st.columns(2)  # [1, 1] means both columns have equal width
    
    # Column 1 for Inputs
with col1:
        # Display the inputs (which is the left side of the screen)
        st.write("### Inputs")
        Rated_VA = st.number_input("Rated Power (VA)", min_value=1, step=1)
        CL = st.number_input("Core Losses (CL) in Watts", min_value=0, step=1)
        FCL = st.number_input("Full Load Copper Losses (FCL) in Watts", min_value=0, step=1)
        K = st.number_input("Loading on Transformer (K)", min_value=0.0, max_value=1.0, step=0.01)
        PF = st.number_input("Power Factor (PF)", min_value=0.0, max_value=1.0, step=0.01)
        
    # Column 2 for Output
with col2:
        # Button to calculate and show output on the right side
    if st.button("Calculate Efficiency and Copper Losses"):
        Eff, CUL = Tran_Eff(Rated_VA, CL, FCL, K, PF)
            
            # Display results on the right side (col2)
        st.write("### Results")
        st.write(f"*Transformer Efficiency:* {Eff:.2f}%")
        st.write(f"*Copper Losses at K load factor:* {CUL:.2f} W")
