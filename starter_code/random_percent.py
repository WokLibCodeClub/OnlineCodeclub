from random import randint

# function to generate return True or False
def random_percent(p):
  if randint(1, 100) <= p:
    return True
  else:
    return False

# set the percent of True returns
percent_true = 50

# set the number of times to test the function
number_of_tests = 100

# variable to count the number of True returns
true_count = 0

# loop to do many tests of the function
for _ in range(number_of_tests):
  if random_percent(percent_true):
    true_count += 1
    
# print the results to the Result window
print("Number returned true: ", true_count)
print("Percent returned true: ", true_count/number_of_tests * 100, "%")
