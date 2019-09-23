def weight_on_planets():
   # write your code here

   weight = input("What do you weigh on earth? ")
   weight = float(weight)
   jupiterWeight = weight * 2.34
   marsWeight = weight * 0.38
   print('\nOn Mars you would weigh %.2f pounds.' % (marsWeight), '\nOn Jupiter you would weigh %.2f pounds.' % (jupiterWeight))


if __name__ == '__main__':
   weight_on_planets()