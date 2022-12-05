print("insert card!")
print(" Or enter your card number!")

card_no=112233

card = int(input("Enter your card no:"))

if card == card_no:
     print('Succefulley entered your card')

else:
     print("Wrong card try again")


password = 2233

pin = int(input("Enter your pin no:"))

balance = 5000

while pin == password:
    print("Welcome to your account!")

    print("""
          1 == Balance
          2 == withdraw
          3 == Deposit balance
          4 == Exit
            """)

    try:
        option = int(input("Please enter your choice:"))
    except:
        print("Please enter valid option")

    if option == 1:
        print("Your current balance is ",balance)

        print("=====================================================")
        print("=====================================================")




    if option == 2:
        withdraw_ammount = int(input("Please enter withdraw amount"))
        balance -= withdraw_ammount
        print("withdarw amount is debited from you account")
        print("Your current balance is:",balance)

        print("=====================================================")
        print("=====================================================")

    if option == 3:
        deposit_ammount = int(input("Please enter deposit_amount"))
        balance +=  deposit_ammount
        print("\n Amount Deposited:",balance)


        print(deposit_ammount," is credited yo tour account")

        print("=====================================================")
        print("=====================================================")

        print("Your current balance is ",balance)

        print("=====================================================")
        print("=====================================================")

    if option == 4:
        break

else:
    print("wrong pin try again")
