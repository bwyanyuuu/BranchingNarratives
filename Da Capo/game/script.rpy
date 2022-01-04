# import labels
call ch0_0 from ch0
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# define chapter = Character(None, window_xalign=0.5, what_text_align=0.5,  text_xpos=0.5)

define q = Character("???")     #第二章不知名魔物
define qc = Character("???")   #第一章切羅出登場
define u = Character("[username]", image = "user")
define coll = Character("[college]", image = "college")
define c = Character("切羅", image = "cello")
define shm = Character("雙胞胎男")
define shf = Character("雙胞胎女")
define n = Character("尼爾")
define s = Character("桑杰斯")



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
            $ img_usr = "female0.png"
            $ img_susr = "side female0.png"
            $ img_coll = "male1.png"
            $ img_scoll = "side male1.png"
            $ college = "艾弗利"

    # init after gender selected
    image user = "[img_usr]"
    image side user = "[img_susr]"
    image college = "[img_coll]"
    image side college = "[img_scoll]"
    image cello = "cello.jpg"
    image side cello = "side cello.jpg"
    image hand = "hand injury.jpg"

    jump ch0_0

   