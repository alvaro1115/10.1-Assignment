import os

directory = input("Please enter a directory to save the file in: ")
while True:
    if os.path.isdir(directory):
        print('The directory was found.')
    else:
        print ("The directory was not found. Please try again.")
    break

fileName = input("Please enter the file name: ")
name = input("Please enter your name: ")
address = input("Please enter your address: ")
phoneNumber = input("Please enter your phone number: ")

with open("{}/{}.csv".format(directory, fileName), 'w') as file:
  file.write(",".join([name, address, phoneNumber]) + "n")

with open("{}/{}.csv".format(directory, fileName), 'r') as file:
  print("{}/{}.csv contents".format(directory, fileName))
  for line in file:
    print(line)