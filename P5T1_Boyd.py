# CTI 110
# P5T1 - Functions
# boydj
# 10/24

def main():
  print("Hello world!")
  burger = 4.999
  print_money(burger)
  print_money(12)
  print_money(0.3)
# main() ends

# other functions go here
def print_money(amount):
  print("$", format(amount, ".2f"), sep="")



# Now, start the program
main()