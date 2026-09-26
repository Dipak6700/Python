# Ask the user for their name
name = input("Enter your name: ")

# Set the total spending to 0
total_spent = 0

# Repeat the process for 3 days
for day in range(1, 4):
    print("Day", day)

    # Ask for today's spending
    spent = float(input("Enter money spent today ($): "))

    # Add today's spending to the total
    total_spent = total_spent + spent

    # Check the daily $20 budget
    if spent > 20:
        print("Over your $20 budget today!")
    else:
        print("Great! Under budget today.")

# Display the final total
print("Total money spent over 3 days: $",
      format(total_spent, ".2f"))

# Check the overall $60 budget
if total_spent <= 60:
    print("Overall Result: You stayed under your $60 total budget!")
else:
    print("Overall Result: You went over your $60 total budget!")


