dict = {}
dict_1 = {}
dict_2 = {}


def add_details_holder():
    ser_3 = int(input("EN SERIAL NO : "))
    mobile_no = int(input("EN MOBILE NO : "))
    email = input("EN EMAIL : ")
    father_n = str(input("EN FATHER NAME : "))
    dict_2.update({ser_3: {mobile_no, email, father_n}})
    front_page()
    # print(dict_2)1


def create_account():
    password__()


def password__():
    serial_no = int(input("EN Account NO : "))
    name = str(input("EN Name : "))
    # print(" 'Name' Cannot be the Integer type, please Re-input the Field\n\n")
    print("Create Password { Only No Input }")
    password = int(input("EN Password : "))
    c_password = int(input("EN Conform-Password : "))
    if password == c_password:
        if len(str(password)) >= 6:
            a = str(password)
            b = str(serial_no)
            dict.update({b: a})
            # print(dict)
            print("\t\t\tPlease Make A Login To Add Minimum Deposit To Bank Account.\n\n")
            login_0()
        else:
            print(
                "\t\t\tDear Sir, Please Make A Password Of More Than 6 Characters.\nPlease Re-Input Credentials.\n\n")
            password__()
    else:
        print("\n\t\t\tPassword Un-Matched!\n\t\t\tRe-Enter Credits\n")
        password__()


def login():
    ser = int(input("EN Account No : "))
    try:
        if len(str(ser)) >= 10 or len(str(ser)) <= 12:
            pas = input("EN Password : ")
            c = str(ser)
            d = str(pas)
            if dict[c] == d:
                print("\n\t\t\t\tCredits Matched !\n")
                print("\t\t\tWelcome, To Your Banking Portal Space\n\n")
                front_page(ser)
            else:
                print("\t\t\tLogin Credentials Un-Matched\n\t\t\tTry-Again\n\n")
                frontpage(ser)
    except:
        print(
            "\t\t\tDear Sir, You Have Entered Incomplete Account No\n\t\t\tOr There Is No Account Exists For Given Credentials.\n\t\t\tKindly Re-Check\n\n  ")
        frontpage()


def login_0():
    print("\t\tBank Login\n")
    ser = int(input("EN Account No : "))
    pas = input("EN Password : ")
    c = str(ser)
    d = str(pas)
    if dict[c] == d:
        print("\n\t\t\t\tCredits Matched !\n")
        print("\t\t\tWelcome, Sir",)
        f_deposit(ser)
    else:
        print("\t\t\tLogin Credentials Un-Matched\n\t\t\tTry-Again\n\n")
        frontpage(ser)


def f_deposit(_a):
    print("Input Deposit Amount : \n{ Min_500_Rs* }\n")
    move_depo = int(input("EN Amount{Rs}: "))
    try:
        if move_depo < 500:
            print("\t\t\tFirst Deposit Should Be More Than Rs.500\n\n")
            f_deposit(_a)
        else:
            print("\n")
            e = str(_a)
            f = str(move_depo)
            dict_1.update({e: f})
            # print(dict_1)
            frontpage()
    except:
        print("\nDear Holder, Enter Valid Amount In (Int)\n\nTry Again\n\n")
        f_deposit(_a)


def deposit(ser):
    depo = int(input("Input Amount To Deposit Rs."))
    # ser_2=int(input("EN SERIAL NO : "))
    i = str(ser)
    j = int(bool(dict_1.get(i)))
    # print(j)
    # first of all it will check whether the serial number is there in bank or not.
    if j == 1:
        k = int(dict_1.get(i))
        depo = depo+k
        dict_1.update({i: depo})
        front_page(ser)
    else:
        print("\t\t\tYou Do Not Have A Account In This Bank Please Create Account To Make Deposit. or Try Again\n\n")
        print("1. Re-Try\n2. Frontpage\n")
        choice_1 = int(input("EN CHOICE : "))
        if choice_1 == 1:
            deposit(ser)
        elif choice_1 == 2:
            front_page(ser)


def withdraw(ser):
    # ser_1=int(input("EN SERIAL NO : "))
    with_draw = int(input("EN Amount TO Withdraw Rs."))
    g = str(ser)
    h = int(dict_1.get(g))
    k = int(bool(dict_1.get(g)))
    print(h)
    if k == 1:
        if h >= with_draw:
            w_d = (h - with_draw)
            print("\t\t\tYou Bank Balance Left With Is Rs.", w_d)
            dict_1.update({g: w_d})
            # print(dict_1)
            front_page(ser)
        elif h < with_draw:
            print("\t\t\tInputed Amount Is Greater Than Bank Amount Balance.\n")
            print("\t\t\tYou Have Only Rs", h,
                  "In Your Bank Account.\n\t\t\tKindly Re-Enter The Amount .\n")
            withdraw(ser)
        elif h == 0:    
            print("\t\t\tYou Have Null Amount In Bank Account.\n\n")
            front_page(ser)
    else:
        print("\t\t\tYou Do Not Have A Account In This Bank Please Create Account To Make Withdraw. or Try Again\n\n")
        print("1. Re-Try\n2. Frontpage\n")
        try:
            choice_1 = int(input("EN CHOICE : "))
            if choice_1 == 1:
                withdraw(ser)
            elif choice_1 == 2:
                front_page(ser)
            elif choice_1 < 1 or choice_1 > 2:
                print(
                    "\t\t\tMr Account Holder, You Have Selected Incorrect Option\nPlease Try-Again\n\n")
        except:
            print("\n\t\t\tMr Account Holder, Select Options in (Int)* Only\n\n")
            front_page()


def frontpage():
    print("\t\t\t\tBanking Solutions PVT LTD")
    print(
        "\t\t\t\tSelect Services.\n------------------\n1. Create Account\n2. Login\n0. Exit\n\n")
    try:
        sel = int(input("Select Option : "))
        if sel == 1:
            create_account()
        elif sel == 2:
            try:
                login()
            except:
                print("\n\n\nDear Sir, There Is No Account For Inputted Credentials.\n\t\t\tIn Order To Continue Please Create Account.\n\t\t\tThank You\n\n")
                frontpage()
        elif sel == 0:
            exit()
        elif sel > 2 or sel < 0:
            print(
                "\t\t\tMr Account Holder, You Have Selected Incorrect Option\nPlease Try-Again\n\n")
            frontpage()
    except:
        print("\n\t\t\tMr Account Holder, Select Options in (Int)* Only\n\n")
        frontpage()


def password_up(ser):
    # here we need to update the password
    passw = int(input("EN New-Pass : "))
    pass_1 = int(input("EN Conform-Pass : "))
    p = str(passw)
    l = str(ser)
    if passw == pass_1:
        print("\t\t\tCredits Matched\n")
        print("\t\t\tPassword Changed-Successfully!\n\n")
        dict.update({l: p})
        front_page(ser)
    else:
        print("\t\t\tCredits-Un-Matched\n\n")
        password_up(ser)


def balance_info(ser):
    print("\nAccount_Balance ")
    # ser_4=int(input("EN SERIAL NO : "))
    z = str(ser)
    x = dict_2.get(z)
    y = int(bool(dict_1.get(z)))
    s = dict_1.get(z)
    if y == 1:
        print("\t\t\tMr/Ms Account Holder,Your Balance : Rs", s, "\n\n")
        front_page(ser)
    else:
        print("\t\t\tDear, Sir You Do Not Have A Account In This Bank.\n\n")
        frontpage()


def front_page(ser):
    print(
        "\t\t\t\tSelect Services.\n--------------------\n1. Withdraw_Amount\n2. Deposit_Amount\n3. Add Details Holder\n4. Log_Out\n5. Balance Info\n6. Password Change\n\n")
    try:
        sel = int(input("Select Option : "))
        if sel == 1:
            withdraw(ser)
        elif sel == 2:
            deposit(ser)
        elif sel == 3:
            add_details_holder()
        elif sel == 4:
            frontpage()
        elif sel == 5:
            balance_info(ser)
        elif sel == 6:
            password_up(ser)
    except:
        print("\n\t\t\tEnter List Options in (Int)* Only\n\n")
        front_page(ser)


frontpage()
