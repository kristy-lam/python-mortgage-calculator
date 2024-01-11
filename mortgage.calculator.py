"""
This programme calculates the monthly mortgage repayment based on the type
of mortgage chosen (repayment or interest only) and the user inputs for
house value, down payment, interest rate, and repayment months.
"""

def is_float_and_larger_than_zero(user_input):
    """
    The function checks if a user input is a float and larger than zero. If it
    is not, return appropriate error message.
    """

    while True:

        # Try except to check for value error
        try:

            num = float(user_input)

            # If loop to check for 0 or a negative number
            if num > 0:
                break

            print("An error has occurred: input must be a number larger than " +
                    "0.\n" + "="*80)
            user_input = input("Please enter an appropriate input: ")

        except ValueError:
            print("An error has occurred: input must be a number.\n" + "="*80)
            user_input = input("Please enter an appropriate input: ")

    # Return user input casted into float
    return float(num)

# end def


def is_down_payment_larger_than_house_value(x, y):
    """
    The function checks if the down payment is larger than the house value
    and prompts the user to enter a new value if it is not.
    """

    while True:

        if float(y) < float(x):
            break

        print("An error has occurred: the down payment must be smaller than "+
              "or equal to the house value.\n" + "="*80)
        y = input("Please enter an appropriate input: ")

    # Return user input casted into float
    return float(y)

# end def


# While loop to keep programme running

while True:

    # Ask for mortgage type
    mortgage_type = input("Enter the mortgage type - 'A' for repayment " +
                            "or 'B' for interest only: ").upper()

    # Calculate monthly mortgage repayment according to mortgage type
    if mortgage_type == "A": # Repayment option

        # Ask for house value
        house_value = input("Enter the value of your house (numbers only): ")

        # Function checking input value
        house_value = is_float_and_larger_than_zero(house_value)

        # Ask for down payment paid
        down_payment = input("Enter the down payment paid for your house " +
                             "(numbers only): ")

        # Function checking input value
        down_payment = is_float_and_larger_than_zero(down_payment)

        # Function checking whether down payment is larger than house value
        down_payment = is_down_payment_larger_than_house_value(
            house_value, down_payment)

        # Calculate mortgage loan
        mortgage_loan = house_value - down_payment

        # Ask for interest input
        interest_input = input("Enter the monthly interest rate (numbers " +
                               "only without the '%'): ")

        # Function checking input value and convert to monthly rate
        interest_rate = is_float_and_larger_than_zero(interest_input)\
            / 100 / 12

        # Ask for repayment years
        repayment_years = input("Enter the number of years you " +
                                        "plan to take to repay the mortgage " +
                                        "(numbers only): ")

        # Function checking input value and convert to months
        repayment_months = is_float_and_larger_than_zero(repayment_years) * 12

        # Calculate monthly repayment
        monthly_repayment = mortgage_loan * \
            (interest_rate * (pow((1 + interest_rate), repayment_months)) /\
                ((pow((1 + interest_rate), repayment_months) - 1)))

        # Round result to 2 decimal places
        monthly_repayment = round(monthly_repayment, 2)

        print(f"Your monthly mortgage repayment is : £{monthly_repayment}")

        break

    if mortgage_type == "B": # Interest only option

        # Ask for house value
        house_value = input("Enter the value of your house (numbers only): ")

        # Function checking input value
        house_value = is_float_and_larger_than_zero(house_value)

        # Ask for down payment paid
        down_payment = input("Enter the down payment paid for your house " +
                             "(numbers only): ")

        # Function checking input value
        down_payment = is_float_and_larger_than_zero(down_payment)

        # Function checking whether down payment is larger than house value
        down_payment = is_down_payment_larger_than_house_value(
            house_value, down_payment)

        # Calculate mortgage loan
        mortgage_loan = house_value - down_payment

        # Ask for interest input
        interest_input = input("Enter the monthly interest rate (numbers " +
                               "only without the '%'): ")

        # Function checking input value and convert to monthly rate
        interest_rate = is_float_and_larger_than_zero(interest_input)\
            / 100 / 12

        # Calculate monthly repayment
        monthly_repayment = (mortgage_loan * interest_rate) / 12

        # Round result to 2 decimal places
        monthly_repayment = round(monthly_repayment, 2)

        print("Your monthly interest only repayment is : £" +
                f"{monthly_repayment}.\nPlease note that the capital you "
                "owe the bank isn't shrinking.")

        break

    # Error message for invalid input for mortgage type
    print("An error has occurred: enter 'A' for repayment or 'B' for " +
          "interest only.\n" + "="*80)
