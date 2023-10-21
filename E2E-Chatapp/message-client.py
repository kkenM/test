import os
import threading
from time import sleep
import cipher
from colorama import Fore, Back, Style

#Flag to check for end of chat
exit_flag = False

class MessageClient:

    def __init__(self):
        self.username = None
        self.chat_access_password = None
        self.current_chat = None

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
        print("3. Exit")
        print("4. Diag.")

        prompt_satisfied = False
        while not prompt_satisfied:
            choice = input("> ")

            if choice == "1":
                self.startChatSetup()
            elif choice == "2":
                self.chatSelectionGUI()
            elif choice == "3":
                print("Thanks for using SCC. Goodbye!")
                exit()
            elif choice == "4":
                print(self.username)
                print(self.chat_access_password)
                print(self.current_chat)
            else:
                print("Incorrect operation.")

    def chatSelectionGUI(self):
        folders = [folder for folder in os.listdir("./") if os.path.isdir(os.path.join("./", folder))]
        
        print("Please select a chat to join by typing the name of the chat or type EXIT to exit:")
        for folder in folders:
            print(folder)

        while True:
            selection = input("> ")

            if selection in folders:
                self.chatHandler(connect_to_host="./%s" %selection)
            elif selection == "EXIT":
                self.printDefaultGUI()
            else:
                print("Chat not found please try again or type EXIT to exit.")


        
    #Pulls all messages from msg file and decrypts them and puts them in an array.
    def pullAllMsg(self, chat_folder_path):
        encrypted_lines = []
        bit_masks = []

        with open("%s/msg.txt" %chat_folder_path, 'r', encoding='ascii') as msg_file:
            for line in msg_file:
                encrypted_lines.append(line)

        with open("%s/bme.txt" %chat_folder_path, 'r', encoding='ascii') as mask_file:
            for mask in mask_file:
                bit_masks.append(mask)

        message_list = []

        for cur_line, mask_list in zip(encrypted_lines, bit_masks):
            message_list.append(cipher.decipher_message(cur_line, mask_list))

        return message_list



    def chatHandler(self, connect_to_host=None):

        #If the user is the creator of the chat
        if self.current_chat != None:
            chat_path = self.current_chat

            #Injecting Introduction into Message Stream
            chat_file = open("%s/msg.txt" %chat_path, mode="a", encoding='ascii')
            bitmask_file = open("%s/bme.txt" %chat_path, mode="a", encoding='ascii')

            msg, bit_mask = cipher.cipher_message("Welcome to chat:%s" %self.username)
            msg = msg + "\n"
            bit_mask = bit_mask + "\n"
            chat_file.write(msg) #MAY HAVE TO HANDLE 
            bitmask_file.write(bit_mask)
            
            msg, bit_mask = cipher.cipher_message("====================================================================")
            msg = msg + "\n"
            bit_mask = bit_mask + "\n"
            chat_file.write(msg) #MAY HAVE TO HANDLE 
            bitmask_file.write(bit_mask)

            msg, bit_mask = cipher.cipher_message("Exiting this chat at anytime will delete the chat messsage data.")
            msg = msg + "\n"
            bit_mask = bit_mask + "\n"
            chat_file.write(msg) #MAY HAVE TO HANDLE 
            bitmask_file.write(bit_mask)

            msg, bit_mask = cipher.cipher_message("To exit at anytime please enter: SCC-END")
            msg = msg + "\n"
            bit_mask = bit_mask + "\n"
            chat_file.write(msg) #MAY HAVE TO HANDLE 
            bitmask_file.write(bit_mask)

            msg, bit_mask = cipher.cipher_message("Start typing at any time to begin a new message.")
            msg = msg + "\n"
            bit_mask = bit_mask + "\n"
            chat_file.write(msg) #MAY HAVE TO HANDLE 
            bitmask_file.write(bit_mask)

            msg, bit_mask = cipher.cipher_message("====================================================================")
            msg = msg + "\n"
            bit_mask = bit_mask + "\n"
            chat_file.write(msg) #MAY HAVE TO HANDLE 
            bitmask_file.write(bit_mask)

            chat_file.close()
            bitmask_file.close()

            #Main chat behavior loop

            #Open chat dialouge with greeters
            os.system('cls')
            new_messages = self.pullAllMsg(chat_path)
            for message in new_messages:
                print(message)

            #Constantly poll the file for any changes, if so immediatly update the chat
            def pollForChanges():
                last_updated_timestamp = os.path.getmtime("%s/msg.txt" %chat_path)
                global exit_flag
                while not exit_flag:
                    current_timestamp = os.path.getmtime("%s/msg.txt" %chat_path)

                    if current_timestamp != last_updated_timestamp:
                        os.system('cls')
                        new_messages = self.pullAllMsg(chat_path)

                        for message in new_messages:
                            print(message)
                        last_updated_timestamp = current_timestamp

            def pollForInput():
                global exit_flag
                while True:
                    user_input = input("%s>"%self.username)
                    if user_input == "SCC-END":
                        exit_flag = True
                        #TODO: Pass to deletion of chat handler
                        break
                    else:
                        chat_file = open("%s/msg.txt" %chat_path, mode="a", encoding='ascii')
                        bitmask_file = open("%s/bme.txt" %chat_path, mode="a", encoding='ascii')
                        msg, bit_mask = cipher.cipher_message("%s>" %self.username + " %s" %user_input)
                        msg = msg + "\n"
                        bit_mask = bit_mask + "\n"
                        chat_file.write(msg)
                        bitmask_file.write(bit_mask)
                        chat_file.close()
                        bitmask_file.close()

            input_thread = threading.Thread(target=pollForInput)
            update_thread = threading.Thread(target=pollForChanges)

            update_thread.start()
            input_thread.start()
            
            update_thread.join()
            print("Threads dead update")
            input_thread.join()
            print("Threads dead input")
            

            self.deleteChatOnHostLeave()
            self.current_chat = None
            self.printDefaultGUI()

        elif connect_to_host is not None:
            pw_line = ""
            print(connect_to_host)
            try:
                with open('%s/pw.txt' %connect_to_host, 'r') as password_file:
                    pw_line = password_file.readline()
            except:
               print("ERROR: Chat not found. Chat might have been closed. Returning to main menu.")
               sleep(5)
               self.printDefaultGUI()
            
            pw_check = input("Please confirm chat password: ")

            if pw_check != pw_line:
                print("Wrong password. Exiting.")
                sleep(2)
                self.chatSelectionGUI()
            elif pw_check == pw_line:
                self.current_chat = connect_to_host
                chat_path = self.current_chat

                #Main chat behavior loop

                #Open chat dialouge with greeters
                os.system('cls')
                new_messages = self.pullAllMsg(chat_path)
                for message in new_messages:
                    print(message)

                #Constantly poll the file for any changes, if so immediatly update the chat
                def pollForChanges():
                    last_updated_timestamp = os.path.getmtime("%s/msg.txt" %chat_path)
                    global exit_flag
                    while not exit_flag:
                        current_timestamp = os.path.getmtime("%s/msg.txt" %chat_path)

                        if current_timestamp != last_updated_timestamp:
                            os.system('cls')
                            new_messages = self.pullAllMsg(chat_path)

                            for message in new_messages:
                                print(message)
                            last_updated_timestamp = current_timestamp

                def pollForInput():
                    global exit_flag
                    while True:
                        user_input = input("%s>"%self.username)
                        if user_input == "SCC-END":
                            exit_flag = True
                            break
                        else:
                            chat_file = open("%s/msg.txt" %chat_path, mode="a", encoding='ascii')
                            bitmask_file = open("%s/bme.txt" %chat_path, mode="a", encoding='ascii')
                            msg, bit_mask = cipher.cipher_message("%s>" %self.username + " %s" %user_input)
                            msg = msg + "\n"
                            bit_mask = bit_mask + "\n"
                            chat_file.write(msg)
                            bitmask_file.write(bit_mask)
                            chat_file.close()
                            bitmask_file.close()

                input_thread = threading.Thread(target=pollForInput)
                update_thread = threading.Thread(target=pollForChanges)

                update_thread.start()
                input_thread.start()
                
                update_thread.join()
                print("Threads dead update")
                input_thread.join()
                print("Threads dead input")
                

                self.current_chat = None
        
                self.printDefaultGUI()



    #Creates a folder for the chat to occur in
    #3 files
    #chat information: name of the chat, and chat password
    #encrypted message list
    #bitmask list
    def startChatSetup(self):
        #Make a folder that will contain the chat under the host users name
        os.mkdir("./%s" %self.username)

        #Make the chat password file that contains the chats password
        with open("./%s/pw.txt" %self.username, 'w') as pwf:
            pwf.write('%s' %self.chat_access_password)


        #Make the chat message folder that will contain encrypted messages
        with open("./%s/msg.txt" %self.username, 'w') as msgf:
            pass

        #Make the chat bitmask encryption keylist
        with open("./%s/bme.txt" %self.username, 'w') as bmf:
            pass

        self.current_chat = "./%s" %self.username
        self.chatHandler()

    
                
    def deleteChatOnHostLeave(self):
        os.system('RMDIR %s /S' %self.current_chat[2:])
        os.system('pause')


new_mc = MessageClient()
new_mc.getStartUpInfo()
new_mc.printDefaultGUI()
