import pandas as pd
import uuid
import random

# Generate 10,000 rows
data = []
users = [f"User_{i}" for i in range(1, 10001)]

# Some shared identifiers
shared_uid1 = [str(uuid.uuid4()) for _ in range(50)]  # 50 shared UUIDs
shared_uid2 = [f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1000,9999)}" for _ in range(50)]
shared_uid3 = [random.randint(100000, 200000) for _ in range(50)]

for i in range(10000):
    user = f"User_{i+1}"
    
    # Randomly decide if identifiers should be shared
    if random.random() < 0.2:  # 20% chance of sharing
        uid1 = random.choice(shared_uid1)
    else:
        uid1 = str(uuid.uuid4())
    
    if random.random() < 0.2:
        uid2 = random.choice(shared_uid2)
    else:
        uid2 = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1000,9999)}"
    
    if random.random() < 0.2:
        uid3 = random.choice(shared_uid3)
    else:
        uid3 = random.randint(100000, 200000)
    
    fraud = 1 if random.random() < 0.1 else 0  # 10% fraud
    
    data.append([user, uid1, uid2, uid3, fraud])

df = pd.DataFrame(data, columns=["user", "uniqueidentifier1", "uniqueidentifier2", "uniqueidentifier3", "Fraud"])
df.to_csv("fraud_data_10k.csv", index=False)