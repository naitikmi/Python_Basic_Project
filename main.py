import random 

subjects = [
    "Hrithik Roshan",
    "A Bull",
    "A Group Of White Horses",
    "Donald Trump",
    "Carryminati",
    "Yogi Adityanath",
    "Gautam Gambhier",
]

actions = [
    "dances",
    "eating",
    "walking on",
    "speaking",
    "orders",
    "celebrates with",
    "trolls on",
]

places_or_things = [
    "mumbai local train",
    "a red fort",
    "in a pond",
    "china wall",
    "effel tower",
    "in wankhade stadium",
    "twitter and instagram",
]

while True : 
    subject = random.choice(subjects)
    action =  random.choice(actions)
    object =  random.choice(places_or_things)

    headline = f"Breaking News : {subject} {action} {object}"
    print("\n" + headline)

    user_input = input("\n Do you want another Headline ? (Yes/No)").strip().lower()

    if user_input == "no" :
       break

print("\n Thanks for using Fake News Generator")