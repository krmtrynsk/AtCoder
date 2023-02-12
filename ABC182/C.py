N=input()
d=len(N)
ans=100

for num in range(1<<d):
	N_tmp=""
	ans_tmp=0
	
	for shift in range(d):
		if 1 & num>>shift ==1:
			N_tmp+=N[shift]
			
		else:
			#消した数字の個数をカウントする
			ans_tmp+=1
	
	if N_tmp=="":
		continue
		
	if int(N_tmp)%3==0:
		ans=min(ans,ans_tmp)
		
if ans==100:
	print(-1)
else:
	print(ans)