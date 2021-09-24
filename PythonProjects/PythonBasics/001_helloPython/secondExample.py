#just another example of the book
import time, locale

name = input('Geben Sie Ihren Namen an: ')
print('Hallo %s' % name)

#local date and time
locale.setlocale(locale.LC_ALL,'')
time = time.strftime('Heute ist %A, der %d. %B.')
print(time)