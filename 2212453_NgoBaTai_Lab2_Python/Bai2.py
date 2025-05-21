class PhanSo:
	def __init__(self, tu: int, mau: int) -> None:
		self.tu = tu
		self.mau = mau

	@staticmethod
	def tim_uoc_chung(a: int, b: int) -> int:
		while b != 0:
			a, b = b, a % b
		return a
            
	def rut_gon(self):
		i = self.tim_uoc_chung(abs(self.tu), abs(self.mau))
		self.tu //= i  
		self.mau //= i  
		if self.mau < 0:  
			self.tu = -self.tu
			self.mau = -self.mau

	def __str__(self):
		return f"{self.tu}/{self.mau}"

	def __add__(self, other):
		tu = self.tu * other.mau + other.tu * self.mau
		mau = self.mau * other.mau
		ketqua = PhanSo(tu, mau)
		ketqua.rut_gon()
		return ketqua

	def __sub__(self, other):
		tu = self.tu * other.mau - other.tu * self.mau
		mau = self.mau * other.mau
		ketqua = PhanSo(tu, mau)
		ketqua.rut_gon()
		return ketqua

	def __mul__(self, other):
		tu = self.tu * other.tu
		mau = self.mau * other.mau
		ketqua = PhanSo(tu, mau)
		ketqua.rut_gon()
		return ketqua

	def __truediv__(self, other):
		other = PhanSo(other.mau, other.tu)
		return self*other

class DanhSachPhanSo:
	def __init__(self):
		self.dsps = []
	
	def themPhanSo(self, ps: PhanSo) -> None:
		self.dsps.append(ps)
	
	def xuat(self):
		for ps in self.dsps:
			print(ps)
	
	def demPSAm(self) -> int:
		count = 0
		for ps in self.dsps:
			if(ps.tu < 0 or ps.mau < 0):
				count+= 1
		return count
	
	def timPSDuongMin(self) -> PhanSo:
		phan_so_duong = [ps for ps in self.dsps if ps.mau > 0 and ps.tu > 0]

		if not phan_so_duong:
			return None
		
		min_ps = min(phan_so_duong, key = lambda ps: ps.tu / ps.mau)
		# min = PhanSo(0,0)
		# for ps in self.dsps:
		# 	if (ps.tu > 0 and ps.mau > 0):
		# 		min = ps
		# 		break

		# for ps in self.dsps:
		# 	if(ps.tu < 0 or ps.mau < 0):
		# 		continue
		# 	elif(min.tu / min.mau > ps.tu / ps.mau):
		# 		min = ps
		return min_ps
	
	def timVTPSX(self, other):
		# ket_qua = []
		# for i in range(len(self.dsps)):
		# 	if self.dsps[i].tu == other.tu and self.dsps[i].mau == other.mau:
		# 		ket_qua.append(i)
		return [i for i, ps in enumerate(self.dsps) if ps.tu == other.tu and ps.mau == other.mau]
	
	def tongPSAm(self) -> PhanSo:
		ket_qua = PhanSo(0, 1)  
		phan_so_am = [ps for ps in self.dsps if ps.tu < 0 and ps.mau > 0]  
		for ps in phan_so_am:
			ket_qua += ps  
		return ket_qua
	
	def xoaPS(self, vt: int):
		if vt != 1:
			del self.dsps[vt]
			return True
		else:
			return False
		
	def sap_xep(self, key_func, reverse=False):
		return sorted(self.dsps, key=key_func, reverse=reverse)
	
	# def sap_xep_tang_giam(self):
	# 	print("Sắp xếp tăng dần theo giá trị:")
	# 	self.sap_xep(key_func=lambda ps: ps.tu/ps.mau)
	# 	self.xuat()

	# 	print("Sắp xếp giảm dần theo giá trị:")
	# 	self.sap_xep(key_func=lambda ps: ps.tu/ps.mau, reverse=True)

	# 	print("Sắp xếp tăng dần theo tử số:")
	# 	print(self.sap_xep(key_func=lambda ps: ps.tu))

	# 	print("Sắp xếp giảm dần theo tử số:")
	# 	print(self.sap_xep(key_func=lambda ps: ps.tu, reverse=True))

	# 	print("Sắp xếp tăng dần theo mẫu số:")
	# 	print(self.sap_xep(key_func=lambda ps: ps.mau))

	# 	print("Sắp xếp giảm dần theo mẫu số:")
	# 	print(self.sap_xep(key_func=lambda ps: ps.mau, reverse=True))

