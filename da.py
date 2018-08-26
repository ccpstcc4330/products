#載入作業系統來檢查檔案在不在
import os


def read_file():
	products =[] #在最外面是因為動作一定要做
	#讀取檔案
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			products.append([name,price])
	return products #回傳並儲存

def user_input(products):
	#讓使用者輸入
	while True: 
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

def print_products(products):
	#列出商品明細
	for p in products:
		print(p[0], '的價格是:' , p[1], '元')

def write_file(filename, products):
	#寫入檔案
	with open(filename, 'w', encoding='utf-8') as f: 
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')



def main():
	products =[]
	filename = 'produtct.csv'
	if os.path.isfile(filename):#os.path 是標準函式庫裡的模組:os這個模組裡面的PATH的ISFILE功能
		print('yes!')
		products = read_file(filename)
	else:
		print('oops, no...')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()