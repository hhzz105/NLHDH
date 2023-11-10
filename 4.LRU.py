
capacity = 3
# processList = [ 7, 0, 1, 2, 0, 3, 0,
# 				4, 2, 3, 0, 3, 2]
# Bài 16: [0, 1, 2, 1, 3, 4, 2, 3, 0, 1, 0, 3, 5, 2, 3, 1, 0, 2, 0, 1, 6, 2, 3, 1]
# Bài 12: [1,2,3,2,4,1,2,3,0,3,1,5,7,1,3,2,1,2,4,5]	
processList = 	[1,2,3,1,4,5,3,1,4,3,1,2,3,4,3,1,6,2]
s = []

pageFaults = 0
# pageHits = 0

for i in processList:
	if i not in s:
		if(len(s) == capacity):
			s.remove(s[0])
			s.append(i)
		else:
			s.append(i)
		pageFaults +=1
	else:
		s.remove(i)
		s.append(i)
	
print("So trang loi LRU: {}".format(pageFaults))

