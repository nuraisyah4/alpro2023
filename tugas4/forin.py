

if  __name__ ==  "__main__":
	tinggi = int(input('masukkan tinggi:'  ))
	
	for x in range(tinggi):
		for y in range(x, tinggi):
			print('*', end='')
		print()
		
	print('selesai')  
