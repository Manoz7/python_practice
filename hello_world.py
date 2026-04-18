def hello_world():
  return "Hello\"s World"

m = hello_world()
print(len(m))

print(m.split())

# Slicing
print(m[10])

print(m[::-1])
print(m[6::])

print(m.strip())

print(hello_world())


message = "Hello, I am John DOe. You can call me John. One time my friend said \"Hey John, How are you? \" I said I am great. Thank you!"
print(message)
print(message.count("I"))

new_message = message.replace('I am', 'He is')
print(new_message)

print(m + " " + message)

chr = "python";

if chr == "Java" or "":
  print("Successful")
else:
  print("unsuccessful")