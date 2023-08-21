def str_manipulation(input_string):
    return input_string.lower().strip()


class UnitConverter:
    conversion_factors = {
        "mass": {
            "kg": 1.0,
            "gr": 1e-3,
            "lb": 0.45359237,
            "metric-ton": 1e3,
            "ton": 907.18474,
        },
        "volume": {
            "m3": 1.0,
            "e3m3": 1e3,
            "e6m3": 1e6,
            "us-gal": 3.785411784e-3,
            "bbl": 1.589872949e-1,
            "mbbl": 1.589872949e2,
            "mmbbl": 1.589872949e5,
            "scf": 2.831684659e-2,
            "mscf": 2.831684659e1,
            "mmscf": 2.831684659e4,
            "bscf": 2.831684659e7,
        },
        "energy": {
            "j": 1.0,
            "kj": 1e3,
            "mj": 1e6,
            "gj": 1e9,
            "cal": 4.184,
            "kcal": 4184.0,
            "btu": 1055.06,
            "mm-btu": 1.05506e9,
            "wh": 3600.0,
            "kwh": 3.6e6,
            "mwh": 3.6e9,
            "therm": 1.055e8,
        },
        "length": {
            "m": 1.0,  # meters
            "km": 1e3,  # kilometers
            "cm": 1e-2,  # centimeters
            "mm": 1e-3,  # millimeters
            "ft": 0.3048,  # feet
            "in": 0.0254,  # inches
            "yd": 0.9144,  # yards
            "mi": 1609.34,  # miles
            "nmi": 1852.0,  # nautical miles
            "fathom": 1.8288,  # fathoms
            "rod": 5.0292,  # rods
        },
        "pressure": {
            "kpa": 1.0,
            "psia": 6.89475729316836,
            "mpa": 1e3,
            "bar": 1e2,
            "atm": 101.325,
            "mmhg": 0.133322368421053,
            "inh2o": 0.24884,
            "inhg": 3.386389e1,
        },
        "temperature": {
            "degc": [0.0, 1.0],
            "degk": [-273.15, 1.0],
            "degf": [-32.0, 5.0 / 9.0],
            "degr": [-491.67, 5.0 / 9.0],
        },
    }

    def convert(self, quantity, input_value, from_unit, to_unit):
        quantity = str_manipulation(quantity)
        from_unit = str_manipulation(from_unit)
        to_unit = str_manipulation(to_unit)

        if quantity not in self.conversion_factors.keys():
            return "Invalid property type"

        conversion_data = self.conversion_factors[quantity]

        if quantity == "temperature":
            constant, multiplier = conversion_data[from_unit]
            converted_value = (input_value + constant) * multiplier
            constant, multiplier = conversion_data[to_unit]
            return (converted_value / multiplier) - constant

        converted_value = (
            input_value * conversion_data[from_unit] / conversion_data[to_unit]
        )
        return converted_value


if __name__ == "__main__":
    input_temperature_val = 560.0
    from_unit = "degk"
    to_unit = "degr"
    unit_converter = UnitConverter()
    output_temperature_val = unit_converter.convert(
        "temperature", input_temperature_val, from_unit, to_unit
    )
    print(
        f"Temperature => {input_temperature_val:.2f} {from_unit} = {output_temperature_val:.3f} {to_unit}"
    )
