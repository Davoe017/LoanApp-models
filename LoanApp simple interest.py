from tabulate import tabulate

from matplotlib import pyplot as plt

def loan_repayment():
    loan_amount = float(input("Enter loan amount: "))
    interest_rate = float(input("Enter interest rate in decimal: "))
    fix_flex = input("Do you want to pay at fixed intervals (y/n)? ").lower()

    data = []
    payment_array = []
    month = 0
    loan_amount = loan_amount + loan_amount*(1 + interest_rate)
    if fix_flex == 'y':
        payment_amount = float(input("Enter monthly repayment amount: "))
        while loan_amount > 0:
            month += 1
            loan_amount -= payment_amount

            if loan_amount < 0:
                loan_amount = 0
            else:
                data.append([month, loan_amount, payment_amount])
                payment_array.append(payment_amount)

        print(tabulate(data, headers=['Month', 'Remaining Amount', 'Amount Paid this Month'], floatfmt=('.2f'), tablefmt='grid'))
    else:
        while loan_amount > 0:
            month += 1
            payment_amount = float(input(f"Enter amount you are paying in month {month}: $"))
            loan_amount -= payment_amount


            if loan_amount < 0:
                loan_amount = 0
            else:
                data.append([month, loan_amount, payment_amount])
                payment_array.append(payment_amount)

        print(tabulate(data, headers=['Month', 'Remaining Amount', 'Amount Paid this Month'], floatfmt=('.2f'), tablefmt='grid'))

    monthly_range = range(1, month + 1)
    loan_balance = [loan_amount - sum(payment_array[:i]) for i in monthly_range]
    plt.plot(monthly_range, loan_balance, marker='o', linestyle='-')
    plt.xlabel('Months')
    plt.ylabel('Loan Balance')
    plt.title("Loan Repayment Schedule graph - Months against Loan Balance")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    loan_repayment()