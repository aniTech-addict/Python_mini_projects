

def main():
    print("\n~~ Simple Chatbot ~~\n")
    print(" Hey there! How can I help you?\n")
    
    while True:
        #user_input = input()
        user_input = "Hello"
        
        
        if user_input.lower() == "exit":
            print("Thank you for using the chatbot. Goodbye!")
            break
        


if __name__ == "__main__":
    main()