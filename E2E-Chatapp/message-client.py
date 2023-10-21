import os
from time import sleep

class MessageClient:

    def __init__(self):
        self.username = None
        self.chat_access_password = None

    def setUserInfo(self, screen_name, password):
        self.username = screen_name
        self.chat_access_password = password

    def getStartUpInfo(self):
        print("Hello. Welcome to Simple Chat Connect.")
        print("SCC is private messaging application that")
        print("encrpts your messages during transmission.")
        print("Please set a username and a default chat")
        print("access password so others can connect to")
        print("your chat session.")
        print("+++++++++++++++++++++++++++++++++++++++++++")
        name = input("Username: ")
        pw = input("Password: ")

        self.setUserInfo(name, pw)

    def printDefaultGUI(self):
        os.system('cls')
        print("Welcome:",self.username)
        print("=========" + ("=" * len(self.username) * 2))
        print("Would you like to: ")
        print("1. Start a chat")
        print("2. Join a chat")
        print("3. Exit and delete all chat data")

        prompt_satisfied = False
        while not prompt_satisfied:
            choice = input("> ")

            if choice == "1":
                self.startChatSetup()
                #pass to chat GUI function
            elif choice == "2":
                pass
                #pass to chat selection function
            elif choice == "3":
                pass
                #pass to chat deletion function
            else:
                print("Incorrect operation.")

    #Creates a folder for the chat to occur in
    #3 files
    #chat information: name of the chat, and chat password
    #encrypted message list
    #bitmask list
    def startChatSetup(self):
        #Make a folder that will contain the chat under the host users name
        os.mkdir("./%s" %self.username)
        os.system('pause')

        #Make the chat password file that contains the chats password
                


new_mc = MessageClient()
new_mc.getStartUpInfo()
new_mc.printDefaultGUI()
