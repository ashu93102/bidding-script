logo = '''                                                                       
      d88b                               ,d    ""                          
     d8'`8b                              88                                
    d8'  `8b    88       88  ,adPPYba, MM88MMM 88  ,adPPYba,  8b,dPPYba,   
   d8YaaaaY8b   88       88 a8"     ""   88    88 a8"     "8a 88P'   `"8a  
  d8""""""""8b  88       88 8b           88    88 8b       d8 88       88  
 d8'        `8b "8a,   ,a88 "8a,   ,aa   88,   88 "8a,   ,a8" 88       88  
d8'          `8b `"YbbdP'Y8  `"Ybbd8"'   "Y888 88  `"YbbdP"'  88       88 
'''
logo_hammer = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo)
print(logo_hammer)
name_list = {}

def new_dic(name, bid):
    name_list[name] = bid

bidding = True

while bidding:
    person_name = input("what is your name\n")
    bid_price = int(input("What amount do you wanna bid\n"))
    new_dic(person_name, bid_price)

    other_bidder = input("Is there are other people who want to bid? Type yes or no\n").lower()

    if other_bidder == "no":
        bidding = False
        max_bid = max(zip(name_list.values(), name_list.keys()))[1]
        max_bid_value = max(zip(name_list.values(), name_list.keys()))[1]
        print(f"The winner of bidding is {max_bid} with a total bid of ${name_list[max_bid_value]}")
    elif other_bidder == "yes":
        bidding = True
    else:
        print("You have enetered wrong inpit. Try again later")
        break



