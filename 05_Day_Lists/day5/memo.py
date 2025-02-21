# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6, 7]

# 3. Find the length of your list
print(f"Length of my_list: {len(my_list)}")

# 4. Get the first, middle, and last item of the list
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]
print(f"First item: {first_item}, Middle item: {middle_item}, Last item: {last_item}")

# 5. Declare a list called mixed_data_types
mixed_data_types = ["Your Name", 30, 1.75, "Single", "123 Main St"]  # Example values

# 6. Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(f"Number of companies: {len(it_companies)}")

# 9. Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(f"First company: {first_company}, Middle company: {middle_company}, Last company: {last_company}")

# 10. Print the list after modifying one of the companies
it_companies[1] = "Alphabet"  # Changing Google to Alphabet
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Intel")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Salesforce")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()  # Changing Facebook to FACEBOOK
print(it_companies)

# 14. Join the it_companies with a string '#;  '
joined_companies = "#;  ".join(it_companies)
print(joined_companies)

# 15. Check if a certain company exists in the it_companies list.
company_exists = "Microsoft" in it_companies
print(f"Does Microsoft exist in the list? {company_exists}")

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# 20. Slice out the middle IT company or companies from the list
middle_companies = it_companies[len(it_companies) // 2 - (1 if len(it_companies) %2 == 0 else 0):len(it_companies) // 2 + 1]
print(middle_companies)

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    it_companies.pop(middle_index)
    it_companies.pop(middle_index -1)
else:
    it_companies.pop(middle_index)
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies
# print(it_companies)  # This would cause an error because the list no longer exists

# 26. Join the following lists:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
joined_list = front_end + back_end
print(joined_list)

# 27. Copy the joined list and assign it to full_stack, then insert Python and SQL after Redux.
full_stack = joined_list.copy()
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)

#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()
print("Sorted ages:", ages)

# Find the min and max age
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Ages with min/max added:", ages)

# Find the median age
ages.sort() # Important to sort again after adding min/max
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("Median age:", median_age)

# Find the average age
average_age = sum(ages) / n
print("Average age:", average_age)

# Find the range of the ages
age_range = max_age - min_age
print("Age range:", age_range)

# Compare the value of (min - average) and (max - average), use abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print("Absolute difference (min - average):", min_avg_diff)
print("Absolute difference (max - average):", max_avg_diff)

# --- Countries List ---
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Find the middle country(ies)
n_countries = len(countries)
if n_countries % 2 == 0:
    middle_countries = countries[n_countries//2 - 1 : n_countries//2 + 1]
else:
    middle_countries = [countries[n_countries//2]]
print("Middle country(ies):", middle_countries)

# Divide the countries list into two equal lists
first_half = countries[:(n_countries + 1) // 2]
second_half = countries[(n_countries + 1) // 2:]
print("First half of countries:", first_half)
print("Second half of countries:", second_half)

# Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic = countries
print("China:", china)
print("Russia:", russia)
print("USA:", usa)
print("Scandic countries:", scandic)
