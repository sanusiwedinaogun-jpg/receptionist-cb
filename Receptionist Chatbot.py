print("System: Virtual Receptionist Online. Type 'exit' to leave the front desk.")
print("-" * 65)

# 1. Knowledge Base: Dictionary with 5+ tailored intents
responses = {
    "hello": "Hello! Welcome to Mr. Ogun's office. I'm his virtual receptionist. How can I help you today?",
    "hi": "Hi there! Welcome to Mr. Ogun's office. What can I do for you?",
    "is mr ogun around": "Mr. Ogun is currently in a meeting, but I'd be happy to take a message or help you schedule a time to speak with him.",
    "speak to mr ogun": "Mr. Ogun is currently unavailable. Would you like me to leave him a message or help you book an appointment?",
    "book appointment": "I would love to help you set that up! Please leave your name and preferred date, and I will check Mr. Ogun's calendar.",
    "schedule meeting": "Certainly! Just let me know what day works best for you, and I will get that on Mr. Ogun's schedule.",
    "office hours": "Our office is open Monday through Friday, from 9:00 AM to 5:00 PM.",
    "location": "We are located in the Main Plaza building, Suite 402. Let me know if you need directions!",
    "contact": "You can reach Mr. Ogun's direct desk at (555) 019-8372 or email him at office@mrogun.com.",
    "help": "I can help you check our office hours, get contact details, or book an appointment with Mr. Ogun. What do you need?",
    "thank you": "You are very welcome! Let me know if you need anything else.",
    "bye": "Goodbye! Have a wonderful day, and thank you for stopping by."
}

# 2. Continuous Loop
while True:
    raw_input = input("\nYou: ")
    
    # 3. Input Sanitization
    clean_input = raw_input.lower().strip()
    
    # 4. Exit Strategy
    if clean_input == "exit":
        print("Receptionist: Have a great day! Closing down the front desk.")
        break
    
    # 5. Atomic Lookup & Fallback Handling
    # If the user's input isn't in the dictionary, it defaults to the polite fallback message.
    fallback_message = "I'm just a virtual receptionist, so I didn't quite catch that. Try asking about office hours, booking an appointment, or type 'exit' to leave."
    reply = responses.get(clean_input, fallback_message)
    
    print(f"Receptionist: {reply}")