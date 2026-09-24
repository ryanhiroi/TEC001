talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

grams_per_lot = 13.3
grams_per_pound = 32 * grams_per_lot
grams_per_talent = 20 * grams_per_pound

total_grams = (talents * grams_per_talent) + (pounds * grams_per_pound) + (lots * grams_per_lot)

kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")