months_expenses = [5200, 6350, 4600, 4130, 3190]

feb_extra_expense = months_expenses[1] - months_expenses[0]
print(f"1. The extra money you spent in February compared to January is {feb_extra_expense} pesos.")

total_expense = months_expenses[0] + months_expenses[1] + months_expenses[2]
print(f"2. The total expense in the first quarter (first three months) of the year is {total_expense} pesos.")

spent_2000 = any(expense == 2000 for expense in months_expenses)
print(f"3. Did you spend exactly 2000 pesos in any month? {spent_2000}")

june_expense = 1980
months_expenses.append(june_expense)
print(f"4. The updated monthly expenses list with the month of June is {months_expenses} pesos.")

april_refund = 200
months_expenses[3] -= april_refund
print(f"5. The expenses after the refund in April is {months_expenses} pesos.")
