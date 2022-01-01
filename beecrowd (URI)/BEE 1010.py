product_code,product_units,product_price  = input().split()
a = int(product_code)
b = int(product_units)
c = float(product_price)
value_to_pay1 = b * c
product_code,product_units,product_price  = input().split()
d = int(product_code)
e = int(product_units)
f = float(product_price)
value_to_pay = e * f
g = value_to_pay + value_to_pay1
print("VALOR A PAGAR: R$ %.2f"%g)
