from customtkinter import *
from PIL import Image
import tkinter
import random

set_appearance_mode("System")

root = CTk()
root.geometry("900x660")






game_bg_1a = "#1a1a1a"
xoxma_normal = "xoxma_face.png"
heading_size = 40
txt_family = "Arial"
txt_size = 16
txt_color_g = "#A3FDA1"
txt_color_p = "#925FF0"
title_size= 22
radio_txt_size =13
radio_color_g = "#A3FDA1"
btn_color_g ="#A3FDA1"
btn_hover_color_a ="#4E515C"
border_color_g ="#A3FDA1"
border_color_p ="#925FF0"
dis_txt = "The purpose of the game is not \n\nto determine your real IQ. \n\nThis is all for entertainment purposes \n\nand it is not meant to offend anyone. \n\nAll characters met in the game are fictional\n\n and any matches are just a coincidence..."
ins_txt = "You have 3 lives. \n\nyou have to choose anyone of the given \n\ncharacters that you relate with. \n\nAfter that you will be given riddles to answer\n\n and for each riddle you get right \n\nyou get some IQ point but \n\nfor each you get wrong you loose \n\nsome IQ points and 1 of your lives."
#10 questions for future game






lvl_1_4 = [
    ["What has to be broken before you can use it?","An egg"],
    ["Iʼm tall when Iʼm young, \nand Iʼm short when Iʼm old. \nWhat am I?","candle"],
    ["What month of the year has 28 days?","All"],
    ["What is full of holes but still\n holds water?","sponge"],
    ["What is always in front of you \nbut canʼt be seen?","The future"],
    ["What goes up but never comes down?","Your age"],
    ["A man who was outside in the rain\n without an umbrella or hat \n and he didnʼt get a single hair\n on his head wet. Why?","He was bald"],
    ["I shave every day, \nbut my beard stays the same. \nWhat am I?","A barber"],
    ["You walk into a room that contains a match,\n a kerosene lamp, a candle and a fireplace. \nWhat would you light first?","The match"],
    ["What canʼt talk but will reply when spoken to?","An echo"],
    ["Davidʼs parents have three sons: \nSnap, Crackle, \nwhatʼs the name of the third son?","David"],
    ["I follow you all the time and \ncopy your every move, \nbut you canʼt touch me or catch me. \nWhat am I?","Your shadow"],
    ["What invention lets you look right through a wall?","A window"],
    ["If youʼre running in a race and\n you pass the person in second place,\n what place are you in?","Second place"],
    ["It belongs to you, but \nother people use it more than you do.\n What is it?","Your name"],
    ["What has legs, but doesnʼt walk?", "A table"]
]


lvl_5_8 = [
    ["I am an odd number. \nTake away a letter and I become even. \nWhat number am I?","Seven"],
    ["What has four wheels and flies?","A garbage truck"],
    ["You see a boat filled with people, \nyet there isnʼt a single person on board. \nHow is that possible?","All the people on the boat are married"],
    ["The more of this there is,\n the less you see. What is it?","Darkness"],
    ["If youʼve got me, \nyou want to share me; if you share me,\n you havenʼt kept me. \nWhat am I?","A secret"],
    ["Iʼm light as a feather, \nyet the strongest person canʼt \nhold me for five minutes. \nWhat am I?","Your breath"],
    ["What building has the most stories?","The library"],
    ["A man dies of old age on his 25 birthday. \nHow is this possible?","He was born on February 29"],
    ["Where does today come before yesterday?","The dictionary"],
    ["Which is heavier: a ton of bricks or a ton of feathers?","Neither—they both weigh a ton"],
    ["What has words, but never speaks?","A book"],
    ["Two fathers and two sons are in a car, \nyet there are only three people\n in the car. How?","They are a grandfather, father and son."],
    ["A man describes his daughters, saying, \nThey are all blonde, but two;\n all brunette but two; \nand all redheaded but two. \nHow many daughters does he have?","Three"],
    ["What five-letter word becomes shorter\n when you add two letters to it?","Short"],
    ["You see me once in June, \ntwice in November and not at all in May. \nWhat am I?","The letter e"],
    ["What 4-letter word can be written forward, \nbackward or upside down, \nand can still be read from left to right?","NOON"],
    ["Where does one wall meet the other wall?","On the corner"],
    ["What has a head and a tail but no body?","A coin"]
]


lvl_9_10 = [
    ["Forward I am heavy, but backward I am not. \nWhat am I?","The word “not”"],
    ["A girl has as many brothers as sisters, \nbut each brother has only\n half as many brothers as sisters. \nHow many brothers and sisters are\n there in the family?","Four sisters and three brothers"],
    ["What does man love more than life, \nhate more than death or mortal strife; \nthat which contented men desire; \nthe poor have, the rich require; \nthe miser spends, the spendthrift saves, \nand all men carry to their graves?","Nothing"],
    ["I have lakes with no water, \nmountains with no stone and cities with no buildings. \nWhat am I?","A map"],
    ["A man looks at a painting in a museum and says, \n“Brothers and sisters I have none, \nbut that manʼs father is my fatherʼs son.” Who isin thepainting?","The manʼs son"],
    ["What goes through cities and fields,\n but never moves?","A road"],
    ["I am always hungry and will die if not fed,\n but whatever I touch will soon turn red. \nWhat am I?","Fire"],
    ["The person who makes it has no need of it; \nthe person who buys it has no use for it. \nThe person who uses it can neither see nor feel it. \nWhat is it?","A coffin"],
    ["The more you take, the more you leave behind. \nWhat are they?","Footsteps"],
    ["Speaking of rivers, \na man calls his dog from \nthe opposite side of the river. The dog crosses the river without getting wet, \nand without using a bridge or boat. \nHow?","The river was frozen"],
    ["If you drop me Iʼm sure to crack, \nbut give me a smile and Iʼll always smile back. \nWhat am I?","A mirror"],
    ["What can fill a room but takes up no space?","Light"]
]


lvl_bonus = [
    ["With pointed fangs I sit and wait; \nwith piercing force I crunch out fate; \ngrabbing victims, proclaiming might; \nphysically joining with a single bite. \nWhat am I?","A stapler"],
    ["What is 3/7 chicken, 2/3 cat and 2/4 goat?","Chicago"],
    ["The day before yesterday I was 21, \nand next year I will be 24.\n When is my birthday?","December 31; today is January 1"],
    ["I turn once, what is out will not get in. \nI turn again, what is in will not get out. \nWhat am I?","A key"],
    ["People make me, save me, change me, raise me. \nWhat am I?","Money"],
    ["What breaks yet never falls, \nand what falls yet never breaks?","Day, and night"],
    ["What tastes better than it smells?","Your tongue"],
    ["What three numbers, none of which is zero, \ngive the same result whether theyʼre \nadded or multiplied?","One, two and three"],
]

selection_quest_ron = [
    "You are just a lucky one","That's a shame that you chose Ron and still failed the riddle"
]

selection_p_f_quest_toddler = ["I mean, \nthis on is suppused to be easy, \nso don't be happy about this",
"Hmm... This one was hard for you?\n I don't know what I'm suppose to do with you then"]

selection_p_f_quest_procrastinator = ["Good, good. Good enough...","Wow! not only the work you doing is slow, \nbut your brain itself is slow"]

selection_p_f_quest_gollum = ["We are happy, Gollum is smart.","Oh no, this is not good for Gollum."]

selection_p_f_quest_weekend = ["You have kept your plank, but its not for a long time.","Maybe it's just a mistake, maybe you are a liar."]


correct_quest_ron = ["Do you bet that your brain capacity is bigger than Rons'?\n Then try the next riddle","I think you got help from Harry", "And again the luck is on your side", "Good job! i guess...", "Come on, make it faster", "I think you are getting better,\n i think..."]

correct_quest_toddler = ["Ohh, who is a good baby, do you want a candy?","Look honney, baby is takinging his first steps","Wow, your success is almost as surprising as\n the fact that I didn't see it coming","Oh no, it's growing to fast","Maybe you were just typing random words and got lucky?","I can see you are surprised \nas me that you did right"]

correct_quest_procrastinator = ["Yey, you answered the question on time,\n not that we had a timer on it, \nbut congrats!","Thinking is time and energy consuming,\n but you finaly did a sacrifice.","Finaly you started to do some brain activity.","My congratulations. \nHopefully, this will become something\n more than just an","excuse to spend another evening \non something not very important.","The only value you giving to the world\n is right answer on God forgotten riddle","quiz.","It's good, but we could wait more, \nwe have plenty of time."]

correct_quest_gollum = ["Precious solver, yes. \nSmarter than those stupid fat hobbitses.","Gollum is happy.","Masterful! \nYou unraveled the mystery, \njust like Smeagol with the precious,\n yes.","Well done,\n precious! Unraveled the secret, you did. \nSmarter than them all.","Master solver, yes. \nEven Gollum impressed, we are. \nClever little thing, aren't we","Found the answer, did we?\n Clever as a wily hobbit,\n not as stupid as the"]

correct_quest_weekend = ["Congratulations. \nAnother step forward. \nTime will tell if it was worth it.","A new reason for congratulations. \nWho would have thought that \nthese events could be so exciting.","Look at you, the master codebreaker. \nWho knew you had it in you?","Congratulations on solving the mystery. \nIt's not like anyone was\n losing sleep over it, but hey, \ngood job.","Solved the riddle, did you?\n I suppose every mind needs a little exercise, \neven if it's just once in a while.","Well played, Sherlock. \nI hope solving the riddle brought you \nthe intellectual satisfaction you were seeking."]


wrong_quest_ron = ["Nice try","Oh no, how did that happened?","I guess that's the way we do it.","Hermione won't help you this time.","Minus 50 points from Gryffindor.","Should've go to Slitherin."
]

wrong_quest_toddler = [ "Nice try.","Someone needs to change their diaper.","Someone needs to sleep.","I think our baby is doing something wrong,\n we need to give him more attention.","Don't worry, you are just a special child.","It doesn't matter,\n when you will grow up you figure it out."]

wrong_quest_procrastinator = ["Nice try.","You've really perfected\n the art of doing the bare minimum. \nIt's impressive in its own way.","You might not have nailed it this time, \nbut at least you're consistent.","Consistently not hitting the mark.","Don't worry about this, \nyou're becoming quite an \nexpert at handling disappointment. \nIt's almost impressive.","Another failed attempt? \nIt's like you have a natural talent for \nmaking things more challenging \nthan they need to be.","Yeah, just let it go. \nThere is no time to think that long."]

wrong_quest_gollum = ["Nice try.","Your precious just got stolen from Frodo.","Let's give your second personality a try.","Your desicion making is almost \nfasinating as Baggins not telling\n the Gendalf about the ring.","I think the gollum is seeing you now not\n as friend but as a food.","Gollum is not happy."]

wrong_quest_weekend = ["Nice try.","I admire your confidence to speak up. \nIt's almost like you believe every \nidea is a good one.","You always have the most fascinating ideas. \nI never would have thought of \nthat in a million years.","Congratulations on yet another failed attempt. \nThey say practice makes perfect,\n but I guess that's just a saying.","Cheer up! \nNot everyone can boast such a remarkable \nseries of not-quite-success stories. \nYou're in a league of your own.","Your outcomes remain unpredictable, \na genius experiment in a realm\n beyond comprehension."]




outro_high_equal_low = [["I guess it's possible to jump over your own head","You need to try harder","No surprise"],
                        ["Impressive, you just proved that \nyou more clever than a toddler","Agree, the progression will wait","Amazing, it's surprising me, \nhow disappointing you can be"],
                        ["What a relief when you got something right, \nfinally your relatives can be truely happy for you.","Yeah keep everything same as before,\n no need to be better.","You have to stop it, i mean don't stop. \nstart to do something already,\n go read some book idk."],
                        ["Good job, defended our precious, we are.","Frodo got away with the robbery of our preciuos.","Frodo took our precious and threw it \nINTO THE LAVA!!"],
                        ["You proved that you are megamind, \nthe quiz doesn't desrve you.","It's impresive that you stayed on that level,\n but we dont have any prises.\n the only prise you got is increased ego.","You know its bad when you giving someone a false hope. \nnext time make choices more wisely."]]








#this is for all the frames
start = CTkFrame(master=root, fg_color=game_bg_1a, border_color=btn_color_g, border_width=4)
start.pack(pady=20, padx=60, fill="both", expand=True)

disclaimer = CTkFrame(master=root, fg_color=game_bg_1a, border_color=btn_color_g, border_width=4)

instruction = CTkFrame(master=root, fg_color=game_bg_1a, border_color=btn_color_g, border_width=4)

characterArea = CTkFrame(master=root, fg_color=game_bg_1a, border_color=btn_color_g, border_width=4)

game_Board = CTkFrame(master=root, fg_color=game_bg_1a, border_color=btn_color_g, border_width=4)

end_frame = CTkFrame(master=root, fg_color=game_bg_1a, border_color=btn_color_g, border_width=4)


radio_var = tkinter.IntVar(characterArea, value=0)

def set_init_score(score):
    game_box_score.configure(text=f"IQ Score: {score}")
    get_question()
    renew_values()

def check_lives():
    #visual error, should end when zero, either answere is correct or not it will end the game. we have check the state before giving the riddle or at last wrong answere
    if lives_left  == 0:
        end_comment.configure(text=f"Your IQ score is {score_now}")
        game_end()
    else:
         pass
    
def renew_values():   
    global score_label_value
    score_label_value = str(game_box_score.cget("text"))
    print(score_label_value)
    global score_now
    score_now = int(score_label_value[9:])
    # global init_lvl
    # init_lvl = int(game_box_lvl_txt[9:])
    print(score_now)
    global new_score 
    new_score =  0
    lives = str(game_box_lives.cget("text"))
    global lives_left
    lives_left = int(lives[11:])
          

    

def get_question():
    renew_values()
    if score_now > 1 and score_now < 97:
        get_random_riddle(lvl_1_4)
    elif score_now >= 97 and score_now < 161:
        get_random_riddle(lvl_5_8)
    elif score_now >= 161:
        get_random_riddle(lvl_9_10)




def get_random_riddle(lst):
    global real_ans
    random_index = random.randint(0, len(lst) - 1)
    res = "Riddle:" + " " + str(lst[random_index][0])
    real_ans = str(lst[random_index][1]).lower()
    game_box_riddle.configure(text=res)




def get_random_joke(lst):
    random_index = random.randint(0, len(lst) - 1)
    res = str(lst[random_index])
    game_box_comment.configure(text=res)
     
def get_random_joke_correct():
    if radio_var.get() == 1:
        get_random_joke(correct_quest_ron)
    elif radio_var.get() == 2:
        get_random_joke(correct_quest_toddler)

    elif radio_var.get() == 3:
        get_random_joke(correct_quest_procrastinator)

    elif radio_var.get() == 4:
        get_random_joke(correct_quest_gollum)
    
    elif radio_var.get() == 5:
        get_random_joke(correct_quest_weekend)
     
def get_random_joke_wrong():
    if radio_var.get() == 1:
        get_random_joke(wrong_quest_ron)
    elif radio_var.get() == 2:
        get_random_joke(wrong_quest_toddler)

    elif radio_var.get() == 3:
        get_random_joke(wrong_quest_procrastinator)

    elif radio_var.get() == 4:
        get_random_joke(wrong_quest_gollum)
    
    elif radio_var.get() == 5:
        get_random_joke(wrong_quest_weekend)



def check_answer():
    check_lives()
    if compare_answers() == True:
        add_points(score_now)
        get_question()
        renew_values()
    else:
        minus_points(score_now)
        reduce_lives()
        get_question()
        renew_values()
         
def close_game ():    
     root.destroy()

def compare_answers():
    correct=""
    ans = game_box_answer.get().lower()
    print(ans)
    ans_b = ans.split()
    real_ans_b = real_ans.split()
    print(ans_b)
    print(real_ans)
    print(real_ans_b)
    for i in range(len(ans_b)):
        if ans_b[i] in real_ans_b:
            correct = True
            print(correct)
        else: 
            correct = False
            print(correct)
    print(correct)
    if correct == True:
         return True
    else:
        return False
     
        
def reduce_lives():
     new_lives_left = lives_left - 1
     game_box_lives.configure(text=f"Lives Left: {new_lives_left}")

def add_points(score_now):
    get_random_joke_correct()
    if score_now > 1 and score_now < 97:
            points= 50
            new_score = score_now + points
            
    elif score_now >= 97 and score_now < 161:
            points = 40
            new_score = score_now + points
    elif score_now >= 161:
            points = 25
            new_score = score_now + points
    score_now = new_score
    game_box_score.configure(text=f"IQ Score: {new_score}")

def minus_points (score_now):
    get_random_joke_wrong()
    renew_values()
    if score_now > 1 and score_now < 97:
            points= int(score_now//(100//50))
            new_score = score_now - points
    elif score_now >= 97 and score_now < 161:
            points = int(score_now//(100//20))
            new_score = score_now - points
    elif score_now >= 161:
            points = int(score_now//(100//10))
            new_score = score_now - points
        
    score_now = new_score
    game_box_score.configure(text=f"IQ Score: {new_score}")


    
    

def radiobutton_event():
    if radio_var.get() == 1:
        joke =""
        ron_jokes =  ["Damn, you must disrespect yourself so hard", 
              "I guess this is really what you are.",
              "Mashalla, you must be kidding."]
        random_index = random.randint(0, len(ron_jokes) - 1)
        joke = str(ron_jokes[random_index])
        comment.configure(text=f"You are Ron from Harry Potter\n\n\"{joke}\"")
        set_init_score(50)
        

    elif radio_var.get() == 2:
        joke =""
        toddler_jokes =  ["Respect the toddler, he is better than you.",
                      "We all knew that you needed someone to look after you.",
                      "At least you know your place."]
        random_index = random.randint(0, len(toddler_jokes) - 1)
        joke = str(toddler_jokes[random_index])
        comment.configure(text=f"You are just a Toddler\n\n\"{joke}\"")
        set_init_score(71)

    elif radio_var.get() == 3:
        joke =""
        procrastinator_jokes =  ["Agree, the project itself should be\n done the day before the deadline",
                      "From tomorrow morning we are all\n capable of doing anything. \nBut only of tomorrow is Monday 1st January",
                      "Solving the riddle? Well, \nthat's one way to spend your time, \nI suppose."]
        random_index = random.randint(0, len(procrastinator_jokes) - 1)
        joke = str(procrastinator_jokes[random_index])
        comment.configure(text=f"So You're a Procrastinator,\n\n\"{joke}\"")
        set_init_score(91)

    elif radio_var.get() == 4:
        joke =""
        gollum_jokes =  ["I think you're overestimating yourself.",
                      "I see you have high self-esteem,\n let's put you on your place.",
                      "Are you sure about this?"]
        random_index = random.randint(0, len(gollum_jokes) - 1)
        joke = str(gollum_jokes[random_index])
        comment.configure(text=f"You are Gollum from Lord of the rings,\n\n\"{joke}\"")
        set_init_score(121)
    
    elif radio_var.get() == 5:
        joke =""
        weekend_jokes =  ["I can't imagine how you live\n With this big brain \n(either you are smart or \nyou have a megalocephaly).",
                      "You are not guy pal, you are not that guy.",
                      "Interesting..."]
        random_index = random.randint(0, len(weekend_jokes) - 1)
        joke = str(weekend_jokes[random_index])
        comment.configure(text=f"Good to know you write code \nduring the weekends,\n\n\"{joke}\"")
        set_init_score(161)




def start_dis():
    start.pack_forget()
    disclaimer.pack(pady=20, padx=60, fill="both", expand=True)

def dis_ins():
    disclaimer.pack_forget()
    instruction.pack(pady=20, padx=60, fill="both", expand=True)

def ins_char():
    instruction.pack_forget()
    characterArea.pack(pady=20, padx=60, fill="both", expand=True)

def char_game():
    if radio_var.get() == 0 or radio_var.get() == None:
        comment.configure(text=f"\"No character selected yet, \nyou better pick someone good\"")
        
    else:
        characterArea.pack_forget()
        game_Board.pack(pady=20, padx=60, fill="both", expand=True)

def game_end():
    game_Board.pack_forget()
    end_frame.pack(pady=20, padx=60, fill="both", expand=True)

def end_start():
    end_frame.pack_forget()
    start.pack(pady=20, padx=60, fill="both", expand=True)





#THIS IS ALL FOR THE START FRAME
game_title = CTkLabel(master=start, text="XOXMA", font=(txt_family,heading_size), text_color=txt_color_p)
game_title.place(relx=0.5, rely=0.2, anchor="center")

# Open the image file and create a CTkImage instance
button_image = CTkImage(Image.open(xoxma_normal), size=(180, 280))

# Create a CTkButton with the image
image_button = CTkButton(master=start, image=button_image, text="" ,fg_color="transparent", hover_color=game_bg_1a)

# Place the button into the window
image_button.place(relx=0.5, rely=0.55, anchor="center")

start_btn = CTkButton(master=start, text="          PLAY          ",font=(txt_family,txt_size), text_color=txt_color_g, fg_color=game_bg_1a,hover_color=btn_hover_color_a, border_color=btn_color_g, border_width=2, command=start_dis,)
start_btn.place(relx=0.5, rely=0.9, anchor="center")








#THIS IS ALL FOR THE DISCLAIMER FRAME
disclaimer_title = CTkLabel(master=disclaimer, text="DISCLAIMER:", font=(txt_family,title_size), text_color=txt_color_p)
disclaimer_title.place(relx=0.5, rely=0.1, anchor="center")

disclaimer_txt = CTkLabel(master=disclaimer, text=dis_txt, font=(txt_family,txt_size), text_color=txt_color_p)
disclaimer_txt.place(relx=0.5, rely=0.5, anchor="center")

disclaimer_btn = CTkButton(master=disclaimer, text="     I UNDERSTAND     ",font=(txt_family,txt_size), text_color=txt_color_g, fg_color=game_bg_1a,hover_color=btn_hover_color_a, border_color=btn_color_g, border_width=2, command=dis_ins)
disclaimer_btn.place(relx=0.5, rely=0.9, anchor="center")






#THIS IS ALL FOR THE INSTRUCTIONS FRAME
instruction_title = CTkLabel(master=instruction, text="INSTRUCTIONS:", font=(txt_family,title_size), text_color=txt_color_p)
instruction_title.place(relx=0.5, rely=0.1, anchor="center")

instruction_txt = CTkLabel(master=instruction, text=ins_txt, font=(txt_family,txt_size), text_color=txt_color_p)
instruction_txt.place(relx=0.5, rely=0.5, anchor="center")

instruction_btn = CTkButton(master=instruction, text="     I UNDERSTAND     ",font=(txt_family,txt_size), text_color=txt_color_g, fg_color=game_bg_1a,hover_color=btn_hover_color_a, border_color=btn_color_g, border_width=2, command=ins_char)
instruction_btn.place(relx=0.5, rely=0.9, anchor="center")





#THIS IS ALL FOR THE CHARACTER AREA FRAME
character_title = CTkLabel(master=characterArea, text="CHOOSE YOUR CHARACTER:", font=(txt_family,title_size), text_color=txt_color_p)
character_title.place(relx=0.5, rely=0.1, anchor="center")

char_1 = CTkRadioButton(master=characterArea, text_color=txt_color_p, text="Ron                                  .",font=(txt_family,radio_txt_size), fg_color=radio_color_g, hover_color=radio_color_g, command=radiobutton_event, variable=radio_var, value=1)
char_2 = CTkRadioButton(master=characterArea, text_color=txt_color_p, text="Todler                              .",font=(txt_family,radio_txt_size), fg_color=radio_color_g, hover_color=radio_color_g, command=radiobutton_event, variable=radio_var, value=2)
char_3 = CTkRadioButton(master=characterArea, text_color=txt_color_p, text="Procrastinator!!!             .",font=(txt_family,radio_txt_size), fg_color=radio_color_g, hover_color=radio_color_g, command=radiobutton_event, variable=radio_var, value=3)
char_4 = CTkRadioButton(master=characterArea, text_color=txt_color_p, text="Gollum                             .",font=(txt_family,radio_txt_size), fg_color=radio_color_g, hover_color=radio_color_g, command=radiobutton_event, variable=radio_var, value=4)
char_5 = CTkRadioButton(master=characterArea, text_color=txt_color_p, text="The Weekend coder        .",font=(txt_family,radio_txt_size), fg_color=radio_color_g, hover_color=radio_color_g, command=radiobutton_event, variable=radio_var, value=5)

char_1.place(relx=0.5, rely=0.18, anchor="center")
char_2.place(relx=0.5, rely=0.26, anchor="center")
char_3.place(relx=0.5, rely=0.35, anchor="center")
char_4.place(relx=0.5, rely=0.44, anchor="center")
char_5.place(relx=0.5, rely=0.54, anchor="center")

characterComment = CTkFrame(master=characterArea, fg_color="transparent", width=700, height=140, border_width=4, border_color=border_color_p)
characterComment.place(relx=0.5, rely=0.73, anchor="center")

# Open the image file and create a CTkImage instance
comment_image = CTkImage(Image.open(xoxma_normal), size=(56, 96))
image = CTkButton(master=characterComment, image=comment_image, text="" ,fg_color="transparent", hover_color=game_bg_1a)
image.place(relx=0.2, rely=0.5, anchor="center")

comment = CTkLabel(master=characterComment, text="\"You need to select a \ncharacter to play the game\"", font=(txt_family,txt_size), text_color=txt_color_g)
comment.place(relx=0.56, rely=0.5, anchor="center")

char_area_btn = CTkButton(master=characterArea, text="    I CHOOSE THIS CHARACTER    ",font=(txt_family,txt_size), text_color=txt_color_g, fg_color=game_bg_1a,hover_color=btn_hover_color_a, border_color=btn_color_g, border_width=2, command=char_game)
char_area_btn.place(relx=0.5, rely=0.9, anchor="center")





#FOR THE GAME BOARD FRAME
top_game_box = CTkFrame(master=game_Board, fg_color="transparent", width=700, height=96, border_width=4, border_color=border_color_g)
top_game_box.place(relx=0.5, rely=0.2, anchor="center")

game_box_score = CTkLabel(master=top_game_box, text="iq_score", font=(txt_family,txt_size), text_color=txt_color_g)
game_box_score.place(relx=0.1, rely=0.5, anchor="center")

game_box_lvl_txt = CTkLabel(master=top_game_box, text="QUESTION", font=(txt_family,txt_size), text_color=txt_color_g)
game_box_lvl_txt.place(relx=0.5, rely=0.5, anchor="center")

game_box_lives = CTkLabel(master=top_game_box, text="Lives Left: 3", font=(txt_family,txt_size), text_color=txt_color_g)
game_box_lives.place(relx=0.9, rely=0.5, anchor="center")


game_box_riddle = CTkLabel(master=game_Board, text='Riddle: A man describes his daughters, saying, \n“They are all blonde, but two;\n all brunette but two; \nand all redheaded but two.” \nHow many daughters does he have?","Three: A blonde, a brunette and a redhead"', font=(txt_family,txt_size), text_color=txt_color_p)
game_box_riddle.place(relx=0.5, rely=0.41, anchor="center")

game_box_answer = CTkEntry(master=game_Board, placeholder_text="Your Answer goes here", width=300, font=(txt_family,txt_size), height=50, text_color=txt_color_g, placeholder_text_color=txt_color_g,border_color=border_color_p)
game_box_answer.place(relx=0.35, rely=0.58, anchor="center")

game_box_btn = CTkButton(master=game_Board, text="    THAT'S MY ANSWER    ",font=(txt_family,txt_size), text_color=txt_color_g, fg_color=game_bg_1a,hover_color=btn_hover_color_a, border_color=btn_color_g, border_width=2, command=check_answer)
game_box_btn.place(relx=0.68, rely=0.58, anchor="center")


bottom_game_box = CTkFrame(master=game_Board, fg_color="transparent", width=700, height=140, border_width=4, border_color=border_color_p)
bottom_game_box.place(relx=0.5, rely=0.75, anchor="center")

game_box_image = CTkImage(Image.open(xoxma_normal), size=(56, 96))
game_box = CTkButton(master=bottom_game_box, image=game_box_image, text="" ,fg_color="transparent", hover_color=game_bg_1a)
game_box.place(relx=0.2, rely=0.5, anchor="center")

game_box_comment = CTkLabel(master=bottom_game_box, text="\"Xoxma in english is pronounced as khokhma\"", font=(txt_family,txt_size), text_color=txt_color_p)
game_box_comment.place(relx=0.56, rely=0.5, anchor="center")

game_play_btn = CTkButton(master=game_Board, text="    EXIT    ",font=(txt_family,txt_size), text_color=txt_color_g, fg_color=game_bg_1a,hover_color=btn_hover_color_a, border_color=btn_color_g, border_width=2, command=game_end)
game_play_btn.place(relx=0.5, rely=0.9, anchor="center")





#FOR THE END FRAME
end_comment = CTkLabel(master=end_frame, text="GOODbye", font=(txt_family,heading_size), text_color=txt_color_p)
end_comment.place(relx=0.5, rely=0.2, anchor="center")

# Open the image file and create a CTkImage instance
button_image = CTkImage(Image.open(xoxma_normal), size=(180, 280))

# Create a CTkButton with the image
image_button = CTkButton(master=end_frame, image=button_image, text="" ,fg_color="transparent", hover_color=game_bg_1a)

# Place the button into the window
image_button.place(relx=0.5, rely=0.55, anchor="center")

start_btn = CTkButton(master=end_frame, text="          ARE YOU FINNISH?          ",font=(txt_family,txt_size), text_color=txt_color_g, fg_color=game_bg_1a,hover_color=btn_hover_color_a, border_color=btn_color_g, border_width=2, command=close_game,)
start_btn.place(relx=0.5, rely=0.9, anchor="center")


root.mainloop()