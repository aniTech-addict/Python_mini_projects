import time

def main():
    '''
    initializes the chatbot, starts the conversation loop, and
    imports the necessary functions from handle_responses.py 
'''
    print("\n~~ Simple Chatbot ~~\n")
    print(" Hey there! How can I help you?\n")
    
    while True:
        
        print("-> ", end="")
        user_input = input()
        #responses = handle_responses(user_input)
        
        if user_input.lower() == "exit":
            print("Thank you for using the chatbot. Goodbye!")
            break
        


if __name__ == "__main__":
    main()