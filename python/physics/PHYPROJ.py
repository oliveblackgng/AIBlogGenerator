def calculate_bragg_shift(lambda_B, strain, delta_T, p_e=0.22, alpha=0.55e-6, xi=8.6e-6):
    """
    Calculate Bragg wavelength shift due to strain and temperature.

    Parameters:
    - lambda_B: Original Bragg wavelength (in nm)
    - strain: Strain applied (unitless, e.g., 1000 microstrain = 0.001)
    - delta_T: Temperature change (in °C)
    - p_e: Effective strain-optic coefficient (default 0.22)
    - alpha: Thermal expansion coefficient (default 0.55e-6 /°C)
    - xi: Thermo-optic coefficient (default 8.6e-6 /°C)

    Returns:
    - delta_lambda_B: Wavelength shift (in nm)
    """

    strain_term = (1 - p_e) * strain
    temp_term = (alpha + xi) * delta_T
    relative_shift = strain_term + temp_term

    delta_lambda_B = lambda_B * relative_shift
    return delta_lambda_B

# Example usage:
original_lambda = 1550  # nm
strain_applied = 1000e-6  # 1000 microstrain
temperature_change = 20  # °C

shift = calculate_bragg_shift(original_lambda, strain_applied, temperature_change)
print(f"Bragg wavelength shift: {shift:.4f} nm")
    