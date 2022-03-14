from piGen import piNums

p1name = str(input("First player name:"))
p2name = str(input("Second player name:"))

print("Let's gooooo!!")

def play(p1name,p2name):
	pi1 = input(p1name+", input as many characters of pi as you can")
	pi2 = input(p2name+", your turn!")

	pi1Nums=[]
	pi2Nums=[]

	for i in range(len(pi1)):
		if pi1[i]==piNums[i]:
			pi1Nums.append(pi1[i])
		else: 
			break
	for i in range(len(pi2)):
		if pi2[i]==piNums[i]:
			pi2Nums.append(pi2[i])
		else:
			break

	if len(pi1Nums)==0:
		print(p1name+" you should start with 3.14...")
		play(p1name,p2name)
	if len(pi2Nums)==0:
		print(p2name+" you should start with 3.14...")
		play(p1name,p2name)

	if len(pi1Nums)>len(pi2Nums):
		print(p1name+" WINS!!!")
	elif len(pi2Nums)>len(pi1Nums):
		print(p2name+" WINS!!!")
	else:
		print("dam, it's a tie.")


play(p1name,p2name)