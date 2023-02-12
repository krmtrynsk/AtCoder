# 一行だけ取る
　# input: string
　s = input() # s="abcde"
　
　# input: list
　s = list(input()) # s = ['a','b','c','d','e']
　
　# input: int
　i = int(input()) # i = 5
　
　# input: int型の数字２つ
　x,y = map(int, input().split()) # x=1,y=2
　
　# input: list:int
　li = input().split() # li=[1,2,3,4,5.....]
　
　# 区切り文字指定 input: "FFFTFFTFT"
　li = input().split('T') # li=["FFF","FF","F"]
　
#複数行を取る
	#パターン1
	#input
	#3
	#hoge
	#foo
	#bar
	n=int(input())
	string_list=[input() for i in range(n)]
	
	#パターン2
	#12231
	#23131452453
	#42525
	#一行だけで処理できるなら
	while True:
		try:
			listA=list(map(int,input().split()))
			#listA<-[1,2,2,1,2,1,2]
			#ここに逐次処理を書けばいいと思う
		except:
			break;
		
	#複数行全て集めて処理するときは
	listA = []
	while True:
		try:
			listA.append(list(map(int,input().split())))
		except:
			break;
			
	print(listA)
	
#出力
	print(s) 				#hogehoge\n
	print(s,end='') #hogehoge
	

#ゼロ埋め・幅寄せ
	print("python".ljust(15,'-'))
	#python---------
	print("python".center(15,'_'))
	#-----python----
	print("python".rjust(15,'-'))
	#---------python
	
	print(str(29).rjust(10,'0'))
	#0000000029
	
#二分探索
	import bisect
	listA.[1,2,3,3,4,65,5,5,3,34,0,0,0,0,0,-1,34,24,324,2,34]
	#降順ソート
	listA.sort()
	#ソートされたリスト内で0の場所を探し、右側Indexを返す
	zeroindex=bisect.bisect_right(listA,0)
	#0以下が存在しないリストを得る 
	clearlistA=listA[zeroindex:]
	
#文字列操作
	'abc123def'[:] #全ての文字列が取れる
	
	'abc123def'[-1:] #終端の文字が取れる(f)
	
	'abc123def'[:-1] #最後の一文字以外のものが取れる。
	
	'abc123def'[::-1] #文字が逆転する
	
	# 配列について
	# [start:stop]という感じで書く
	# start <= x < stop の範囲が適用される
	# 開始位置を省略すると先頭から。終了位置を省略すると末尾までが選択される。
	# [::ステップ数] ステップ数がマイナスの場合逆順で進んでいく
	# [::-1]の時は、リストが逆順になる
	