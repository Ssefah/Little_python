from secrets import compare_digest
password=(input(("Enter password:")))
valid=compare_digest(password,"ssefah524")
if valid== True:
    print("Access Granted")
else:
    print("Access Denied")