start_range = 10
end_range = 50

prime_numbers = [num for num in range(start_range, end_range + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")
