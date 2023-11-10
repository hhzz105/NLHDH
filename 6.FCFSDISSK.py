# Python program to demonstrate
# FCFS Disk Scheduling algorithm



def FCFS(arr, head):

	seek_count = 0
	distance, cur_track = 0, 0

	for i in range(size):
		cur_track = arr[i]

		# calculate absolute distance
		distance = abs(cur_track - head)

		# increase the total count
		seek_count += distance

		# accessed track is now new head
		head = cur_track
	
	print("Total number of seek operations = ",
								seek_count)

	# Seek sequence would be the same
	# as request array sequence
	print("Seek Sequence is", arr)

	# for i in range(size):
	# 	print(arr[i])
	
# Driver code
if __name__ == '__main__':

	# request array
	# [100,10,40,150,130,2,68,70,180,160,63] 
	# [98,183,37,122,14,124,65,67]
	# [122,14,124,65,98,185,37,67]
	arr = [122,14,124,65,98,185,37,67]
	head = 53
	size = len(arr)

	FCFS(arr, head)

# This code contributed by Rajput-Ji
