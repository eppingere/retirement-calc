#!/usr/bin/env python3

# current tax rates for individual (https://taxfoundation.org/2021-tax-brackets/)
TAX_RATES = [
    (9950, 0.10),
    (40525, 0.12),
    (86375, 0.22),
    (164925, 0.24),
    (209425, 0.32),
    (523600, 0.35),
    (float("inf"), 0.37)
]

YOUR_TAXABLE_INCOME = int(input("taxable income this year (dollars): "))
# how many years till retirement
# avg investment gains over the last 100 years (S&P 500)
EXPECTED_INVESTMENT_RATE = 0.08
LIMIT_CONTRIBUTION = int(input(
    "how much do you plan on contributing to retirement this year (dollars, max $19500): "))
YEARS_TO_WITHDRAWL = int(
    input("how long until you plan on retiring (years): "))

# i used: https://www.blueprintincome.com/tools/life-expectancy-calculator-how-long-will-i-live/
NUMBER_OF_YEARS_LIVE_ON_RETIREMENT = int(
    input("how long do you expect on live after you retire (years): "))

<<<<<<< HEAD
CURRENT_401k_VALUE = int(
    input("what is the current value of your 401k (dollars): "))

=======
>>>>>>> aa365264a8cdeab53ab0fb1377c4033cc15b317c
# my guess at the highest taxes can be in the future (feel free to make them lower) if you think that taxes will different in the future
WITHDRAWL_GAINS_TAX_RATE = 0.2  # future capital gains tax?
FUTURE_TAX_RATES = [
    (9950 * (1.02 ** YEARS_TO_WITHDRAWL), 0.10),
    (40525 * (1.02 ** YEARS_TO_WITHDRAWL), 0.12),
    (86375 * (1.02 ** YEARS_TO_WITHDRAWL), 0.22),
    (164925 * (1.02 ** YEARS_TO_WITHDRAWL), 0.30),
    (209425 * (1.02 ** YEARS_TO_WITHDRAWL), 0.38),
    (523600 * (1.02 ** YEARS_TO_WITHDRAWL), 0.41),
    (float("inf") * (1.02 ** YEARS_TO_WITHDRAWL), 0.43)
]


def compute_income_tax(income, rates=TAX_RATES):
    post_tax_dollars = 0.0
    tax_paid = 0.0
    income_processed = 0.0

    for inc, rate in rates:
        taxable_at_level = min(income, inc) - income_processed

        post_tax_dollars += taxable_at_level * (1.0 - rate)
        tax_paid += taxable_at_level * rate
        income_processed += taxable_at_level

        if inc >= income:
            break

    return (post_tax_dollars, tax_paid)


def _401k_income():
    # 401k contributions dont count towards taxable income
    return YOUR_TAXABLE_INCOME - compute_income_tax(YOUR_TAXABLE_INCOME - LIMIT_CONTRIBUTION)[1]


def roth_income():
    # roth is contributed from post tax dollars
    return YOUR_TAXABLE_INCOME - compute_income_tax(YOUR_TAXABLE_INCOME)[1]


def roth_performance():
    # the extra tax you have to pay because you have higher tax basis
    cost = _401k_income() - roth_income()
    gains = LIMIT_CONTRIBUTION * \
        ((1 + EXPECTED_INVESTMENT_RATE) ** YEARS_TO_WITHDRAWL)

    return (gains, cost)


def _401k_performance():
    _401k_gains = LIMIT_CONTRIBUTION * \
        ((1 + EXPECTED_INVESTMENT_RATE) ** YEARS_TO_WITHDRAWL)

    # this computes the amount of tax you pay
    # worst case if you only invest in 401k at the same level every year (scaled for inflation)
    total_expected_401k = sum((LIMIT_CONTRIBUTION * (1.02 ** (YEARS_TO_WITHDRAWL - i))) *
                              ((1 + EXPECTED_INVESTMENT_RATE) ** i) for i in range(YEARS_TO_WITHDRAWL))

<<<<<<< HEAD
    total_expected_401k += CURRENT_401k_VALUE * \
        ((1 + EXPECTED_INVESTMENT_RATE) ** YEARS_TO_WITHDRAWL)

=======
>>>>>>> aa365264a8cdeab53ab0fb1377c4033cc15b317c
    # you withdraw the same amount every year of retirement (plus 10 that your heirs can withdraw)
    annual_withdrawl = total_expected_401k / \
        (NUMBER_OF_YEARS_LIVE_ON_RETIREMENT + 10)

    # you pay income taxes on the amount you withdraw every year
    tax_rate_on_401k_gains = compute_income_tax(
        annual_withdrawl, rates=FUTURE_TAX_RATES)[1] / annual_withdrawl

    print("max (worst case) tax rate on 401k withdrawl: {}%, expected annual withdrawl (pre taxes): ${}".format(
        round(tax_rate_on_401k_gains * 100, 2), round(annual_withdrawl)))

    tax_on_401k_gains = _401k_gains * tax_rate_on_401k_gains

    # tax_on_401k_gains = _401k_gains * WITHDRAWL_INCOME_TAX_RATE

    extra_income = _401k_income() - roth_income()

    extra_income_gains = extra_income * \
        ((1 + EXPECTED_INVESTMENT_RATE) ** YEARS_TO_WITHDRAWL)

    tax_on_extra_income_gains = WITHDRAWL_GAINS_TAX_RATE * \
        (extra_income_gains - extra_income)

    return (_401k_gains + extra_income_gains, tax_on_401k_gains + tax_on_extra_income_gains)


def no_retirement_performance():

    income_tax = _401k_income() - roth_income()

    gains = LIMIT_CONTRIBUTION * \
        ((1 + EXPECTED_INVESTMENT_RATE) ** YEARS_TO_WITHDRAWL)

    tax_on_gains = WITHDRAWL_GAINS_TAX_RATE * (gains - LIMIT_CONTRIBUTION)

    return (gains, income_tax + tax_on_gains)


def main():

    options = {
        "401k/IRA": _401k_performance,
        "Roth 401k": roth_performance,
        "None (invest on your own)": no_retirement_performance
    }

<<<<<<< HEAD
    print()
=======
>>>>>>> aa365264a8cdeab53ab0fb1377c4033cc15b317c
    print("These are the expected performance of this years retirement investment")
    for option in options:
        print(option + ":")
        gains, cost = options[option]()

        gains = round(gains)
        cost = round(cost)
        print("gains (value of investment at retirement): ${}, cost (income and gains tax paid): ${}, total benefit: ${}\n".format(
            gains, cost, gains - cost))


if __name__ == "__main__":
    main()
