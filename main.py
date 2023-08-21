import streamlit as st

from unit_converter import UnitConverter


def main():
    st.title("Unit Converter for Mehdi Joon" + "😍")

    converter = UnitConverter()
    quantity_options = list(converter.conversion_factors.keys())
    selected_quantity = st.selectbox("Select Quantity Type", quantity_options)

    # Get the available units for the selected quantity
    available_units = list(converter.conversion_factors[selected_quantity].keys())

    # Create drop-down boxes for selecting the "from" and "to" units
    from_unit = st.selectbox("From Unit", available_units)
    to_unit = st.selectbox("To Unit", available_units)

    # Create an input box for entering the value to be converted
    input_value = st.number_input("Input Value", value=1.0)

    # Create a button for performing the conversion
    if st.button("Convert"):
        # Perform the conversion and display the result
        try:
            result = converter.convert(
                selected_quantity, input_value, from_unit, to_unit
            )
            st.write(f"{input_value} **{from_unit}** = {result} **{to_unit}**")
        except Exception as e:
            st.write(f"Error: {e}")


if __name__ == "__main__":
    main()
