# Python3 implementation of FIFO page
# replacement in Operating Systems.
from queue import Queue


def pageFaults(pages, n, capacity):
	s = set()
	indexes = Queue()

	page_faults = 0
	for i in range(n):
		if (len(s) < capacity):
			if (pages[i] not in s):
				s.add(pages[i])
				page_faults += 1
				indexes.put(pages[i])
		else:
			if (pages[i] not in s):
				val = indexes.queue[0]

				indexes.get()
				s.remove(val)
				s.add(pages[i])
				indexes.put(pages[i])
				page_faults += 1

	return page_faults
# [0, 1, 2, 1, 3, 4, 2, 3, 0, 1, 0, 3, 5, 2, 3, 1, 0, 2, 0, 1, 6, 2, 3, 1]
# [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
# [1,2,3,1,4,5,3,1,4,3,1,2,3,4,3,1,6,2]
if __name__ == '__main__':
	pages = [1,2,3,1,4,5,3,1,4,3,1,2,3,4,3,1,6,2]
	n = len(pages)
	capacity = 3
	print("So trang loi FIFO: ",pageFaults(pages, n, capacity))


