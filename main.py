#........ and shoot for the Sky in you getting a big promotion & opportunity
#Enter Full Names
print("Enter First and Last Name")
fname = input("fname")              #First Name
lname = input("lname")              #last Name
fullnames = fname + " " + lname
#Enter phone, email
print('Enter Customers Phone Number: ')
phone = input("phone")
print('Enter Customers email address: ')
email = input ("email")
#price of a used car
price = input('10000')
has_good_credit = True
if has_good_credit:
 down_payment = 0.1 * float('price')
else:
 down_payment = 0.2 * float('price')
print("fDown Payment: {down_payment}")
print('')
print("FullNames:" + fullnames)
print('Phone Number: '+ phone)
print("Email: " + email)
print("down_payment:" +str("down_payment"))
