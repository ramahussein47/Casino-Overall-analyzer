import hashlib
usercode="122334"
server_code="this is my server"
combined_seed=usercode+server_code
# uses the haslin to convert the combined_seed to encode the hex fron a string
hash_seed=hashlib.sha256(combined_seed.encode().hexdigest())
print("The combined seed is:",hash_seed)
