def options():
    print("1. Celsius")
    print("2. Farenheit")
    while True:
        try:
            num=int(input("Enter your choice: "))
            if num == 1:
                celsius_to_farenheit()
                break
            elif num == 2:
                farenheit_to_celsius()
                break
            else:
                print("invalid choice.")
        except ValueError:
            print("Invalid choice")


def celsius_to_farenheit():
    try:
        temperature=float(input("Enter the temperature: "))
        farenheit= temperature* (9/5) + 32
        print(farenheit)
    except ValueError:
        print("Try again")
     
exit

def farenheit_to_celsius():
    try:
        temp=float(input("Enter the temperature: "))
        celsius= (temp - 32) * 5/9
        print(f"{celsius}")
    except:
        print("Try again")

options()





