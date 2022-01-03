# import labels
call ch0_0 from ch0
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# define chapter = Character(None, window_xalign=0.5, what_text_align=0.5,  text_xpos=0.5)
define e = Character("Eileen")
define q = Character("???")
define c = Character("切羅")
define u = Character("[username]", image = "user")
define coll = Character("[college]", image = "college")

# user define variables
default img_usr = ""
default img_susr = ""
default img_coll = ""
default img_scoll = ""

# The game starts here.
label start:
    scene bg example

    # username
    python:
        username = renpy.input("你的名字是什麼？", length=32)
        username = username.strip()

        while not username:
            username = renpy.input("麻煩請輸入你的名字！", length=32)
            username = username.strip()

    # u "我的名字是 [username]!"

    # select gender
    menu gender:
        "請問您的性別是？"
        "男":
            $ img_usr = "male0.png"
            $ img_susr = "side male0.png"
            $ img_coll = "female1.png"
            $ img_scoll = "side female1.png"
            $ college = "艾弗麗"
        "女":
<<<<<<< Updated upstream
            $ img0 = "female0.png"
            $ img1 = "female1.png"

    image user0 = "[img0]"
    image user1 = "[img1]"

    show user0

    # u "You've created a new Ren'Py game."

    # u "Once you add a story, pictures, and music, you can release it to the world!"
=======
            $ img_usr = "female0.png"
            $ img_susr = "side female0.png"
            $ img_coll = "male1.png"
            $ img_colls = "side male1.png"
            $ college = "艾弗利"

    # init after gender selected
    image user = "[img_usr]"
    image side user = "[img_susr]"
    image college = "[img_coll]"
    image side college = "[img_scoll]"
>>>>>>> Stashed changes

    jump ch0_0

   