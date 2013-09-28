from inori.validator import is_password

a = ['aa', 'a123', 'Aa241', 'a79214', 'abcdegefda', '1312512512312', 'fty19910720', 'M07y02h1991']

for b in a:
    print b
    print is_password(b)
