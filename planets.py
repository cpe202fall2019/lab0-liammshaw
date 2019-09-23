def weight_on_planets():
   # write your code here

   weight = input("what is your weight on earth? ")
   weight = float(weight)
   jupiterWeight = weight * 2.34
   marsWeight = weight * 0.38
   print('\nYour weight on mars is %.2f' % (marsWeight), '\nYour weight on jupiter is %.2f' % (jupiterWeight))


if __name__ == '__main__':
   weight_on_planets()