print "Welcome:"
print "1. Returning Customer"
print "2. New Customer"
print "3. Guest"

choice = raw_input("Please enter a number: ")

if choice == '1':
    print"Returning Customer"
elif choice == '2':
    print "New Customer"
elif choice == '3':
    print "Guest"
else:
    print "ERROR: Not Valid"
