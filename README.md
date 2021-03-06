# retirement-calc
A simple python tool to decide whether to do a Roth or 401k this year

To use:
```
$ python3 retirement_calculator.py
```

Based on a few assumptions that in the future taxes are as follows:
* capital gains tax is `15%` when you retire
* tax rates go up `6%` for the top `4` tax brackets and the cutoffs scale by `2%` per year with inflation in the year you retire
* when considering the 401k option it assumes that you continuously choose 401k until retirement (to compute largest possible taxed withdrawl at retirement)


Example:

```
bezos@aws $ python3 retirement_calculator.py
taxable income this year (dollars): 1680000
how much do you plan on contributing to retirement this year (dollars, max $19500): 19500
how long until you plan on retiring (years): 13
how long do you expect on live after you retire (years): 20
what is the current value of your 401k (dollars): 3000000

These are the expected performance of this years retirement investment
401k/IRA:
max (worst case) tax rate on 401k withdrawl: 27.22%, expected annual withdrawl (pre taxes): $287720
gains (value of investment at retirement): $72655, cost (income and gains tax paid): $16919, total benefit: $55736

Roth 401k:
gains (value of investment at retirement): $53033, cost (income and gains tax paid): $7215, total benefit: $45818

None (invest on your own):
gains (value of investment at retirement): $53033, cost (income and gains tax paid): $13922, total benefit: $39111
```