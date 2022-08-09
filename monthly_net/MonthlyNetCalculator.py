TOTAL_ZUS_RATE = 0.1371
HEALTH_RATE = 0.09
ANNUAL_THRESHOLD = 120000
TAX_RATE_17 = 0.0832
TAX_RATE_32 = 0.1432
MONTH = 12


def calculate_total_zus(monthly_gross):
    return monthly_gross - monthly_gross * TOTAL_ZUS_RATE


def calculate_health(monthly_gross):
    return calculate_total_zus(monthly_gross) - (calculate_total_zus(monthly_gross) * HEALTH_RATE)


def calculate_net(monthly_gross):
    health = calculate_health(monthly_gross)
    if monthly_gross * MONTH < ANNUAL_THRESHOLD:
        return health - (health * TAX_RATE_17)
    else:
        return health - (health * TAX_RATE_32)
