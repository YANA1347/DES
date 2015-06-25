#encoding:utf-8

#初始置换表
IP_Table = (
	58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
)

#逆初始置换表
IPR_Table = (
	40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
	38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
	34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41,  9, 49, 17, 57, 25
)

#扩展置换表
Extension_Table = (
	32,  1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9,
	 8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
	16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
	24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32,  1
)

#P盒置换表
P_Table = (
	16, 7, 20, 21, 29, 12, 28, 17, 1,  15, 23, 26, 5,  18, 31, 10,
	2,  8, 24, 14, 32, 27, 3,  9,  19, 13, 30, 6,  22, 11, 4,  25
)

#密钥置换表 
PCK_Table = (
	57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
	10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
	63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
	14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4
)

#压缩置换表 
PCC_Table = (
	14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
	23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
	41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
	44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
)

#每轮移动的位数 
LOOP_Table = (
	1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1
)

#S盒设计
S_Box = (
	#S盒1 
	((14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7),
	 ( 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8),
	 ( 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0),
     (15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13)),
	#S盒2 
    ((15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10),
	 ( 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5),
	 ( 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15),
     (13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9)),
	#S盒3 
    ((10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8),
	 (13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1),
	 (13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7),
     ( 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12)),
	#S盒4 
    (( 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15),
	 (13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9),
	 (10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4),
     ( 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14)),
	#S盒5 
    (( 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9),
	 (14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6),
	 ( 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14),
     (11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3)),
	#S盒6 
    ((12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11),
	 (10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8),
	 ( 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6),
     ( 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13)),
	#S盒7 
    (( 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1),
	 (13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6),
	 ( 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2),
     ( 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12)),
	#S盒8 
    ((13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7),
	 ( 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2),
	 ( 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8),
     ( 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11))
)


#字节转换函数
def ByteToBit(In, bits):
	tempbit=[]
	out=[]
	for x in xrange(bits):
		tempbit.append((ord(In[x>>3])>>(x&7))&1)
	for x in xrange(len(tempbit)):
		out.insert(0+8*(x/8), tempbit[x])
	return out

#比特转换函数
def BitToByte(In, bits):
	tempbit=[0]*(bits/8)
	out=[]
	for x in xrange(bits):
		tempbit[x>>3]+=In[x]*(2**(7-(x&7)))
	for x in xrange(len(tempbit)):
		out.append(chr(tempbit[x]))
	return out

#pc-1置换
def pc_1(key, temp):
	for x in xrange(56):
		temp.append(key[PCK_Table[x]-1])

#循环左移
def rol(temp, number):
	for x in xrange(number):
		a=temp[0]
		b=temp[28]
		temp.pop(0)
		temp.insert(27, a)
		temp.pop(28)
		temp.append(b)

#pc-2压缩置换
def pc_2(temp, keys):
	tempbit=[]
	for x in xrange(48):
		tempbit.append(temp[PCC_Table[x]-1])
	keys.append(tempbit)

#生成子密钥
def sub_keys(key):
	temp=[]
	keys=[]
	pc_1(key, temp)
	for x in xrange(16):
		rol(temp, LOOP_Table[x])
		pc_2(temp, keys)
	return keys

#IP置换
def ip_transform(data):
	ip=[]
	for x in xrange(64):
		ip.append(data[IP_Table[x]-1])
	return ip

#ip逆置换
def ip_1_transform(data):
	ip_1=[]
	for x in xrange(64):
		ip_1.append(data[IPR_Table[x]-1])
	return ip_1

#扩展置换
def e_transform(data):
	e=[]
	for x in xrange(48):
		e.append(data[Extension_Table[x]-1])
	return e

#异或
def xor(dataL, dataR):
	for x in xrange(len(dataL)):
		dataL[x]^=dataR[x]
	return dataL

#s盒置换
def s_transform(data, i):
	c=[]
	row=data[0]*2+data[5]
	column=data[1]*(2**3)+data[2]*(2**2)+data[3]*2+data[4]
	s=S_Box[i][row][column]
	for x in xrange(4):
		c.insert(0, s%2)
		s/=2
	return c

#p置换
def p_transform(data):
	p=[]
	for x in xrange(32):
		p.append(data[P_Table[x]-1])
	return p

#交换
def swap(dataL, dataR):
	return dataR, dataL

#加密
def Encrypt(data):
	L=[]
	R=[]
	keys=sub_keys(key)
	data=ip_transform(data)
	for x in xrange(32):
		L.append(data[x])
		R.append(data[x+32])
	r=[]
	for x in xrange(16):
		r=R
		R=e_transform(R)
		R=xor(R, keys[x])
		c=[]
		for y in xrange(8):
			tempbit=[]
			for i in xrange(6):
				tempbit.append(R[y*6+i])
			C=s_transform(tempbit, y)
			for j in xrange(4):
				c.append(C[j])
		R=c
		R=p_transform(R)
		L=xor(L, R)
		if x!=15:
			L, R=swap(L, r)
	for x in xrange(32):
		L.append(r[x])
	data=ip_1_transform(L)
	return data

#解密
def Decrypt(data):
	L=[]
	R=[]
	keys=sub_keys(key)
	data=ip_transform(data)
	for x in xrange(32):
		L.append(data[x])
		R.append(data[x+32])
	r=[]
	for x in xrange(16):
		r=R
		R=e_transform(R)
		R=xor(R, keys[15-x])
		c=[]
		for y in xrange(8):
			tempbit=[]
			for i in xrange(6):
				tempbit.append(R[y*6+i])
			C=s_transform(tempbit, y)
			for j in xrange(4):
				c.append(C[j])
		R=c
		R=p_transform(R)
		L=xor(L, R)
		if x!=15:
			L, R=swap(L, r)
	for x in xrange(32):
		L.append(r[x])
	data=ip_1_transform(L)
	return data

keysour=raw_input('what is the key?')
key=ByteToBit(keysour, 8*len(keysour))
data=raw_input('Please input:')
IN_data=ByteToBit(data, 8*len(data))
C=Encrypt(IN_data)
out_E=BitToByte(C, len(C))
M=Decrypt(C)
out_D=BitToByte(M, len(M))
print  C,'\n', out_D