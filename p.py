#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品, 價格' in line:
			continue #繼續
		name , price = line.strip().split(',') #先把換行符號去除，再用逗點當作切割的標準
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	p = []
	p.append(name) #小清單
	p.append(price)	#小清單
	#也可以將7-9行直接縮成: p = [name, price]
	products.append(p) #大清單 (小清單中裝入大清單)
	#又或者直接縮成products.append([name, price])
print(products)

# products[0][0] #大清單的第0格，小清單的第0格

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是$', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: 
#寫入模式，所以沒有products.txt也沒關係
# 修正亂碼問題，要加encoding = 'utf-8'，讓語言可被讀取
#用csv存取檔案，可以用excel開啟(直接開excel中文字跑不出，所以:
#資料-取得外部資料-從文字檔選UTF-8。分隔符號用逗點)
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) +'\n') #字串可以做 + 跟 *
# 但是＋只能用在字串加字串，或者整數加整數。所以利用str轉成字串
