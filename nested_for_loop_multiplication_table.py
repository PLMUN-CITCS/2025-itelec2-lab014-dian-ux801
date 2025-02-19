# Python script to print multiplication table using nested loops

# Outer loop for rows (1 to 5)
for i in range(1, 6):
    # Inner loop for columns (1 to 5)
    for j in range(1, 6):
        product = i * j  # Calculate product
        print(f"{product:4}", end="")  # Print with formatting
    print()  # New line after each row
