# Filename: MaldonadoSebastian_086_p1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: Sebastian G. Maldonado Rosado
# STUDENT ID: ###-##-####
# SECTION: 086
############      DEFINE CONSTANTS BELOW      ############
KILOMETERS_PER_MILE = 1.60934
KILOGRAMS_PER_POUND = 2.20462


############       ADD YOUR CODE BELOW        ############

def convert_miles_to_kilometers():
    miles = input("Enter the miles to be converted: ")
    if is_float(miles):
        # Convert string to numeric miles
        miles = float(miles)
        if miles < 0:
            print("Illegal unit of conversion. Input miles cannot be a negative number.")
        # Conversion should be rounded to 2 decimal places.
        elif miles > 0:
            km = round(miles * KILOMETERS_PER_MILE, 2)
            print(miles, "miles are equivalent to", km, "kilometers")
    else:
        print("Illegal unit of conversion. Input miles are not a number.")


def convert_kilometers_to_miles():
    km = input("Enter the kilometers to me converted: ")
    if is_float(km):
        km = float(km)
        if km < 0:
            print("Illegal unit of conversion. Input kilometers cannot be a negative number.")
        elif km > 0:
            miles = round(km / KILOMETERS_PER_MILE, 2)
            print(km, "kilometers are equivalent to", miles, "miles")
    else:
        print("Illegal unit of conversion. Input kilometers are not a number.")


def convert_pounds_to_kilograms():
    pounds = input("Enter the pounds to be converted: ")
    if is_float(pounds):
        pounds = float(pounds)
        if pounds < 0:
            print("Illegal unit of conversion. Input pounds cannot be a negative number.")
        elif pounds > 0:
            kg = round(pounds / KILOGRAMS_PER_POUND, 2)
            print(pounds, "pounds are equivalent to", kg, "kilograms")
    else:
        print("Illegal unit of conversion. Input pounds are not a number.")


def convert_kilograms_to_pounds():
    kg = input("Enter the kilograms to be converted: ")
    if is_float(kg):
        kg = float(kg)
        if kg < 0:
            print("Illegal unit of conversion. Input kilograms cannot be a negative number.")
        elif kg > 0:
            pounds = round(kg * KILOGRAMS_PER_POUND, 2)
            print(kg, "kilograms are equivalent to", pounds, "pounds")
    else:
        print("Illegal unit of conversion. Input kilograms are not a number.")


def convert_fahrenheit_to_celsius():
    fahrenheit = input("Enter the Fahrenheit degrees to be converted: ")
    if is_float(fahrenheit):
        fahrenheit = float(fahrenheit)
        celsius = round(((fahrenheit - 32) / 1.8), 2)
        print(fahrenheit, "Fahrenheit are equivalent to", celsius, "Celsius")
    else:
        print("Illegal unit of conversion. Input Fahrenheit degrees are not a number.")


def convert_celsius_to_fahrenheit():
    celsius = input("Enter the Celsius degrees to be converted: ")
    if is_float(celsius):
        celsius = float(celsius)
        fahrenheit = round(((celsius * 1.8) + 32), 2)
        print(celsius, "Celsius are equivalent to", fahrenheit, "Fahrenheit")
    else:
        print("Illegal unit of conversion. Input Celsius degrees are not a number.")


def convert_miles_per_hour_to_kilometers_per_hour():
    mph = input("Enter the miles/hour to be converted: ")
    if is_float(mph):
        mph = float(mph)
        if mph < 0:
            print("Illegal unit of conversion. Input miles/hour cannot be a negative number.")
        elif mph > 0:
            kmh = round(mph * KILOMETERS_PER_MILE, 2)
            print(mph, "miles/hour are equivalent to", kmh, "kilometers/hour")
    else:
        print("Illegal unit of conversion. Input miles/hour are not a number.")


def convert_kilometers_per_hour_to_miles_per_hour():
    kmh = input("Enter the kilometers/hour to me converted: ")
    if is_float(kmh):
        kmh = float(kmh)
        if kmh < 0:
            print("Illegal unit of conversion. Input kilometers/hour cannot be a negative number.")
        elif kmh > 0:
            mph = round(kmh / KILOMETERS_PER_MILE, 2)
            print(kmh, "kilometers/hour are equivalent to", mph, "miles/hour")
    else:
        print("Illegal unit of conversion. Input kilometers/hour are not a number.")


def process_conversion(numericOption):
    if numericOption == 1:
        convert_miles_to_kilometers()
    elif numericOption == 2:
        convert_kilometers_to_miles()
    elif numericOption == 3:
        convert_pounds_to_kilograms()
    elif numericOption == 4:
        convert_kilograms_to_pounds()
    elif numericOption == 5:
        convert_celsius_to_fahrenheit()
    elif numericOption == 6:
        convert_fahrenheit_to_celsius()
    elif numericOption == 7:
        convert_miles_per_hour_to_kilometers_per_hour()
    elif numericOption == 8:
        convert_kilometers_per_hour_to_miles_per_hour()


############ DO NOT MODIFY THE SECTION BELOW  ############

def is_float(s):
    try:
        float(s)
        # Return True if no exception is thrown
        return True
    except ValueError:
        return False


def print_program_menu():
    print("\n--------")
    print("Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Miles/hour to kilometers/hour")
    print("8. Kilometers/hour to miles/hour")
    print("9. Exit")


def identify_option(option):
    # Verify that a number was input
    if option.isdigit():
        numericOption = int(option)
        # Check if the selection is within permitted range
        if numericOption >= 1 and numericOption <= 9:
            return numericOption
        else:
            return -1  # Invalid option
    else:
        return -1  # Invalid option


def main():
    done = False
    while not done:
        print_program_menu()
        userOption = input("Enter option: ")
        optionInfo = identify_option(userOption)
        if optionInfo != -1:
            # Option was valid
            if optionInfo == 9:
                done = True
                print("Thanks for using the unit conversion program!")
            else:
                process_conversion(optionInfo)
        else:
            # Option was invalid
            print("Invalid option\n")


# This line makes python start the program from the main function
if __name__ == "__main__":
    main()
