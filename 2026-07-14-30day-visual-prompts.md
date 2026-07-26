# 三能戶外 30 天視覺 Prompt 生產包（佔位符版）

**版本：** v2（產品佔位符版）
**日期：** 2026-07-14
**用途：** 逐格圖片／影片生成 prompt，情境用 AI 生、產品用佔位符預留，你再請 GPT 換成實際三能產品照。
**涵蓋：** 單圖 17 ・ Reels 10（逐格）・ 輪播 3（逐張）＝ 88 格
**搭配：** [30 天貼文內容手冊](./2026-07-14-30day-content-scripts.html)

---

## 0｜怎麼用（佔位符流程）

> ✅ **風格定案**（2026-07-15，經 `0715` 系列驗證）：Snow Peak 風格特徵（**不點名品牌**，避免生出它的 logo）＋人物氛圍化柔焦、**有自然互動不擺拍**（器物為焦點、無前景手）＋夏季短袖。右下菱形浮水印為生圖工具所加，需工具端關閉／後製移除。此 §0 為全 88 格共用骨架。

1. 複製某格的**情境 prompt**（英文）貼進 GPT-5.5 圖像。
2. prompt 裡的 **`【產品：XXX】`** 是佔位符——標記「這裡要放一件三能產品」。
3. 依該格下方標的**型號**，到官網找對應產品照上傳給 GPT。
4. 把下面這句**替換指令**一起丟給 GPT：

> **【替換指令・複製用】**
> 這是一段場景描述，其中 `【產品：XX】` 是佔位符。我會上傳三能的實際產品照片，請把場景中對應的佔位符替換成我上傳的產品，維持**霧面拉絲純鈦質感**，讓產品的光影、角度、陰影與場景自然融合，**不要改變產品本身的外觀與比例**。其餘場景照 prompt 生成。

**BASE PROMPT（風格骨架，串在每格情境後）：**
```
editorial lifestyle photograph in the aesthetic of understated high-end Japanese minimalist outdoor lifestyle campaigns (do NOT render any real brand's products or logos) —
cinematic, quiet, wabi-sabi refined, generous negative space, thoughtful minimal composition, still and contemplative, minimal activity,
the titanium tableware, food and natural setting are the FOCUS; a Taiwanese family in SUMMER (parents 35-45 with one or two kids, lightweight short-sleeve earth-tone wear, caps / sun hats)
kept soft and atmospheric but caught mid natural candid interaction — passing food, leaning toward each other, laughing, tending the camp — real gestures and motion, never static, lined-up or posed; NO close-up hands or limbs in the foreground, NEVER a sharp posed subject,
shaded forest / riverside / cool high-altitude campsite, soft diffused natural light with gentle golden backlight, subtle atmospheric depth, bright but calm,
medium-format look, 50mm, shallow depth of field, Kodak Portra film aesthetic, fine film grain, low contrast,
muted desaturated earthy palette (deep green, khaki, charcoal, warm tan, cream, brushed titanium),
natural imperfect candid moment, quiet human presence, premium but unpretentious
```
**NEGATIVE（每格加）：**
```
hyperrealistic, flawless skin, plastic skin, 8k, masterpiece, perfect, oversaturated, CGI, 3d render, glossy plastic,
stock photo, studio lighting, watermark, text overlay,
winter clothing, fleece jacket, down jacket, puffer, long sleeves, scarf, beanie, autumn or winter mood, cold weather,
steaming hot pot, kettle boiling, any brand logo or text on cups/bowls/gear, competitor branding, "keith" text,
snow peak logo, harsh on-camera flash, busy cluttered composition, cheerful over-bright stock photo
```
> ⚠️ **防競品**：生成底圖時，所有杯碗盤器皿**盡量留白／不特寫、不帶任何品牌字樣**——AI 常亂生出對手 logo（實測 D1 生出了 "keith" 競品杯）。器皿一律等佔位替換階段換成三能真品；若底圖非生器皿不可，須為**無 logo 的乾淨霧面拉絲鈦**。
> 產品佔位一律呈現為 **matte brushed titanium（霧面拉絲鈦）**，替換時保持此質感。產品池與型號見 spec §2。

**輸出比例（生圖時務必指定，否則預設橫式、放 IG 會被裁）：**
| 格式 | 比例 | 尺寸 | 用途 |
|------|------|------|------|
| 單圖 | **4:5 直式** | 1080×1350 | IG／FB 貼文，版面最大、觸及最好 |
| 輪播 | **4:5 直式** | 1080×1350 | 每張同比例，滑動不跳版 |
| Reels 分鏡 | **9:16 直式** | 1080×1920 | 全螢幕短影音 |
> 指定法：GPT 圖像 prompt 講「vertical 4:5 photo」或「9:16 vertical」；Midjourney／FLUX 加 `--ar 4:5` 或 `--ar 9:16`。生直式時構圖要重想（桌面器物在下 1/3、森林光影往上留白）。
> **生圖 vs 最終尺寸**：上表是**最終發布**尺寸。生圖時先求「比例對＋解析度盡量高」（GPT 圖像選直式 portrait，約 1024×1536；Reels 選最接近 9:16 的直式），再把底圖拉進 **Canva 畫布（畫布尺寸設成上表值）** 裁切＋合成產品，匯出就是 IG 標準尺寸。生圖若不夠大，先 upscale 放大再合成。

---

## 1｜單圖（17 篇）　＝ 情境 prompt ＋ BASE ＋ NEGATIVE

**D1 開篇（FB）**
`wide candid shot, a family of four around a low camping table in a forest campsite at early morning, steam rising from a 【產品：純鈦雙層杯300ml】, a 【產品：折疊雪拉碗450ml】 with food, warm side light through trees, parents relaxed, kids reaching for food, cozy home-away-from-home mood`
產品：雙層杯 300ml（404004）、折疊雪拉碗 450ml（105004）

**D4 親子備料（IG）**
`top-down flat lay on a wooden camp table, prepped colorful vegetables, small seasoning containers, a 【產品：純鈦砧板IGT】 and 【產品：折疊雪拉碗450ml】 in a row, a child's hand sneaking a cherry tomato, morning light, organized-chaos outdoor kitchen`
產品：純鈦砧板 IGT（107001）、折疊雪拉碗（105004）

**D8 圍爐早晨（FB）**
`candid morning at campsite, a parent holding a 【產品：純鈦單層杯450ml】 with coffee steam, a kid running blurred outside the tent, soft golden morning haze, unhurried peaceful mood`
產品：純鈦單層杯 450ml（404002）

**D9 雙層杯保冷（FB）**
`close-up, a small child's hands holding a 【產品：純鈦雙層杯300ml】 filled with iced tea / cold drink, sweat-free outer wall (double-wall vacuum, no condensation), bright summer daylight, refreshing tone, shallow focus on the mug`
產品：純鈦雙層杯 300ml（404004）

**D10 孩子的餐具（IG）**
`a young child proudly holding a 【產品：三合一純鈦刀叉勺】, sitting at a camp table setting their own plate, focused proud expression, soft afternoon light, sense of ownership`
產品：三合一純鈦刀叉勺

**D13 森林下午茶（IG）**
`a patch of forest with sunbeams through canopy, a picnic mat with a 【產品：純鈦窗花餐盤16cm】 of biscuits and a 【產品：純鈦單層杯450ml】 of pour-over coffee, a child swinging legs, dreamy golden light, lens flare`
產品：窗花餐盤 16cm（105041）、單層杯 450ml（404002）

**D16 認識食材（FB）**
`a child at a camp prep table holding a whole spring onion with curiosity, a 【產品：純鈦砧板IGT】 with whole vegetables, parent guiding, teaching moment, soft daylight, documentary feel`
產品：純鈦砧板 IGT（107001）

**D18 窗花餐盤（IG）**
`beautiful food styling on a 【產品：純鈦窗花餐盤18cm】 (hollow window-pattern rim), colorful outdoor meal plated, on a wood table, appetizing angle, natural light, elegant but real`
產品：窗花餐盤 18cm（105044）（可帶 16/20cm 疊放）

**D19 黃昏餐桌（FB）**
`wide shot, a family at an outdoor dinner table at dusk, orange sunset glow, steam from food, 【產品：純鈦窗花餐盤20cm】 and 【產品：純鈦雙層杯300ml】, kids talking animatedly, golden-hour backlight, film grain`
產品：窗花餐盤 20cm（105047）、雙層杯 300ml（404004）

**D21 野餐拼盤（IG）**
`overhead flat lay, a rustic no-cook grazing board on a 【產品：純鈦砧板IGT】: hard cheese, nuts, dried fruit, crackers, arranged casually by a child, bright daylight, fresh and abundant, summer picnic mood`
產品：純鈦砧板 IGT（107001）

**D22 星空夜營（IG）**
`night scene, family lying under an open tarp looking at a dense starry sky over Taiwan mountains, a 【產品：純鈦雙層杯300ml】 with faint steam beside them, soft warm lantern glow, milky way, quiet wonder, low-light natural grain`
產品：雙層杯 300ml（404004）

**D23 水壺補水（FB）**
`a 【產品：純鈦水壺800ml】 on a trail rock, family blurred hiking behind, one member drinking, clean mountain daylight, condensation droplets, shared family hydration`
產品：純鈦水壺 800ml（106020）

**D24 雨天帳篷（FB）**
`inside a tarp on a rainy day, family playing a board game, steaming food in 【產品：折疊雪拉碗450ml】, cozy dim rainy light, raindrops on tarp edge, warm togetherness, shallow focus`
產品：折疊雪拉碗 450ml（105004）

**D25 餐具全家福（IG）**
`neat flat lay of 【產品：純鈦飯勺・湯勺・濾勺】 arranged like a family portrait on linen, soft window light, matte titanium texture detail, minimal elegant styling`
產品：純鈦飯勺（105025）、湯勺（105027）、濾勺（105028）

**D26 收營（IG）**
`packing up campsite, hands placing cleaned titanium plates and bowls into a 【產品：40L折疊收納箱】, tent half-down behind, restored grass, bittersweet end-of-trip mood, soft overcast light`
產品：40L 木桌板折疊收納箱（301007）

**D29 餐桌美學全景（FB）**
`hero overhead of a fully set outdoor family table showing the complete titanium tableware system: 【產品：純鈦單層杯450ml】【產品：折疊雪拉碗450ml】【產品：純鈦窗花餐盤18cm】【產品：純鈦砧板IGT】, warm cohesive earthy styling, natural daylight, editorial but real`
產品：單層杯（404002）、雪拉碗（105004）、窗花餐盤（105044）、砧板（107001）

**D30 收尾 CTA（FB＋IG）**
`warm wide shot at golden hour, family walking away on a mountain trail carrying gear, or a last shared table moment with titanium tableware, nostalgic hopeful tone, strong golden backlight, film grain, room for closing text`
產品：（品牌收束，產品為背景可選）

---

## 2｜Reels 逐格（10 支・每支 5 格）　`[秒] 畫面｜運鏡｜字卡`

**D2 單層杯・一杯的一天（IG）**
- `0–3s` pour-over coffee streaming into a 【產品：純鈦單層杯450ml】 at dawn, steam ｜ slow push-in ｜「我背包裡只有一個杯子」
- `3–6s` quick cuts: sipping, packing tent, walking ｜ handheld ｜「因為它一個抵三個」
- `6–10s` the same 【產品：純鈦單層杯450ml】 now with hot soup at noon ｜ match-cut ｜「同一個杯子，不用洗、不串味」
- `10–14s` macro of brushed titanium texture, tossed into backpack ｜ macro ｜「純鈦・無塗層・沒有金屬味」
- `結尾` mug on table, family bokeh ｜ static ｜「450ml 剛剛好｜LINE 領新朋友 100 元」
產品：純鈦單層杯 450ml（404002）

**D5 雪拉碗 450ml（IG）**
- `0–3s` a 【產品：純鈦雪拉碗450ml】 full of food ｜ top-down ｜「一碗多用，飯麵湯都行」
- `3–6s` the folding handle flipped inward against the bowl ｜ close-up ｜「折疊手柄，一折就收」
- `6–9s` several bowls stacked, placed into a pouch ｜ follow ｜「疊起來，收得小」
- `結尾` bowl on table ｜ static ｜「純鈦雪拉碗 450ml｜折疊手柄好收」
產品：純鈦雪拉碗 450ml（105004・碗身固定、**折疊手柄**收納，非碗身壓平）

**D6 莎莎醬 DIY（IG）**
- `0–3s` macro knife cutting tomato/pepper/onion/cilantro on a 【產品：純鈦砧板IGT】, vivid colors ｜ macro top-down ｜「露營版莎莎醬，免開火」
- `3–8s` a child helping chop and stir into a 【產品：折疊雪拉碗450ml】 ｜ handheld quick cuts ｜「孩子也能一起做」
- `8–12s` spooning salsa onto a tortilla chip, a bite ｜ close-up ｜「配玉米片，秒殺」
- `結尾` overhead of the colorful salsa bowl ｜ top-down ｜「留言『莎莎』拿黃金比例配方卡」
產品：純鈦砧板 IGT（107001）、折疊餐刀（105017）、折疊雪拉碗（105004）

**D7 Challenge① 司康（FB）**
- `0–3s` scones out of a home oven, warm ｜ close-up ｜「司康在家烤好，帶上山」
- `3–7s` slicing scone on a 【產品：純鈦砧板IGT】, spreading jam from a 【產品：折疊雪拉碗450ml】 ｜ handheld ｜「現場只要切、抹、開動」
- `7–11s` pairing with pour-over in a 【產品：純鈦單層杯450ml】, family sharing ｜ warm mid ｜「森林裡的下午茶」
- `結尾` styled scone plating ｜ top-down ｜「留言『司康』拿食譜｜下週：燕麥能量棒」
產品：砧板（107001）、雪拉碗（105004）、單層杯（404002）

**D11 折疊餐刀叉勺（三件・IG）**
- `0–3s` three pure titanium folding cutlery pieces (knife, fork, spoon) laid out ｜ macro ｜「刀、叉、勺，三件一套」
- `3–7s` unfolding one, using it on food ｜ quick cuts ｜「折疊收合，用完就收」
- `7–10s` folding, into a pouch, into backpack ｜ follow ｜「輕到孩子自己拿」
- `結尾` three pieces neatly arranged ｜ static ｜「純鈦折疊餐刀叉勺｜加入官網會員送 100 購物金」
產品：純鈦折疊餐刀 105017／叉 105018／勺 105019

**D14 Challenge② 能量棒（FB）**
- `0–3s` pressing oats/nuts/honey into a mold at home ｜ top-down ｜「燕麥能量棒，在家壓一壓」
- `3–7s` cutting into bars, wrapping, into backpack ｜ close-up ｜「乾的、超耐放，放一週沒問題」
- `7–11s` biting a bar at a summit, on a 【產品：純鈦窗花餐盤18cm】 ｜ mid with vista ｜「爬到哪、吃到哪」
- `結尾` bar cross-section macro ｜ macro ｜「留言『能量棒』拿配方｜下週：野餐拼盤」
產品：窗花餐盤 18cm（105044）、雙層杯（404004）

**D15 純鈦砧板（IG）**
- `0–3s` spreading a 【產品：純鈦砧板IGT】, chopping colorful ingredients ｜ top-down ｜「一塊砧板，備料上桌一次搞定」
- `3–7s` chopping garlic then rinsing the board clean under water ｜ close-up ｜「切過蒜，沖一下就乾淨」
- `7–10s` wipe dry, hang up ｜ close-up ｜「純鈦不吃色、不卡味」
- `結尾` titanium board texture ｜ macro ｜「純鈦砧板 IGT｜加入官網會員送 100 購物金」
產品：純鈦砧板 IGT（107001）

**D17 格蘭諾拉杯（IG）**
- `0–3s` pouring granola, nuts, dried fruit into a 【產品：純鈦雙層杯300ml】 ｜ top-down ｜「三種材料，倒一倒」
- `3–7s` shaking, eating, pouring shelf-stable plant milk ｜ handheld ｜「免火免冷藏，超省事」
- `7–10s` a child assembling their own cup ｜ mid ｜「孩子自己 DIY」
- `結尾` colorful granola cup close-up ｜ top-down ｜「留言『穀物』拿黃金比例」
產品：雙層杯 300ml（404004）、折疊雪拉碗（105004）

**D27 折疊收納箱（FB）**
- `0–3s` a 【產品：50L折疊收納箱】 packed full of gear ｜ mid ｜「裝得下全家的鍋碗」
- `3–6s` placing the wood tabletop on it, becomes a table ｜ follow ｜「蓋上，就是一張桌」
- `6–9s` titanium mugs/plates on top, family dining ｜ warm mid ｜「收納＋桌面，一物兩用」
- `9–12s` collapsing it flat when packing up ｜ time-lapse feel ｜「不用時，摺平帶走」
- `結尾` box side profile ｜ static ｜「40/50L 折疊收納箱｜LINE 新朋友 100 元」
產品：50L 木桌板折疊收納箱（301008）

**D28 Challenge④ 磅蛋糕（IG）**
- `0–3s` slicing pound cake at home, wrapping in paper ｜ close-up ｜「磅蛋糕在家烤好，常溫放得住」
- `3–7s` plating slices on a 【產品：純鈦窗花餐盤20cm】 at summit, tea ｜ styled mid ｜「山頂下午茶，擺盤就很美」
- `7–11s` family sharing, laughing, tired-but-happy ｜ warm candid ｜「甜的東西，讓累了一天的人瞬間回血」
- `結尾` pound cake slice macro ｜ macro ｜「留言『磅蛋糕』拿食譜｜四週 Challenge 完結」
產品：窗花餐盤 20cm（105047）

---

## 3｜輪播逐張（3 組・食安三問）

> 版式：品牌綠 `#314235` 底、米白 `#F5F2EC` 字、Georgia＋黑體混排，每張一重點、留白乾淨。內頁多為文字卡（Canva 套版即可，無需生圖）；**封面**可用情境照＋半透明綠遮罩＋大字，情境照才需 AI 生。

**D3 食安①（7 張）**
- 封面照 prompt：`close-up of a young child frowning and pushing away a metal water bottle at a campsite, candid, natural light`（＋BASE／NEGATIVE）｜疊字「孩子喝一口就吐掉的水／不是水的問題」
- 2「我聞了一下，一股鐵味——不鏽鋼瓶放久的那種」
- 3「那不是水的問題，是材質在跟水反應」
- 4「純鈦不會：夠純、不跟食物作用」
- 5「表面緻密不吸味——裝過什麼都不會偷偷記著」
- 6「最關鍵：沒有塗層，刮花了也不掉屑、安全無毒」
- 7 CTA「好餐具，讓你只嚐到食物本身／媽媽食安三問①／下一題：怎麼看出塗層？追蹤」

**D12 食安②（7 張）**
- 封面照 prompt：`macro of a scratched, peeling non-stick coating inside an old worn pot, harsh honest detail, natural light`｜疊字「你家的鍋杯，在偷偷剝落嗎？」
- 2「用久了刮花、掉色，那層塗層去哪了？」
- 3「答案：一部分，可能被你吃下去了」
- 4「怎麼避免？選一體成型、無塗層的」
- 5「純鈦本身就是安全材質，不需要塗層」
- 6「判斷法：看內壁有沒有另一層『膜』」
- 7 CTA「媽媽食安三問②／下一題：戶外沒冰箱怎麼吃得安全？追蹤」

**D20 食安③（7 張）**
- 封面照 prompt：`summer campsite table with food under warm daylight, a cooler box nearby, candid family camping`｜疊字「戶外沒冰箱，這些能放多久？」
- 2「夏天最怕：生的、乳製品、拌過美乃滋的」
- 3「原則一：能買常溫耐放的，就別帶冷藏的」
- 4「原則二：生鮮現做現吃，別留到下一餐」
- 5「原則三：餐具好清潔、不殘留＝少一個風險」
- 6「純鈦不卡味、不殘留，洗一下就乾淨」
- 7 CTA「媽媽食安三問③（完）／三題記得收藏／追蹤看更多」

---

## 4｜產品佔位對照（快速查）

| 佔位符 | 官網型號 | 官網 URL 關鍵字 |
|--------|---------|----------------|
| 純鈦單層杯450ml | 404002 | titanium-camp-mug-450ml-with-lid-1 |
| 純鈦單層杯300ml | 404001 | titanium-camp-mug-300ml-with-lid-1 |
| 純鈦雙層杯300ml | 404004 | titanium-camp-mug-300ml-1 |
| 純鈦雙層杯450ml | 404005 | 站內搜「404005／雙層杯450」|
| 折疊雪拉碗450ml（深碗，裝飯麵湯）| 105004 | pure-titanium-folding-sila-bowl-450ml |
| 純鈦雪拉杯450ml（淺杯，≠雪拉碗）| 105002 | 站內搜「105002／雪拉杯450」|
| 折疊餐刀／叉／勺（三件）| 105017／105018／105019 | pure-titanium-folding-knife/fork/spoon |
| ⚠️ 三合一刀叉勺（105023）已下架 | — | 改推上面三件分開 |
| 折疊餐刀/叉/勺 | 105017-20 | pure-titanium-folding-knife/fork/spoon |
| 純鈦飯勺/湯勺/濾勺 | 105025/27/28 | pure-titanium-rice-spoon / spoon / filter-spoon |
| 純鈦窗花餐盤16/18/20cm | 105041/44/47 | ..-pure-titanium-window-patterned-dinner-plate |
| 純鈦水壺800ml | 106020 | pure-titanium-water-bottle |
| 純鈦砧板IGT | 107001 | pure-titanium-cutting-board |
| 40/50L折疊收納箱 | 301007/08 | ..-foldable-storage-box-with-side-open-door |

---

*搭配 [內容手冊](./2026-07-14-30day-content-scripts.html) 與 [內容 spec](./2026-07-14-30day-social-content-spec.md) 使用。先生 D1／D2 首格／D3 封面 3 張校準風格，再全量。*
