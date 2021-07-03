"""largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        # print(num)
        n = int(num)
        if largest is None or n > largest:
            largest = n
        elif smallest is None or n < largest:
            smallest = n

    except:
        print("Invalid input")
        continue


print("Maximum", largest)
print("Minimum", smallest)
"""
total = 0.0
count = 0

fname = input("Enter file name: ")
fhand = open(fname)


for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        line = float(line[21:])
        total = line + total
        count = count + 1
# print(total)
average = total / count

print("Average spam confidence:", average)
