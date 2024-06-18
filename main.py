start = int(input("Enter start : "))

end = int(input("Enter end: "))

sum_even = 0

count_even = 0

sum_odd = 0

count_odd = 0

sum_multiple_of_9 = 0

count_multiple_of_9 = 0

for num in range(start, end + 1):

   if num % 2 == 0:

       sum_even += num

       count_even += 1

   else:

       sum_odd += num

       count_odd += 1

   

   if num % 9 == 0:

       sum_multiple_of_9 += num

       count_multiple_of_9 += 1

average_even = sum_even / count_even if count_even > 0 else 0

average_odd = sum_odd / count_odd if count_odd > 0 else 0

average_multiple_of_9 = sum_multiple_of_9 / count_multiple_of_9 if count_multiple_of_9 > 0 else 0
print("sum of even numbers :", sum_even)
print("Arithmetic mean of even numbers :", average_even)
print("The sum of odd numbers :", sum_odd)
print("Arithmetic mean of odd numbers :", average_odd)
print("The sum of numbers that are multiples of 9 :", sum_multiple_of_9)
print("Arithmetic average of numbers that are multiples of 9 :", average_multiple_of_9)