
my_string = "HeipaMinaOlenAegir!"

my_string = "".join(
        [ i if i.islower() else " " + i.lower()
            if i in ["M", "O"] else " " + i for i in my_string]
        )[1:]
        ## i.lower() -- muudab konditsioonile vastava tähe väikses.
print(my_string)


