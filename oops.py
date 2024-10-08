class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()
    def menu(self):
        user_input= input(""" Welcome to Chatbook
                                press 1 for Signup
                                press 2 for signin
                                press 3 for write a Post
                                press 4 for send message to friend
                                press any key for exit
                                ---------------->>>>> """)
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.my_post()
        elif user_input=='4':
            self.sent_msg()
        else:
            print("You are succesfully exit from sevice")

    def signup(self):
        email=input("enter your email:     - ")
        pwd= input("enter your password:      -  ")
        self.username=email
        self.password=pwd
        print("you are successfully signup")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.password=='':
            print("please first signup")
        else :
            uname=input("enter your email:      ")
            pwd=input("enter your password:     ")
            if self.username==uname and self.password==pwd:
                print ("you successfully logged in")
                self.loggedin=True
            else:
                print("you have incorrect email password please enter correct")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin== True:
            txt=input("enter your post:      ")
            print(f"your contentes are posted:      {txt}")
        else:
            print("you firsrt signup")
        print("\n")
        self.menu()
    def sent_msg(self):
        if self.loggedin== True:
            msg=input(" enter your msg:      ")
            frnd= input(" to whom you send this message:     ")
            print(f"you have sent message to {frnd} this is your message {msg}")
        else:
            print("you first signup")

        print("\n")
        self.menu()
    
obj= chatbook()
