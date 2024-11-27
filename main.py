def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_f(c):
    return (c * 9 / 5) + 32

def inch_to_cm(inches):
    return inches * 2.54

def cm_to_inch(cm):
    return cm / 2.54
def menuChoices():
    print("Unit Conversion Program")
    print("------------------------")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Inches to Centimeters")
    print("4. Centimeters to Inches")
    print("5. Exit")
    
def main():
    while True:
        menuChoices()
        choice = input("\nEnter the number of your choice: ")
        
        if choice == '1':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f} °F is {f_to_c(f):.2f} °C")
        elif choice == '2':
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c} °C is {c_to_f(c):.2f} °F")
        elif choice == '3':
            inches = float(input("Enter length in inches: "))
            print(f"{inches} inches is {inch_to_cm(inches):.2f} cm")
        elif choice == '4':
            cm = float(input("Enter length in centimeters: "))
            print(f"{cm} cm is {cm_to_inch(cm):.2f} inches")
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()
main()
