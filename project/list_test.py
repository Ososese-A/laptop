import random

easy_riddles = [["What has to be broken before you can use it?","An egg"],
                ["Iʼm tall when Iʼm young, and Iʼm short when Iʼm old. What am I?","A candle"],
                ["What month of the year has 28 days?","All of them"],
                ["What is full of holes but still holds water?", " A sponge"],
                ["What is always in front of you but canʼt be seen?", "The future"],
                ["What goes up but never comes down?", "Your age"],
                ["A man who was outside in the rain without an umbrella or hat didnʼt get a single hair on his head wet. Why?", "He was bald"],
                ["I shave every day, but my beard stays the same. What am I?", "A barber"],
                ["You walk into a room that contains a match, a kerosene lamp, a candle and a fireplace. What would you light first", "The match"],
                ["A man dies of old age on his 25 birthday. How is this possible?", "He was born on February 29"],
                ["I have branches, but no fruit, trunk or leaves. What am I?", "A bank"],
                ["What canʼt talk but will reply when spoken to?", "An echo"],
                ["The more of this there is, the less you see. What is it?", "Darkness"]]
ron_jokes =  ["Damn, you must disrespect yourself so hard", 
              "I guess this is really what you are.",
              "Mashalla, you must be kidding."
]

random_index = random.randint(0, len(easy_riddles) - 1)

# print("Random index:", random_index)
quest = "Riddle:" + " " + str(easy_riddles[random_index][0])
print(quest)







































