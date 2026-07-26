# 第二批 AI 場景 Prompt（萬用底圖 ＋ 精緻情境）

**版本：** v1
**日期：** 2026-07-15
**用途：** 第二批 AI 生成。**4 張萬用底圖**（生活／食譜格輪流換文案、套產品用）＋ **精緻情境**（星空、全景）。D1 開篇已生（0715-5）。
**風格：** 已串定案 §0（Snow Peak 特徵不點名、夏天短袖、人物柔焦互動不擺拍、Kodak Portra、留白、4:5、防競品／logo／浮水印／怪手）。搭配 [visual-prompts](./2026-07-14-30day-visual-prompts.md) 與 [asset-sourcing](./2026-07-15-30day-asset-sourcing-plan.md)。

> **萬用底圖＝留空版**（桌面留空，產品之後 Canva 貼／或另用 GPT 擺）。生完一張可套多格。

---

## 4 張萬用底圖

### 底圖 A｜晨光木桌（→ 套 D4 備料、D8 圍爐早晨）
```
editorial lifestyle photograph, understated high-end Japanese minimalist outdoor aesthetic (no real brand products or logos), cinematic quiet wabi-sabi, generous negative space,
a low wooden camping table at a shaded forest campsite in early summer morning, soft warm side light with gentle golden backlight,
CLEAN EMPTY TABLETOP with open center-front space for tableware later, only a linen napkin and a few leaves as props,
behind the table a family (short-sleeve, caps) softly out of focus, caught mid natural candid interaction, not posed,
Kodak Portra film aesthetic, fine grain, low contrast, muted desaturated earthy palette, vertical 4:5

--no cups bowls plates mugs on table, brand logo, snow peak, "keith", watermark, winter clothing, long sleeves, deformed hands, posed, oversaturated, CGI
```

### 底圖 B｜林蔭／溪邊下午茶（→ 套 D13 下午茶、D7 司康、D16 認識食材）
```
editorial lifestyle photograph, understated high-end Japanese minimalist outdoor aesthetic (no real brand products or logos), cinematic quiet wabi-sabi, generous negative space,
a picnic setting in a sunlit forest clearing or by a stream in summer afternoon, dappled light, a low table or picnic mat,
CLEAN EMPTY surface with open space for food and tableware later, natural props (leaves, wood),
a family (short-sleeve, caps) softly out of focus, relaxed candid interaction, not posed,
Kodak Portra film aesthetic, fine grain, low contrast, muted desaturated earthy palette, vertical 4:5

--no cups bowls plates on surface, brand logo, snow peak, "keith", watermark, winter clothing, long sleeves, deformed hands, posed, oversaturated, CGI
```

### 底圖 C｜備料桌面（→ 套 D4 備料、D16 認識食材、D21 拼盤）
```
editorial lifestyle photograph, understated high-end Japanese minimalist outdoor aesthetic (no real brand products or logos), cinematic quiet,
top-down / high angle of a wooden camp prep table in summer daylight, fresh colorful vegetables and ingredients laid out,
open space reserved for a cutting board and tableware later, natural imperfect arrangement,
a hand or two softly blurred at the edge (not close-up), documentary feel,
Kodak Portra film aesthetic, fine grain, low contrast, muted earthy palette, vertical 4:5

--no cutting board or bowls placed yet, brand logo, snow peak, "keith", watermark, winter clothing, deformed hands, extra fingers, posed, oversaturated
```

### 底圖 D｜黃昏營地（→ 套 D19 黃昏餐桌、D24 雨天可改陰天版）
```
editorial lifestyle photograph, understated high-end Japanese minimalist outdoor aesthetic (no real brand products or logos), cinematic quiet wabi-sabi, generous negative space,
a low wooden camping table at a campsite at golden-hour dusk in summer, warm orange glow at horizon, soft atmospheric light,
CLEAN EMPTY TABLETOP with open center space for tableware later, linen and leaves as props,
a family (short-sleeve, caps) softly out of focus at the table, warm candid interaction, not posed,
Kodak Portra film aesthetic, fine grain, low contrast, muted earthy palette, vertical 4:5

--no cups bowls plates on table, brand logo, snow peak, "keith", watermark, winter clothing, long sleeves, deformed hands, posed, oversaturated
```

---

## 精緻情境（2 張特殊）

### D22｜星空夜營
```
editorial lifestyle photograph, understated high-end Japanese minimalist outdoor aesthetic (no real brand products or logos), cinematic quiet,
a family lying under an open tarp at night, looking up at a dense starry sky and milky way over Taiwan mountains in summer,
soft warm lantern glow, low-light natural grain, deep muted tones, quiet wonder, generous negative space for text,
figures softly lit, not posed, an empty space beside them for a titanium mug later,
film aesthetic, low contrast, vertical 4:5

--no bright daylight, brand logo, snow peak, "keith", watermark, winter clothing, deformed hands, posed, oversaturated, CGI, fake-looking stars
```

### D29｜餐桌全景（全產品線收束）
```
editorial lifestyle photograph, understated high-end Japanese minimalist outdoor aesthetic (no real brand products or logos), cinematic quiet,
a hero overhead / 45-degree shot of a fully set outdoor family dining table in summer daylight, warm cohesive earthy styling,
CLEAN table surface with clearly arranged open spots where titanium tableware (mugs, bowls, plates, cutting board) will be composited later,
food and natural props present, a family softly out of focus around the table, candid,
Kodak Portra film aesthetic, fine grain, low contrast, muted earthy palette, vertical 4:5

--no tableware drawn yet (leave spots), brand logo, snow peak, "keith", watermark, winter clothing, deformed hands, posed, oversaturated
```
> 全景產品多、logo 風險高 → **強烈建議 Canva 合成官網真品**（別讓 AI 畫一整桌鈦餐具）。這張留空底圖，產品全部後製貼。

---

## 生成順序建議

1. 先生 **4 張萬用底圖**（A→D）——這 4 張輪用最多格，優先
2. 再生 **D22 星空、D29 全景**（特殊，各一張）
3. 每張生完，需要產品的格子 → Canva 貼官網真品＋調光影（見 [product-cards-copy](./2026-07-15-product-cards-copy.md) 的合成邏輯）
4. 全部走定案 §0，logo／浮水印靠 Canva 後製官方檔＋去除元數據
