import stripe
stripe.api_key="sk_test_51HwUlaA67jZ6i4HK3X9Ddp6QtOMIVGzGEtMu4DjYMQN5W6dBWZo4ig8PhyLzr4fYMBPWDNoGSsjzgFHXQ8KD88EB00Du50yLoA"

connected_accounts = stripe.Account.list(limit=10)

# Print the IDs of connected accounts
for account in connected_accounts:
    print("Connected Account ID:", account.id)
