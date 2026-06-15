'''
LOGIC BOX - PROJECT 2
Name : Jay Ankurkumar Shah
Mobile : 7698780653
Email : jayshah1505@gmail.com
'''

while True:
    print("\nWelcome to the Pattern Generator and Number Analyzer!")
    print("\nSelect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice : "))

    #Option 1
    if choice == 1:
        rows = int(input("Enter number of rows : "))
        print("\nPattern")
        for i in range(1, rows+1):
            for j in range(i):
                print("*", end = " ")
            print()

    # Option 2
    elif choice == 2:
        start = int(input("\nEnter the start of range : "))
        end = int(input("Enter the end of range : "))
        print("\n")
        total = 0

        for num in range(start, end+1):
            if num%2 == 0:
                print(f"Number ",num," is Even")
            else:
                print(f"Number ",num," is Odd")

            total += num
        print("\nSum of all numbers from ",start, " to ", end, " is ", total)

    #Option 3
    elif choice == 3:
        print("\nExiting the program. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again!")
