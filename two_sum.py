# Two-Sum

def two_sum(arr, target):
	left = 0
	right = len(arr) -1

	while left < right:
		current_sum = arr[left] + arr[right]

		if current_sum == target:
			return left, right
		elif current_sum < target:
			left +=1
		else:
			right -=1


if __name__ == "__main__":
	arr = [22, 13, 34, 45, 66, 75, 86]

	target = 79

	print(two_sum(arr,target))