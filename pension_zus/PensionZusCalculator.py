PENSION_ZUS_RATE = 0.0976


def calculate_pension_zus(monthly_gross):
    return monthly_gross * PENSION_ZUS_RATE
