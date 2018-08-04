#Guess My Number Exercise

def main():
	#s = raw_input()
	#your code here
	m_m = 50
	l_l = 0
	h_h = 100
	i_i = 'l'
	g_g = 0
	while (i_i != 'c'):
		print(m_m)
		i_i = input("enter h to guess the number is too high,'l' if number is low 'c' indicate number is correct")
		if(i_i=='h'):
			h_h=m_m
			m_m=(h_h+l_l)//2
		elif(i_i=='l'):
			l_l=m_m
			m_m=(h_h + l_l)//2
	print('guess number is ',m_m)

if __name__== "__main__":
	main()