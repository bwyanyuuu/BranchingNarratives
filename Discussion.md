# 多線專題討論
會議連結：https://meet.google.com/zwd-tqfy-rxc  
GitHub：https://github.com/linxiii/BranchingNarratives  
Mediawiki：http://139.162.117.77/mediawiki  
創作企劃書：https://hackmd.io/06iA2Ic2Tn637_xRbai0EA  
共用雲端硬碟：https://drive.google.com/drive/folders/0AOTZsYAiFx0vUk9PVA  
主機IP位址：139.162.117.77  
密碼：545463993C3BBDB920BD2A51591CEC83  
計畫詳細規則：https://docs.google.com/presentation/d/1C5Ozy4hyuokuXDqoQ6gLT5LP0nVAjq5-m_w91qhcLL4/edit#slide=id.g104796644d3_0_16
### 角色設定
+ 主角
    + 個性：冷酷、聰明
    + 內心OS：
    + 「伊洛」
+ 迪弗爾/切羅(自稱)：第一任魔王
+ 同事(男：艾弗利，女：艾弗麗)：序章
    + 自嗨、嘮叨
+ 
### renpy
+ 官方中文文件 https://renpy.cn/doc-tw/index.html
+ 支援中文：gui.rpy裡font相關都改成可支援中英字體的.ttf檔
+ 命名方式：
    + rpy：`ch%d.rpy -> ch0.rpy`
    + label：`ch%d_%d` 統一以0做開頭，編號遞增 → 每章開頭為 `ch%d_0`
        + 每多一層分支就再加一個 `_%d`，數字為選項編號 → `ch0_1_2`
    + 圖片檔名：每個人都有正常版(l)、灰灰版(d)，(可能會有表情版)，請用英文命名
        + `[name] l [emoji].png`：正常版，有表情再加後面
        + `[name] d.png`：灰灰版不會有表情
        + `bg [background name].png`：背景名稱
        + 有這個人/景但還沒有圖片，就直接 show 他，它會自動變成預設圖片
        + 主角一律用 `user[.*].png`，定義在 script.rpy
+ 語法：
    + 從別的 py 匯入 label：`call [label name] from [script name]` 
    + 跳到某 label：`jump [label name]` 
    + 建立角色：`define [variable] = Character('角色名', image = "標籤名字")`
        + 一律寫在 `script.rpy`?
        + 旁白：narrator
        + 整頁旁白：nvl_narrator，換頁要先 `nvl clean`
    + 小頭像：`image side [name] = "filename"`
        + 圖片 w 225 h 310
    + 顯示角色圖片：`show [img name] {at left/right}`
+ 其他參考資料：
    + https://www.reddit.com/r/RenPy/comments/ax5bnp/wikis_and_links_in_renpy/
    + https://lemmasoft.renai.us/forums/viewtopic.php?t=21303
    + https://lemmasoft.renai.us/forums/viewtopic.php?t=50239
    + https://www.renpy.org/doc/html/text.html#text-tag-a
    + 句末加結尾符號：https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=22196
### 縮短網址
+ 歐克里斯 https://reurl.cc/k70XEq
+ 諾特 https://reurl.cc/VjXL8N
+ 魔物 https://reurl.cc/Zr7Wl3
### 立繪
+ 填完找mini，開始動工後不能再改，做完會把vroid檔放雲端，想改自己改
    + 可以看下方的"其他參考"
    + 可以填
        + 網址
        + 圖片(我放在雲端的都可)
        + 顏色或其他條件:我隨便找較為符合的texture，決定完就不改
        + "不變":照原本的模
        + "隨便":我自己決定完就不改
        + "無":裸著(ex.不用鞋子就填"無")
    + 我已經有放幾個我覺得比較合適的參考上去，要改都可
+ 主角男：
    + 原王子(專題)
    + ![](https://i.imgur.com/hbMK4cA.png)
    + 衣服修
    + A. 金(玩家選擇主角)
        + 參考:![](https://i.imgur.com/Z4fjk6D.png)
        + 髮色:不變
        + 膚色:不變
        + 瞳色:![](https://i.imgur.com/M4veUt3.png)
    + B. 咖啡(同事)
        + 參考:![](https://i.imgur.com/jckGluM.png)
        + 髮色:![](https://i.imgur.com/i03Hh63.png)
        + 膚色:不變
        + 瞳色:![](https://i.imgur.com/UV4ZYeE.png)
    + 第一套:
        + 衣服: https://booth.pm/ja/items/2456669
        + 褲子:
        + 鞋子:
    + 第二套:
        + 衣服:
        + 褲子:
        + 鞋子:

+ 主角女：
    + 原公主(專題)
    + ![](https://i.imgur.com/lHjpZI8.png)
    + ![](https://i.imgur.com/8D1gind.png)
    + A. 金(玩家選擇主角)
        + 髮色:不變
        + 髮型:不變
        + 膚色:不變
        + 瞳色:![](https://i.imgur.com/M4veUt3.png)
    + B. 咖啡(同事)
        + 髮色:![](https://i.imgur.com/i03Hh63.png)
        + 髮型:不變
        + 膚色:不變
        + 瞳色:![](https://i.imgur.com/UV4ZYeE.png)
    + 第一套:
        + 衣服: https://booth.pm/ja/items/2456669
        + 褲子:
        + 鞋子:
    + 第二套:
        + 衣服:
        + 褲子:
        + 鞋子:
+ 主角斗篷蓋頭遮臉
+ 第一任魔王
    + 帥
    + 快三十，年長
    + 有三隻眼睛，瀏海蓋住(若隱若現)
    + 髮色:
    ![](https://i.imgur.com/qVKkaIf.png)
    ![](https://i.imgur.com/pTUD3kM.png)
    ![](https://i.imgur.com/11JIp78.png)
    ![](https://i.imgur.com/BRMbsEO.png)    
    ![](https://i.imgur.com/21kCA48.png)
    ![](https://i.imgur.com/oKOHkDn.png)
        + book：
            + 我想要深藍色的髮
    + 瞳色:![](https://i.imgur.com/limP2xA.png)
    ![](https://i.imgur.com/r52iNm8.png)
    ![](https://i.imgur.com/HduXPWk.png)
    ![](https://i.imgur.com/iJXYvye.png)
        + book：https://booth.pm/ja/items/2513611
            + ![](https://i.imgur.com/8yoq2fs.png)
            + ![](https://i.imgur.com/jEJ4ZrC.png)
            + 額頭上的眼是全黑的

    + 髮型:
        + book：https://booth.pm/ja/items/2788026
            + 我想要長髮帥大叔
            + ![](https://i.imgur.com/RA3HlUP.png)

    + 膚色:
    + 第一套:
        + 衣服:
        + 褲子:
        + 鞋子:
+ 村民A、B
    + 換髮色就好
    + 樸素的樣子
    + 髮色:黑
    + 瞳色:黑
    + 膚色:白
    + A:
        + 髮型:
        + 衣服:
        + 褲子:
        + 鞋子:
    + B:
        + 髮型:
        + 衣服:
        + 褲子:
        + 鞋子:
+ 人形魔物
    + 瞇瞇眼都是怪物
    + 長角：https://booth.pm/ja/items/2457350
        + ![](https://i.imgur.com/ADQKx2B.png)
    + 耳朵：https://booth.pm/ja/items/2308160
        + ![](https://i.imgur.com/0vCjeIY.png)
    + 髮色:
    + 髮型:
    + 瞳色:
    + 膚色:
    + 衣服:
    + 褲子:
    + 鞋子:
+ 鬼音鈴(團長、副團長)
    + 雙胞胎兄妹模
    + ![](https://i.imgur.com/LGV2DXH.png)
    + ![](https://i.imgur.com/zMPW7lj.png)
    + ![](https://i.imgur.com/j8KOcqZ.png)
    + 髮色:
    + 瞳色:
    + 膚色:
    + A. 兄
        + 髮型:
        + 衣服:
        + 褲子:
        + 鞋子:
    + A. 妹
        + 髮型:
        + 衣服:
        + 褲子:
        + 鞋子:
+ 其他參考
    + 髮型跟角色: https://drive.google.com/drive/u/1/folders/1N4wWlTemgQJD5mkl_wxZcF6EFhDesLmC
    https://drive.google.com/drive/u/1/folders/1P1Yiz3yX-_eragko76xxEoDhql1evEs5
    + 我有的各種texture們: https://drive.google.com/drive/u/1/folders/13muBtksOfEqh7eBSAfbDhrsmXeDLhHZ8
    + 衣服(網站): https://booth.pm/ja/search/VRoid?max_price=0




