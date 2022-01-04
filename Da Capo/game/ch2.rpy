call ch3_0 from ch3

default sky_cnt = 0
default stone_cnt = 0
default surface_cnt = 0
default heal_cnt = 0

# $ sky_cnt = 0

label ch2_0:
    # chapter transition
    scene bg black with fade
    show text "{size=+36}{font=temingti.ttf}第二章{/font}{/size}" at truecenter with fade
    pause 1.0
    scene bg black with Dissolve(0.5)

    # start
    scene bg otherworld with fade
    u "這裡就是康切爾托啊……"

    jump choose
    

label choose:
    while True:
        nvl clear
        if stone_cnt > 0 and surface_cnt > 0 and sky_cnt > 0 and heal_cnt > 0:
            jump ch2_1
        nvl_narrator "我環顧四周，自己正置身於一片無際的荒野。挾帶砂石的風無差別的拍打在荒原上的所有事物上。這裡沒有樹木，唯一的綠意來自一簇一簇匍匐在地、接近枯萎的雜草，一些大小不一的{a=jump:stone}{color=#ffffff}石塊{/color}{/a}散落其間，從手掌大小到半人高都有，{a=jump:surface}{color=#ffffff}表面粗糙且凹凸不平{/color}{/a}。所有的景物都因為來自{a=jump:sky}{color=#ffffff}天空{/color}{/a}光線的反射，泛著妖異的紅。"
        

label stone:
    $ stone_cnt += 1
    if stone_cnt == 1:
        "我撿起地上一塊稍微小一點的石頭，試圖解析它的諾特組成，但被石塊銳利的邊緣劃傷了掌心。"
        show hand with Dissolve(1.0)
        u "糟糕…得趕緊治療才行，要是傷口感染就不好了。"
        hide hand
        "我試著釋放治療術，但是在魔法生效前，異象突生。"
        "伴隨著一個刺耳的聲響，手中的石塊在我眼前消失了。手裡一輕的同時……"
        "我的手掌被割成兩半。"
        u "！！！"
        "我下意識的用力甩手，好像這麼做可以擺脫現在的詭異景象似的，結果顯然是徒勞無功。"
        "我的手掌仍然維持著從虎口處將整個掌心橫向割斷的狀態，兩部分之間維持著一個不近不遠的距離，切面沒有流血，也看不見本應該存在的身體組織，只有一片空洞的黑。"
        "但是我沒有感受到任何一點疼痛，看似分隔的手指仍然活動自如，就好像一切只是我的幻覺一般。"
        "這樣感知矛盾的景象讓我毛骨悚然，我想要大叫出聲，但嘴裡只能發出不成聲的嗚咽。"
        "掙扎了許久，就在我放棄讓手恢復原狀的念頭，準備起身繼續觀察環境時，僅僅一次簡單的彎曲手指，一切便恢復原狀，甚至連原先的傷口也消失得無影無蹤。"
        "對這個事件來說或許是一個皆大歡喜的結局，但總覺得沒辦法只靠一句「可喜可賀」就將事件畫上句點。相反的，它帶出了更多謎團。"
        "最後{a=jump:heal}{color=#ffffff}治療術{/color}{/a}成功了嗎？剛剛的事情還會再次發生嗎？那個存在著黑色切面的手，真的屬於我自己嗎？"
        jump choose
    else:
        "不久前的恐怖經歷讓我不敢再觸碰這些石塊。"
        "但是剛剛釋放的{a=jump:heal}{color=#ffffff}治療術{/color}{/a}似乎和平常不一樣，必須正視這一點。"
        jump choose


label surface:
    $ surface_cnt += 1
    if surface_cnt == 1:
        "我直直盯著身旁一個與視線齊平的巨大石塊。"
        u "總覺得有哪裡不對勁……"
        u "……"
        u "……唔哇！！！"
        "一陣強風迎面吹來，裡面挾帶的沙子直接飛進我的眼睛。我痛苦地泛出生理性淚水，一面低下頭讓沙子順著眼淚流出，同時繼續思考。"
        "或許是眼睛傳來的刺痛讓我清醒了一點，我很快發現了違和感的來源。"
        u "……這些石頭的斷面也太粗糙了點，幾乎沒有被風侵蝕的痕跡。"
        u "簡直就像剛被「什麼東西」折斷似的。"
        u "這裡似乎沒有想像中安全啊……"
        jump choose
    else:
        u "這裡似乎沒有想像中安全……"
        u "調查完這裡就趕緊離開吧。"
        jump choose


label sky:
    $ sky_cnt += 1
    "我抬頭仔細地觀察這片天空。"
    "沒有雲朵與樹蔭的遮蔽，如同剛流出的鮮血一般的紅色天空壓迫著我的視覺迴路，彷彿再多看一秒就會將雙眼灼傷。"
    if sky_cnt == 1:
        "我不適的移開視線。"
        jump choose
    elif sky_cnt == 2:
        "正當我打算將注意力重新放回地面時，似乎有什麼東西從那片血色天空中一閃而過。"
        u "咦…？是幻覺…嗎？"
        "原本想再仔細看看，但被天空的顏色刺得雙眼發疼，只得作罷。\n我閉上眼睛，用力的甩了甩頭，讓眼睛休息了一會兒才重新睜眼。"
        jump choose
    elif sky_cnt == 3:
        "我瞇起眼睛，努力壓抑著移開視線的衝動，想再次捕捉到那個一閃即逝的事物。\n過了許久，我終於等到同樣的景象再次出現。"
        scene bg code with dissolve
        "就像顯影魔法釋放中斷一樣，整片天空開始扭曲、碎裂，最後消失。\n其後所揭露出來的「真實的天空」——就先這麼稱呼眼前的景象吧——是一片純粹、無盡的黑，一連串古怪的符號在上面快速的出現、滾動、消失，速度快得讓我差點看不清。"with vpunch
        "我忘記這詭異的景象持續了多久，或許僅僅一瞬，或許早已過了數個小時。這期間我只是失神地看著那片「天空」，研究者的本能叫囂著，要求我去解析這一切，手指在沙地上不停描摹著所有映入眼簾的符號。"
        "來不及思考。"
        "必須再寫得更快一點。"
        "再快一點。"
        "再快。"
        scene bg otherworld with fade
        u "………啊，結束了。"
        "我回過神來，天空已經恢復成原先的血紅色。，彷彿之前什麼都沒發生過，唯一能證明剛才的經歷的只剩下我身周圍繞成一圈、密密麻麻的奇怪符號。"
        u "先把所有東西都記下來吧，接著統計各個符文組合出現次數，然後再跟現存字彙的出現次數進行比對，要做的事情還有很多呢……"
        nvl clear
        nvl_narrator "…"
        nvl_narrator "最後這個符文組合消失後不久，天空就恢復了，「初步推斷與本次異象存在因果關係」……"
        nvl_narrator "好了，就先這樣吧。"
        nvl clear
        "我在用來記錄時間回溯詳細過程的筆記本重重畫上最後一串符文，「error」，確認沒有任何遺漏後才闔上筆記本。"
        jump choose
    else:
        "我不適的移開視線。"
        jump choose


label heal:
    $ heal_cnt += 1
    u "等一下，剛剛的治療術生效了嗎？"
    "我閉上眼，仔細回想剛才釋放魔法的過程以及一些更微妙的，對魔法的感應。"
    u "諾特的調動、排列的順序跟高低位置也沒什麼問題……"
    u "可是為什麼在排列完成的瞬間，發動的魔法比起「加快再生」的治療術，更像是「回到受傷之前」的時間回溯魔法呢？"
    u "唉…必須再做其他的確認才行，試著做原本要做的諾特組成分析好了。"
    "魔法的釋放過程和平常一樣順利，但在完成諾特的排列後，另一個石塊再次發出刺耳的聲音並憑空消失。"
    u "不管釋放什麼魔法，最後都會變成時間回溯嗎……糟糕，隨便使用魔法的話，後果可能不堪設想啊……"
    u "一個用不了魔法的魔法師，根本就是一個廢人吧。"
    jump choose

label ch2_1:
    "此時地面傳來震動，而且在我反應過來之前迅速轉為劇烈的搖晃，看著擁有嶄新斷面的巨大石塊，我馬上明白接下來即將發生什麼事。"
    u "要在魔物抵達之前藏起來。\n妨礙認知的魔法……可惡，不能用魔法！"
    "情急之下，我只能躲到一個巨大石塊邊，它有明顯的風蝕痕跡，應該不是那個龐然大物的主要活動範圍。"
    "很快的，造成石塊崩裂的罪魁禍首來到現場。"
    "那是兩頭形似牛的巨型魔物，牠們互相咆哮，用頭部形似角的構造衝撞對方，讓周遭的石塊破碎得更徹底。"
    "這場戰鬥很快就結束了，勝者對著倒在地上，無力動彈的敗者低下頭顱。"
    "這個動作在歐克里斯被稱為「魔物的懺悔」，魔物會對著倒在地上、瀕死的獵物低下頭，像是在祈禱一般，隨後給予獵物最後一擊。這個詞彙隨後成為「假惺惺」的代名詞。"
    "這本是一個普通至極的魔物生態學知識，但隨後的發展出乎我的意料。"
    "一個發著光芒的魔法陣出現在落敗魔物的身下，下一秒，在魔法陣上的魔物便不見蹤影。\n而那個魔法陣的構造與讓我來到這裡的魔法陣幾乎一樣，只在細部符文處有一點不同。"
    "來不及思考太多，身為一個無法使用魔法的弱小生物，我得趁著剩下的魔物還沒發現我，偷偷的離開這裡。"
    u "……"
    u "……"
    u "周圍的景物重複了？"
    "不管往哪個方向走，出現在我眼前的永遠是同樣的景象。空曠的荒野、散亂的雜草，以及破碎的石塊都出現在大同小異的位置，只在毀損程度產生細微的變化。"
    "我很快就失去方向。"
    "這也許是很糟糕的情況，但打從來到這裡以來，我已經接受了太多刺激，反而冷靜了下來，甚至還有餘力沿路做上記號。\n一路走來，我終於有時間好好整理思緒。"
    u "魔物之間的械鬥造成石塊毀損，使地貌產生差異，但透過比對多個破壞較少的地塊，可以得知單位地塊的原始地貌相同……"
    u "再加上之前的「手」、所有變成時間回溯的魔法……"
    u "第一代魔王…切羅想讓我發現什麼？"
    "鬼使神差地，我停下腳步。"
    "這裡是一個新的單位地塊，與之前看見的所有地塊有著決定性的差異。"
    "它沒有任何缺損，就連風蝕也沒有在其上留下痕跡。說是之前所見地塊最初始的模樣也不為過。"
    u "不對……不是沒有留下痕跡，而是它無時無刻不在恢復原狀。"
    "我在最高的巨石邊站定，經過近距離的觀察，可以看出任何外力造成的刮痕，都會在下一秒恢復如初。我不禁看得入神。"
    q "你還是不要碰到那塊石頭比較好喔，稍微把臉移開一點，如何？"
    "這個聲音離我非常近，幾乎就貼著我的耳朵發出。\n我反射性的倒退了一大步，看向聲音的來向。"
    "那是一名人形魔物"
    q "你想要知道的關於異常空間……也就是阿雷格爾謎團的線索，我剛好知道不少，那傢伙…也就是你遇到的那個切羅，他知道的一切也都是從我這兒得來的。"
    u "你為什麼……"
    q "為什麼知道那些事情嗎？"
    q "全部都是從你的「這裡」得到的。"
    "他指了指自己的腦袋。"
    q "我可以接收到這個世界任何生物的腦部活動，打從你來到康切爾托，我就一直在觀察著你。你的思考與情感很有趣。\n一直以來我接收到的只有純粹的情緒，這還是我第一次接觸到「語言」這個概念。我學得還不錯吧？"
    "意思是…這隻魔物會讀心？"
    menu:
        "所以，連我之前考慮過的「魔物的肉能不能吃」也被知道了？":
            "所以，連我之前考慮過的「魔物的肉能不能吃」也被知道了？"
            q "嗯，都知道。在荒野迷路也不忘確保食物來源，非常實際、有前瞻性的想法……咳……噗哈哈哈哈哈！"

        "而且在剛知道「語言」這一概念的極短時間內便習得了新語言，再加上他散發出的氣勢…這個魔物，很危險":
            "而且在剛知道「語言」這一概念的極短時間內便習得了新語言，再加上他散發出的氣勢…這個魔物，很危險。"
            q "你剛剛起了殺心，對嗎？害怕我前往你生長的世界大肆破壞。"
            q "不用擔心，我哪裡都走不了。"
            "原本他臉上一直帶著的笑容稍微黯淡幾分。"
    q "好了好了，閒聊先到此結束。"
    q "你這個小傢伙還挺合我眼緣，我就再加碼一下，把這個世界的真相告訴你吧。切羅大概是在那個歐克里斯發現了與這裡一樣的狀況，才會讓你過來。\n希望你能在知道真相後，好好思考關於你所在的世界的一切。"
    q "你在想：「就這樣把世界的真相告訴一個來自異世界的陌生人真的好嗎?」"
    q "這個問題嘛……我的回答是：要是對一個即將走向崩毀的世界見死不救，就算是我也會因此愧疚得睡不著覺的。"
    "聽到這句話，我的心頓時沉到谷底。"
    "那個即將崩壞的世界指的是什麼已經顯而易見，但我還不想，也不敢去理解他的話所代表的意思。"
    if sky_cnt < 3:
        q "對了，你好像還沒看到過「那個」，先抬頭看看天空吧。算算周期的話，應該差不多要出現了。"
        "我不得不再次抬起頭仔細觀察那片血紅的天空。不久，就像顯影魔法釋放中斷一樣，整片天空開始扭曲、碎裂，最後消失。"with vpunch
        scene bg code with dissolve
        "其後所揭露出來的「真實的天空」，是一片純粹、無盡的黑。\n儘管整個過程只持續了幾秒，但那空洞的顏色仍帶給我極大的震撼。"
        "他等我消化完一切後重新開口。"
        scene bg otherworld with fade
    q "康切爾托曾經被過多的生命佔據，使這個世界無力負擔這龐大的情感、思緒與生命現象，開始崩毀。天空的異象，還有你遇到的分割的手，都是世界崩壞的結果，絕非康切爾托原本應有的景象。"
    q "而此地，我們稱為「大地的基準」，也是異象之一。原本只是一個無法觸及的概念，但在世界開始崩毀後，它成為真實的存在，囚禁了所有觸碰到它的生命。在無時無刻的「刷新」之下失去自我的認知，成為大地的基準的一部分。"
    q "我們曾經因為世界的崩毀陷入混亂，為了減少行走於這片大地之上的生命而互相殺戮。時至今日，仍有不少魔物利用魔法陣將另一隻魔物驅逐至其他世界。但即使現在的魔物數量已經遠低於崩毀發生前，康切爾托的毀滅也不曾停止。"
    "我在他的話語中發現一個值得注意的地方。這片大地所有地塊的原始狀態，大地的基準。\n與時間斷崖相同，曾經是一個永遠無法抵達的地方，而現在正像是一隻貪婪的野獸，毫無節制地吞食、消化著生命。"
    "那麼，時間斷崖最終也將如此嗎？"
    q "你發現到了吧?大地的基準、時間斷崖，它們驚人的相似度。"
    q "「為什麼會這樣?」這個問題很有趣。說不定是因為我們的世界都出自同一位造物主之手，畢竟誰也沒有規定造物主只能有一個創作。"
    u "那麼刷新是指……"
    q "每隔一段時間，這裡就會回復到之前的狀態。生物會隨著多次刷新，漸漸失去對於時間的認知，然後是自己的存在，最後成為它的一部分。"
    q "能撐過幾輪刷新因人而異，你的話大概是5輪？"
    "他的語氣輕鬆得像在談論今天的天氣，但內容著實讓我心底發寒。\n一旦被困在異常空間，幾乎等於被宣判死刑，毫無掙扎的餘地。\n等等，掙扎？"
    u "沒有脫離這種異常空間的辦法嗎？"
    q "有喔。"
    u "有……？那你為什麼還被困在這裡？"
    q "我錯過了離開這裡的時機。"
    q "……別用這麼震驚的眼神看著我嘛，機會可不會永遠留在原地等著你。"
    q "脫離異常空間的方法是尋找這個空間的「破綻」，並「打破」這個無盡的輪迴，一旦再也無法認知到那個「需要被打破的東西」的存在的話，可不就是永遠出不去的意思嗎？"
    q "即使現在還保有自我意識，我離成為這裡的一部分也不遠了。一開始的時候，要是我沒出聲，你也不會意識到我的存在吧？"
    "說到這裡，他露出了有些落寞的表情，但很快的又恢復成原先那彷彿不在乎任何事的微笑。"
    q "故事到此結束，你應該得到你想要的情報了。感謝你為我帶來一段有趣的時光，那麼，永別了。"
    if sky_cnt > 3:
        q "你似乎曾經發現了一些有趣的東西，我就送你一個小禮物，在需要的時候你應該就會知道了。"
    "我在他的指示下畫出了目的地為歐克里斯的魔法陣。在魔法陣刺目的光芒中，他的身影漸漸模糊。"
    jump ch3_0

    



