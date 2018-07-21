products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name) #小清單
	p.append(price)	#小清單
	#也可以將7-9行直接縮成: p = [name, price]
	products.append(p) #大清單 (小清單中裝入大清單)
	#又或者直接縮成products.append([name, price])
print(products)

# products[0][0] #大清單的第0格，小清單的第0格

for p in products:
	print(p[0], '的價格是$', p[1])