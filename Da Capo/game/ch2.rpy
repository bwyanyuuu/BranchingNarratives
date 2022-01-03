call ch3_0 from ch3
label ch2_0:
    # chapter transition
    scene bg black with fade
    show text "{size=+36}{font=temingti.ttf}第二章{/font}{/size}" at truecenter with fade
    pause 1.0
    scene bg black with Dissolve(0.5)

    # start
    scene bg otherworld
    u "這裡就是康切爾托啊……"
    while True:
        nvl_narrator "我環顧四周，自己正置身於一片無際的荒野。挾帶砂石的風無差別的拍打在荒原上的所有事物上。這裡沒有樹木，唯一的綠意來自一簇一簇匍匐在地、接近枯萎的雜草，一些大小不一的{a=jump:stone}{color=#ffffff}石塊{/color}{/a}散落其間，從手掌大小到半人高都有，{a=jump:surface}{color=#ffffff}表面粗糙且凹凸不平{/color}{/a}。所有的景物都因為來自{a=jump:sky}{color=#ffffff}天空{/color}{/a}光線的反射，泛著妖異的紅。"
        nvl clear

    
label stone:
    "我撿起地上一塊稍微小一點的石頭，試圖解析它的諾特組成，但被石塊銳利的邊緣劃傷了掌心。"
    jump ch2_1


label surface:
    "我直直盯著身旁一個與視線齊平的巨大石塊。"
    jump ch2_1

label sky:
    "我抬頭仔細地觀察這片天空。"
    "沒有雲朵與樹蔭的遮蔽，如同剛流出的鮮血一般的紅色天空壓迫著我的視覺迴路，彷彿再多看一秒就會將雙眼灼傷。"
    jump ch2_1

label ch2_1:
    jump ch3_0

    



