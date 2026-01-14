total = int(input("Enter time in seconds:\n"))

hrs = total // 3600
mins = (total % 3600) // 60
secs = (total % 60)

print(f"The time is {hrs} hours, {mins} minutes, and {secs} seconds")

""" Sample output results:
Enter time in seconds:
7255
The time is 2 hours, 0 minutes, and 55 seconds
"""
