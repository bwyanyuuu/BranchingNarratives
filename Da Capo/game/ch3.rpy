call be2_0 from be2
call ch4_0 from ch4
label ch3_0:
    # chapter transition
    scene bg black with dissolve
    show text "{size=+36}{font=temingti.ttf}第三章{/font}{/size}" at truecenter with dissolve
    pause 1.0
    scene bg black with Dissolve(0.5)

    # start
    scene bg grass with dissolve

    "頭頂的艷陽太熱烈，刺的我睜不開眼，但是風輕輕拂過，倒是將太陽的溫存帶走的一點都不剩。\n過了一陣適應之後，我才緩緩張開眼睛。"
    u "我回來了啊，歐克里斯......。"
    "一旁有隻小白兔一跳而過，我伸手將它攔了下來，把它放在懷裡揉了揉。\n小兔子叫了一聲，掙脫了我的懷抱，向前方一蹦一蹦的跳去。"
    "我的眼光隨著小兔看去，匆匆瞥見草原另一端的森林裡，好似有魔力的流動。\n我站起來，活動活動我那感覺有點生鏽的雙腳，向森林的方向走去。"
    u "現在不知道是甚麼年代了，先去前面探探究竟吧......。"

    scene bg forest with dissolve
    "走到森林的邊陲時，傳來一陣嘶吼與兵器相接的聲音。\n我感受到了強烈且是在康切爾托感受到過的魔力波動。"
    u "難道是魔物......？"
    "我趕忙向前跑去，忽然一道藍色魔法波打到我面前，我側身一閃躲了過去，前方的地上猛地出現一道焦痕。" with vpunch
    "我定了定眼向發來攻擊的方向看去，是一隻巨型魔物在與一個冒險者隊伍作戰，戰況膠著，看起來毫無分心之餘裕，想來是無意間波及到外圍的。"
    show shm at halfleft with dissolve
    show shf at halfright with dissolve
    "那個冒險者小隊是由一對雙胞胎所帶領的，兩人雖配合默契，但還是落處下風。\n眼看那魔物又發出了極強烈的魔力坡動，那是大型攻擊的前兆，但雙胞胎好似沒有注意到。"
    u "小心......！！！"
    shm "啊啊......，呃......！"
    "我一個箭步衝了上去，發動防護盾魔法，將攻擊擋了下來。\n但我的魔法竟比以前的力量還要強大，看來是從康切爾托回來之後，受到了一些能力的強化。"
    "回頭看了看那群冒險者，各個一臉疲態，看來剛才那一番惡戰持續了很久。"
    u "......沒事吧？"
    shf "可以的，多謝！它的實力可不容小覷，請小心！\n大家，我們再拼一拼，一會兒就能將它拿下！"
    "看著他們上氣不接下氣的樣子，我對著他們搖搖頭。\n以我現在的實力，一個人就足以應付。"
    u "沒關係，我來就行。"
    "衝著他們笑了笑，轉過頭來看向魔物，沒想到它竟呈一個臣服的姿態，並且停下了攻擊。\n我微微詫異，對魔物的態度甚是不解，就感覺我是它的首領一樣。"
    "仔細想想，若是因為我從康切爾托回來，而且我還得到了強化，導致了這樣的結果的話。\n在人眼中這是個什麼樣子，魔物屈服於人類？太可笑了。"
    "總之先阻止這個場面繼續發展吧！"
    menu:
        "將魔物暫時隱形，把魔物引去別處，再好好研究它們是怎麼一回事。":
            u "唉，真難辦啊......。先把眼下這一關過了再說吧！"
            # 正義值++
        "直接使用攻擊魔法將魔物消滅。":
            u "不論如何，先將魔物消滅再說！"
            # 正義值--
    "我開始蓄力操控諾特，將我腦海中魔法的樣子排列出來。\n但就在我將其排列好，要釋放出去的時候，我的手像電訊號般閃爍了兩下，而還沒放出去的魔法就在原地直接消失，巨型魔物也跟著不翼而飛。"
    u "這......？"


    "搞不懂剛剛這是怎麼回事，魔法就像被強制終止了一樣，魔物的消失也是十分離奇。\n難道歐克里斯也開始發生異象了嗎？"
    shm "那個，謝謝你幫了我們一把。\n但那魔物怎麼就消失了......？"
    u "我學過一種空間移動魔法，我將它先移動了別處。\n你們先休息一下，剩下的我來處理就行。"
    "先暫時搪塞過去吧......，我頭也不回的匆匆離開了森林。"
    u "我先走了，我們有緣再見。"
    shf "那個......，等等！\n怎麼一下就跑走了......。"
    shm "他打起魔物來可是非常輕鬆呢！\n不知道是甚麼來頭，甚麼時候出現了這麼個佼佼者。"
    shf "但他所用的魔法雖然看起來和我們平時所見的差不多，但所造成的效果可是完全沒有見過的！\n能讓物體直接消失的魔法......，威力可不是我們這個水平可以匹敵的。"
    shm "的確是有點古怪了。\n不過他救了我們，應該也不是什麼壞人吧......。\n總之還是多虧他了，心存感激吧！"

    scene bg market with dissolve
    "我慌忙地跑了出來，毫無目的的亂走，因為心裡在思考著剛剛那個奇怪的一幕。"
    "仔細想想，那魔法確實在那一個剎那間，我就對他失去了控制力。\n手部的消失也是很不正常，看來我的猜想或許是正確的。"
    u "看來要採取一些行動了......。"
    "歐克里斯面臨了康切爾托所發生的問題，生物太多而導致世界發生了異常......。"
    u "......啊。" with hpunch
    show luren with dissolve
    "不知不覺中我已經走到了附近小鎮的市集上，沒有注意到前方來人而不小心撞了上去。\n那個人一臉驚恐地看著我，慌慌張張的樣子看起來有點奇怪。"
    u "那個......你還好嗎？"
    l "沒事沒事......。"
    "這個人一講完馬上轉頭就急著要走，但是我瞥見了那隻放在口袋裡緊緊握住的手。\n刺眼的光芒一閃而過，看來口袋裡藏的是一把匕首。"
    "我想伸手將他攔下來，不曾想他一個甩手就將我掙脫直接跑了。"
    u "等等......別走！"
    "我也跟著跑了出去，但是就算追到了又如何？大概還是拿他沒辦法。\n雖然不知道他拿著匕首要去做什麼，但看起來並沒有其他人在追著他跑，也不像是需要自我防衛的樣子。"

    menu:
        "繼續追著他跑。":
            # [選擇1] 正義值-- (無故浪費體力)
            "我還是決定追了上去，但是跑著跑著體力逐漸跟不上，我停了下來。"

        "直接發動魔法阻止他。": 
            # [選擇2] 正義值++ (聰明的作法)
            "我發動魔法將街邊的一顆石頭飛去他行徑路線的前方，他匆匆忙忙的沒有注意，被石頭絆了一下。\n雖然在他倒地上有一點點的耽擱，但又很快速地站起來繼續跑了出去。"
    
    "忽然我想起在康切爾托見過的一個特殊的法陣，它可以讓物體的物質不滅卻將它的存在消去。\n當下我立即將腦海中的法陣畫了出來，並讓它以最快的速度飛到那個人的匕首之下。"
    "彈指之間，匕首化為一到煙霧消失不見了。那個人在奔跑中，並沒有發現他的口袋一輕，匕首已經無影無蹤了。"
    hide luren with dissolve
    u "沒想到在歐克里斯這法陣也成功了......。"
    "突然一個想法閃進我的腦海裡，若是能將生物以這種方式離開歐克里斯，既不會消彌他本身的存在，又能將歐克里斯的危機降低，或許是個不錯的方法。"
    u "歐克里斯有了一線生機！！！"
    "忽然一個腳軟，我跌坐在了地上，沒想到小小一個法陣消耗的魔力竟然這麼多。\n這次只不過是消除了一個匕首，要是要消除一個生物不知道要花多少心思呢......。"
    u "......看來得好好修練修練了。"

    scene bg black with dissolve
    show text "{size=+24}{font=temingti.ttf}1年後{/font}{/size}" at truecenter with dissolve
    pause 1.0
    scene bg black with Dissolve(0.5)
    scene bg palace1 with dissolve

    show neo at halfleft with dissolve
    q "真是沒想到魔物又開始蠢蠢欲動了，明明好不容易消停了幾十年。"
    show ss at halfright with dissolve
    q "那不都是又殺出了一個魔王「伊洛」嗎？魔物竟然擁有人類的型態，腦袋的思維還跟人類一模一樣，也不知道它到底甚麼來頭。\n尼爾，你有聽說過他怎麼出現的嗎？"
    n "擁有高智慧的魔物真的很棘手，先不論打不打得過，根本猜不到它到底在想什麼。\n聽過最多的大概是某一天憑空出現在厄多斯大森林裡，還將一隻高階魔物打得落花流水，從此魔物就臣服於它，全聽它的調遣。"
    s "我桑杰斯就沒有聽過這麼離奇的事情，很少有聽過魔物間互鬥的，它們明明一直都是非常團結的群體。\n但最近高階魔物越來越少出現了，現在要想接到高等委託是何等的困難。"
    n "這倒是，除了伊洛之外，其他魔物的總體實力倒是不如從前了。\n不過它集結這麼多小魔物，不知道他到底有什麼打算。"
    s "想來肯定是有大陰謀，以它的智慧要將這些魔物的作用放到最大一定是可能的。\n因為有好多冒險者隊伍和軍隊討伐它之後全部都消失了，我相信以一己之力是絕對做不到的。"
    n "總之等一下進入地宮，要小心各處可能隱藏起來的魔物發動偷襲。"
    s "那是當然。"

    scene bg black with dissolve
    show text "{size=+24}{font=temingti.ttf}多年後{/font}{/size}" at truecenter with dissolve
    pause 1.0
    scene bg black with Dissolve(0.5)
    scene bg palace2 with fade
    scene bg palace2 with dissolve
    "自我回到歐克里斯，大概也有20多年了。"
    "因為每次進行消除需要的魔力太多了，雖然這些年來有持續在努力，但是我也只將大部分的高階魔物消除了。\n雖然歐克里斯的異象發生的頻率有下降，但他們還是存在，所以我還有太多太多需要去努力的了。"
    u "再這樣下去也是治標不治本......。"
    "這些年一味埋頭在消除這件事裡，都沒有好好思考過這件事到底有沒有意義。\n最近幾日才開始慢慢地思考這件事，或許時間斷崖才有真正解決異象的答案......。"
    "記得當初在研究組裡，有研究過元年附近的一段歷史，那時候歐克里斯常常發生突如其來的災害。\n現在在我看來可能也是異象頻生，就像康切爾托那樣不穩定。"
    "在這樣不穩定的狀態下，也許有一些時間斷崖的線索，元年是個特殊的年份，因為人類突來迎來沒有頻繁天災的太平。"
    u "或許是時候該放棄現在了......。"
    "碰！我所處在的地宮秘室的門忽然被撞開了，來者是一隻冒險者小隊。\n領頭的那兩個人似曾相識，稍微回想了一下，原來是我從康切爾托回到歐克里斯時，救下的那對雙胞胎。"
    u "沒想到竟讓你們找到了這裡......。"
    shf "伊洛，你終於被我們找到了。
    你將會是我們鬼音鈴的手下敗將！"
    shm "大夥兒，一起上啊啊啊啊啊！"
    menu:
        "直接進行時間回溯":
            # [選擇1] BE2 / 偽裝死亡"
            jump be2_0
        "製造一場自己的死亡，再進行時間回溯":
            "不能就這樣離開，至少要讓他們相信我真的死亡了，這個世界才能合理的運作下去。\n這時鬼音鈴排起了他們最著名音律魔法，五人合力，威力加倍。"
            "我開始思考各種可能性，當一道火光在他們的音樂之下熊熊燃起時，我想到了個非常不錯的辦法。"
            # "一段音樂......"
            "我在火光襲來之時，用魔法點燃了我的斗篷，並將它燃的非常旺盛。\n然後在他們看來我被困在一片火海中的時候，我用最快的速度發動了 Da Capo 回到元年前一天，而現場只會剩下一團灰燼。"
            u "......再見了。"

    jump ch4_0

    



