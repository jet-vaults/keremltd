# -*- coding: utf-8 -*-
"""Static site generator for keremltd.co.il.

    python tools/build.py

Writes every HTML page under wwwroot/. Content lives in this file so the
whole site can be regenerated after a copy change. No dependencies.
"""
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WWW = os.path.join(ROOT, "wwwroot")
with open(os.path.join(ROOT, "tools", "images.json"), encoding="utf-8") as _f:
    IMAGES = json.load(_f)
with open(os.path.join(WWW, "assets", "css", "site.css"), encoding="utf-8") as _f:
    CSS = _f.read().replace("</", "<\\/")

SITE = "https://keremltd.co.il"
BRAND = "כרם יזמות והתחדשות עירונית"
PHONE = "03-6121314"
PHONE_TEL = "+97236121314"
EMAIL = "office@keremltd.co.il"
ADDRESS = "דרך בגין 82, בית אופקים, קומה 5, תל אביב 67138"
FACEBOOK = "https://www.facebook.com/keremltd"
EN_SITE = "https://keremltd.com/"
WEB3FORMS_KEY = "YOUR-WEB3FORMS-ACCESS-KEY"
TODAY = date.today().strftime("%d.%m.%Y")

# --------------------------------------------------------------------------
# Content
# --------------------------------------------------------------------------

PROJECTS = [
    # --- בשיווק ---
    dict(slug="louis-marshall-11", img="marshall", name="לואי מרשל 11", city="תל אביב", area="הצפון הישן",
         status="התקבל היתר", group="marketing", type="תמ״א 38/2, הריסה ובנייה",
         floors="8", units="20", shops=None,
         short="בניין בוטיק בן 8 קומות בצפון הישן, בין כיכר המדינה לפארק הירקון.",
         desc=[
             "פרויקט מגורים ייחודי בלב תל אביב, ברחוב לואי מרשל השקט, בצפון הישן האיכותי והיוקרתי, בקרבת פארק הירקון, כיכר המדינה ואבן גבירול, ובמרחק הליכה מהים.",
             "הפרויקט מעניק חוויית מגורים בבניין בוטיק בן 8 קומות בעיצוב אדריכלי מודרני ומוקפד ובסטנדרט גבוה, הכולל 20 יחידות דיור בעלות מפרט טכני עשיר.",
             "הדירות כולן מתוכננות בקפידה תוך ניצול מקסימלי של החלל. לכל דירה מרפסת שמש מרווחת, 3 דירות בלבד בקומה ו־2 כיווני אוויר לכל דירה. בקומת הקרקע 2 דירות גן ובקומת הגג 2 דירות פנטהאוז.",
         ],
         marshall=True),
    dict(slug="grofit-3", img="grofit", name="מבוא גרופית 3", city="תל אביב", area="הצפון הישן",
         status="הבנייה החלה", group="marketing", type="תמ״א 38/2, הריסה ובנייה",
         external="https://www.grofit3.co.il/",
         short="חוויית מגורים מושלמת, איכות חיים גבוהה, במיקום נדיר ובאווירה תל אביבית מקורית."),
    dict(slug="bernstein-11", img="bernstein", name="אדוארד ברנשטיין 11", city="תל אביב", area="",
         status="אושר בוועדה המקומית", group="marketing", type="תמ״א 38/2, הריסה ובנייה",
         external="https://eduard11.co.il/",
         short="פרויקט תמ״א 38/2, הריסה ובנייה מחדש."),
    dict(slug="arlozorov-53", img="arlozorov", name="ארלוזורוב 53", city="רמת גן", area="שכונת חשמונאים",
         status="בשיווק", group="marketing", type="בניין מגורים חדש",
         external="https://arlozorov53.co.il/",
         short="בניין מגורים חדש בשכונת חשמונאים הוותיקה."),
    # --- בתכנון ---
    dict(slug="pinsker-53-55", img="pinsker", name="פינסקר 53+55", city="תל אביב", area="רובע 3, לב העיר",
         status="בשלבי תכנון", group="planning", type="תמ״א 38/2, הריסה ובנייה",
         floors="7 + גג", units="37", shops="3",
         short="7 קומות, 37 דירות ו־5 מיני פנטהאוזים עם בריכה פרטית, במרחק הליכה מכיכר דיזנגוף.",
         desc=[
             "הפרויקט ממוקם ברובע 3 במרכז תל אביב, בסביבה עירונית נעימה, במרחק הליכה מכיכר דיזנגוף, דיזנגוף סנטר ורחוב בוגרשוב השוקק, וכמה דקות הליכה מהים, מבתי הקפה והמסעדות. נגישות נוחה לכל שירותי היום־יום: בהליכה, באופניים, בתחבורה ציבורית וברכב.",
             "אנחנו מקדמים מבנה חדש בגובה 7 קומות + גג, הכולל 37 דירות, מתוכן 5 מיני פנטהאוזים עם בריכה פרטית על הגג לכל יחידה, ושלוש חנויות בקומת הקרקע.",
         ]),
    dict(slug="cordovero-22", img="cordovero", name="קורדובירו 22", city="תל אביב", area="פלורנטין",
         status="בשלבי תכנון", group="planning", type="תמ״א 38/2, הריסה ובנייה",
         floors="4 + גג", units="18", shops="2",
         short="4 קומות ו־18 דירות במדרחוב בלב פלורנטין, כולל פנטהאוז עם בריכה על הגג.",
         desc=[
             "בלב שכונת פלורנטין התוססת, במדרחוב, במרחק הליכה מבתי קפה, מסעדות, גלריות וחיי רחוב מלאי אופי. השילוב המושלם בין קצב עירוני לאיכות חיים.",
             "אנחנו מקדמים מבנה חדש בגובה 4 קומות + גג, הכולל 18 דירות, מתוכן פנטהאוז עם בריכה על הגג, ושתי חנויות בקומת הקרקע.",
         ]),
    dict(slug="weisburg-4", img="weisburg4", name="ויסבורג 4", city="תל אביב", area="צהלה",
         status="בשלבי תכנון", group="planning", type="תמ״א 38/2, הריסה ובנייה",
         floors="5", units="14", shops=None,
         short="בניין בן 5 קומות ו־14 יחידות דיור בלב צהלה.",
         desc=["בלב הפועם של צהלה יוקם בניין בן 5 קומות, הכולל 14 יחידות דיור."]),
    dict(slug="weisburg-6", img="weisburg6", name="ויסבורג 6", city="תל אביב", area="צהלה",
         status="בשלבי תכנון", group="planning", type="תמ״א 38/2, הריסה ובנייה",
         floors="5", units="9", shops=None,
         short="בניין בן 5 קומות ו־9 יחידות דיור ברחוב שקט בצהלה.",
         desc=["בלב צהלה, ברחוב שקט, יוקם בניין בן חמש קומות הכולל 9 יחידות דיור."]),
    dict(slug="nahmani-64", img="nahmani", name="נחמני 64", city="תל אביב", area="לב העיר, פינת בגין 27",
         status="בשלבי תכנון", group="planning", type="שימור והשבחה",
         floors="3", units="13 ← 32", shops="10 ← 9",
         short="בניין לשימור בלב מרכז העסקים של תל אביב: מ־13 דירות ו־10 חנויות ל־32 דירות ו־9 חנויות.",
         desc=[
             "בניין מגורים בן 3 קומות, הכולל 13 דירות מעל קומת מסחר ובה 10 חנויות (חלקן מחוברות) וקומת מרתף חלקית. הבניין מוגדר לשימור עם הגבלות מחמירות במסגרת תכנית השימור של תל אביב, בלב מרכז העסקים הראשי של העיר.",
             "בשלב הנוכחי אנו מקדמים תכנית להשביח את הבניין הקיים מ־13 דירות ו־10 חנויות ל־32 דירות ו־9 חנויות.",
         ]),
    dict(slug="mazeh-71", img="mazeh", name="מזא״ה 71", city="תל אביב–יפו", area="לב העיר",
         status="בשלבי תכנון", group="planning", type="שימור והשבחה",
         floors=None, units="18 ← 30", shops=None,
         short="בניין לשימור בלב תל אביב: השבחה מ־18 ל־30 דירות, חצרות וגגות.",
         desc=[
             "בניין מגורים הכולל 18 דירות, המוגדר לשימור ללא הגבלות מחמירות במסגרת תכנית השימור של העיר תל אביב.",
             "בשלב הנוכחי אנו מקדמים תכנית להשביח את הבניין הקיים מ־18 דירות ל־30 דירות, חצרות וגגות.",
         ]),
    dict(slug="herut-40", img="herut", name="חירות 40", city="רמת גן", area="שכונת הגפן",
         status="בשלבי תכנון", group="planning", type="תמ״א 38/2, הריסה ובנייה",
         floors="9", units="21", shops=None,
         short="בניין בן 9 קומות ו־21 דירות בלב שכונת הגפן הפסטורלית.",
         desc=[
             "בניין בן 9 קומות, סה״כ 21 דירות, בלב שכונת הגפן הפסטורלית, בקרבת גני ילדים ובית ספר, ובמרחק קצר מפארק הירקון ומקניון איילון. הבניין ממוקם באחד המיקומים המבוקשים והנחשקים באזור.",
             "סטטוס: הפרויקט בשלבי תכנון מול העירייה.",
         ]),
    dict(slug="talpiot-30", img="talpiot", name="תלפיות 30", city="רמת גן", area="מרכז העיר",
         status="בשלבי תכנון", group="planning", type="תמ״א 38/2, הריסה ובנייה",
         floors="9", units="22", shops=None,
         short="בניין בן 9 קומות ו־22 דירות במרכז העיר השוקק של רמת גן.",
         desc=[
             "בניין בן 9 קומות, סה״כ 22 דירות, במיקום מושלם בלב העיר רמת גן, במרכז העיר השוקק. במרחק דקות ספורות ונגיש לכל שירותי הקהילה: חנויות, גני ילדים, בתי ספר, שירותי ציבור וגינות.",
             "סטטוס: הפרויקט בשלבי תכנון מול העירייה.",
         ]),
    # --- הסתיימו ---
    dict(slug="jaffa-road-13", img="yafo", name="דרך יפו 13", city="תל אביב", area="לב העיר, ליד רוטשילד",
         status="הסתיים ואוכלס", group="done", type="שימור ושחזור",
         floors="4", units="35", shops="10",
         short="אחד הבניינים המרהיבים מימיה הראשונים של תל אביב, משוחזר ומודרני. 35 דירות ו־10 חנויות.",
         desc=[
             "בניין לשימור בן 4 קומות, סה״כ 35 דירות ו־10 חנויות. הבניין הוכרז לשימור, ועם סיום הפרויקט נחשף אחד הבניינים המרהיבים של תל אביב מימיה הראשונים של העיר: מבנה משוחזר ומודרני, עם כל הפינוקים.",
             "במרתף חלל משותף גדול עם מכונות כביסה ומייבשים לשימוש הדיירים. הבניין בקרבת שדרות רוטשילד ורחוב לילינבלום, ובמרחק דקות ספורות על קורקינט מהים.",
             "סטטוס: הפרויקט הסתיים ואוכלס.",
         ]),
    dict(slug="rothschild-135", img="rothschild", name="רוטשילד 135", city="תל אביב", area="הבית על הבימה",
         status="הסתיים ואוכלס", group="done", type="בניין בוטיק",
         floors="5", units="15", shops=None,
         short="הבית על הבימה: בניין בוטיק בן 5 קומות עם דירות יוקרה ופנטהאוז ענק.",
         desc=[
             "בניין בן 5 קומות, סה״כ 15 דירות, בלב תל אביב. הבית על הבימה הוא בניין בוטיק המציע דירות יוקרה ופנטהאוז ענק, ומעניק חוויית מגורים מושלמת: איכות חיים גבוהה, מיקום ייחודי מסוגו, עיצוב לנוחות, שלווה וחברותא, באווירה תל אביבית מקורית.",
             "סטטוס: הפרויקט הסתיים ואוכלס.",
         ]),
    dict(slug="hoshea-21-23", img="hoshea", name="הושע 21+23", city="בני ברק", area="",
         status="בביצוע", group="done", type="הריסה ובנייה מחדש",
         floors=None, units="41", shops=None,
         short="41 דירות חדשות להשכרה לטווח ארוך, וקומת קרקע עם 3 גני ילדים חדשים.",
         desc=[
             "פרויקט הריסה ובנייה מחדש: 41 דירות מגורים חדשות להשכרה לטווח ארוך, ובנוסף קומת קרקע עם 3 גני ילדים חדשים.",
         ],
         extra_img="hoshea-2"),
    dict(slug="bat-shua-8", img="batshua", name="בת שוע 8", city="רמת גן", area="",
         status="השיווק הסתיים", group="done", type="בניין מגורים",
         short="בניין מגורים חדש ברמת גן. השיווק הסתיים.",
         desc=["בניין מגורים חדש ברמת גן. שיווק הדירות בפרויקט הסתיים."]),
]
BY_SLUG = {p["slug"]: p for p in PROJECTS}
GROUPS = [
    ("marketing", "פרויקטים בשיווק", "היתרים, בנייה ושיווק פעיל"),
    ("planning", "פרויקטים בתכנון", "לפני החלטת ועדה: מחירי הנחה והטבות למצטרפים מוקדם"),
    ("done", "פרויקטים שהסתיימו", "מסירה ואכלוס"),
]

SPECIALTIES = [
    ("ייזום ותכנון", "מהתכנון ועד המסירה",
     "אנו מטפלים בפרויקטי נדל״ן בשני מסלולים: רכישה של הפרויקט כולו, או ניהול רכיב היזמות לאורך כל הפרויקט, מהתכנון דרך הביצוע ועד המסירה."),
    ("התחדשות עירונית", "פינוי־בינוי ושימור במרכזי הערים",
     "תחום זה הוא בליבת העשייה שלנו: פרויקטי נדל״ן בתוך מרכזי הערים, כולל בניינים לשימור, שבהם נדרשת רגישות אדריכלית לצד יכולת ביצוע."),
    ("תמ״א 38", "הריסה ובנייה מחדש",
     "החברה מציעה את שירותיה וניסיונה כיזם בפרויקטי תמ״א 38/2, עם התחייבות לתהליך אישי, שקוף ומסודר מול הדיירים."),
]

GROUP_COMPANIES = [
    ("אחזקת נכסים", "מעגן בע״מ",
     "חברת הניהול והאחזקה של נכסי המשפחה ונכסים נוספים. עוסקת בניהול שוטף של נכסים רבים, כולל השכרת דירות למגורים ותחזוקתן."),
    ("שירותים משפטיים", "ד״ר משה וינברג ושות׳, עורכי דין ונוטריון",
     "תחומי העיסוק העיקריים: תכנון ובנייה, הפשרת קרקעות, פיתוח מקרקעין, הפקעת מקרקעין, נדל״ן, משפט אזרחי כללי וליטיגציה. המשרד קידם ויזם פיתוח של אלפי יחידות דיור ברחבי הארץ."),
    ("פיננסים", "מ.ו. השקעות בע״מ",
     "פועלת מול גופי המימון למימון נדל״ן, יחד עם כל מערכת הפיננסים בישראל: בנקים, חברות ביטוח, חברות מימון ושוק ההון."),
    ("מלאי דירות להשכרה", "רכישה, השבחה וניהול",
     "התמחות בדירות להשכרה ליד תחבורה ציבורית בגוש דן (רכבת קלה, מטרו, נת״צ): זיהוי הזדמנויות, רכישה והשבחה, תחזוקה ומימוש בעיתוי הנכון."),
]

FIRST_STEP = [
    "שולחים לנו שם של איש קשר. אנו יוצרים קשר טלפוני ומתאמים פגישה ראשונה להיכרות כללית.",
    "יחד נכין רשימה של הדיירים בנכס עם פרטי התקשרות.",
    "מאתרים דייר אחד דומיננטי שמוביל את הצעד הראשון בנכס. זה מקל מאוד על ההתקדמות בשלב זה. בהמשך, כשהפרויקט יתקדם, תיבחר נציגות של 3 דיירים.",
    "נפגשים יחד עם כל הדיירים לאסיפת דיירים ראשונית להיכרות.",
    "רק לאחר אסיפת הדיירים נוכל להבין יחד, היזם והדיירים, האם יש בנכס כדאיות לפרויקט, ונכין רשימה של שלבים להתקדמות.",
    "נעשה שיעורי בית מול הרשות המקומית והצוות הפנימי שלנו, נחזור אליכם ונציג לדיירים הצעה התפורה לנכס שבבעלותם, ונתקדם לפי התייחסויות הדיירים.",
]

MARSHALL_APTS = [
    ("דירה 1", "דירת גן", "2 חדרים", "67 מ״ר", "55 מ״ר גן", ""),
    ("דירה 2", "דירה", "3 חדרים", "70 מ״ר", "11 מ״ר מרפסת", "מבצע לזמן מוגבל"),
    ("דירה 3", "דירה", "3 חדרים", "76 מ״ר", "11 מ״ר מרפסת", "4,820,300 ₪ · מבצע לזמן מוגבל"),
    ("דירה 4", "דירה", "3 חדרים", "62 מ״ר", "14 מ״ר מרפסת", "נמכרה"),
    ("דירה 5", "דירה", "3 חדרים", "70 מ״ר", "11 מ״ר מרפסת", "מבצע לזמן מוגבל"),
    ("דירה 17", "פנטהאוז", "3 חדרים", "80 מ״ר", "50 מ״ר מרפסת", ""),
    ("דירה 18", "מיני פנטהאוז", "2 חדרים", "60 מ״ר", "21 מ״ר מרפסת", "נמכרה"),
    ("דירה 19", "דירה", "3 חדרים", "73 מ״ר", "6 מ״ר מרפסת", ""),
    ("דירה 20", "דירה", "2 חדרים", "56 מ״ר", "5.5 מ״ר מרפסת", ""),
    ("איחוד 19+20", "פנטהאוז", "4 חדרים", "120 מ״ר", "20 מ״ר מרפסת", ""),
]

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def picture(name, alt, sizes, cls="", eager=False, aspect=None):
    m = IMAGES[name]
    variants = m["sizes"]
    avif = ", ".join(f"/assets/img/{name}-{v['w']}.avif {v['w']}w" for v in variants)
    webp = ", ".join(f"/assets/img/{name}-{v['w']}.webp {v['w']}w" for v in variants)
    largest = variants[-1]
    fallback = variants[min(1, len(variants) - 1)]
    attrs = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (
        f'<picture{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>'
        f'<source type="image/avif" srcset="{avif}" sizes="{sizes}">'
        f'<img src="/assets/img/{name}-{fallback["w"]}.webp" srcset="{webp}" sizes="{sizes}" '
        f'width="{largest["w"]}" height="{largest["h"]}" alt="{esc(alt)}" {attrs}>'
        f"</picture>"
    )


def preload(name, sizes):
    m = IMAGES[name]
    srcset = ", ".join(f"/assets/img/{name}-{v['w']}.avif {v['w']}w" for v in m["sizes"])
    return f'<link rel="preload" as="image" fetchpriority="high" type="image/avif" imagesrcset="{srcset}" imagesizes="{sizes}">'


def card(p, eager=False):
    href = p.get("external") or f"/projects/{p['slug']}/"
    ext = ' target="_blank" rel="noopener"' if p.get("external") else ""
    city = p["city"] + (f" · {p['area']}" if p.get("area") else "")
    return f"""<a class="card rv-img" href="{href}"{ext} data-status="{p['group']}">
  <div class="frame">{picture(p['img'], f"{p['name']}, {p['city']}", "(max-width:560px) 92vw, (max-width:900px) 46vw, 30vw", eager=eager)}</div>
  <div class="meta">
    <h3>{esc(p['name'])}</h3>{'<span class="ext"> · אתר הפרויקט ↗</span>' if p.get('external') else ''}
    <div class="sub"><span>{esc(city)}</span><span class="status">{esc(p['status'])}</span></div>
  </div>
</a>"""


def cards(items, cols):
    return f'<div class="cards cards--{cols}">\n' + "\n".join(card(p) for p in items) + "\n</div>"


def project_groups(cols_by_group=None):
    cols_by_group = cols_by_group or {"marketing": 2, "planning": 4, "done": 4}
    out = []
    for key, title, note in GROUPS:
        items = [p for p in PROJECTS if p["group"] == key]
        out.append(f"""<div class="group" id="{key}">
  <div class="group-head"><h3>{title}</h3><span class="note">{note} · {len(items)}</span></div>
  {cards(items, cols_by_group[key])}
</div>""")
    return "\n".join(out)


def head(title, desc, path, extra="", og_image="hero-1200"):
    full = f"{title} | {BRAND}" if path != "/" else f"{BRAND} | ארבעה דורות של יזמות נדל״ן בגוש דן"
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="he_IL">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/assets/img/{og_image}.webp">
<meta name="theme-color" content="#f6f4ef">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="preload" href="/assets/fonts/plex-hebrew-300-hebrew.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plex-hebrew-400-hebrew.woff2" as="font" type="font/woff2" crossorigin>
{extra}
<style>{CSS}</style>
<script>document.documentElement.classList.remove('no-js')</script>
</head>
<body>
<a class="skip" href="#main">דלג לתוכן</a>
"""


def header(current):
    items = [("/", "ראשי"), ("/about/", "אודות החברה"), ("/projects/", "פרויקטים"),
             ("/how-we-start/", "איך מתחילים פרויקט"), ("/contact/", "צור קשר")]
    links = "".join(
        f'<a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if h == current else ""}>{t}</a>' for h, t in items)
    return f"""<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="/" aria-label="{esc(BRAND)} - דף הבית"><img src="/assets/img/logo.png" width="150" height="43" alt="{esc(BRAND)}"></a>
    <nav class="menu" id="menu" aria-label="ניווט ראשי">
      {links}
      <a href="{EN_SITE}" lang="en" hreflang="en">EN</a>
      <a class="menu-phone" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a>
    </nav>
    <a class="head-phone" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a>
    <button class="burger" type="button" aria-controls="menu" aria-expanded="false" aria-label="פתיחת תפריט"><span></span></button>
  </div>
</header>
<main id="main">
"""


def footer():
    return f"""</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="/assets/img/logo.png" width="150" height="43" alt="" loading="lazy">
        <p>חברה משפחתית בבעלות פרטית, מקבוצת וינברג. ארבעה דורות של יזמות נדל״ן, תכנון ובנייה של אלפי יחידות דיור ומסחר.</p>
      </div>
      <div class="foot-col">
        <p class="foot-h">ניווט</p>
        <a href="/about/">אודות החברה</a>
        <a href="/projects/">פרויקטים</a>
        <a href="/how-we-start/">איך מתחילים פרויקט</a>
        <a href="/contact/">צור קשר</a>
        <a href="{EN_SITE}" lang="en">English</a>
      </div>
      <div class="foot-col">
        <p class="foot-h">מידע</p>
        <a href="/accessibility/">הצהרת נגישות</a>
        <a href="/privacy/">מדיניות פרטיות</a>
        <a href="{FACEBOOK}" target="_blank" rel="noopener">פייסבוק</a>
      </div>
      <div class="foot-col">
        <p class="foot-h">פרטי התקשרות</p>
        <a href="tel:{PHONE_TEL}" dir="ltr" style="text-align:start">{PHONE}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <span style="display:block;padding:4px 0">{ADDRESS}</span>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© {date.today().year} {BRAND}. כל הזכויות שמורות.</span>
      <span>התמונות וההדמיות להמחשה בלבד</span>
    </div>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
<script src="/assets/js/a11y.js" defer></script>
</body>
</html>
"""


def contact_form(project_field=True, compact=False):
    proj = ""
    if project_field:
        opts = "".join(f'<option value="{esc(p["name"])}">{esc(p["name"])}, {esc(p["city"])}</option>' for p in PROJECTS)
        proj = f"""<div class="full"><label for="f-topic">בנוגע ל</label>
      <select id="f-topic" name="topic"><option value="">בחרו נושא</option><option>רכישת דירה</option><option>התחדשות עירונית / פינוי־בינוי</option><option>תמ״א 38</option><option>יזמות</option><option>אחר</option></select></div>
    <div class="full"><label for="f-project">פרויקט (אם רלוונטי)</label>
      <select id="f-project" name="project"><option value="">ללא פרויקט מסוים</option>{opts}</select></div>"""
    return f"""<form class="form" action="https://api.web3forms.com/submit" method="POST" novalidate>
    <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
    <input type="hidden" name="subject" value="פנייה חדשה מאתר כרם">
    <input type="hidden" name="from_name" value="keremltd.co.il">
    <label class="hp" aria-hidden="true">אין למלא שדה זה <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></label>
    <div><label for="f-name">שם מלא</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
    <div><label for="f-phone">טלפון</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
    <div class="full"><label for="f-email">אימייל</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
    {proj}
    {'' if compact else '<div class="full"><label for="f-msg">הודעה</label><textarea id="f-msg" name="message"></textarea></div>'}
    <label class="consent"><input type="checkbox" name="consent" value="כן" required><span>אני מאשר/ת יצירת קשר בהתאם ל<a href="/privacy/" class="link">מדיניות הפרטיות</a>.</span></label>
    <div class="actions"><button class="btn" type="submit">שליחה</button><span class="small muted">או התקשרו: <a href="tel:{PHONE_TEL}" dir="ltr" class="link">{PHONE}</a></span></div>
    <p class="form__msg" aria-live="polite"></p>
  </form>"""


def contact_section():
    return f"""<section class="section rule" id="contact">
  <div class="wrap grid">
    <div class="contact-info rv">
      <span class="eyebrow">צור קשר</span>
      <h2>מעוניינים שנחזור אליכם?</h2>
      <p class="lead">רכישת דירה, בניין שמתאים להתחדשות עירונית, או התייעצות בכל עניין בנדל״ן. השאירו פרטים ונציג יחזור אליכם בהקדם.</p>
      <dl class="dl">
        <div><dt>טלפון</dt><dd><a href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a></dd></div>
        <div><dt>אימייל</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>משרד</dt><dd>{ADDRESS}</dd></div>
      </dl>
    </div>
    <div class="contact-form rv">{contact_form()}</div>
  </div>
</section>"""


def write(path, html):
    full = os.path.join(WWW, path.strip("/"), "index.html") if path != "/" else os.path.join(WWW, "index.html")
    if path.endswith(".html"):
        full = os.path.join(WWW, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", path)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------

def page_home():
    hero_sizes = "(max-width:900px) 92vw, 48vw"
    marketing = [p for p in PROJECTS if p["group"] == "marketing"]
    planning = [p for p in PROJECTS if p["group"] == "planning"]
    done = [p for p in PROJECTS if p["group"] == "done"]
    specialties = "".join(f"""<div class="row rv"><span class="num">0{i+1}</span><h3>{t}<small>{s}</small></h3><p>{d}</p></div>""" for i, (t, s, d) in enumerate(SPECIALTIES))
    steps = "".join(f"<li>{s}</li>" for s in FIRST_STEP[:4])
    html = head(BRAND, "כרם יזמות והתחדשות עירונית, מקבוצת וינברג: חברה משפחתית עם ניסיון של ארבעה דורות ביזמות נדל״ן, תמ״א 38, פינוי־בינוי ושימור בתל אביב, רמת גן ובני ברק.", "/", preload("hero", hero_sizes))
    html += header("/")
    html += f"""<section class="hero">
  <div class="wrap grid">
    <div class="hero-text">
      <span class="eyebrow">כרם יזמות והתחדשות עירונית · מקבוצת וינברג</span>
      <h1>בונים את העיר מחדש.<br>כבר ארבעה דורות.</h1>
      <p class="lead">חברה משפחתית בבעלות פרטית, המתמחה בפרויקטי מגורים במרכזי הערים: תמ״א 38, פינוי־בינוי ושימור, בתל אביב, רמת גן ובני ברק.</p>
      <div class="cta-row"><a class="btn" href="/projects/">לפרויקטים</a><a class="btn btn--ghost" href="/how-we-start/">איך מתחילים פרויקט</a></div>
    </div>
    <div class="hero-media">
      <figure>
        <div class="frame">{picture("hero", "הדמיית מזא״ה 71, תל אביב: בניין לשימור שעובר השבחה", hero_sizes, eager=True)}</div>
        <figcaption><span>מזא״ה 71, תל אביב–יפו · בניין לשימור</span><span>בשלבי תכנון</span></figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="wrap section--tight">
  <div class="facts rv">
    <div><b>4</b><span>דורות של יזמות נדל״ן</span></div>
    <div><b>{len(PROJECTS)}</b><span>פרויקטים בשיווק, בתכנון ובאכלוס</span></div>
    <div><b>אלפי</b><span>יחידות דיור ומסחר שתוכננו ונבנו</span></div>
    <div><b>3</b><span>ערים: תל אביב, רמת גן, בני ברק</span></div>
  </div>
</section>

<section class="section" id="projects">
  <div class="wrap">
    <div class="sec-head rv"><h2>פרויקטים המשתבחים עם השנים</h2><a class="link aside" href="/projects/">כל הפרויקטים</a></div>
    <div class="group">
      <div class="group-head"><h3>בשיווק</h3><span class="note">היתרים, בנייה ושיווק פעיל · {len(marketing)}</span></div>
      {cards(marketing, 2)}
    </div>
    <div class="group">
      <div class="group-head"><h3>בתכנון</h3><span class="note">לפני החלטת ועדה: מחירי הנחה והטבות · {len(planning)}</span></div>
      {cards(planning[:4], 4)}
    </div>
    <div class="group">
      <div class="group-head"><h3>הסתיימו</h3><span class="note">מסירה ואכלוס · {len(done)}</span></div>
      {cards(done, 4)}
    </div>
    <div class="cta-row" style="justify-content:flex-start"><a class="btn btn--ghost" href="/projects/">לרשימת הפרויקטים המלאה</a></div>
  </div>
</section>

<section class="section rule">
  <div class="wrap grid split">
    <div class="split-text rv">
      <span class="eyebrow">אודות החברה</span>
      <h2>חברה משפחתית. ארבעה דורות של בנייה.</h2>
      <p>כרם יזמות נדל״ן והתחדשות עירונית היא חברה של מומחים, עם ניסיון של ארבעה דורות ביזמות נדל״ן, תכנון ובנייה של אלפי יחידות דיור ומסחר. ההתמחות בשנים האחרונות היא בפרויקטי מגורים במרכז העיר: תמ״א 38 ופינוי־בינוי.</p>
      <p>החברה בבעלות פרטית מלאה של המשפחה, המחזיקה גם חברות משלימות בתחומי המשפט, אחזקת הנכסים והמימון. מנכ״ל החברה: רני וינברג.</p>
      <div class="cta-row"><a class="link" href="/about/">על החברה ועל קבוצת וינברג</a></div>
    </div>
    <div class="split-media rv-img">
      <figure>
        <div class="frame" style="aspect-ratio:3/2">{picture("yafo", "דרך יפו 13, תל אביב: בניין לשימור משוחזר, הסתיים ואוכלס", "(max-width:900px) 92vw, 48vw")}</div>
        <figcaption><span>דרך יפו 13, תל אביב · בניין לשימור, משוחזר</span><span>הסתיים ואוכלס</span></figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap">
    <div class="sec-head rv"><h2>תחומי ההתמחות</h2><span class="aside">מגורים · תמ״א 38 · פינוי־בינוי · שימור</span></div>
    <div class="rows">{specialties}</div>
  </div>
</section>

<section class="band band--navy statement">
  <div class="wrap grid">
    <div class="statement-text rv">
      <span class="eyebrow">איך מתחילים פרויקט?</span>
      <h2>הצעד הראשון הוא היכרות. בלי חתימות, בלי התחייבות.</h2>
      <p>כבעלי דירה בבניין, לא פשוט להזיז קדימה דבר כזה: קשה לאסוף את כל הדיירים, קשה להבין מה נכון מול הרבה יזמים שמבטיחים הבטחות, וקשה להתנהל מול יזם ועורך דין בלי להכיר את המושגים.</p>
      <p>לכן יש לנו שיטה סדורה ופשוטה, צעד אחר צעד, לכל סוג פרויקט. מטרת הצעד הראשון היא היכרות בלבד: להבין יחד, היזם והדיירים, האם יש בנכס כדאיות.</p>
      <div class="cta-row"><a class="btn btn--light" href="/how-we-start/">כל השלבים</a><a class="btn btn--outline-light" href="/contact/">שולחים שם של איש קשר</a></div>
    </div>
    <div class="statement-aside rv">
      <ol>{steps}</ol>
    </div>
  </div>
</section>

{contact_section()}
"""
    html += footer()
    write("/", html)


def page_projects():
    html = head("פרויקטים", "כל הפרויקטים של כרם יזמות והתחדשות עירונית: בשיווק, בתכנון ואחרי אכלוס. תמ״א 38, פינוי־בינוי ושימור בתל אביב, רמת גן ובני ברק.", "/projects/")
    html += header("/projects/")
    html += f"""<section class="wrap page-head">
  <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><span>פרויקטים</span></nav>
  <h1>פרויקטים המשתבחים עם השנים</h1>
  <p class="lead">בניינים במרכזי הערים של גוש דן: הריסה ובנייה מחדש, שימור והשבחה, ופרויקטים חדשים. מסודרים לפי שלב.</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  {project_groups({"marketing": 2, "planning": 4, "done": 4})}
</section>
{contact_section()}
"""
    html += footer()
    write("/projects/", html)


def page_project(p):
    title = f"{p['name']}, {p['city']}"
    desc = p.get("short", "")
    html = head(title, desc, f"/projects/{p['slug']}/", preload(p["img"], "(max-width:1280px) 92vw, 1184px"), og_image=f"{p['img']}-1200")
    html += header("/projects/")
    facts = []
    if p.get("type"):
        facts.append(("סוג הפרויקט", p["type"]))
    facts.append(("עיר", p["city"] + (f", {p['area']}" if p.get("area") else "")))
    if p.get("floors"):
        facts.append(("קומות", p["floors"]))
    if p.get("units"):
        facts.append(("יחידות דיור", p["units"]))
    if p.get("shops"):
        facts.append(("מסחר", p["shops"] + " חנויות"))
    facts.append(("סטטוס", p["status"]))
    spec = "".join(f"<div><dt>{k}</dt><dd>{esc(v)}</dd></div>" for k, v in facts)
    body = "".join(f"<p>{esc(d)}</p>" for d in p.get("desc", [p.get("short", "")]))

    # neighbours: next 3 projects in list order (wrap around)
    idx = PROJECTS.index(p)
    others = [PROJECTS[(idx + i) % len(PROJECTS)] for i in range(1, 4)]

    extra = ""
    if p.get("marshall"):
        rows = "".join(
            f'<tr class="{"sold" if n == "נמכרה" else ""}"><td>{a}</td><td>{t}</td><td>{r}</td><td>{s}</td><td>{o}</td><td>{"<span class=tag>" + n + "</span>" if n and n != "נמכרה" else n}</td></tr>'
            for a, t, r, s, o, n in MARSHALL_APTS)
        gallery = "".join(
            f'<figure class="rv-img"><div class="frame">{picture(f"apt-{i}", f"הדמיית פנים, לואי מרשל 11, תמונה {i}", "(max-width:640px) 92vw, 48vw")}</div></figure>'
            for i in range(1, 9))
        extra = f"""
<section class="wrap section rule">
  <div class="sec-head rv"><h2>הדירות</h2><span class="aside">3 דירות בקומה · 2 כיווני אוויר · מרפסת שמש לכל דירה</span></div>
  <div style="overflow-x:auto"><table class="apts">
    <thead><tr><th>דירה</th><th>סוג</th><th>חדרים</th><th>שטח</th><th>חוץ</th><th>הערות</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
  <p class="notice">הפרטים בדף זה הינם להמחשה ולמסירת מידע בלבד, ואינם מהווים התחייבות מצד החברה. את החברה יחייבו הסכם המכר והמפרט הטכני לפי חוק המכר עליו יחתמו החברה והרוכשים. תכניות המכירה כוללות פרטי ריהוט ומוצרי חשמל להמחשה בלבד, שאינם כלולים בממכר. ט.ל.ח.</p>
</section>
<section class="wrap section rule">
  <div class="sec-head rv"><h2>הדמיות פנים</h2><span class="aside">להמחשה בלבד</span></div>
  <div class="gallery">{gallery}</div>
</section>
<section class="wrap section rule">
  <div class="grid">
    <div class="proj-body prose rv">
      <span class="eyebrow">מפרט טכני</span>
      <h2 style="margin-top:0">מרווח, מוקפד, ברמה הגבוהה ביותר</h2>
      <ul>
        <li>דלת ביטחון מעוצבת בכניסה לדירה, מערכת אינטרקום עם צפייה במעגל סגור במסך צבעוני. דלתות פנים יוניק פרימיום בגובה 2.1 מ׳.</li>
        <li>מערכת מיזוג אוויר VRF.</li>
        <li>חשמל חכם, אביזרי קצה גוויס או ביטיצ׳ינו.</li>
        <li>מטבח מעוצב, גודלו על פי התכנון האדריכלי ותכניות הדירה.</li>
        <li>חדרי אמבטיה: חיפוי עד התקרה, ברזים, אסלות, אמבטיות ומקלחונים וניאגרה סמויה. חמת, גרוהה, אידיאל סטנדרט או גיבריט.</li>
        <li>חלונות וויטרינות קליל או אקסטל, תריסים חשמליים עם מנועי סומפי, זיגוג כפול אקוסטי מבודד, רשתות נגד יתושים בכל הפתחים (למעט ממ״ד, על פי תקן).</li>
      </ul>
    </div>
    <div class="proj-side rv">
      <div class="people" style="grid-template-columns:1fr">
        <div><p class="role">האדריכל</p><h3>מאור לוי, לוי לוסטיג אדריכלים</h3><p class="small muted">המשרד עוסק בתכנון ועיצוב בתים ודירות מגורים ובפרויקטי תמ״א 38. מאור לוי הוא אדריכל, בעל תואר שני במנהל עסקים ומוסמך מכון התקנים כמלווה בנייה ירוקה, עם ניסיון רב שנים בבנייה אורבנית ופרטית.</p></div>
        <div><p class="role">עורך דין היזם</p><h3>משרד עו״ד ד״ר משה וינברג</h3><p class="small muted">משרד מוביל בתחום האזרחי: תכנון ובנייה, הפשרת קרקעות, פיתוח והפקעת מקרקעין ומשפט אזרחי. המשרד קידם ויזם פיתוח של אלפי יחידות דיור ברחבי הארץ ומקיים קשר שוטף עם רשויות התכנון.</p></div>
      </div>
    </div>
  </div>
</section>"""

    extra_fig = ""
    if p.get("extra_img"):
        extra_fig = f"""<figure class="rv-img" style="margin:40px 0 0"><div class="frame" style="overflow:hidden;background:var(--bg-2)">{picture(p['extra_img'], f"{p['name']}, {p['city']}: הדמיה נוספת", "(max-width:900px) 92vw, 58vw")}</div></figure>"""

    html += f"""<section class="wrap page-head">
  <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><a href="/projects/">פרויקטים</a><span>/</span><span>{esc(p['name'])}</span></nav>
  <span class="eyebrow">{esc(p['status'])} · {esc(p.get('type',''))}</span>
  <h1>{esc(p['name'])}, {esc(p['city'])}</h1>
  {'<p class="lead">' + esc(p['short']) + '</p>' if p.get('short') else ''}
</section>
<section class="wrap proj-hero">
  <figure style="margin:0">
    <div class="frame">{picture(p['img'], f"הדמיית {p['name']}, {p['city']}", "(max-width:1280px) 92vw, 1184px", eager=True)}</div>
    <figcaption>הדמיה להמחשה בלבד</figcaption>
  </figure>
</section>
<section class="wrap section">
  <div class="grid">
    <div class="proj-body prose rv">
      <span class="eyebrow">על הפרויקט</span>
      {body}
      {extra_fig}
    </div>
    <aside class="proj-side rv">
      <dl class="spec">{spec}</dl>
      <div class="cta-row"><a class="btn" href="/contact/">מעוניינים בפרטים נוספים</a></div>
      <p class="small muted" style="margin-top:14px">או התקשרו: <a class="link" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a></p>
    </aside>
  </div>
</section>
{extra}
<section class="wrap section rule">
  <div class="sec-head rv"><h2>פרויקטים נוספים</h2><a class="link aside" href="/projects/">כל הפרויקטים</a></div>
  {cards(others, 3)}
</section>
{contact_section()}
"""
    html += footer()
    write(f"/projects/{p['slug']}/", html)


def page_about():
    specialties = "".join(f"""<div class="row rv"><span class="num">0{i+1}</span><h3>{t}<small>{s}</small></h3><p>{d}</p></div>""" for i, (t, s, d) in enumerate(SPECIALTIES))
    companies = "".join(f"""<div class="row rv"><span class="num">0{i+1}</span><h3>{t}<small>{s}</small></h3><p>{d}</p></div>""" for i, (t, s, d) in enumerate(GROUP_COMPANIES))
    html = head("אודות החברה", "כרם יזמות נדל״ן והתחדשות עירונית: חברה משפחתית מקבוצת וינברג, עם ניסיון של ארבעה דורות ביזמות, תכנון ובנייה של אלפי יחידות דיור ומסחר.", "/about/")
    html += header("/about/")
    html += f"""<section class="wrap page-head">
  <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><span>אודות החברה</span></nav>
  <span class="eyebrow">אודות החברה</span>
  <h1>ניסיון של ארבעה דורות ביזמות נדל״ן</h1>
  <p class="lead">כרם יזמות נדל״ן והתחדשות עירונית היא חברה מובילה של מומחים, עם ניסיון עשיר של ארבעה דורות ביזמות נדל״ן, תכנון ובנייה של אלפי יחידות דיור ומסחר.</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  <div class="grid split">
    <div class="split-text prose rv">
      <p>ההתמחות בשנים האחרונות היא בפרויקטי מגורים במרכז העיר: תמ״א 38 ופינוי־בינוי, לצד שימור והשבחה של בניינים היסטוריים בלב תל אביב.</p>
      <p>החברה משפחתית ובבעלות פרטית מלאה של המשפחה. בנוסף מחזיקה המשפחה חברות נוספות המתמחות במוצרים משלימים בתחום הנדל״ן: שירותים משפטיים, תחזוקת נכסים, פיננסים ומלאי דירות להשכרה. כך, כל שלב בפרויקט נשען על ידע וניסיון מתוך הבית.</p>
      <p>מנכ״ל החברה: רני וינברג.</p>
    </div>
    <div class="split-media rv-img">
      <figure>
        <div class="frame" style="aspect-ratio:3/2">{picture("rothschild", "רוטשילד 135, הבית על הבימה, תל אביב", "(max-width:900px) 92vw, 48vw")}</div>
        <figcaption><span>רוטשילד 135, הבית על הבימה · תל אביב</span><span>הסתיים ואוכלס</span></figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="section rule">
  <div class="wrap grid split">
    <div class="split-text rv">
      <span class="eyebrow">מקבוצת וינברג</span>
      <h2>חברה משפחתית, מנוהלת מקרוב</h2>
      <p class="lead">כל פרויקט מלווה אישית, מהפגישה הראשונה עם הדיירים ועד מסירת המפתחות.</p>
      <p>הקבוצה פועלת בתל אביב, רמת גן ובני ברק, ומשלבת יזמות, תכנון, מימון, ייצוג משפטי וניהול נכסים תחת קורת גג אחת. מנכ״ל החברה: רני וינברג.</p>
    </div>
    <div class="split-media rv-img">
      <figure>
        <div class="frame" style="aspect-ratio:3/2">{picture("yafo", "דרך יפו 13, תל אביב: בניין לשימור משוחזר", "(max-width:900px) 92vw, 48vw")}</div>
        <figcaption><span>דרך יפו 13, תל אביב · שימור ושחזור</span><span>הסתיים ואוכלס</span></figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="section rule">
  <div class="wrap">
    <div class="sec-head rv"><h2>תחומי ההתמחות</h2><span class="aside">מתמחים בפרויקטים של מגורים, תמ״א 38 ופינוי־בינוי</span></div>
    <div class="rows">{specialties}</div>
  </div>
</section>
<section class="section rule">
  <div class="wrap">
    <div class="sec-head rv"><h2>חברות נוספות בבעלות המשפחה</h2><span class="aside">מוצרים משלימים בתחום הנדל״ן</span></div>
    <div class="rows">{companies}</div>
  </div>
</section>
{contact_section()}
"""
    html += footer()
    write("/about/", html)


def page_how():
    steps = "".join(f"<li>{s}</li>" for s in FIRST_STEP)
    html = head("איך מתחילים פרויקט?", "הצעד הראשון בפרויקט תמ״א 38 או פינוי־בינוי: שיטה סדורה ופשוטה, צעד אחר צעד, בלי חתימות ובלי התחייבות. כך מתחילים עם כרם.", "/how-we-start/")
    html += header("/how-we-start/")
    html += f"""<section class="wrap page-head">
  <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><span>איך מתחילים פרויקט</span></nav>
  <span class="eyebrow">איך מתחילים פרויקט?</span>
  <h1>כבעלי דירה בבניין, לא פשוט להזיז קדימה דבר כזה</h1>
  <p class="lead">״איך מתחילים?״ זה הצעד הראשון, וגם הקשה ביותר. לכן יש לנו שיטה סדורה ופשוטה, צעד אחר צעד, לכל סוג פרויקט.</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  <div class="grid split">
    <div class="split-text prose rv">
      <p>קשה לאסוף את כל הדיירים ולהגיע להחלטות. קשה להבין מה נכון מול הרבה יזמים, שכל אחד מהם מבטיח הבטחות. וקשה להתנהל מול יזם ומול עורך דין בלי להכיר את המושגים.</p>
      <p><strong>אבל זה שווה הכול.</strong> בסוף התהליך אתם יושבים בסלון החדש, אוכלים ארוחת ערב משפחתית במרפסת החדשה, ואז החיוך שווה הכול.</p>
      <p>ההתחלה של תהליך לפרויקט תמ״א 38, פינוי־בינוי, כל פרויקט התחדשות עירונית או תכנון וביצוע מסוג אחר בנכס שלכם, היא להבין בדיוק מה רוצים.</p>
    </div>
    <div class="split-media rv-img">
      <figure>
        <div class="frame" style="aspect-ratio:3/2">{picture("herut", "הדמיית חירות 40, רמת גן", "(max-width:900px) 92vw, 48vw")}</div>
        <figcaption><span>חירות 40, רמת גן · שכונת הגפן</span><span>בשלבי תכנון</span></figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="section rule">
  <div class="wrap grid">
    <div class="proj-body prose rv">
      <span class="eyebrow">הצעד הראשון</span>
      <h2 style="margin-top:0">מסע ארוך מתחיל בצעד קטן</h2>
      <p>״הצעד הראשון״ של התהליך הוא פשוט ופועל בשיטה מסודרת מאוד. מטרתו היא היכרות בלבד:</p>
      <ol>{steps}</ol>
      <p style="margin-top:24px">רק כשכל הדיירים יסכימו באופן כללי (ולא מחייב בשום אופן) על אופי ההצעה, נמשיך לשלב הבא.</p>
      <p class="small muted">ההחלטות עצמן, לגבי כל דבר, מתקבלות רק באסיפת דיירים עם נוכחות מלאה של כל הדיירים וזכות הצבעה לדיירים בלבד. בשלב זה לא מדובר בהחלטות, אלא רק באיסוף מידע להבנת הצרכים של הפרויקט.</p>
    </div>
    <aside class="proj-side rv">
      <dl class="spec">
        <div><dt>התחייבות</dt><dd>לא נדרשת</dd></div>
        <div><dt>חתימות</dt><dd>לא נדרשות</dd></div>
        <div><dt>מטרת השלב</dt><dd>היכרות ובחינת כדאיות</dd></div>
      </dl>
      <p style="margin-top:22px"><strong>חשוב לדעת:</strong> אנחנו רק בשלב ההיכרות, לבחון האם יש כדאיות. מהצד של הדיירים: האם כדאי כל הבלגן הזה? מהצד של היזם: האם יש רווחיות?</p>
      <div class="cta-row"><a class="btn" href="/contact/">שולחים שם של איש קשר</a></div>
    </aside>
  </div>
</section>
{contact_section()}
"""
    html += footer()
    write("/how-we-start/", html)


def page_contact():
    html = head("צור קשר", "נשמח לייעץ, ליזום, לתכנן, לפקח ולהוביל אתכם לפרויקט מוצלח של תמ״א 38, התחדשות עירונית ופינוי־בינוי. טלפון 03-6121314, office@keremltd.co.il.", "/contact/")
    html += header("/contact/")
    html += f"""<section class="wrap page-head">
  <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><span>צור קשר</span></nav>
  <span class="eyebrow">צור קשר</span>
  <h1>״איך מתחילים? ומה האסטרטגיה?״</h1>
  <p class="lead">נשמח לייעץ, ליזום, לתכנן, לפקח ולהוביל אתכם לפרויקט מוצלח של תמ״א 38, התחדשות עירונית ופינוי־בינוי, וגם להתייעצות בכל עניין בנדל״ן.</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  <div class="grid">
    <div class="contact-info rv">
      <dl class="dl" style="margin-top:0">
        <div><dt>טלפון</dt><dd><a href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a></dd></div>
        <div><dt>אימייל</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>כתובתנו</dt><dd>{ADDRESS}<br><a class="small" href="https://www.google.com/maps/search/?api=1&query=%D7%93%D7%A8%D7%9A+%D7%9E%D7%A0%D7%97%D7%9D+%D7%91%D7%92%D7%99%D7%9F+82+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91" target="_blank" rel="noopener">פתיחה במפות ↗</a></dd></div>
        <div><dt>פייסבוק</dt><dd><a href="{FACEBOOK}" target="_blank" rel="noopener">facebook.com/keremltd</a></dd></div>
      </dl>
    </div>
    <div class="contact-form rv">{contact_form()}</div>
  </div>
</section>
"""
    html += footer()
    write("/contact/", html)


def page_accessibility():
    html = head("הצהרת נגישות", "הצהרת הנגישות של אתר כרם יזמות והתחדשות עירונית.", "/accessibility/")
    html += header("/accessibility/")
    html += f"""<section class="wrap page-head">
  <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><span>הצהרת נגישות</span></nav>
  <span class="eyebrow">נגישות</span>
  <h1>הצהרת נגישות</h1>
</section>
<section class="wrap prose" style="padding-bottom:var(--section)">
  <p>אנו בכרם יזמות והתחדשות עירונית משקיעים ככל שניתן כדי לספק לכל לקוחותינו שירות שוויוני ונגיש, ולאפשר חוויית גלישה נוחה לכלל האוכלוסייה, לרבות אנשים עם מוגבלויות, בהתאם לחוק שוויון זכויות לאנשים עם מוגבלות.</p>
  <p>באתר זה בוצעו התאמות נגישות על פי דרישות תקנות שוויון זכויות לאנשים עם מוגבלות (התאמות נגישות לשירות), התשע״ג-2013, בצורה קפדנית ככל שניתן. ההתאמות בוצעו על פי המלצות התקן הישראלי (ת״י 5568) לנגישות תכנים באינטרנט ברמת AA ומסמך WCAG 2.0 הבינלאומי.</p>
  <h2>מידע על נגישות האתר</h2>
  <p>באתר מוטמע תפריט נגישות, הנפתח באמצעות כפתור הנגישות בתחתית המסך. התפריט כולל:</p>
  <ul>
    <li>הגדלת טקסט והקטנת טקסט</li>
    <li>גווני אפור</li>
    <li>ניגודיות גבוהה וניגודיות הפוכה</li>
    <li>רקע בהיר</li>
    <li>הדגשת קישורים</li>
    <li>פונט קריא</li>
    <li>איפוס ההגדרות</li>
  </ul>
  <p>בנוסף, האתר נבנה עם מבנה כותרות תקין, ניווט מלא באמצעות מקלדת, טקסט חלופי לתמונות, תמיכה בהעדפת הפחתת תנועה (Reduced Motion) ותגיות ARIA בתפריטים ובטפסים.</p>
  <h2>פנייה בנושא נגישות</h2>
  <p>אנו ממשיכים לפעול לשיפור נגישות האתר כחלק ממחויבותנו לאפשר לכלל האוכלוסייה לקבל שירות שווה והוגן. אם נתקלתם בבעיה כלשהי בנושא הנגישות, נשמח שתעדכנו אותנו ונעשה כל מאמץ למצוא פתרון מתאים ולטפל בבעיה בהקדם.</p>
  <p>טלפון: <a class="link" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a><br>דוא״ל: <a class="link" href="mailto:{EMAIL}">{EMAIL}</a></p>
  <h2>פרסום הצהרת הנגישות</h2>
  <p>הצהרת הנגישות עודכנה ביום {TODAY}.</p>
</section>
"""
    html += footer()
    write("/accessibility/", html)


def page_privacy():
    html = head("מדיניות פרטיות", "מדיניות הפרטיות של אתר כרם יזמות והתחדשות עירונית.", "/privacy/")
    html += header("/privacy/")
    html += f"""<section class="wrap page-head">
  <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><span>מדיניות פרטיות</span></nav>
  <span class="eyebrow">משפטי</span>
  <h1>מדיניות פרטיות</h1>
</section>
<section class="wrap prose" style="padding-bottom:var(--section)">
  <p>המידע המוצג להלן נועד לעזור למשתמש להבין מה המידע הנאסף על ידי כרם יזמות והתחדשות עירונית במהלך השימוש באתר האינטרנט שהיא מנהלת ומפעילה בכתובת keremltd.co.il (להלן: ״האתר״), מה השימושים שאנו עשויים לעשות במידע ומהם הכלים הטכנולוגיים שבהם אנו עשויים לעשות שימוש באתר.</p>
  <p>במדיניות פרטיות זו: ״משתמש״: כל אדם העושה שימוש כלשהו באתר, לרבות צפייה, גלישה, קריאה וכיו״ב. ״מידע אישי״: נתון הנוגע לאדם מזוהה או לאדם הניתן לזיהוי. ״עיבוד״, ״שימוש״ במידע: כל פעולה שמבוצעת על מידע, לרבות קבלתו, איסופו, אחסונו, העתקתו, עיון בו, העברתו או מתן גישה אליו. מדיניות פרטיות זו כתובה בלשון זכר מטעמי נוחות בלבד, והיא מתייחסת באופן שווה לכל המינים.</p>
  <h2>הסכמה למסירת מידע</h2>
  <p>בכפוף להוראות הדין, השימוש באתר מהווה הסכמה שלך למסירת מידע ושימוש בו למטרות המפורטות במדיניות פרטיות זו. בהתאם לחוק, לא חלה עליך חובה למסור לנו מידע. עם זאת, ככל שתבחר לא למסור לנו מידע, ייתכן שלא תוכל לעשות שימוש באתר ובשירותיו. ככל שתבחר למסור לנו מידע, הנך מצהיר ומאשר כי הפרטים נמסרים מרצונך החופשי ובהסכמתך. בנוסף, השימוש באתר מהווה הסכמה שלך לאיסוף, עיבוד, שימוש, העברה ושמירה של מידע שיתקבל על ידינו בהתאם למדיניות פרטיות זו.</p>
  <h2>המידע שנאסף על ידינו</h2>
  <p>ככלל, ניתן לגלוש באתר מבלי לספק לנו מידע אישי כלשהו. המידע האישי שאנו עשויים לאסוף במהלך שימוש באתר הוא מידע שתבחר למסור לנו במקרה שתפנה אלינו באמצעות האתר (כגון שם, אימייל, מספר טלפון וכיו״ב). בנוסף אנו עשויים לאסוף מידע אנליטי וסטטיסטי על אופן השימוש בשירותים שלנו (כגון דפים שבהם ביקרת, קישורים שעליהם לחצת ועוד), מידע על אופן ההתחברות לשירותים שלנו (כגון מיקום גיאוגרפי, כתובת IP, סוג הדפדפן, העדפת שפה, דפי נחיתה, מכשיר הקצה ועוד), וכדומה. אנו עשויים לאסוף מידע כאמור בעצמנו, באמצעות שירותים של צדדים שלישיים וכן באמצעות אמצעי ניטור (כגון עוגיות).</p>
  <h2>מטרות השימוש במידע</h2>
  <p>חברתנו עשויה להשתמש במידע אישי שתמסור לנו לצורך התקשרות אתך, כגון כדי להציע לך שירותים המסופקים על ידי חברתנו, לשיפור איכות השירותים ולצורך יצירת קשר עם המשתמש. מידע אישי כאמור לא ייחשף לעובדים ו/או נותני שירותים של החברה אלא באופן מוגבל ככל האפשר, ורק באותם מקרים שבהם הדבר חיוני להתקשרות אתך ולתפעול, תחזוקה ומתן תמיכה טכנית. מידע סטטיסטי על שימושים באתר נועד לשיפור פעילות האתר והשירותים המוצעים, בכפוף לכל הוראת דין.</p>
  <h2>עוגיות (Cookies)</h2>
  <p>אתר זה אינו מציב עוגיות מעקב ואינו משתמש בכלי ניתוח של צדדים שלישיים. תפריט הנגישות שומר את ההעדפות שבחרת (למשל גודל טקסט או ניגודיות) באחסון המקומי של הדפדפן שלך בלבד. מידע זה אינו נשלח אלינו ואינו מזהה אותך.</p>
  <h2>העברת מידע לצדדים שלישיים</h2>
  <ul>
    <li>המידע עשוי להיות מועבר לצדדים שלישיים בהתאם לתנאי מדיניות הפרטיות, באופן מידתי ובהתאם למטרות המוגדרות, ויכלול רק את המידע הרלוונטי למטרה זו.</li>
    <li>חברתנו רשאית להעביר את המידע לצדדים שלישיים המספקים לה שירותים שונים, כגון אבטחת מידע, טכנולוגיית מידע, אחסון מידע (לרבות שירות שליחת טפסים), ייעוץ משפטי ושירותים מקצועיים נוספים.</li>
    <li>במקרה שבו התקבל צו שיפוטי המחייב את חברתנו למסור את פרטי המשתמש בהתאם להוראות הדין; במקרים של מחלוקות או הליכים משפטיים בין המשתמש לבין חברתנו; במקרים של העברת בעלות, מיזוג או שינוי שליטה בחברתנו; וכאשר חברתנו סבורה כי מסירת המידע נדרשת לצורך מניעת נזק או צמצומו.</li>
  </ul>
  <h2>אבטחת מידע והגבלת אחריות</h2>
  <p>חברתנו נוקטת אמצעים טכניים ופיזיים מקובלים וסבירים כדי להגן על פרטיות ואבטחת המידע, בהתאם לסטנדרטים המקובלים. עם זאת, העברת מידע דרך האינטרנט אינה יכולה להיות בטוחה לחלוטין, וחברתנו אינה מתחייבת שהאתר יתנהל ללא כל הפרעה או שהאתר, מאגרי המידע והנתונים שנאספו יהיו חסינים באופן מוחלט מפני גישה בלתי מורשית. השימוש באתר מותנה בהסכמת המשתמש כי הוא מוסר את המידע על אחריותו בלבד. במקרה של חשש להפרת אבטחת מידע, יש לפנות אלינו בהקדם האפשרי.</p>
  <p>האתר עשוי להכיל קישורים לאתרים אחרים שאינם בפיקוחנו. השימוש באתרים של צדדים שלישיים כפוף לתנאי השימוש שלהם, וחברתנו לא תישא באחריות לכל נזק או הפסד שייגרם כתוצאה מהשימוש בהם.</p>
  <h2>תקופת שמירת המידע</h2>
  <p>חברתנו תשמור את המידע לפרק הזמן הדרוש למימוש המטרות המפורטות במדיניות זו, אלא אם כן נדרשת תקופת שמירה ארוכה יותר על פי דין.</p>
  <h2>מידע על צדדים שלישיים</h2>
  <p>אם המשתמש מספק לחברתנו מידע אישי על צדדים שלישיים, עליו לוודא כי קיבל את ההסכמה החוקית הנדרשת על פי דין.</p>
  <h2>הזכויות שלך</h2>
  <p>בכפוף להוראות הדין, תוכל לעיין במידע אישי אודותיך שיימצא במאגרי המידע של חברתנו ולבקש לתקן או למחוק מידע זה אם אינו נכון, שלם, ברור או מעודכן. כמו כן תוכל לבקש למחוק מידע אישי אודותיך ככל שהתקבל, נמסר או נאסף בניגוד להוראות הדין, או ככל שאינו נחוץ עוד למטרות שלשמן נאסף. כדי לממש זכויות אלו ניתן לפנות אלינו דרך <a class="link" href="/contact/">דף צור קשר</a>.</p>
  <h2>שונות</h2>
  <p>מדיניות הפרטיות והשימוש באתר כפופים לחוקי מדינת ישראל. סמכות השיפוט הבלעדית בכל מחלוקת שתתעורר תהיה בבתי המשפט בתל אביב–יפו. בעלת האתר רשאית לשנות מדיניות זו מעת לעת ותודיע על כך באמצעות פרסום מדיניות מתוקנת באתר עם תאריך עדכון. המשך השימוש באתר לאחר עדכון יהווה הסכמה למדיניות המתוקנת.</p>
  <h2>דרכי יצירת קשר</h2>
  <p>בכל שאלה ובקשה הנוגעת למדיניות פרטיות זו, ניתן לפנות אלינו בטלפון <a class="link" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a> או בדוא״ל <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <p class="small muted">תאריך עדכון: {TODAY}</p>
</section>
"""
    html += footer()
    write("/privacy/", html)


def page_404():
    html = head("הדף לא נמצא", "הדף המבוקש לא נמצא.", "/404.html")
    html += header("")
    html += """<section class="wrap err">
  <div>
    <span class="eyebrow">404</span>
    <h1>הדף לא נמצא</h1>
    <p class="lead">ייתכן שהכתובת השתנתה או שהדף הוסר.</p>
    <div class="cta-row" style="justify-content:center"><a class="btn" href="/">לדף הבית</a><a class="btn btn--ghost" href="/projects/">לפרויקטים</a></div>
  </div>
</section>
"""
    html += footer()
    write("/404.html", html)


def sitemap():
    urls = ["/", "/about/", "/projects/", "/how-we-start/", "/contact/", "/accessibility/", "/privacy/"]
    urls += [f"/projects/{p['slug']}/" for p in PROJECTS if not p.get("external") and p.get("desc")]
    today = date.today().isoformat()
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
    xml += "</urlset>\n"
    with open(os.path.join(WWW, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(xml)
    with open(os.path.join(WWW, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


def main():
    page_home()
    page_projects()
    for p in PROJECTS:
        if not p.get("external") and p.get("desc"):
            page_project(p)
    page_about()
    page_how()
    page_contact()
    page_accessibility()
    page_privacy()
    page_404()
    sitemap()


if __name__ == "__main__":
    main()
