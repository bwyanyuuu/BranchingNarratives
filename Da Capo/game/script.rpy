# The script of the game goes in this file.
call ch0_0 from ch0
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define u = Character("[username]")

# user img
default img0 = ""
default img1 = ""

# The game starts here.
label start:
    scene bg_example

    # username
    python:
        username = renpy.input("你的名字是什麼？", length=32)
        username = username.strip()

        while not username:
            username = renpy.input("麻煩請輸入你的名字！", length=32)
            username = username.strip()

    u "我的名字是 [username]!"

    # select gender
    menu gender:
        "請問您的性別是？"
        "男":
            $ img0 = "male0.png"
            $ img1 = "male1.png"
        "女":
            $ img0 = "female0.png"
            $ img1 = "female1.png"

    image user0 = "[img0]"
    image user1 = "[img1]"

    show user0

    u "You've created a new Ren'Py game."

    u "Once you add a story, pictures, and music, you can release it to the world!"

    jump ch0_0