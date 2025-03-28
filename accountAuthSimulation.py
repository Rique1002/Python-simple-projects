usernames = ["Hozier", "Andrew", "Mr.Byrne"]
passwords = ["francesca11", "toosweet12", "sedated2001"]


usernameField = input("Enter your registered username: ")
passwordField = input('Enter your password: ')

# for username in usernames:
#    if username == usernameField:
#       usernameMatch = username 
#       usernameIndex = usernames.index(username)
   
     

#       for password in passwords:
#         if password == passwordField:
#            passwordMatch = password
#            passwordIndex = passwords.index(password)
        
           

#            if usernameIndex == passwordIndex:
#               print("Welcome " + username)
            
#            else: 
#               print("Account not Found")
           
           

for x in range(len(usernames)):
    if usernameField == usernames[x] and passwordField == passwords[x]:
        print("Welcome " + usernames[x])
        break
    else: 
      print("Account not Found")
 


                
    
        
       
    
       

            
            

    
    



     
