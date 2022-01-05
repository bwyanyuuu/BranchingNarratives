call ch2_0 from ch2
call be1_0 from be1
label ch1_0:
    # chapter transition
    scene bg black with fade
    show text "{size=+36}{font=temingti.ttf}第一章{/font}{/size}" at truecenter with fade
    pause 1.0
    scene bg black with Dissolve(0.5)

    # start
    scene bg market with fade

    nvl_narrator "四周傳來了人的聲音。\n等到時空回溯帶來的暈眩感過去後，我睜開了雙眼。"
    nvl_narrator "兩旁是用木材簡單搭建起來的棚架，婦人牽著光著腳的孩子在攤販前對檯子上的水果挑挑揀揀，
    身穿毛皮衣的男人肩上扛著一隻滴著血的羔羊從我旁邊走過，還有三個醉漢躺在巷口喝酒大笑。"
    nvl_narrator "似乎是回溯到了一個市集的正中間，身旁人來人往，攤販老闆吆喝叫賣向人們推銷自家的商品，
    群眾的目光也放在老闆手中的貨品，所幸沒有人注意到突然出現在人群之中的我。"

    # scene dissolve
    scene bg street with fade

    nvl_narrator "我盡量壓低身形，穿過人群的包圍來到一旁無人的暗巷內。"
    nvl clear
    u "看起來時空回溯是成功了，不過應該在慎選一下抵達的地點吧，雖然有妨礙認知的魔法，但萬一被人識破就不好了。"
    u "好了......接下來就是等待諾特回復就可以進行下一次的時空回溯。"

    "畢竟有任務在身上，沒有多餘的時間和閒情逸致去到處參觀。"
    "趁著還在等待的時間，我看著市場裡忙碌的人們，盡可能去觀察這個時空的生活。"
    "人們交流的方式、使用的貨幣、衣服的穿著以及日常吃的食物，比起書上記錄的知識，眼前的光景才是這個過去的真實。"
    "我就是為了一窺真實的歷史才參加了這次時空回溯。"
    
    show cello with dissolve
    qc "......你覺得這幅景象很美嗎？"
    u "誰！？"
    c "恩......我想你可以稱呼我為切羅。"
    c "年輕人，為什麼你要一直盯著市場裡的人們？是好奇嗎？還是因為這幅景色很美？"
    "男人......或者該稱他為切羅，十分執著於從我這裡得到答案。\n說到底，這個問題本身就相當怪異。"
    "充滿生氣的市井景象，吵雜凌亂的街道，穿梭不止的人群。\n面對這幅景象，我當然覺得—"

    menu:
        "很美":
            u "這幅光景是美麗的，望眼過去處處都充滿著生機，每個人都享受著平穩安祥的生活。\n如此幸福和平的日常，就足夠稱之為美了。"
            "現在我見證了這個時代的最後一刻，不久後第一任魔王就會現身，將這一切破壞殆盡。\n
                美好的事物消亡，只留下些許文字紀錄流傳下來，這真是令人感到十分遺憾。"
            c "原來如此，這就是你覺得的美嗎。"

        "並不美":
            u "這幅光景並不能稱之為美麗，畢竟這是人們日常的一部份。\n
                而美是該被追求的事物，這種平穩的生活只是生存的必備條件。"
            u "我......只是好奇著他們的日常才一直注視著這幅景象。"
            "對現在的人來說是未來，但對我來說這已經是過去了。"
            "不久後第一任魔王就會摧毀這座村莊，開始他的征途。\n而這幅平凡無奇的日常光景成為了那個時代的人們最渴望的事物。"
            "已經發生的事是沒有辦法被改變的。\n不能隨意改變過去的既定事實，否則我存在的未來就會被毀滅。"
            "所以現在，我能做到的也只有靜靜的看著這個時代毀滅前最後的平穩光景，並把這些記錄在我的腦海中。"
            c "原來如此，對即將逝去的日常的最後一刻，你在哀嘆著它的未來。\n因此你沒辦法用欣賞或好奇的眼光看待它，你在憐憫它。"
            c "失禮了，看來你和你的前輩們並不一樣。"
    
    c "......"
    c "我知道你是從未來來的人。"
    c "從不久前開始就常常會有人突然憑空出現，雖然有些人用了妨礙認知的魔法，讓普通人察覺不到異常，但我還是查覺到了。"
    c "雖然難以想像未來竟然發展出時空回溯的魔法，但是那些出現的人們讓我不得不相信。"
    "他竟然能察覺到從未來回溯來的人！明明以這個時代的魔法技術是沒辦法察覺到未來魔法造成的異狀的。\n這個人究竟是！？"
    u "你究竟是誰！？"
    c "我恰巧知道了有關這個世界的一些真相，作為你剛剛回答我問題的報酬，我可以給你一些提示。"
    c "如果你真的想了解，恩......你們稱之為「阿雷格爾謎團」的歷史的話，有個地方你必須先去看看。\n
        當你看了那個地方的狀況後，去思考我們的世界就竟是個什麼樣的存在，然後才能往那段空白歷史前進。"
    u "我為什麼要相信你？\n連百年後都找不到關於那段歷史的任何一絲線索，你怎麼有辦法知道關於那段歷史的真實？"
    c "……如果說我不是來自這個世界的話，是不是就會相信我了。"

    show cello eye with Fade(0.2, 0.0, 0.8, color="#fff")

    "切羅將遮住額頭的瀏海向上撥，底下露出了一隻眼。"
    "額頭的正中央突兀的長著一隻沒有眼白、眼瞳是一片漆黑的眼，被那隻眼盯著彷彿就會失去意識，本能強烈地叫囂快點逃走，但是雙腿卻像灌了鉛般只能立在原地一動也不動。"
    "無喜無悲只收割生命的第三隻黑眸，本以為是傳說誇大而成的，沒想到竟然是如此的......"
    u "你......你是魔王嗎！？"
    c eye "如果你這麼稱呼我的話，那我應該就是魔王了吧。\n畢竟是你才知道未來所發生的事。"

    show cello with dissolve

    "切羅把瀏海放下，黑眸也隨之被隱藏起來。"
    "剛剛所感受到的壓力煙消雲散，彷彿只是一場錯覺。\n回過神來時，我才反應過來我冒了一身冷汗。"
    u "......就這麼直白的把身份告訴我，不怕我討伐你阻止未來的慘劇嗎？"
    c "因為這不是你的目的，你是追求真實之人，不會因此停下你的腳步的。"
    c "我的家鄉「{a=https://reurl.cc/6Elxkk}康切爾托{/a}」有著一些線索，去到那你就能知道你想要的東西，我可以幫你開啟通往康切爾托的傳送陣。"
    "我決定—"

    menu:
        "為了阻止悲劇發生，我要在這裡阻止他":
            jump be1_0
        "雖然不太相信他，但我必須去康切爾托":
            u "我確實沒辦法改變過去發生的事，改變過去也就是否定我存在的那個未來。\n我無法在這裡阻止你，對於你提出來的建議也還是半信半疑。"
            u "但既然你都特意展現出真面目讓我看到了，之後也沒有打算殺掉我，肯定是有特別的原因。\n那我就照你的話去看看康切爾托到底有什麼。"
            c "那麼祝你一路順風，希望你知道世界的真相時仍能保持初心。"
            "像是早就看穿我的選擇，切羅一揮手地上就出現了一個傳送陣。"
            "抱著不安的心情，我踏進傳送陣內。"
            u "......為什麼要毀滅人類？"
            "即使知道問了也是無用，人類與魔王是無法互相理解，況且我還是用他尚未犯下的罪再質問他。"
            "站在那裏還未成為魔王的男人有些悲傷地笑了，他周身不穩定的諾特躁動起來。\n魔法陣發出耀眼的光芒，男人的身影消失在光芒中。"
            c "......我們只是為了活下去而已。"

            jump  ch2_0

    



