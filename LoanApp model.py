from tabulate import tabulate

from matplotlib import pyplot as plt

def repayment_loan():
    user_details = []
    status = True
    user = 0
    amount_borrowed = 0
    avg_income_per_month = []
    while status:
        print(f"For user {user}")
        user += 1
        loan = int(input("Enter your loan amount: "))
        amount_borrowed = amount_borrowed + loan
        rate = float(input("Enter the interest rate (in deciaml: )"))
        #payment = int(input("Enter the payment amount you want to make each month: $"))
        print("Input 1 for fixed and 2 for flexible")
        fx = int(input("Are you paying fixed: "))

        if fx == 2:
            print("flexible payment option")
            data = []
            paymentArr = []
            month = 0
            while loan > 0:
                loan = loan + (loan * rate)
                month += 1
                print(f'Amount for month {month} is {loan}')
                payment = float(input("Enter the payment amount you want to make this month: $"))
                loan -= payment
                print(f"month {month}, you paid {payment}, amount remaining is {loan}")
                if loan < 0:
                    loan = 0
                else:
                    data.append([month, loan, payment])
                    paymentArr.append(payment)
        else:
            print("fixed payment option")
            data = []
            paymentArr = []
            month = 0
            payment = float(input("Enter the payment amount you want to pay monthly: $"))
            while loan > 0:
                loan = loan + (loan * rate)
                month += 1
                print(f'Amount for month {month} is {loan}')
                if loan < payment:
                    payment = loan
                loan -= payment
                data.append([month, loan, payment])
                paymentArr.append(payment)
                if loan == 0:
                    break
                #if loan < 0:
                #    loan = 0
                #else:
                #    data.append([month, loan, payment])
                #    paymentArr.append(payment)
        print(tabulate(data, headers=['month', 'remain amount', 'payment'], floatfmt=('.2f'), tablefmt='grid'))
        print("\nCongratulations! You've paid off the loan.")

        #visualize loan repayment schedule
        monthly_range = range(1, month + 1)
        loan_balance = [loan - sum(paymentArr[:i]) for i in monthly_range]
        plt.plot(monthly_range, loan_balance, marker='o', linestyle='-')
        plt.xlabel('Months')
        plt.ylabel('Loan Balance')
        plt.title('Loan Repayment Schedule')
        plt.grid(True)
        plt.show()

        user_details.append(paymentArr)
        print("Is there another user: ")
        next = int(input("Input 1 for yes and 2 for no: "))
        if next == 2:
           status = False
        else:
            continue 
    #for i in user_details:
    #   print(i)
    print(f"Total amount borrowed is {amount_borrowed}")
    
    iden = 0
    month_sum = 0
    # for i in user_details:
    #     iden = iden + 1
    #     for k in range(0, len(user_details[iden-1])):
    #         month_sum = month_sum + user_details[iden-1][k]
    #         avg_income_per_month

    # for i in range(len(user_details)):
    #     for j in range(0, len(user_details[i])):
    #         month_sum = 
if __name__ == "__main__":
    repayment_loan()

