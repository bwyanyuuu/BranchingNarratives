call be3_0 from be3
call ch6_0 from ch6
default action_cnt = 0
default hill_cnt = 0
default loop = 0
default last = ""
default before = ""

default hill = "{a=jump:hill}山坡{/a}"
default grass = "{a=jump:grass}草原{/a}"
default village = "{a=jump:village}村莊{/a}"
default villagers = "{a=jump:villagers}村民{/a}"
default flower = "{a=jump:flower}花朵{/a}"
default squirrel = "{a=jump:squirrel}松鼠{/a}"
default bird = "{a=jump:bird}鳥鳴{/a}"
default butterfly = "{a=jump:butterfly}蝴蝶{/a}"
default magic = "{a=jump:magic}魔法{/a}"
default skyy = "天空"

label ch5_0:
    scene bg black with dissolve
    show text "{size=+36}{font=temingti.ttf}第五章{/font}{/size}" at truecenter with dissolve
    pause 1.0
    scene bg black with Dissolve(0.5)

label begin:
    if loop > 5:
        jump be3_0
    elif loop == 1 and flower != "■■":
        $ flower = "■■"
        $ squirrel = "■■"
        $ bird = "■■"
    elif loop == 2 and butterfly != "■■":
        $ butterfly = "■■"
    elif loop == 3 and magic != "■■":
        $ magic = "■■"
    elif loop == 4 and villagers != "■■":
        $ villagers = "■■"

    $ action_cnt = 0
    $ hill_cnt = 0
    scene bg grass with dissolve
    "我猛然睜開雙眼。"
    "映入眼簾的是一片藍天，幾朵白雲點綴其上。輕柔的微風拂過草地，我身周的草葉被帶得搖擺起來，輕輕搔著我的臉頰。"
    u "唔…好痛！"
    "我似乎躺在地上，當我試著坐起來，身上的傷口被牽動，發出一陣陣刺痛。\n最後，等到我掙扎著爬起來時，已經是十幾分鐘後了。"
    label begin1:
    $ before = "begin1"
    "我環顧四周，這裡是一片草原，幾朵淺色的[flower]點綴其間，不遠處可以看見幾座[hill]佇立，儼然一副祥和景象。滿身灰塵與血汙的我顯得格格不入。\n或是，異常的不是我，而是這個地方。\n如果最後的時間回溯[magic]釋放成功的話，這裡應該就是時間斷崖了。"
    
    jump hill

label hill:
    if last != "hill":
        $ action_cnt += 1
        if action_cnt == 7:
            scene bg black with dissolve
            "突然間，我失去意識。"
            $ loop += 1
            jump begin
        scene bg 

    $ last = "hill"
    $ hill_cnt += 1

    scene bg hill with dissolve
    "離開[grass]，我開始朝著山坡前進。"
    if hill_cnt == 1:
        "路途中沒有地裂，也沒有巨型龍捲風，一切都平靜得不可思議，但總有種不安的感覺縈繞在我心頭。"
        u "完了，這一趟時間旅行下來，我都搞出被害妄想症了。"
        "但隨後，我就搞清楚這不安的源頭。\n從我醒來開始，我沒有看到任何動物。耳邊的聲音只剩下我的腳步聲以及風吹過草地發出的沙沙聲，一切都顯得安靜過頭了。"
    else:
        "與最初的路程不同，這次一路上多了許多生氣。"
        label hill1:
        $ before = "hill1"
        "身周的樹枝深處偶爾能聽見幾聲[bird]，[squirrel]在樹上上竄下跳，[butterfly]在[flower]間飛舞著。"
        "……一想到這些東西都是在一瞬間出現的，就令人不寒而慄。"
    
    if action_cnt == 4:
        "我在一處河床邊停下腳步。"
        "看看周遭碧草如茵的樣子，這裡怎麼都不像是缺水地區，但這個河道卻是乾涸的，沒有任何水流過。"
        u "還是水源被堵住了呢？"
        "我沿著河道向源頭前進，但一直到溪流的發源地都絲毫不見流水的蹤影。"
        u "大概是像動物一樣，不久後就會出現了。\n如果見證到水出現的瞬間，或許能得到什麼線索。"
        "我開始耐心的等待。"
        scene bg waterfall with dissolve
        label hill2:
        $ before = "hill2"
        "瞬時之間，一道水柱從溪流的源頭直直往頭頂的[skyy]衝去……這樣描述也不太準確，因為那水柱更像是一道瀑布，一去不復返，再也沒有掉回地面上過。"
        "我試著往水柱的方向丟了幾件物品，所有東西都跟著水流一起直衝天際。"
        u "看來流水附近的重力場與周遭不同……"
        label hill3:
        $ before = "hill3"
        u "或許可以乘著這道水柱飛上[skyy]也說不定。"
        "說完，我自己都被這個突發奇想給逗笑了。畢竟我也沒什麼理由非要飛上空中不可。"
        "過了一會兒，那道瀑布「刷啦」的一聲落回河床，濺起的水花把包括我在內的所有東西都弄溼了。我又觀察了一下這汩汩流動的水，但現在它似乎就只是一條普通的小溪。"
    elif action_cnt < 4:
        "我在一處河床邊停下腳步。"
        "看看周遭碧草如茵的樣子，這裡怎麼都不像是缺水地區，但這個河道卻是乾涸的，沒有任何水流過。"
        u "這裡也很可疑，或許藏著離開時間斷崖的線索。"
    else:
        "我在一條小溪邊停下腳步。"
        "比對了一下位置，這似乎就是我剛才看到的水柱。我仔細的觀察了一下，但現在它似乎就只是一條普通的小溪。"
    
    jump grass


label grass:
    if last != "grass":
        $ action_cnt += 1
        if action_cnt == 7:
            scene bg black with dissolve
            "突然間，我失去意識。"
            $ loop += 1
            jump begin

    $ last = "grass"
    scene bg grass with dissolve
    "我重新回到我醒來的草原。"
    if action_cnt == 4:
        scene bg waterfall with dissolve
        "這時，[hill]的方向隱隱傳出奇怪的聲響，我往那個方向看去，只見一道水柱直直往天上衝去……這樣描述也不太準確，因為那水柱更像是一道瀑布，一去不復返，再也沒有掉回地面上過。"
        "這樣的奇景僅僅持續一會兒便消失蹤跡，我只得將注意力重新放回草原。"
        scene bg grass with dissolve

    label grass1:
    $ before = "grass1" 
    "幾朵淺色的[flower]點綴其間，[butterfly]圍繞著[flower]飛舞，不遠處可以看見幾座[hill]佇立，在山坡的相反方向，一座[village]似乎正從這樣祥和的景象中甦醒，漸漸傳出人聲。"

    jump village

label village:
    if last != "village":
        $ action_cnt += 1
        if action_cnt == 7:
            scene bg black with dissolve
            "突然間，我失去意識。"
            $ loop += 1
            jump begin
        scene bg 
    
    $ last = "village"
    scene bg village with dissolve
    u "之前並沒有這座村莊的……算了，在時間斷崖發生什麼都有可能。\n不管怎樣，先去那邊探探情況吧。"
    "我向那座村莊走去，想著或許能從村民口中問出什麼。"
    if action_cnt == 4:
        scene bg waterfall with dissolve
        "這時，山坡的方向隱隱傳出奇怪的聲響，我往那個方向看去，只見一道水柱直直往天上衝去……這樣描述也不太準確，因為那水柱更像是一道瀑布，一去不復返，再也沒有掉回地面上過。"
        "這樣的奇景僅僅持續一會兒便消失蹤跡，我只得將注意力重新放回眼前的村莊裡。"
        scene bg village with dissolve

    label village1:
    $ before = "village1"
    "這個的建築物只有幾間簡陋的木造小屋，一些[villagers]在屋子那兒忙進忙出。"
    jump hill

label villagers:
    $ skyy = "{a=jump:sky}天空{/a}"
    "我試著向在一旁休息的村民搭話。"
    u "不好意思，我是剛來到這裡的冒險者，很想了解這裡的生活。\n請問你們在做什麼呢？"
    v "啊啊，這是在準備謝神的儀式。"
    label villagers1:
    v "為了感謝來自天上的神明賜予我們萬物，一直以來在天空之上眷顧著被乘裝在箱子中的我們，每年村裡都會舉辦這個儀式。晚上還會有非常熱鬧的祭典，你可真是來對時間了……"
    "可是你們直到不久前才出現在這裡。\n我努力按捺著反駁的欲望，繼續聽下去。"
    "那個「神明」灌輸了這樣的思想，或許正暗示了這個世界真正的模樣。如果這個世界是神明的玩具盒，那麼唯一的出口就位於頭頂的天空。"
    "如果能到達天空中的話……！"
    "我震驚於自己這個瘋狂的想法，但無法控制思緒沿著這條道路奔馳而去。我甚至忘了村民之後說了什麼，只想著該怎麼到天上去。"
    "我大概是瘋了。"
    
    jump expression before

label flower:
    "在任何時代都隨處可見的五瓣小花。"
    
    jump expression before

label squirrel:
    "怕生的小動物，一旦接近就會飛快跑走。"
    
    jump expression before

label bird:
    "有著不同的音高與持續時間。"
    "……並沒有暗號藏在裡頭。"
    
    jump expression before

label butterfly:
    "……等等，蝴蝶?"
    "我重新看向那些數量不少的蝴蝶。"
    u "這個數量，根本不可能是相約一起飛來這裡的吧。看起來更像是憑空出現的……"
    u "這就是你說的世界的破綻……"
    
    jump expression before

label magic:
    "雖然心中已有定論，但為了保險起見，我還是將手按在草地上，試著進行諾特組成分析。"
    u "唉，果然是「這裡不存在物體」嗎……"
    "我又試著釋放各式種類的魔法，無一例外全數失敗。我甚至無法感受到諾特的存在，更不要說調動它們了。"
    
    jump expression before

label sky:     
    scene bg waterfall with dissolve
    "我抬頭看了看水柱的盡頭，緊張的咽了一口口水。\n一旦推測出了問題那就是死無全屍，但這是目前最有可能的答案。"
    "而且我也不清楚我還剩下多少時間。會不會下一秒就失去對自我的認知，被這個時間斷崖吞噬。"
    "我——"
    menu:
        "走向水柱":
            "我深吸一口氣，閉上眼睛，直直朝著水柱走去。"
            "在全身被水流浸濕的同時，我開始墜落。"
            "第一次體驗到自由落體的感覺，總覺得五臟六腑都要被周圍的空氣擠壓出來。我幾乎感受不到我的身體，更不用說把眼睛睜開了。"
            "或許過了很久，或許只是一剎那，我似乎穿過了一片薄膜。先前強烈得能穿透眼皮的光線不復存在，而我的腦袋也清醒不少，回想起之前失去認知的事物。我這才意識到不久前的我離失去自我認知有多近。"
            "但現在我已經成功脫離時間斷崖了。"
            jump ch6_0
        "不走向水柱":
            "我最後還是卻步了。"
            u "現在還沒有到必須為一個不成熟的推論賭上性命的地步。"
            jump expression before