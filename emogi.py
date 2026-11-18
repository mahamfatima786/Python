# Convert text-based emotions into emojis. 

msg = input("Enter your msg:")

msg = msg.replace(":)", "😊") 
msg = msg.replace(":(", "☹️") 
msg = msg.replace(":D", "😃") 
msg = msg.replace(";)", "😉") 

print(msg) 