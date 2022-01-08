# Get user email

email= input('What is your email?: ').strip()

# Slice out username

user = email[:email.index('@')]

# slice domain name

domain = email[email.index('@')+ 1 :]

# Format message

output = 'Your username is {} and your domaine name is {}'.format(user,domain)


# Display output message

print(output)
