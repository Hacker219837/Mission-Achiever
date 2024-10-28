

import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections


# Hotel Booking Conversation with user
hotel_chatbot_Responses = [
   ["Hi|Hello|Hey", 
     ["Hi!Welcome to Mission Achievers Hotel! How can I assist you today?"]], 
#  -------------------------------------------------------------------------------------------------------------

    ["I Would like to book a room",
     ["Great! I'd be happy to assist you with your booking. How many days are you planning to stay us?"]],

#  --------------------------------------------------------------------------------------------------------------

    [" 1 day|2 days|3 days|4 Days|5 days|1 week|2 weeks|3 weeks|1 month",
     ["Thank you! How many guests will be staying, and what type of room would you like? We offer 3 types of rooms: Standard, Deluxe, and Suite options "]],

#  --------------------------------------------------------------------------------------------------------------

    ["it will be 1 guest, and i'd like a Standard room|it will be 2 guests, and we'd like a Standard room|it will be 3 guests, and we'd like a Standard room |it will be 4 guests and we'd like a Standard room|it will be 5 guests, and we'd like a Standard room|it will be 6 guests, and we'd like a Standard room|it will be 7 guests, and we'd like a Standard room", 
     ["Perfect! A Standard room is available for those days at a rate of R700 per night. Would you like to proceed with the booking?"]],

    ["it will be 1 guest, and i'd like a Deluxe room|it will be 2 guests, and we'd like a Deluxe room|it will be 3 guests, and we'd like a Deluxe room |it will be 4 guests and we'd like a Deluxe room|it will be 5 guests, and we'd like a Deluxe room|it will be 6 guests, and we'd like a Deluxe room|it will be 7 guests, and we'd like a Deluxe room",
      ["Perfect! A Deluxe room is available for those days at a rate of R1500 per night. Would you like to proceed with the booking?"]],

    ["it will be 1 guest, and i'd like a Suite room|it will be 2 guests, and we'd like a Suite room|it will be 3 guests, and we'd like a Suite room |it will be 4 guests and we'd like a Suite room|it will be 5 guests, and we'd like a Suite room|it will be 6 guests, and we'd like a Suite room|it will be 7 guests, and we'd like a Suite room",
      ["Perfect! A Suite room is available for those days at a rate of R2500 per night. Would you like to proceed with the booking?"]],

#  --------------------------------------------------------------------------------------------------------------

    [" Yes| Yes, Please| Sure|Absolutely|Go ahead| proceed",
      ["To complete the booking, can I get your name and contact information?"]],

#  -------------------------------------------------------------------------------------------------------------

["My name is Nic Mmeli, and my email is NicMmeli12@gmail.com", 
 ["Thank you, Nic! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Blessing Hlungwani, and my email is BlessingHlungwani@gmail.com", 
 ["Thank you, Mr Blessing! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Mwenge Mukaza, and my email is MwengeMukaza@gmail.com",
  ["Thank you,  MrMwenge! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Zama Maseko, and my email is ZamaMaseko@gmail.com",
  ["Thank you, Ms Zama! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Tino Sinamasa, and my email is TinoSinamasa@gmail.com", 
 ["Thank you, Ms Tino ! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Phophi Malise , and my email is PhophiMalise@gmail.com",
  ["Thank you, Ms Phophi! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Nhlamulo Baloyi, and my email is NhlamuloBaloyi@gmail.com",
  ["Thank you, Ms Nhlamulo! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Tsepo Mukovhi, and my email is TsepoMukovhi@gmail.com",
  ["Thank you, Mr Tsepo! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

["My name is Malefetsane Matsela , and my email is Malefane@gmail.com", 
 ["Thank you, Mr Malefetsane ! Your reservation is almost complete. You will receive a confirmation and payment instructions via email shortly."]],

#  --------------------------------------------------------------------------------------------------------------
   #Quiries_Chatbot_Answers for User
 #  --------------------------------------------------------------------------------------------------------------  

["What are your check-in and check-out hours at Mission Achievers hotel ?",
      ["The Mission Achievers hotel policy states that our Check-in hours start from 2 PM in the Afternoon, and checking-out starts from 11h00 AM in the morning."]],

#  --------------------------------------------------------------------------------------------------------------

    ["Do you offer free Wi-Fi in your hotel?",
      ["Yes, we offer complimentary high-speed Wi-Fi in all areas of the hotel. Would you like the password?"]],

#  --------------------------------------------------------------------------------------------------------------

    ["Yes|Yes, Please",
      ["The Mission Achievers password is as follows: MissionAchievers@2024 "]],

#  --------------------------------------------------------------------------------------------------------------

["What amenities does the hotel offer?", 
 ["We offer a swimming pool, gym, spa, complimentary breakfast, and room service. What else would you like to know?"]],

#  --------------------------------------------------------------------------------------------------------------

    ["What is the price of a standard room?",
      ["The price for a standard room starts at ZAR 1,200 per night. Would you like to proceed with a booking?"]],

#  --------------------------------------------------------------------------------------------------------------

    ["Do you offer airport transfers?", 
     ["Yes, we offer airport shuttle services for an additional fee. Would you like to arrange a pick-up?"]],

#  --------------------------------------------------------------------------------------------------------------

    ["What is the cancellation policy?", 
     ["You can cancel your booking free of charge up to 24 hours before the check-in date."]],

#  --------------------------------------------------------------------------------------------------------------

    ["Can I extend my stay?", ["Yes! Please let us know by how days, and we will check availability for you."]],

#  --------------------------------------------------------------------------------------------------------------
    
     ["Do you offer free Wi-Fi in your hotel?",
       ["Yes, we offer complimentary high-speed Wi-Fi in all areas of the hotel. Would you like the password?"]],

#  --------------------------------------------------------------------------------------------------------------

 ["Where is Mission Achievers Hotel located?", 
  ["The Mission Achievers Hotel is located at private estate on the banks of vaal river in Vanderbijlpark, South Africa 777 Frikkie Meyer Blvd, 1900 in the Gauteng Province. "]],

#  --------------------------------------------------------------------------------------------------------------

 ["The air conditioning isn't working in my room" ,
   ["  I'm sorry to hear you're having trouble with the air conditioning. Let me help you with that. Is it not working at all, or is the room temperature uncomfortable?"]],

#  --------------------------------------------------------------------------------------------------------------

["It's not working at all", 
 [" Thank you for letting me know. Could you please check if the thermostat is turned on and set to the correct temperature?"]],

#  --------------------------------------------------------------------------------------------------------------

["Yes, I checked, but it still doesn't work.", 
 ["I apologize for the inconvenience. I will notify our maintenance team immediately, and someone will be sent to your room shortly to fix it. Would you like me to arrange a portable heater/fan or offer another room in the meantime?"]],

#  --------------------------------------------------------------------------------------------------------------

["I'd like a new room, please", 
 ["Okay, I will arrange a room change for you. Please hold on while I check availability."]],

 #  --------------------------------------------------------------------------------------------------------------

["I'd like a portable heater/fan", 
     ["Understood! I’ll notify housekeeping to bring a portable heater/fan to your room as soon as possible."]],

 #  --------------------------------------------------------------------------------------------------------------  
   #Room_Service_Chatbot
 #  --------------------------------------------------------------------------------------------------------------  

#["Good Morning Chat... i'd like to order in my breakfast", 
 #[" Sure! would you like to see our breakfast menu."]],

#  -------------------------------------------------------------------------------------------------------------- 

["Good Morning Chat... i'd like to order in my breakfast", 
 [" Sure thing! please select a number based on the breakfast of choice from our menu."]],

 #  -------------------------------------------------------------------------------------------------------------- 


#["Our breakfast menu is as follows:", 
 #["1. Egg Omelette(Made to order with your choice of ingredients: Egg, ham, cheese, mushrooms, onions, tomatoes, spinach) 2. Fluffy pancakes served with butter and maple syrup 3. Full English Breakfast(Scrambled eggs, sausage, bacon, baked beans, grilled tomatoes, mushrooms, and toast) 4. Cereals(Cornflakes, Rice crispys, All-brand, weetbix)"]]

 #  -------------------------------------------------------------------------------------------------------------- 

[" That's all for now", ["Thank you for using our Mission Achievers Hotel Chatbot! Have a great day!"]],


]

# Initialize the chatbot with the hotel chat patterns
hotel_chatbot = Chat(hotel_chatbot_Responses, reflections)

# Function to handle user input and display responses
def send_message():
    user_input = input_entry.get()
    if user_input.lower() == 'quit':
        root.quit()
    response = hotel_chatbot.respond(user_input)
    add_message("You: " + user_input, "user")
    add_message("Hotel Bot: " + response, "bot")
    input_entry.delete(0, tk.END)

# Function to add message bubbles to the chat box
def add_message(message, sender):
    chat_box.config(state=tk.NORMAL)
    if sender == "user":
        # Add user message with blue background
        chat_box.insert(tk.END, message + "\n")
        chat_box.tag_add("user", "end-2c linestart", "end-1c lineend")
    else:
        # Add bot message with white background
        chat_box.insert(tk.END, message + "\n")
        chat_box.tag_add("bot", "end-2c linestart", "end-1c lineend")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)  # Scroll to the end of the chat box

# Creating the GUI for the Hotel Chatbot
root = tk.Tk()
root.title("Hotel Assistant Chatbot")

# Create a scrolled text area for the chat box
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=60)
chat_box.tag_config("user", background="#ADD8E6", foreground="black", justify='right', lmargin1=50, rmargin=5)  # Blue for user
chat_box.tag_config("bot", background="#FFFFFF", foreground="black", justify='left', lmargin1=5, rmargin=50)    # White for bot
chat_box.pack(padx=10, pady=10)

# Entry widget for user input
input_entry = tk.Entry(root, width=50)
input_entry.pack(padx=10, pady=10)

# Send button to trigger the chatbot
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

# Exit button to close the application
def exit_app():
    root.quit()

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(padx=10, pady=5)

# Start the Tkinter main loop
root.mainloop()

