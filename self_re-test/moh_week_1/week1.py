import customtkinter as CTKFrame

CTKFrame.set_appearance_mode("System")

pixelFrame = CTKFrame.CTk()
pixelFrame.geometry("1440x1024")

top_game_box = CTKFrame.CTkFrame(master=pixelFrame, fg_color="transparent", width=700, height=96, border_width=4, border_color="#f1f1f1")
top_game_box.place(relx=0.5, rely=0.2, anchor="center")

game_box_score = CTKFrame.CTkLabel(master=top_game_box, text="iq_score", font=('Arial', 24), text_color="#00ff00")
game_box_score.place(relx=0.1, rely=0.5, anchor="center")

game_box_lvl_txt = CTKFrame.CTkLabel(master=top_game_box, text="QUESTION", font=('Arial', 24), text_color="#00ff00")
game_box_lvl_txt.place(relx=0.5, rely=0.5, anchor="center")


pixelFrame.mainloop()