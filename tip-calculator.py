print('========================================')
print('             Tip calculator             ')
print('========================================')
bill_amount = input('Bill Amount (R): R')
bill_percentage = input('Tip Percentage(%): ')
tip_amount = int(bill_percentage)/100 * int(bill_amount)
total_bill = int(bill_amount) + int(tip_amount)

print (f'Your Tip Amount is R{tip_amount} ')
print('========================================')
print(f'The Total For Your Bill Is R{total_bill}.')
print('Thank You!💖')
print('========================================')


