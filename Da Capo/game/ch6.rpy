call end1_0 from end1
call end2_0 from end2
call end3_0 from end3
call end4_0 from end4
default cnt = 0
image credit = Text("{size=+8}故事文本\n\n\n\n\n\n\n\n\n\n張巧如\n\n序章 第三章 終章\nBE1 BE2 BE3\n\n\n\n\n陳書玟\n\n第一章 第四章 結局3 結局4\n\n\n\n\n陳昱喬\n\n第二章 第五章 結局1 結局2\n\n\n\n\n\n\n\n\n\n遊戲設計\n\n\n\n\n\n\n\n\n\n程式\n\n張巧如 陳書玟\n\n\n\n\n背景圖片\n\n陳書玟\n\n\n\n\n人物設計\n\n張巧如\n\n\n\n\n主視覺\n\n陳昱喬{/size}", text_align = 0.5)
transform scroll:
    xpos 0.37
    ypos 1.0
    linear 25.0 ypos -4.0
transform copyright:
    xpos 0.16
    ypos 0.95
label ch6_0:
    # chapter transition
    scene bg black with dissolve
    show text "{size=+36}{font=temingti.ttf}終章{/font}{/size}" at truecenter with dissolve
    pause 1.0
    scene bg black with Dissolve(0.5)
    scene bg white with dissolve

    # start
    u "但這裡......？"
    "時間斷崖是歐克里斯的盡頭，而這裡是時間斷崖的盡頭......\n這裡是一片虛無，沒有聲音、映入眼簾的是一片白色，也不知我否是漂浮著，但我確實能踩著往前走。"
    "對現在我要往何處去，一點頭緒也沒有，這裡沒有方向可言，而且現在我也還在這盡頭的衝擊下，茫茫的不知所措。\n水流向天空什麼的，看起已經那麼的不可思議，沒想到這水的盡頭還有另一番天地。"
    "但是這的確是人型魔物所謂的那個「打破」，我打破了天空，脫離出了時間斷崖。\n每一次場景的重複，就是所謂的「刷新」，而現在我所在的空間，難道就是造物主之地？"
    scene bg mystery
    pause 1.0
    scene bg white
    "忽然這片白色一閃，那些奇怪的符號又出現在我的眼前，我馬上仔細地端詳著。\n但是僅僅一瞬，又變回了一片白色。"
    u "這到底是......."
    "徬徨了一會兒我終於回過神來，忽然覺得剛剛的那些符號們好像有點似曾相識？"
    if hasHint:
        "我想起我在康切爾托也看過這些，並記錄在了筆記本上。\n但是這次我好像能看懂他們的意義了！"
        "我趕緊翻出我的筆記本，謹慎地看了看，我真的能讀懂了！\n難道這就是人型魔物的禮物？"
        "但是全部看完之後，裡面的內容實在是太顛覆我對世界的認知了！"
        "那一字一句全部都是在構建整個康切爾托，包括裡面的一草一木與每個生物的活動。\n而後所有世間萬物的生長與消亡，這些句子沒有去建構與限制，它就自由自在的發展而成，成就了我在康切爾托見到的一切。"
        "由於康切爾托擁有與歐克里斯極高的相似性，我推測造物主也是用像這樣一個個句子創造了歐克里斯。\n但就算我知道祂是怎麼創造我們的，我還是想不通，歐克里斯這一切的存在到底算什麼？"
        "而我到底要去哪裡找到能保護歐克里斯的方法？"
        
        menu:
            "我現在要——"
            "繼續研究那些符號的意義。":
                jump realWorld
            "找找有沒有其他的線索。":
                jump origine2
    else:
        jump origine2

label realWorld:
    "我將筆記本翻到一空白頁，將剛剛出現在一片白裡的符號，憑著腦中的印象寫了下來。\n所幸我記憶力很好，幾乎大部分都還記得，謄寫起來還算完整。"
    "我仔細的看了看，雖然有些不相同的地方，但是兩者大致上的結構是差不多的，只是歐克里斯的稍微更完整一點。\n但是其中的確有很多看起來有問題的敘述，尤其是其中有一句寫成了亂碼。"
    u "終於...找到了嗎......！"
    "我試著唸出那個亂碼，因為它太亂了，所以唸了好幾次才唸對，唸完之後才發現，那是歐克里斯裡的「墮落」的意思。"
    u "墮落......嗎？"
    "我要...怎麼墮落了？難道是要想辦法往下沉嗎？\n所以我用力地跳了起來，再狠狠地跳了下去，然後我就慢慢被白色吞沒了。"
    scene bg black with ImageDissolve("imagedissolve teleport.png", 0.5, 0)
    scene bg white with ImageDissolve("imagedissolve teleport.png", 0.5, 0)
    scene bg black with ImageDissolve("imagedissolve teleport.png", 0.5, 0)
    scene bg white with ImageDissolve("imagedissolve teleport.png", 0.5, 0)
    "接著是一陣暈眩，我眼前的白在不停地閃爍，刺激的我幾乎睜不開眼，整個人好像是被不停搖晃一般。" with hpunch
    scene bg lab with dissolve
    "過了一下子終於停了下來，暈暈呼呼的我睜開眼睛，我身處在一個奇怪的空間，這裡的一切看起來跟歐克里斯很不一樣，所有東西都沒有一條輪廓。"
    "我疑惑的看了看四周，這裡一個像生物的都沒有，倒是有各種再歐克里斯沒有見過的物品。\n環顧了一圈回到我前方，發現眼前是一個箱形物件，它以一個低頻率發出許多諾特，而且它是摺疊起來的，我忍不住將它打開來看。"
    "其中一面上面有很多小方塊但排列不是很整齊，方塊上面寫了很多我見過的奇怪符號，但他們的排列我並不能理解出什麼。"
    "而另一面是一塊黑色的色塊，但就在我打開它沒多久就整片亮了起來，上面顯示的是「請輸入密碼」，下面來有個小方塊寫著「登入」。"
    u "這是什麼東西......？"
    show student with dissolve
    "忽然一陣腳步聲傳來，一個女孩出現在我的視線裡，她的頭髮、四肢、穿著，都和我所認知的女孩不太一樣，就像是另個世界的人類。"
    "而她看到我的時候，先是疑惑了一下，然後用力揉了揉眼睛，然後雙目瞳孔放大的看著我。"
    u "那個...請問.......？"
    "忽然，她變成一臉非常驚恐的樣子，並且激動地叫了出來。"
    st "你...你...你......，怎麼可能......？\n啊啊啊啊啊啊！！！！！！"
    "她轉身就要飛奔出去，我快步跑向前去把她拉住。"
    u "你是誰？你認識我？"
    st "我怎麼可能不知道你......，你就是歐克里斯的人啊。"
    u "那你呢？你是誰？為什麼知道我？"
    "她甩開我的手，匆匆地往那個箱形物件走去，在那些小方塊上按了按，然後發亮的那一面的圖案就變了。
    她又繼續按了很多的小方塊，然後圖案也一直在變。"
    st "什麼？竟然一直都背景執行......。"
    u "你到底什麼意思？請告訴我這是怎麼一回事！"
    "她轉頭過來，將我從頭到腳都看了看，然後一臉懊惱的深深地嘆了口氣，向那個箱型物件指了指。"
    st "你是我電腦裡的一支程式歐克里斯裡面的人物，而你不知道因為甚麼原因竟能跑來現實世界，太不可思義了。"
    u "電腦...？程式...？現實......？\n難道歐克里斯是在這個箱型物件裡面？"
    "她看著我疑惑的眼神點了點頭，又無奈地嘆了口氣。\n她又在方塊上點好幾下，出現了一個有很多奇怪符號的頁面，仔細一看，那些就是我在歐克里斯的天空上看到的符號。"
    u "難道你就是這樣把歐克里斯創造出來的？"
    st "嗯...？你看得懂？"
    "我陷入了沉思，也就是說，在我眼前的這位女孩就是歐克里斯的造物主。\n看來那個箱型物件就是她所說的「電腦」，可以按上面的小方塊來控制發亮區域的圖案。"
    "而那個我本來生活的歐克里斯只是電腦的一支「程式」......。\n我們所有人都是他創造出來的一些虛無渺小的存在......。"
    menu:
        "我覺得---"
        "天崩地裂，覺得整個精神世界都要崩塌了。":
            $ point -= 3
            
        "盡管如此，我還是希望歐克里斯好好地存在著。":
            $ point += 3
            
    if point >= 0:
        jump end1_0
        
    else:
        jump end2_0

label origine1:
    "我想起我在康切爾托也看過這些，只是那時候的天空一閃即逝，只有稍稍瞥到一些部份而已。\n那些符號的出現的確非常的奇怪，就好像天空被撕開了然後將這些符號露出來一樣。"
    "我一邊想著，一邊胡亂地走，走著走著也沒有任何新的發現。"
    jump origineCont

label origine2:
    "我決定再到處看看，找找有沒有其他奇怪的地方。\n雖然這裡感覺不出時間的流逝，但是我有感覺到我又走了很久，因為腳漸漸失去力氣。"
    "可悲的是，在我看來我就是在這無盡的白裡面打轉，甚麼都沒有，就連天空也不再有任何突發的改變。"
    jump origineCont

label origineCont:
    "突然，我好像撞到了甚麼東西，但是定眼看去還是那一望無際的白。\n我將手伸出去，發現眼前有一到隱形的屏障，只要我碰到那個屏障就無法再前進。"
    "我大力地往屏障上敲一敲，但它還是無動於衷。\n忽然，眼前的白終於又閃爍了起來，在那些閃爍的間隙中，我瞥見一段文字，這次竟然不是那些奇怪的符號，而是歐克里斯的文字。"
    "——「歐克里斯程式計畫：本作品僅支援windows系統，因計畫進度落後，導致趕工中或許有很多錯漏，但大體上完成度很高，可放心使用。」"
    u "程式...？計畫...？系統...？\n這是甚麼意思......？"
    "完全不理解，這句話裡所講述的東西都是完全沒聽過的，但是大致上看起來是造物主為了某項計畫把歐克里斯創造了出來。\n因為他製造的時候時間不夠所以才造成了歐克里斯的這些異象......？"
    "造物主......不是應該是神一樣的存在嗎？\n怎麼反而會是造成這些異象的罪魁禍首呢？"
    "我覺得屏障後面或許有更深的意義？"

    menu smash:
        "我決定——"
        "助跑一下來通過屏障。":
            $ cnt += 1
            "屏障還是一動不動，看起來毫無要被我撞破的意思。"
            if cnt == 3:
                jump cont
            else: 
                jump smash 

        "不想嘗試突破屏障了。":
            "我想我盡力了，屏障是不可能通過的。"
            jump cont
        


label cont:
    if cnt == 2:
        $ point += 3
        
    else:
        $ point -= 3
        
    if point >= 0:
        jump end3_0

    else:
        jump end4_0