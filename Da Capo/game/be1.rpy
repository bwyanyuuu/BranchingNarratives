
label be1_0:
    # chapter transition
    scene bg black with fade
    show text "{size=+36}{font=temingti.ttf}結局 《錯用正義》{/font}{/size}" at truecenter with fade
    pause 1.0
    scene bg black with Dissolve(0.5)

    scene bg street
    show cello
    "錯不了的，在歷史上迪弗爾最明顯就是它那詭異的第三隻眼睛，充滿著混沌與黑暗。"
    "我既然都時間回溯到了這裡，還遇上了迪弗爾，我就不能放著之後會發生的大屠殺不管。"
    u "你停下吧！屠殺這裡的人對你有什麼好處。"
    c "你以為我是是因為好玩嗎？一切只不過是為了活下去而已。"
    "看來要這麼阻止它是不可能的了，那現在我必除之而後快！"
    u "那我絕不能讓你逞心如意！"
    "說完剛要發動魔法，就見切羅對著我詭異的笑了笑。"
    c "你確定？你改變不了什麼的......。"
    hide cello with dissolve
    "一說完，切羅便化為一道煙霧消失的無影無蹤。"
    u "跑了......。"

    scene bg black with dissolve
    "迪弗爾的強大是歷史上詳細記載過的，要阻止它也沒這麼簡單。"
    "接下來的幾年裡，各地的魔物開始向人類侵襲，而我也在監視著魔王的一舉一動，屢屢破壞許多它們計劃的行動。"
    "魔物在我的頻頻干擾下整體戰力下滑，人類的傷亡並沒有歷史上這麼的嚴重，人們在這場戰爭中漸漸處於上風。"
    "終於在某次精心計畫下，我帶著一個小隊的人，成功剿滅了迪弗爾。"

    scene bg forest with dissolve
    show cello eye
    u "終於將你打敗了......！"
    c eye "你...把我殺了...也...改變...不了這一切的......。"
    
    scene bg black with fade
    with Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=2.0)
    
    "就在迪弗爾斷氣的那一刻，我眼前的世界開始分裂成一個個小碎片，一點點的消失。\n而我也控制不了我的身體，四肢慢慢散落、消逝......，眼前的黑暗逐漸吞噬我。"
    "世界崩壞來臨時我開始飛速地思考，到底是什麼造成這樣的結果，我究竟做錯了哪一步？"
    "改變歷史本身就是大錯特錯的......，改變了歷史上的重大事件，造成我來自的那個未來被傾覆，存在上出現嚴重的矛盾。"
    "......\n或許是這樣吧？在被完全吞噬前的那一刻，我這麼想著......。"

    scene bg black with fade
    show text "{size=+36}{font=temingti.ttf}Game Over{/font}{/size}" at truecenter with fade
    pause 1.0
    scene bg black with Dissolve(0.5)

    return

    



