import random
from datetime import datetime, timedelta

# Generate random integer between 0 and 5 (excluding 6)
random_int_0_to_5 = random.randrange(0, 6)

# Generate random integer between 5 and 9 (excluding 10)
random_int_5_to_9 = random.randrange(5, 10)

# Generate random integer between 0 and 10 with a step of 3
random_int_with_step = random.randrange(0, 11, 3)

# Generate random date between two dates
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
random_days = random.randrange((end_date - start_date).days)
random_date = start_date + timedelta(days=random_days)

# Example usage
print("Random Integer between 0 and 5:", random_int_0_to_5)
print("Random Integer between 5 and 9:", random_int_5_to_9)
print("Random Integer between 0 and 10 with step 3:", random_int_with_step)
print("Random Date between 2022-01-01 and 2022-12-31:", random_date)