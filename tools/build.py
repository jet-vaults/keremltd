# -*- coding: utf-8 -*-
"""Static site generator for keremltd.co.il (Hebrew + English).

    python tools/build.py

Writes every HTML page under wwwroot/ (Hebrew at /, English at /en/).
Content lives in this file so the whole site can be regenerated after a
copy change. No dependencies.
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
PHONE = "03-6121314"
PHONE_TEL = "+97236121314"
EMAIL = "office@keremltd.co.il"
FACEBOOK = "https://www.facebook.com/keremltd"
MAPS = "https://www.google.com/maps/search/?api=1&query=%D7%93%D7%A8%D7%9A+%D7%9E%D7%A0%D7%97%D7%9D+%D7%91%D7%92%D7%99%D7%9F+82+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91"
WEB3FORMS_KEY = "YOUR-WEB3FORMS-ACCESS-KEY"
TODAY = date.today().strftime("%d.%m.%Y")
STATEMENT_DATE = "23.09.2026"  # legal statements are dated when their text changes, not on every build


# --------------------------------------------------------------------------
# UI strings
# --------------------------------------------------------------------------

T = {
    "he": dict(
        dir="rtl", locale="he_IL",
        brand="כרם יזמות והתחדשות עירונית",
        brand_short="כרם",
        site_title="כרם יזמות והתחדשות עירונית | ארבעה דורות של יזמות נדל״ן בגוש דן",
        site_desc="כרם יזמות והתחדשות עירונית, מקבוצת וינברג: חברה משפחתית עם ניסיון של ארבעה דורות ביזמות נדל״ן, תמ״א 38, פינוי־בינוי ושימור בתל אביב, רמת גן ובני ברק.",
        skip="דלג לתוכן", home="ראשי", about="אודות החברה", projects="פרויקטים", how="איך מתחילים פרויקט", contact="צור קשר",
        lang_switch="EN", lang_switch_full="English", menu_open="פתיחת תפריט",
        cta_projects="כל הפרויקטים", cta_how="איך מתחילים פרויקט", cta_contact="השאירו פרטים", cta_steps="כל השלבים", cta_home="לדף הבית",
        hero_eyebrow="מקבוצת וינברג",
        hero_h1="בונים את העיר מחדש. כבר ארבעה דורות.",
        hero_lead="חברה משפחתית בבעלות פרטית, המתמחה בתמ״א 38, פינוי־בינוי ושימור במרכזי הערים של גוש דן.",
        hero_caption="מזא״ה 71, תל אביב-יפו. בניין לשימור בשלבי תכנון.",
        stick_title="מעוניינים שנחזור אליכם?", stick_name="שם מלא", stick_phone="טלפון", stick_send="השאירו פרטים", stick_close="סגירה",
        projects_h2="פרויקטים המשתבחים עם השנים",
        projects_lead="בניינים במרכזי הערים של גוש דן: הריסה ובנייה מחדש, שימור והשבחה ופרויקטים חדשים, מסודרים לפי שלב.",
        groups={"marketing": ("בשיווק", "היתרים, בנייה ושיווק פעיל"), "planning": ("פרויקטים לפני החלטת וועדה מחירי הנחה והטבות", "בשלבי תכנון"), "done": ("בביצוע ואכלוס", "בנייה, מסירה ואכלוס")},
        more_projects="עוד {n} פרויקטים בתכנון", projects_h1="הפרויקטים שלנו", m_scroll_hint="ניתן לגלול את הטבלה לצדדים",
        f_building="כתובת הבניין (לדיירים)", f_sent="תודה, פנייתכם התקבלה. נציג יחזור אליכם בהקדם.",
        about_h2="חברה משפחתית. ארבעה דורות של בנייה.",
        about_p="כרם יזמות נדל״ן והתחדשות עירונית היא חברה של מומחים, עם ניסיון של ארבעה דורות ביזמות נדל״ן, תכנון ובנייה של אלפי יחידות דיור ומסחר. ההתמחות בשנים האחרונות היא בפרויקטי מגורים במרכז העיר: תמ״א 38 ופינוי־בינוי. החברה בבעלות פרטית מלאה של המשפחה. מנכ״ל החברה: רני וינברג.",
        about_link="על החברה ועל קבוצת וינברג",
        about_caption="הושע 21+23, בני ברק. הריסה ובנייה מחדש, בביצוע.",
        spec_h2="תחומי ההתמחות",
        statement_eyebrow="איך מתחילים פרויקט?",
        statement_h2="הצעד הראשון הוא היכרות. בלי חתימות, בלי התחייבות.",
        statement_p1="כבעלי דירה בבניין, לא פשוט להזיז קדימה דבר כזה: קשה לאסוף את כל הדיירים, קשה להבין מה נכון מול הרבה יזמים שמבטיחים הבטחות, וקשה להתנהל מול יזם ועורך דין בלי להכיר את המושגים.",
        statement_p2="לכן יש לנו שיטה סדורה ופשוטה, צעד אחר צעד, לכל סוג פרויקט. מטרת הצעד הראשון היא היכרות בלבד: להבין יחד, היזם והדיירים, האם יש בנכס כדאיות.",
        contact_h2="מעוניינים שנחזור אליכם?",
        contact_lead="רכישת דירה, בניין שמתאים להתחדשות עירונית, או התייעצות בכל עניין בנדל״ן. השאירו פרטים ונציג יחזור אליכם בהקדם.",
        phone="טלפון", email="אימייל", office="משרד", address="דרך בגין 82, בית אופקים, קומה 5, תל אביב 67138", maps="פתיחה במפות", facebook="פייסבוק",
        f_name="שם מלא", f_phone="טלפון", f_email="אימייל", f_topic="בנוגע ל", f_topic_pick="בחרו נושא",
        f_topics=["אני בעל/ת דירה בבניין קיים", "רכישת דירה", "התחדשות עירונית / פינוי־בינוי", "תמ״א 38", "יזמות", "אחר"],
        f_project="פרויקט (אם רלוונטי)", f_project_none="ללא פרויקט מסוים", f_msg="הודעה",
        f_consent="אני מאשר/ת יצירת קשר בהתאם ל", f_privacy="מדיניות הפרטיות", f_send="שליחה", f_or="או התקשרו:",
        f_subject="פנייה חדשה מאתר כרם", f_hp="אין למלא שדה זה",
        foot_p="חברה משפחתית בבעלות פרטית, מקבוצת וינברג. ארבעה דורות של יזמות נדל״ן, תכנון ובנייה של אלפי יחידות דיור ומסחר.",
        foot_nav="ניווט", foot_contact="פרטי התקשרות", accessibility="הצהרת נגישות", privacy="מדיניות פרטיות",
        foot_rights="כל הזכויות שמורות.", foot_note="התמונות וההדמיות להמחשה בלבד",
        crumb_home="ראשי", crumbs_label="פירורי לחם",
        p_type="סוג הפרויקט", p_city="עיר", p_floors="קומות", p_units="יחידות דיור", p_shops="מסחר", p_shops_unit="חנויות", p_status="סטטוס",
        p_about="על הפרויקט", p_render="הדמיה להמחשה בלבד", p_more="פרויקטים נוספים", p_or_call="או התקשרו:",
        p_ext_note="לפרויקט זה קיים אתר ייעודי נפרד:", p_ext_todo="בהמתנה להחלטה",
        m_apts="הדירות", m_apts_note="3 דירות בקומה, 2 כיווני אוויר ומרפסת שמש לכל דירה.",
        m_notes="הערות", m_plan="תכנית", m_spec_note="ט.ל.ח. לכל הסעיפים אפשרות לשווה ערך.", m_team="הצוות",
        m_pdf="PDF", m_pdf_label="הורדת תכנית הדירה",
        m_tours="סיור וירטואלי", m_tours_note="הסיור נטען רק בלחיצה, כדי לא להכביד על הדף.",
        m_pano="סיור פנורמי בדירה", m_pano_btn="פתיחת הסיור הפנורמי", m_pano_p="סיור 360° בדירה לדוגמה. גררו כדי להסתובב בחלל.",
        m_3d="מודל תלת-ממדי", m_3d_btn="פתיחת המודל התלת-ממדי", m_3d_p="הדירה במודל תלת-ממדי אינטראקטיבי. ניתן להסתובב, להתקרב ולעבור בין החללים.",
        m_ext_open="פתיחה בחלון מלא",
        m_notice="הפרטים בדף זה הינם להמחשה ולמסירת מידע בלבד, ואינם מהווים התחייבות מצד החברה. את החברה יחייבו הסכם המכר והמפרט הטכני לפי חוק המכר עליו יחתמו החברה והרוכשים. תכניות המכירה כוללות פרטי ריהוט ומוצרי חשמל להמחשה בלבד, שאינם כלולים בממכר. ט.ל.ח.",
        m_gallery="הדמיות פנים", m_gallery_note="להמחשה בלבד", m_spec="מפרט טכני",
        m_spec_items=[
            "דלת ביטחון מעוצבת בכניסה לדירה, מערכת אינטרקום עם צפייה במעגל סגור במסך צבעוני. דלתות פנים יוניק פרימיום בגובה 2.1 מ׳.",
            "מערכת מיזוג אוויר VRF.",
            "חשמל חכם, אביזרי קצה גוויס או ביטיצ׳ינו.",
            "מטבח מעוצב, גודלו על פי התכנון האדריכלי ותכניות הדירה.",
            "חדרי אמבטיה: חיפוי עד התקרה, ברזים, אסלות, אמבטיות ומקלחונים וניאגרה סמויה. חמת, גרוהה, אידיאל סטנדרט או גיבריט.",
            "חלונות וויטרינות קליל או אקסטל, תריסים חשמליים עם מנועי סומפי, זיגוג כפול אקוסטי מבודד, רשתות נגד יתושים בכל הפתחים (למעט ממ״ד, על פי תקן).",
        ],
        m_architect="האדריכל", m_architect_name="מאור לוי, לוי לוסטיג אדריכלים",
        m_architect_p="המשרד עוסק בתכנון ועיצוב בתים ודירות מגורים ובפרויקטי תמ״א 38. מאור לוי הוא אדריכל, בעל תואר שני במנהל עסקים ומוסמך מכון התקנים כמלווה בנייה ירוקה, עם ניסיון רב שנים בבנייה אורבנית ופרטית.",
        m_lawyer="עורך דין היזם", m_lawyer_name="משרד עו״ד ד״ר משה וינברג",
        m_lawyer_p="משרד מוביל בתחום האזרחי: תכנון ובנייה, הפשרת קרקעות, פיתוח והפקעת מקרקעין ומשפט אזרחי. המשרד קידם ויזם פיתוח של אלפי יחידות דיור ברחבי הארץ ומקיים קשר שוטף עם רשויות התכנון.",
        about_title="אודות החברה",
        about_desc="כרם יזמות נדל״ן והתחדשות עירונית: חברה משפחתית מקבוצת וינברג, עם ניסיון של ארבעה דורות ביזמות, תכנון ובנייה של אלפי יחידות דיור ומסחר.",
        about_h1="ניסיון של ארבעה דורות ביזמות נדל״ן",
        about_lead="כרם יזמות נדל״ן והתחדשות עירונית היא חברה מובילה של מומחים, עם ניסיון עשיר של ארבעה דורות ביזמות נדל״ן, תכנון ובנייה של אלפי יחידות דיור ומסחר.",
        about_body=[
            "ההתמחות בשנים האחרונות היא בפרויקטי מגורים במרכז העיר: תמ״א 38 ופינוי־בינוי, לצד שימור והשבחה של בניינים היסטוריים בלב תל אביב.",
            "החברה משפחתית ובבעלות פרטית מלאה של המשפחה. בנוסף מחזיקה המשפחה חברות נוספות המתמחות במוצרים משלימים בתחום הנדל״ן: שירותים משפטיים, תחזוקת נכסים, פיננסים ומלאי דירות להשכרה. כך, כל שלב בפרויקט נשען על ידע וניסיון מתוך הבית.",
            "מנכ״ל החברה: רני וינברג.",
        ],
        about_caption2="רוטשילד 135, הבית על הבימה, תל אביב. הסתיים ואוכלס.",
        about_mgmt_h2="חברה משפחתית, מנוהלת מקרוב",
        about_mgmt_lead="כל פרויקט מלווה אישית, מהפגישה הראשונה עם הדיירים ועד מסירת המפתחות.",
        about_mgmt_p="הקבוצה פועלת בתל אביב, רמת גן ובני ברק, ומשלבת יזמות, תכנון, מימון, ייצוג משפטי וניהול נכסים תחת קורת גג אחת.",
        about_caption3="פינסקר 53+55, תל אביב. תמ״א 38/2, הריסה ובנייה, בשלבי תכנון.",
        group_h2="חברות נוספות בבעלות המשפחה",
        how_title="איך מתחילים פרויקט?",
        how_desc="הצעד הראשון בפרויקט תמ״א 38 או פינוי־בינוי: שיטה סדורה ופשוטה, צעד אחר צעד, בלי חתימות ובלי התחייבות. כך מתחילים עם כרם.",
        how_h1="כבעלי דירה בבניין, לא פשוט להזיז קדימה דבר כזה",
        how_lead="״איך מתחילים?״ זה הצעד הראשון, וגם הקשה ביותר. לכן יש לנו שיטה סדורה ופשוטה, צעד אחר צעד, לכל סוג פרויקט.",
        how_body=[
            "קשה לאסוף את כל הדיירים ולהגיע להחלטות. קשה להבין מה נכון מול הרבה יזמים, שכל אחד מהם מבטיח הבטחות. וקשה להתנהל מול יזם ומול עורך דין בלי להכיר את המושגים.",
            "<strong>אבל זה שווה הכול.</strong> בסוף התהליך אתם יושבים בסלון החדש, אוכלים ארוחת ערב משפחתית במרפסת החדשה, ואז החיוך שווה הכול.",
            "ההתחלה של תהליך לפרויקט תמ״א 38, פינוי־בינוי, כל פרויקט התחדשות עירונית או תכנון וביצוע מסוג אחר בנכס שלכם, היא להבין בדיוק מה רוצים.",
        ],
        how_caption="חירות 40, רמת גן. שכונת הגפן, בשלבי תכנון.",
        how_step_h2="מסע ארוך מתחיל בצעד קטן",
        how_step_p="״הצעד הראשון״ של התהליך הוא פשוט ופועל בשיטה מסודרת מאוד. מטרתו היא היכרות בלבד:",
        how_after="רק כשכל הדיירים יסכימו באופן כללי (ולא מחייב בשום אופן) על אופי ההצעה, נמשיך לשלב הבא.",
        how_small="ההחלטות עצמן, לגבי כל דבר, מתקבלות רק באסיפת דיירים עם נוכחות מלאה של כל הדיירים וזכות הצבעה לדיירים בלבד. בשלב זה לא מדובר בהחלטות, אלא רק באיסוף מידע להבנת הצרכים של הפרויקט.",
        how_side=[("התחייבות", "לא נדרשת"), ("חתימות", "לא נדרשות"), ("מטרת השלב", "היכרות ובחינת כדאיות")],
        how_important="<strong>חשוב לדעת:</strong> אנחנו רק בשלב ההיכרות, לבחון האם יש כדאיות. מהצד של הדיירים: האם כדאי כל הבלגן הזה? מהצד של היזם: האם יש רווחיות?",
        contact_title="צור קשר",
        contact_desc="נשמח לייעץ, ליזום, לתכנן, לפקח ולהוביל אתכם לפרויקט מוצלח של תמ״א 38, התחדשות עירונית ופינוי־בינוי. טלפון 03-6121314, office@keremltd.co.il.",
        contact_h1="״איך מתחילים? ומה האסטרטגיה?״",
        contact_page_lead="נשמח לייעץ, ליזום, לתכנן, לפקח ולהוביל אתכם לפרויקט מוצלח של תמ״א 38, התחדשות עירונית ופינוי־בינוי, וגם להתייעצות בכל עניין בנדל״ן.",
        contact_address_label="כתובתנו",
        a11y_title="הצהרת נגישות", a11y_desc="הצהרת הנגישות של אתר כרם יזמות והתחדשות עירונית.",
        privacy_title="מדיניות פרטיות", privacy_desc="מדיניות הפרטיות של אתר כרם יזמות והתחדשות עירונית.",
        nf_title="הדף לא נמצא", nf_desc="הדף המבוקש לא נמצא.", nf_lead="ייתכן שהכתובת השתנתה או שהדף הוסר.",
        og_default="hero-1200",
    ),
    "en": dict(
        dir="ltr", locale="en_US",
        brand="Kerem Real Estate Development and Urban Renewal",
        brand_short="Kerem",
        site_title="Kerem Real Estate Development and Urban Renewal | Four generations of building in Tel Aviv",
        site_desc="Kerem, part of the Weinberg group: a family-owned developer with four generations of experience in TAMA 38, urban renewal and heritage preservation in Tel Aviv, Ramat Gan and Bnei Brak.",
        skip="Skip to content", home="Home", about="About", projects="Projects", how="How a project starts", contact="Contact",
        lang_switch="עב", lang_switch_full="עברית", menu_open="Open menu",
        cta_projects="All projects", cta_how="How a project starts", cta_contact="Leave your details", cta_steps="All the steps", cta_home="Back to home",
        hero_eyebrow="Part of the Weinberg group",
        hero_h1="Rebuilding the city. For four generations.",
        hero_lead="A privately held family company specialising in TAMA 38, urban renewal and heritage preservation in the city centres of greater Tel Aviv.",
        hero_caption="Mazeh 71, Tel Aviv-Jaffa. Heritage building in planning.",
        stick_title="Would you like us to call you?", stick_name="Full name", stick_phone="Phone", stick_send="Leave your details", stick_close="Close",
        projects_h2="Projects that improve with the years",
        projects_lead="Buildings in the city centres of greater Tel Aviv: demolition and rebuilding, preservation and upgrading, and new construction, ordered by stage.",
        groups={"marketing": ("In marketing", "Permits, construction and active sales"), "planning": ("Projects before committee approval, discounted prices and benefits", "In planning"), "done": ("Under construction and occupied", "Construction, delivery and occupancy")},
        more_projects="{n} more projects in planning", projects_h1="Our projects", m_scroll_hint="Scroll the table sideways",
        f_building="Building address (for residents)", f_sent="Thank you, your enquiry has been received. We will get back to you shortly.",
        about_h2="A family company. Four generations of building.",
        about_p="Kerem is a team of specialists with four generations of experience in real estate development, planning and construction of thousands of residential and commercial units. In recent years the focus has been residential projects in the city centre: TAMA 38 and urban renewal. The company is fully family owned. CEO: Rani Weinberg.",
        about_link="About the company and the Weinberg group",
        about_caption="Hoshea 21+23, Bnei Brak. Demolition and rebuilding, under construction.",
        spec_h2="What we do",
        statement_eyebrow="How a project starts",
        statement_h2="The first step is getting acquainted. No signatures, no commitment.",
        statement_p1="For apartment owners, moving something like this forward is not simple: gathering all the residents is hard, judging between many developers making promises is hard, and dealing with a developer and a lawyer without knowing the terms is hard.",
        statement_p2="So we work with a clear, simple method, step by step, for every kind of project. The first step is only about getting acquainted: understanding together, developer and residents, whether the building is a viable project.",
        contact_h2="Would you like us to call you?",
        contact_lead="Buying an apartment, a building suited to urban renewal, or advice on any real estate matter. Leave your details and a representative will get back to you shortly.",
        phone="Phone", email="Email", office="Office", address="82 Begin Road, Beit Ofakim, 5th floor, Tel Aviv 67138", maps="Open in maps", facebook="Facebook",
        f_name="Full name", f_phone="Phone", f_email="Email", f_topic="Regarding", f_topic_pick="Choose a topic",
        f_topics=["I own an apartment in an existing building", "Buying an apartment", "Urban renewal", "TAMA 38", "Development", "Other"],
        f_project="Project (if relevant)", f_project_none="No specific project", f_msg="Message",
        f_consent="I agree to be contacted in accordance with the ", f_privacy="privacy policy", f_send="Send", f_or="or call:",
        f_subject="New enquiry from keremltd.co.il (EN)", f_hp="Leave this field empty",
        foot_p="A privately held family company, part of the Weinberg group. Four generations of real estate development, planning and construction of thousands of residential and commercial units.",
        foot_nav="Navigation", foot_contact="Contact", accessibility="Accessibility statement", privacy="Privacy policy",
        foot_rights="All rights reserved.", foot_note="Images and renderings are for illustration only",
        crumb_home="Home", crumbs_label="Breadcrumbs",
        p_type="Project type", p_city="City", p_floors="Floors", p_units="Apartments", p_shops="Retail", p_shops_unit="shops", p_status="Status",
        p_about="About the project", p_render="Rendering for illustration only", p_more="More projects", p_or_call="or call:",
        p_ext_note="This project has a separate dedicated website:", p_ext_todo="pending decision",
        m_apts="The apartments", m_apts_note="Three apartments per floor, two exposures and a sun balcony for every apartment.",
        m_notes="Notes", m_plan="Plan", m_spec_note="E&OE. Equivalent alternatives may be supplied for all items.", m_team="The team",
        m_pdf="PDF", m_pdf_label="Download the apartment plan",
        m_tours="Virtual tour", m_tours_note="The tour loads only when you open it, so the page stays fast.",
        m_pano="360° apartment tour", m_pano_btn="Open the panoramic tour", m_pano_p="A 360° walk through a sample apartment. Drag to look around.",
        m_3d="3D model", m_3d_btn="Open the 3D model", m_3d_p="The apartment as an interactive 3D model. Rotate, zoom and move between rooms.",
        m_ext_open="Open full screen",
        m_notice="The details on this page are for illustration and information only and do not constitute a commitment by the company. The company is bound only by the sale agreement and the technical specification under the Sale Law, as signed by the company and the buyers. Sales plans include furniture and appliances for illustration only, which are not included in the sale. E&OE.",
        m_gallery="Interior renderings", m_gallery_note="For illustration only", m_spec="Technical specification",
        m_spec_items=[
            "Designed security entrance door, intercom with colour closed-circuit video. Unik Premium interior doors, 2.1 m high.",
            "VRF air conditioning system.",
            "Smart electrical system, Gewiss or Bticino fittings.",
            "Designed kitchen, sized according to the architectural plan of each apartment.",
            "Bathrooms: tiling to the ceiling, taps, toilets, baths, shower enclosures and concealed cisterns. Hamat, Grohe, Ideal Standard or Geberit.",
            "Klil or Extal windows and glazing, electric shutters with Somfy motors, acoustic double glazing, insect screens on all openings (except the safe room, per standard).",
        ],
        m_architect="Architect", m_architect_name="Maor Levy, Levy Lustig Architects",
        m_architect_p="The practice designs houses, residential apartments and TAMA 38 projects. Maor Levy is an architect with an MBA, certified by the Standards Institution of Israel as a green building consultant, with many years of experience in urban and private construction.",
        m_lawyer="Developer's counsel", m_lawyer_name="Dr. Moshe Weinberg Law Offices",
        m_lawyer_p="A leading civil law firm: planning and construction, land rezoning, real estate development and expropriation, and general civil law. The firm has initiated and advanced the development of thousands of housing units across Israel and works continuously with the planning authorities.",
        about_title="About",
        about_desc="Kerem Real Estate Development and Urban Renewal: a family company in the Weinberg group, with four generations of experience in developing, planning and building thousands of residential and commercial units.",
        about_h1="Four generations of experience in real estate development",
        about_lead="Kerem is a leading team of specialists with four generations of experience in real estate development, planning and construction of thousands of residential and commercial units.",
        about_body=[
            "In recent years the focus has been residential projects in the city centre: TAMA 38 and urban renewal, alongside the preservation and upgrading of historic buildings in the heart of Tel Aviv.",
            "The company is family run and fully family owned. The family also holds complementary real estate businesses: legal services, property management, finance and a portfolio of rental apartments. Every stage of a project draws on in-house knowledge and experience.",
            "CEO: Rani Weinberg.",
        ],
        about_caption2="Rothschild 135, the House on Habima, Tel Aviv. Completed and occupied.",
        about_mgmt_h2="A family company, closely managed",
        about_mgmt_lead="Every project is personally accompanied, from the first meeting with residents to handing over the keys.",
        about_mgmt_p="The group works in Tel Aviv, Ramat Gan and Bnei Brak, combining development, planning, finance, legal representation and property management under one roof.",
        about_caption3="Pinsker 53+55, Tel Aviv. TAMA 38/2, demolition and rebuilding, in planning.",
        group_h2="Other family-owned companies",
        how_title="How a project starts",
        how_desc="The first step in a TAMA 38 or urban renewal project: a clear, simple method, step by step, with no signatures and no commitment. This is how it starts with Kerem.",
        how_h1="For apartment owners, moving something like this forward is not simple",
        how_lead="“How do we start?” is the first step, and the hardest one. So we work with a clear, simple method, step by step, for every kind of project.",
        how_body=[
            "Gathering all the residents and reaching decisions is hard. Judging what is right between many developers, each making promises, is hard. And dealing with a developer and a lawyer without knowing the terms is hard.",
            "<strong>But it is worth everything.</strong> At the end of the process you are sitting in your new living room, having a family dinner on the new balcony, and the smile is worth it all.",
            "The beginning of any TAMA 38, urban renewal or other planning and construction project in your building is understanding exactly what you want.",
        ],
        how_caption="Herut 40, Ramat Gan. Hagefen neighbourhood, in planning.",
        how_step_h2="A long journey begins with a small step",
        how_step_p="The first step is simple and follows a very orderly method. Its purpose is only to get acquainted:",
        how_after="Only when all the residents agree in general (and in no way bindingly) on the nature of the proposal do we move to the next stage.",
        how_small="Decisions themselves, on any matter, are taken only at a residents' meeting with full attendance, where only residents vote. At this stage there are no decisions, only information gathering to understand the needs of the project.",
        how_side=[("Commitment", "Not required"), ("Signatures", "Not required"), ("Purpose", "Getting acquainted, testing viability")],
        how_important="<strong>Good to know:</strong> we are only at the acquaintance stage, testing whether the project is viable. For the residents: is all the upheaval worth it? For the developer: is it profitable?",
        contact_title="Contact",
        contact_desc="We would be glad to advise, initiate, plan, supervise and lead you to a successful TAMA 38 or urban renewal project. Phone 03-6121314, office@keremltd.co.il.",
        contact_h1="“How do we start? What is the strategy?”",
        contact_page_lead="We would be glad to advise, initiate, plan, supervise and lead you to a successful TAMA 38 or urban renewal project, and to consult on any real estate matter.",
        contact_address_label="Address",
        a11y_title="Accessibility statement", a11y_desc="Accessibility statement for the Kerem website.",
        privacy_title="Privacy policy", privacy_desc="Privacy policy for the Kerem website.",
        nf_title="Page not found", nf_desc="The requested page was not found.", nf_lead="The address may have changed or the page may have been removed.",
        og_default="hero-1200",
    ),
}

# --------------------------------------------------------------------------
# Content
# --------------------------------------------------------------------------

def L(he, en):
    return {"he": he, "en": en}


PROJECTS = [
    # --- in marketing ---
    dict(slug="louis-marshall-11", img="marshall",
         name=L("לואי מרשל 11", "Louis Marshall 11"), city=L("תל אביב", "Tel Aviv"), area=L("הצפון הישן", "Old North"),
         status=L("התקבל היתר", "Permit granted"), group="marketing", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors="8", units="20", shops=None,
         short=L("בניין בוטיק בן 8 קומות בצפון הישן, בין כיכר המדינה לפארק הירקון.",
                 "An eight-storey boutique building in the Old North, between Kikar Hamedina and Hayarkon Park."),
         desc=L([
             "פרויקט מגורים ייחודי בלב תל אביב, ברחוב לואי מרשל השקט, בצפון הישן האיכותי והיוקרתי, בקרבת פארק הירקון, כיכר המדינה ואבן גבירול, ובמרחק הליכה מהים.",
             "הפרויקט מעניק חוויית מגורים בבניין בוטיק בן 8 קומות בעיצוב אדריכלי מודרני ומוקפד ובסטנדרט גבוה, הכולל 20 יחידות דיור בעלות מפרט טכני עשיר.",
             "הדירות כולן מתוכננות בקפידה תוך ניצול מקסימלי של החלל. לכל דירה מרפסת שמש מרווחת, 3 דירות בלבד בקומה ו־2 כיווני אוויר לכל דירה. בקומת הקרקע 2 דירות גן ובקומת הגג 2 דירות פנטהאוז.",
         ], [
             "A distinctive residential project in the heart of Tel Aviv, on quiet Louis Marshall Street in the prestigious Old North, near Hayarkon Park, Kikar Hamedina and Ibn Gabirol, and within walking distance of the sea.",
             "A boutique building of eight storeys in a modern, carefully detailed architectural design and a high standard, with 20 apartments and a rich technical specification.",
             "Every apartment is planned to make the most of its space. Each has a generous sun balcony, only three apartments per floor and two exposures. Two garden apartments on the ground floor and two penthouses on the roof.",
         ])),
    dict(slug="grofit-3", img="grofit",
         name=L("מבוא גרופית 3", "Mevo Grofit 3"), city=L("תל אביב", "Tel Aviv"), area=L("צהלה", "Tzahala"),
         status=L("הבנייה החלה", "Under construction"), group="marketing", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors="4", units="8", shops=None,
         short=L("חוויית מגורים מושלמת, איכות חיים גבוהה, במיקום נדיר ובאווירה תל אביבית מקורית.",
                 "A complete living experience in a rare location, with an authentic Tel Aviv atmosphere."),
         desc=L([
             "הבית במבוא גרופית 3 מעניק לדייריו חוויית מגורים מושלמת, איכות חיים גבוהה, במיקום נדיר ובאווירה תל אביבית מקורית. הדירות תוכננו בקפידה עם דגש על עיצוב לנוחות, שלווה ואירוח, וגימור אלגנטי וקלאסי המבוסס על חומרים מהסטנדרט הגבוה ביותר.",
             "צהלה, בצפון תל אביב, היא מהשכונות הוותיקות והמבוקשות בעיר: בתים פרטיים ודו־קומתיים, קהילה חמה, בית ספר, גני ילדים ומרכז מסחרי שכונתי במרחק הליכה, גינות רבות ופינות טבע, והכול על מדרכות רחבות ומוצלות ברקע נוף ירוק.",
             "התכנון על ידי משרד אדריכלים מוביל המתמחה במבנים באזור זה של צהלה, בדגש על שטחים מרווחים ומודרניים. הבניין נבנה על פי תקן בנייה ירוקה ותקני החיזוק מפני רעידות אדמה, עם לובי מרווח, מעלית שקטה וגינה מעוצבת על ידי יועץ נוף.",
         ], [
             "Mevo Grofit 3 offers its residents a complete living experience in a rare location with an authentic Tel Aviv atmosphere. The apartments are planned with an emphasis on comfort, calm and hosting, with an elegant, classic finish in materials of the highest standard.",
             "Tzahala, in north Tel Aviv, is one of the city's oldest and most sought-after neighbourhoods: private and two-storey homes, a warm community, a school, kindergartens and a neighbourhood shopping centre within walking distance, and many gardens and green corners along wide, shaded pavements.",
             "Designed by a leading architectural practice specialising in this part of Tzahala, with spacious, modern layouts. The building is built to green building and earthquake reinforcement standards, with a generous lobby, a quiet lift and a garden designed by a landscape consultant.",
         ]),
         ),
    dict(slug="bernstein-11", img="bernstein",
         name=L("אדוארד ברנשטיין 11", "Eduard Bernstein 11"), city=L("תל אביב", "Tel Aviv"), area=L("המרכז ההיסטורי", "Historic centre"),
         status=L("אושר בוועדה המקומית", "Approved by local committee"), group="marketing", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors="6", units="14", shops=None, redirect="https://eduard11.co.il/",
         short=L("בניין חדש בן 6 קומות ו־14 דירות ברחוב שקט במרכז ההיסטורי של תל אביב, דקות מהים.",
                 "A new six-storey building with 14 apartments on a quiet street in the historic centre of Tel Aviv, minutes from the sea."),
         desc=L([
             "הפרויקט כולל הריסת מבנה קיים ובנייה של בניין חדש בן 6 קומות הכולל קומת קרקע ו־14 יחידות דיור, מתוכן 7 דירות למכירה. שתיים או שלוש דירות בקומה, שניים או שלושה כיווני אוויר, מרפסת שמש, גינה רחבה, חניה רובוטית ובנייה ירוקה על פי התקנים.",
             "חוויית מגורים תל אביבית נדירה ואותנטית, ברחוב שקט ופסטורלי במרכז ההיסטורי של העיר: במרחק הליכה של דקות מהים, מהטיילת, מבריכת גורדון ומהמרינה, ובסביבה נגישה לבתי ספר, גני ילדים וגינות ציבוריות.",
             "תכנון: קצור־רונן אדריכלים, משרד תל אביבי המתמחה בתכנון מבני מגורים בצפיפות גבוהה ובשימור מבנים היסטוריים.",
         ], [
             "The project replaces an existing structure with a new six-storey building of 14 apartments, seven of them for sale. Two or three apartments per floor, two or three exposures, sun balconies, a wide garden, robotic parking and green construction to standard.",
             "A rare, authentic Tel Aviv living experience on a quiet, pastoral street in the historic centre of the city: a few minutes' walk from the sea, the promenade, the Gordon pool and the marina, with schools, kindergartens and public gardens nearby.",
             "Design: Katzor-Ronen Architects, a Tel Aviv practice specialising in high-density residential buildings and the preservation of historic structures.",
         ])),
    dict(slug="arlozorov-53", img="arlozorov",
         name=L("ארלוזורוב 53", "Arlozorov 53"), city=L("רמת גן", "Ramat Gan"), area=L("שכונת חשמונאים", "Hashmonaim neighbourhood"),
         status=L("בשיווק", "In marketing"), group="marketing", type=L("בניין מגורים חדש", "New residential building"),
         floors="10", units="31", shops=None,
         short=L("בניין מגורים חדש בן 10 קומות בשכונה ותיקה ומשפחתית, במרחק הליכה מהרכבת הקלה.",
                 "A new ten-storey residential building in an established family neighbourhood, a short walk from the light rail."),
         desc=L([
             "הזדמנות מגורים חדשה בלב הפועם של רמת גן, במרחק הליכה מתחנת הרכבת הקלה בצומת עלית. הבית בארלוזורוב 53 מעניק לדייריו חוויית מגורים מושלמת, איכות חיים גבוהה, עיצוב לנוחות ושלווה, באווירה שכונתית מקורית.",
             "השכונה ותיקה ומשפחתית, ממש על גבול תל אביב: סמוך למוקדי הבילוי והתרבות של רמת גן, למרכזי העסקים ולמוסדות החינוך המובילים, במרחק הליכה מרחוב ביאליק וממתחם הבורסה המתחדש, ועם יציאה מהירה לנתיבי איילון, ז׳בוטינסקי ואבא הלל.",
             "הבניין החדש בן 10 קומות ו־4 קומות מרתף, עם 2 מעליות שקטות, לובי מרווח בעיצוב אדריכלי וגינה מעוצבת על ידי אדריכל נוף. הבנייה על פי תקן בנייה ירוקה ותקני החיזוק מפני רעידות אדמה.",
         ], [
             "A new home in the beating heart of Ramat Gan, a short walk from the Elite Junction light rail station. Arlozorov 53 offers its residents a complete living experience, designed for comfort and calm, in an authentic neighbourhood atmosphere.",
             "An established family neighbourhood right on the Tel Aviv border: close to Ramat Gan's leisure and cultural centres, business districts and leading schools, a walk from Bialik Street and the renewed Bursa district, with quick access to the Ayalon, Jabotinsky and Abba Hillel roads.",
             "The new building has ten storeys and four basement levels, two quiet lifts, a generous architect-designed lobby and a garden designed by a landscape architect. Built to green building and earthquake reinforcement standards.",
         ]),
         ),
    # --- in planning ---
    dict(slug="pinsker-53-55", img="pinsker",
         name=L("פינסקר 53+55", "Pinsker 53+55"), city=L("תל אביב", "Tel Aviv"), area=L("לב העיר", "City centre"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors=L("7 + גג", "7 + roof"), units="37", shops="3",
         short=L("7 קומות, 37 דירות ו־5 מיני פנטהאוזים עם בריכה פרטית, במרחק הליכה מכיכר דיזנגוף.",
                 "Seven storeys, 37 apartments and five mini penthouses with private pools, a short walk from Dizengoff Square."),
         desc=L([
             "הפרויקט ממוקם ברובע 3 במרכז תל אביב, בסביבה עירונית נעימה, במרחק הליכה מכיכר דיזנגוף, דיזנגוף סנטר ורחוב בוגרשוב השוקק, וכמה דקות הליכה מהים, מבתי הקפה והמסעדות. נגישות נוחה לכל שירותי היום־יום: בהליכה, באופניים, בתחבורה ציבורית וברכב.",
             "אנחנו מקדמים מבנה חדש בגובה 7 קומות + גג, הכולל 37 דירות, מתוכן 5 מיני פנטהאוזים עם בריכה פרטית על הגג לכל יחידה, ושלוש חנויות בקומת הקרקע.",
         ], [
             "The project sits in District 3 in central Tel Aviv, in a pleasant urban setting within walking distance of Dizengoff Square, Dizengoff Center and bustling Bograshov Street, and a few minutes from the sea, cafes and restaurants. Everyday services are easily reached on foot, by bicycle, public transport or car.",
             "We are advancing a new building of seven storeys plus roof, with 37 apartments, five of them mini penthouses with a private rooftop pool each, and three shops on the ground floor.",
         ])),
    dict(slug="cordovero-22", img="cordovero",
         name=L("קורדובירו 22", "Cordovero 22"), city=L("תל אביב", "Tel Aviv"), area=L("פלורנטין", "Florentin"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors=L("4 + גג", "4 + roof"), units="18", shops="2",
         short=L("4 קומות ו־18 דירות במדרחוב בלב פלורנטין, כולל פנטהאוז עם בריכה על הגג.",
                 "Four storeys and 18 apartments on a pedestrian street in the heart of Florentin, including a penthouse with a rooftop pool."),
         desc=L([
             "בלב שכונת פלורנטין התוססת, במדרחוב, במרחק הליכה מבתי קפה, מסעדות, גלריות וחיי רחוב מלאי אופי. השילוב המושלם בין קצב עירוני לאיכות חיים.",
             "אנחנו מקדמים מבנה חדש בגובה 4 קומות + גג, הכולל 18 דירות, מתוכן פנטהאוז עם בריכה על הגג, ושתי חנויות בקומת הקרקע.",
         ], [
             "In the heart of lively Florentin, on a pedestrian street, within walking distance of cafes, restaurants, galleries and street life full of character. The perfect balance of urban pace and quality of life.",
             "We are advancing a new building of four storeys plus roof, with 18 apartments, including a penthouse with a rooftop pool, and two shops on the ground floor.",
         ])),
    dict(slug="weisburg-4", img="weisburg4",
         name=L("ויסבורג 4", "Weisburg 4"), city=L("תל אביב", "Tel Aviv"), area=L("צהלה", "Tzahala"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors="5", units="14", shops=None,
         short=L("בניין בן 5 קומות ו־14 יחידות דיור בלב צהלה.", "A five-storey building with 14 apartments in the heart of Tzahala."),
         desc=L(["בלב הפועם של צהלה יוקם בניין בן 5 קומות, הכולל 14 יחידות דיור."],
                ["In the heart of Tzahala, a five-storey building with 14 apartments will be built."])),
    dict(slug="weisburg-6", img="weisburg6",
         name=L("ויסבורג 6", "Weisburg 6"), city=L("תל אביב", "Tel Aviv"), area=L("צהלה", "Tzahala"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors="5", units="9", shops=None,
         short=L("בניין בן 5 קומות ו־9 יחידות דיור ברחוב שקט בצהלה.", "A five-storey building with nine apartments on a quiet street in Tzahala."),
         desc=L(["בלב צהלה, ברחוב שקט, יוקם בניין בן חמש קומות הכולל 9 יחידות דיור."],
                ["In the heart of Tzahala, on a quiet street, a five-storey building with nine apartments will be built."])),
    dict(slug="nahmani-64", img="nahmani",
         name=L("נחמני 64", "Nahmani 64"), city=L("תל אביב", "Tel Aviv"), area=L("לב העיר, פינת בגין 27", "City centre, corner of Begin 27"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("שימור והשבחה", "Preservation and upgrading"),
         floors="3", units=L("מ־13 ל־32", "13 to 32"), shops=L("מ־10 ל־9", "10 to 9"),
         short=L("בניין לשימור בלב מרכז העסקים של תל אביב: מ־13 דירות ו־10 חנויות ל־32 דירות ו־9 חנויות.",
                 "A heritage building in the heart of Tel Aviv's business district: from 13 apartments and 10 shops to 32 apartments and 9 shops."),
         desc=L([
             "בניין מגורים בן 3 קומות, הכולל 13 דירות מעל קומת מסחר ובה 10 חנויות (חלקן מחוברות) וקומת מרתף חלקית. הבניין מוגדר לשימור עם הגבלות מחמירות במסגרת תכנית השימור של תל אביב, בלב מרכז העסקים הראשי של העיר.",
             "בשלב הנוכחי אנו מקדמים תכנית להשביח את הבניין הקיים מ־13 דירות ו־10 חנויות ל־32 דירות ו־9 חנויות.",
         ], [
             "A three-storey residential building with 13 apartments above a commercial floor of 10 shops (some combined) and a partial basement. The building is listed for preservation with strict restrictions under Tel Aviv's preservation plan, in the heart of the city's main business district.",
             "We are currently advancing a plan to upgrade the existing building from 13 apartments and 10 shops to 32 apartments and 9 shops.",
         ])),
    dict(slug="mazeh-71", img="mazeh",
         name=L("מזא״ה 71", "Mazeh 71"), city=L("תל אביב-יפו", "Tel Aviv-Jaffa"), area=L("לב העיר", "City centre"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("שימור והשבחה", "Preservation and upgrading"),
         floors=None, units=L("מ־18 ל־30", "18 to 30"), shops=None,
         short=L("בניין לשימור בלב תל אביב: השבחה מ־18 ל־30 דירות, חצרות וגגות.",
                 "A heritage building in the heart of Tel Aviv: upgrading from 18 to 30 apartments, courtyards and roofs."),
         desc=L([
             "בניין מגורים הכולל 18 דירות, המוגדר לשימור ללא הגבלות מחמירות במסגרת תכנית השימור של העיר תל אביב.",
             "בשלב הנוכחי אנו מקדמים תכנית להשביח את הבניין הקיים מ־18 דירות ל־30 דירות, חצרות וגגות.",
         ], [
             "A residential building of 18 apartments, listed for preservation without strict restrictions under Tel Aviv's preservation plan.",
             "We are currently advancing a plan to upgrade the existing building from 18 to 30 apartments, with courtyards and roofs.",
         ])),
    dict(slug="herut-40", img="herut",
         name=L("חירות 40", "Herut 40"), city=L("רמת גן", "Ramat Gan"), area=L("שכונת הגפן", "Hagefen neighbourhood"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors="9", units="21", shops=None,
         short=L("בניין בן 9 קומות ו־21 דירות בלב שכונת הגפן הפסטורלית.", "A nine-storey building with 21 apartments in the heart of the pastoral Hagefen neighbourhood."),
         desc=L([
             "בניין בן 9 קומות, סה״כ 21 דירות, בלב שכונת הגפן הפסטורלית, בקרבת גני ילדים ובית ספר, ובמרחק קצר מפארק הירקון ומקניון איילון. הבניין ממוקם באחד המיקומים המבוקשים והנחשקים באזור.",
             "סטטוס: הפרויקט בשלבי תכנון מול העירייה.",
         ], [
             "A nine-storey building with 21 apartments in the heart of the pastoral Hagefen neighbourhood, near kindergartens and a school, and a short distance from Hayarkon Park and the Ayalon Mall. One of the most sought-after locations in the area.",
             "Status: in planning with the municipality.",
         ])),
    dict(slug="talpiot-30", img="talpiot",
         name=L("תלפיות 30", "Talpiot 30"), city=L("רמת גן", "Ramat Gan"), area=L("מרכז העיר", "City centre"),
         status=L("בשלבי תכנון", "In planning"), group="planning", type=L("תמ״א 38/2, הריסה ובנייה", "TAMA 38/2, demolition and rebuilding"),
         floors="9", units="22", shops=None,
         short=L("בניין בן 9 קומות ו־22 דירות במרכז העיר השוקק של רמת גן.", "A nine-storey building with 22 apartments in the bustling centre of Ramat Gan."),
         desc=L([
             "בניין בן 9 קומות, סה״כ 22 דירות, במיקום מושלם בלב העיר רמת גן, במרכז העיר השוקק. במרחק דקות ספורות ונגיש לכל שירותי הקהילה: חנויות, גני ילדים, בתי ספר, שירותי ציבור וגינות.",
             "סטטוס: הפרויקט בשלבי תכנון מול העירייה.",
         ], [
             "A nine-storey building with 22 apartments in a perfect location in the bustling centre of Ramat Gan, minutes from all community services: shops, kindergartens, schools, public services and gardens.",
             "Status: in planning with the municipality.",
         ])),
    # --- completed ---
    dict(slug="jaffa-road-13", img="yafo",
         name=L("דרך יפו 13", "Jaffa Road 13"), city=L("תל אביב", "Tel Aviv"), area=L("לב העיר, ליד רוטשילד", "City centre, near Rothschild"),
         status=L("הסתיים ואוכלס", "Completed and occupied"), group="done", type=L("שימור ושחזור", "Preservation and restoration"),
         floors="4", units="35", shops="10",
         short=L("אחד הבניינים המרהיבים מימיה הראשונים של תל אביב, משוחזר ומודרני. 35 דירות ו־10 חנויות.",
                 "One of the most striking buildings from Tel Aviv's earliest days, restored and modern. 35 apartments and 10 shops."),
         desc=L([
             "בניין לשימור בן 4 קומות, סה״כ 35 דירות ו־10 חנויות. הבניין הוכרז לשימור, ועם סיום הפרויקט נחשף אחד הבניינים המרהיבים של תל אביב מימיה הראשונים של העיר: מבנה משוחזר ומודרני, עם כל הפינוקים.",
             "במרתף חלל משותף גדול עם מכונות כביסה ומייבשים לשימוש הדיירים. הבניין בקרבת שדרות רוטשילד ורחוב לילינבלום, ובמרחק דקות ספורות על קורקינט מהים.",
             "סטטוס: הפרויקט הסתיים ואוכלס.",
         ], [
             "A listed four-storey building with 35 apartments and 10 shops. On completion, one of the most striking buildings from Tel Aviv's earliest days was revealed: a restored, modern structure with every comfort.",
             "The basement holds a large shared laundry space for residents. The building is near Rothschild Boulevard and Lilienblum Street, and a few minutes by scooter from the sea.",
             "Status: completed and occupied.",
         ])),
    dict(slug="rothschild-135", img="rothschild",
         name=L("רוטשילד 135", "Rothschild 135"), city=L("תל אביב", "Tel Aviv"), area=L("הבית על הבימה", "The House on Habima"),
         status=L("הסתיים ואוכלס", "Completed and occupied"), group="done", type=L("בניין בוטיק", "Boutique building"),
         floors="5", units="15", shops=None,
         short=L("הבית על הבימה: בניין בוטיק בן 5 קומות עם דירות יוקרה ופנטהאוז ענק.",
                 "The House on Habima: a five-storey boutique building with luxury apartments and a vast penthouse."),
         desc=L([
             "בניין בן 5 קומות, סה״כ 15 דירות, בלב תל אביב. הבית על הבימה הוא בניין בוטיק המציע דירות יוקרה ופנטהאוז ענק, ומעניק חוויית מגורים מושלמת: איכות חיים גבוהה, מיקום ייחודי מסוגו, עיצוב לנוחות, שלווה וחברותא, באווירה תל אביבית מקורית.",
             "סטטוס: הפרויקט הסתיים ואוכלס.",
         ], [
             "A five-storey building with 15 apartments in the heart of Tel Aviv. The House on Habima is a boutique building of luxury apartments and a vast penthouse, offering a complete living experience: a unique location, design for comfort, calm and company, in an authentic Tel Aviv atmosphere.",
             "Status: completed and occupied.",
         ])),
    dict(slug="hoshea-21-23", img="hoshea",
         name=L("הושע 21+23", "Hoshea 21+23"), city=L("בני ברק", "Bnei Brak"), area=L("", ""),
         status=L("בביצוע", "Under construction"), group="done", type=L("הריסה ובנייה מחדש", "Demolition and rebuilding"),
         floors=None, units="41", shops=None,
         short=L("41 דירות חדשות להשכרה לטווח ארוך, וקומת קרקע עם 3 גני ילדים חדשים.",
                 "41 new apartments for long-term rental, and a ground floor with three new kindergartens."),
         desc=L(["פרויקט הריסה ובנייה מחדש: 41 דירות מגורים חדשות להשכרה לטווח ארוך, ובנוסף קומת קרקע עם 3 גני ילדים חדשים."],
                ["A demolition and rebuilding project: 41 new apartments for long-term rental, plus a ground floor with three new kindergartens."]),
         extra_img="hoshea-2"),
    dict(slug="bat-shua-8", img="batshua",
         name=L("בת שוע 8", "Bat Shua 8"), city=L("רמת גן", "Ramat Gan"), area=L("", ""),
         status=L("השיווק הסתיים", "Sold out"), group="done", type=L("בניין מגורים", "Residential building"),
         floors=None, units=None, shops=None,
         short=L("בניין מגורים חדש ברמת גן. השיווק הסתיים.", "A new residential building in Ramat Gan. Sold out."),
         desc=L(["בניין מגורים חדש ברמת גן. שיווק הדירות בפרויקט הסתיים."],
                ["A new residential building in Ramat Gan. All apartments have been sold."])),
]
GROUP_ORDER = ["marketing", "planning", "done"]
BY_SLUG = {p["slug"]: p for p in PROJECTS}

SPECIALTIES = L([
    ("ייזום ותכנון", "מהתכנון ועד המסירה",
     "אנו מטפלים בפרויקטי נדל״ן בשני מסלולים: רכישה של הפרויקט כולו, או ניהול רכיב היזמות לאורך כל הפרויקט, מהתכנון דרך הביצוע ועד המסירה."),
    ("התחדשות עירונית", "פינוי־בינוי ושימור במרכזי הערים",
     "תחום זה הוא בליבת העשייה שלנו: פרויקטי נדל״ן בתוך מרכזי הערים, כולל בניינים לשימור, שבהם נדרשת רגישות אדריכלית לצד יכולת ביצוע."),
    ("תמ״א 38", "הריסה ובנייה מחדש",
     "החברה מציעה את שירותיה וניסיונה כיזם בפרויקטי תמ״א 38/2, עם התחייבות לתהליך אישי, שקוף ומסודר מול הדיירים."),
], [
    ("Development and planning", "From planning to handover",
     "We handle real estate projects in two ways: acquiring the entire project, or managing the development component throughout, from planning through construction to handover."),
    ("Urban renewal", "Renewal and preservation in city centres",
     "This is the core of our work: real estate projects inside city centres, including listed buildings, where architectural sensitivity has to go together with the ability to deliver."),
    ("TAMA 38", "Demolition and rebuilding",
     "The company offers its services and experience as developer in TAMA 38/2 projects, with a commitment to a personal, transparent and orderly process with residents."),
])

GROUP_COMPANIES = L([
    ("אחזקת נכסים", "מעגן בע״מ",
     "חברת הניהול והאחזקה של נכסי המשפחה ונכסים נוספים. עוסקת בניהול שוטף של נכסים רבים, כולל השכרת דירות למגורים ותחזוקתן."),
    ("שירותים משפטיים", "ד״ר משה וינברג ושות׳, עורכי דין ונוטריון",
     "תחומי העיסוק העיקריים: תכנון ובנייה, הפשרת קרקעות, פיתוח מקרקעין, הפקעת מקרקעין, נדל״ן, משפט אזרחי כללי וליטיגציה. המשרד קידם ויזם פיתוח של אלפי יחידות דיור ברחבי הארץ."),
    ("פיננסים", "מ.ו. השקעות בע״מ",
     "פועלת מול גופי המימון למימון נדל״ן, יחד עם כל מערכת הפיננסים בישראל: בנקים, חברות ביטוח, חברות מימון ושוק ההון."),
    ("מלאי דירות להשכרה", "רכישה, השבחה וניהול",
     "התמחות בדירות להשכרה ליד תחבורה ציבורית בגוש דן (רכבת קלה, מטרו, נת״צ): זיהוי הזדמנויות, רכישה והשבחה, תחזוקה ומימוש בעיתוי הנכון."),
], [
    ("Property management", "Maagan Ltd.",
     "The management and maintenance company for the family's properties and others. Manages a large portfolio day to day, including residential lettings and their upkeep."),
    ("Legal services", "Dr. Moshe Weinberg and Co., Advocates and Notary",
     "Main practice areas: planning and construction, land rezoning, real estate development and expropriation, property, general civil law and litigation. The firm has advanced the development of thousands of housing units across Israel."),
    ("Finance", "M.W. Investments Ltd.",
     "Works with lenders on real estate finance across Israel's financial system: banks, insurance companies, finance companies and the capital market."),
    ("Rental portfolio", "Acquisition, upgrading and management",
     "Specialises in rental apartments near public transport in greater Tel Aviv (light rail, metro, bus lanes): spotting opportunities, acquiring and upgrading, maintaining and realising at the right time."),
])

FIRST_STEP = L([
    "שולחים לנו שם של איש קשר. אנו יוצרים קשר טלפוני ומתאמים פגישה ראשונה להיכרות כללית.",
    "יחד נכין רשימה של הדיירים בנכס עם פרטי התקשרות.",
    "מאתרים דייר אחד דומיננטי שמוביל את הצעד הראשון בנכס. זה מקל מאוד על ההתקדמות בשלב זה. בהמשך, כשהפרויקט יתקדם, תיבחר נציגות של 3 דיירים.",
    "נפגשים יחד עם כל הדיירים לאסיפת דיירים ראשונית להיכרות.",
    "רק לאחר אסיפת הדיירים נוכל להבין יחד, היזם והדיירים, האם יש בנכס כדאיות לפרויקט, ונכין רשימה של שלבים להתקדמות.",
    "נעשה שיעורי בית מול הרשות המקומית והצוות הפנימי שלנו, נחזור אליכם ונציג לדיירים הצעה התפורה לנכס שבבעלותם, ונתקדם לפי התייחסויות הדיירים.",
], [
    "Send us the name of a contact person. We call and arrange a first meeting to get acquainted.",
    "Together we prepare a list of the residents in the building with contact details.",
    "We identify one lead resident to drive the first step. It makes progress at this stage much easier. Later, as the project advances, a committee of three residents is chosen.",
    "We meet all the residents at an initial residents' meeting.",
    "Only after that meeting can we understand together, developer and residents, whether the building is a viable project, and prepare a list of steps forward.",
    "We do our homework with the municipality and our in-house team, come back to you with a proposal tailored to your building, and proceed according to the residents' feedback.",
])

SOLD = {"he": "נמכרה", "en": "Sold"}

DOOR = L("דלת ביטחון מעוצבת בכניסה לדירה, מערכת אינטרקום עם צפייה במעגל סגור במסך צבעוני. דלתות פנים יוניק פרימיום בגובה 2.1 מ׳.",
         "Designed security entrance door, intercom with colour closed-circuit video. Unik Premium interior doors, 2.1 m high.")
BATH = L("חדרי אמבטיה: חיפוי עד התקרה, ברזים, אסלות, אמבטיות ומקלחונים וניאגרה סמויה. חמת, גרוהה, אידיאל סטנדרט או גיבריט.",
         "Bathrooms: tiling to the ceiling, taps, toilets, baths, shower enclosures and concealed cisterns. Hamat, Grohe, Ideal Standard or Geberit.")
WINDOWS = L("חלונות וויטרינות קליל או אקסטל, תריסים חשמליים עם מנועי סומפי, זיגוג כפול אקוסטי מבודד, רשתות נגד יתושים בכל הפתחים (למעט ממ״ד, על פי תקן).",
            "Klil or Extal windows and glazing, electric shutters with Somfy motors, acoustic double glazing, insect screens on all openings (except the safe room, per standard).")
BALCONY = L([
    "מעקה מסגרות ברזל אומן, או מעקה קל (פלדה או כבלים) לפי בחירת האדריכל.",
    "תריס גלילה חשמלי (מנוע סומפי) וויטרינות אלומיניום מפרופיל קליל 7000, במידות לפי סוג החלון והנחיות היצרן.",
], [
    "Wrought-iron railing, or a light steel or cable railing, at the architect's choice.",
    "Electric roller shutter (Somfy motor) and aluminium glazing in Klil 7000 profiles, sized to the window type and the manufacturer's guidance.",
])
LAWYER = L(("עורך דין היזם", "משרד עו״ד ד״ר משה וינברג",
            "משרד מוביל בתחום האזרחי: תכנון ובנייה, הפשרת קרקעות, פיתוח והפקעת מקרקעין ומשפט אזרחי. המשרד קידם ויזם פיתוח של אלפי יחידות דיור ברחבי הארץ ומקיים קשר שוטף עם רשויות התכנון."),
           ("Developer's counsel", "Dr. Moshe Weinberg Law Offices",
            "A leading civil law firm: planning and construction, land rezoning, real estate development and expropriation, and general civil law. The firm has initiated and advanced the development of thousands of housing units across Israel and works continuously with the planning authorities."))


def apt(he, en, pdf=None, sold=False, note=None):
    return dict(cells=L(he, en), pdf=pdf, sold=sold, note=note)


# Rich project pages: apartments table (+ plan PDFs), tours, gallery, specification, team.
RICH = {
    "louis-marshall-11": dict(
        head=L(["דירה", "סוג", "חדרים", "שטח", "חוץ"], ["Apartment", "Type", "Rooms", "Area", "Outdoor"]),
        note=L("3 דירות בקומה, 2 כיווני אוויר ומרפסת שמש לכל דירה.", "Three apartments per floor, two exposures and a sun balcony for every apartment."),
        rows=[
            apt(["דירה 1", "דירת גן", "2 חדרים", "67 מ״ר", "55 מ״ר גן"], ["Apt. 1", "Garden apartment", "2 rooms", "67 sqm", "55 sqm garden"], "apt-1"),
            apt(["דירה 2", "דירה", "3 חדרים", "70 מ״ר", "11 מ״ר מרפסת"], ["Apt. 2", "Apartment", "3 rooms", "70 sqm", "11 sqm balcony"], "apt-2", note=L("מבצע לזמן מוגבל", "Limited-time offer")),
            apt(["דירה 3", "דירה", "3 חדרים", "76 מ״ר", "11 מ״ר מרפסת"], ["Apt. 3", "Apartment", "3 rooms", "76 sqm", "11 sqm balcony"], "apt-3", note=L("4,820,300 ₪, מבצע לזמן מוגבל", "NIS 4,820,300, limited-time offer")),
            apt(["דירה 4", "דירה", "3 חדרים", "62 מ״ר", "14 מ״ר מרפסת"], ["Apt. 4", "Apartment", "3 rooms", "62 sqm", "14 sqm balcony"], "apt-4", sold=True),
            apt(["דירה 5", "דירה", "3 חדרים", "70 מ״ר", "11 מ״ר מרפסת"], ["Apt. 5", "Apartment", "3 rooms", "70 sqm", "11 sqm balcony"], "apt-5", note=L("מבצע לזמן מוגבל", "Limited-time offer")),
            apt(["דירה 17", "פנטהאוז", "3 חדרים", "80 מ״ר", "50 מ״ר מרפסת"], ["Apt. 17", "Penthouse", "3 rooms", "80 sqm", "50 sqm terrace"], "apt-17"),
            apt(["דירה 18", "מיני פנטהאוז", "2 חדרים", "60 מ״ר", "21 מ״ר מרפסת"], ["Apt. 18", "Mini penthouse", "2 rooms", "60 sqm", "21 sqm terrace"], "apt-18", sold=True),
            apt(["דירה 19", "דירה", "3 חדרים", "73 מ״ר", "6 מ״ר מרפסת"], ["Apt. 19", "Apartment", "3 rooms", "73 sqm", "6 sqm balcony"], "apt-19"),
            apt(["דירה 20", "דירה", "2 חדרים", "56 מ״ר", "5.5 מ״ר מרפסת"], ["Apt. 20", "Apartment", "2 rooms", "56 sqm", "5.5 sqm balcony"], "apt-20"),
            apt(["איחוד 19+20", "פנטהאוז", "4 חדרים", "120 מ״ר", "20 מ״ר מרפסת"], ["19+20 combined", "Penthouse", "4 rooms", "120 sqm", "20 sqm terrace"], "penthouse-19-20"),
        ],
        sale_notice=True,
        tours=True,
        gallery=[(f"apt-{i}", "w6" if i % 3 else "w12") for i in range(1, 9)],
        spec=L([("", ["דלת ביטחון מעוצבת בכניסה לדירה, מערכת אינטרקום עם צפייה במעגל סגור במסך צבעוני. דלתות פנים יוניק פרימיום בגובה 2.1 מ׳.",
                      "מערכת מיזוג אוויר VRF.", "חשמל חכם, אביזרי קצה גוויס או ביטיצ׳ינו.",
                      "מטבח מעוצב, גודלו על פי התכנון האדריכלי ותכניות הדירה.",
                      "חדרי אמבטיה: חיפוי עד התקרה, ברזים, אסלות, אמבטיות ומקלחונים וניאגרה סמויה. חמת, גרוהה, אידיאל סטנדרט או גיבריט.",
                      "חלונות וויטרינות קליל או אקסטל, תריסים חשמליים עם מנועי סומפי, זיגוג כפול אקוסטי מבודד, רשתות נגד יתושים בכל הפתחים (למעט ממ״ד, על פי תקן)."])],
               [("", ["Designed security entrance door, intercom with colour closed-circuit video. Unik Premium interior doors, 2.1 m high.",
                      "VRF air conditioning system.", "Smart electrical system, Gewiss or Bticino fittings.",
                      "Designed kitchen, sized according to the architectural plan of each apartment.",
                      "Bathrooms: tiling to the ceiling, taps, toilets, baths, shower enclosures and concealed cisterns. Hamat, Grohe, Ideal Standard or Geberit.",
                      "Klil or Extal windows and glazing, electric shutters with Somfy motors, acoustic double glazing, insect screens on all openings (except the safe room, per standard)."])]),
        people=L([("האדריכל", "מאור לוי, לוי לוסטיג אדריכלים",
                   "המשרד עוסק בתכנון ועיצוב בתים ודירות מגורים ובפרויקטי תמ״א 38. מאור לוי הוא אדריכל, בעל תואר שני במנהל עסקים ומוסמך מכון התקנים כמלווה בנייה ירוקה, עם ניסיון רב שנים בבנייה אורבנית ופרטית."),
                  LAWYER["he"]],
                 [("Architect", "Maor Levy, Levy Lustig Architects",
                   "The practice designs houses, residential apartments and TAMA 38 projects. Maor Levy is an architect with an MBA, certified by the Standards Institution of Israel as a green building consultant, with many years of experience in urban and private construction."),
                  LAWYER["en"]]),
    ),
    "grofit-3": dict(
        head=L(["דירה", "קומה", "חדרים", "שטח"], ["Apartment", "Floor", "Rooms", "Area"]),
        note=L("2 דירות בלבד בכל קומה, 3 כיווני אוויר לכל דירה.", "Only two apartments per floor, three exposures for every apartment."),
        rows=[
            apt(["דירה 1", "קרקע", "5 חדרים", "142 מ״ר"], ["Apt. 1", "Ground", "5 rooms", "142 sqm"], "apt-1", sold=True),
            apt(["דירה 2", "קרקע", "5 חדרים", "136 מ״ר"], ["Apt. 2", "Ground", "5 rooms", "136 sqm"], None, sold=True),
            apt(["דירה 3", "1", "5 חדרים", "126 מ״ר"], ["Apt. 3", "1", "5 rooms", "126 sqm"], "apt-3"),
            apt(["דירה 4", "1", "5 חדרים", "123 מ״ר"], ["Apt. 4", "1", "5 rooms", "123 sqm"], "apt-4"),
            apt(["דירה 8, דופלקס גג", "3-4", "6 חדרים", "140 מ״ר"], ["Apt. 8, roof duplex", "3-4", "6 rooms", "140 sqm"], "apt-8"),
        ],
        gallery=[("grofit-int-1", "w6"), ("grofit-interior", "w6")],
        spec=L([("הבניין", ["תכנון על ידי משרד אדריכלים מוביל המתמחה במבנים באזור זה של צהלה, בדגש על שטחים מרווחים ומודרניים. הבניין נבנה על פי תקן בנייה ירוקה ותקני החיזוק מפני רעידות אדמה (תמ״א 38).",
                            "לובי מרווח בעיצוב אדריכלי עם פינות נוי, צמחייה, מראה ותאורה דקורטיבית. מעלית שקטה, חכמה ומרווחת.",
                            "גינה מעוצבת על ידי יועץ נוף, תאורת חוץ בתכנון יועץ תאורה, השקיה ותאורה סמויה חסכונית."]),
                ("הדירה", [DOOR["he"], "מערכת מיזוג אוויר VRF.", "חשמל חכם, אביזרי קצה גוויס או ביטיצ׳ינו.",
                           "מטבח מעוצב מחברת דאדא, סמל או בופי, בגודל לפי התכנון האדריכלי ותכניות הדירה.", BATH["he"], WINDOWS["he"],
                           "לכל דירה חניה במכפיל חניה במרתף, עם יציאה וכניסה עצמאיות ועמדת טעינה לרכב חשמלי."]),
                ("המרפסת", BALCONY["he"])],
               [("The building", ["Designed by a leading architectural practice specialising in this part of Tzahala, with spacious, modern layouts. Built to green building and earthquake reinforcement (TAMA 38) standards.",
                                  "A generous architect-designed lobby with planting, a large mirror and decorative lighting. A quiet, smart, spacious lift.",
                                  "A garden designed by a landscape consultant, outdoor lighting by a lighting consultant, irrigation and concealed low-energy lighting."]),
                ("The apartment", [DOOR["en"], "VRF air conditioning system.", "Smart electrical system, Gewiss or Bticino fittings.",
                                   "Designed kitchen by Dada, Semel or Boffi, sized according to the architectural plan of each apartment.", BATH["en"], WINDOWS["en"],
                                   "One parking space per apartment in a basement stacker, independently accessible, with an electric vehicle charger."]),
                ("The balcony", BALCONY["en"])]),
        spec_note=True,
        people=L([("האדריכל", "רון שפיגל אדריכלים",
                   "המשרד, בראשות האדריכל רון שפיגל, בוגר החוג לאדריכלות באוניברסיטת אריאל, הוקם בשנת 2007 ומתמחה בתכנון ועיצוב בתים פרטיים, דירות יוקרה, שיפוץ מבנים קיימים, בנייה אורבנית, בנייני מגורים, תמ״א 38 והתחדשות עירונית."),
                  LAWYER["he"]],
                 [("Architect", "Ron Spiegel Architects",
                   "Founded in 2007 by architect Ron Spiegel, a graduate of Ariel University's architecture department, the practice specialises in private homes, luxury apartments, renovation of existing buildings, urban construction, residential buildings, TAMA 38 and urban renewal."),
                  LAWYER["en"]]),
    ),
    "arlozorov-53": dict(
        head=L(["דירה", "קומה", "חדרים", "שטח"], ["Apartment", "Floor", "Rooms", "Area"]),
        note=L("דירות 2 עד 5 חדרים, דירת גן בקומת הקרקע ושני פנטהאוזים עם נוף לקו הרקיע של תל אביב. 2 כיווני אוויר לכל דירה.",
               "Two- to five-room apartments, a garden apartment on the ground floor and two penthouses facing the Tel Aviv skyline. Two exposures for every apartment."),
        rows=[
            apt(["דירה 1", "1-", "4 חדרים", "103 מ״ר"], ["Apt. 1", "-1", "4 rooms", "103 sqm"], "apt-1"),
            apt(["דירה 2", "קרקע", "2 חדרים", "62.7 מ״ר"], ["Apt. 2", "Ground", "2 rooms", "62.7 sqm"], "apt-2"),
            apt(["דירה 3", "קרקע", "2 חדרים", "64.2 מ״ר"], ["Apt. 3", "Ground", "2 rooms", "64.2 sqm"], "apt-3"),
            apt(["דירה 6", "1", "3 חדרים", "69 מ״ר"], ["Apt. 6", "1", "3 rooms", "69 sqm"], "apt-6", sold=True),
            apt(["דירה 9", "2", "2 חדרים", "51.2 מ״ר"], ["Apt. 9", "2", "2 rooms", "51.2 sqm"], "apt-9", sold=True),
            apt(["דירה 10", "2", "4 חדרים", "98.3 מ״ר"], ["Apt. 10", "2", "4 rooms", "98.3 sqm"], "apt-10"),
            apt(["דירה 11", "2", "2 חדרים", "58.8 מ״ר"], ["Apt. 11", "2", "2 rooms", "58.8 sqm"], "apt-11", sold=True),
            apt(["דירה 15", "4", "3 חדרים", "63.3 מ״ר"], ["Apt. 15", "4", "3 rooms", "63.3 sqm"], "apt-15", sold=True),
            apt(["דירה 18", "5", "3 חדרים", "63.2 מ״ר"], ["Apt. 18", "5", "3 rooms", "63.2 sqm"], "apt-18", sold=True),
            apt(["דירה 22", "6", "2 חדרים", "62.6 מ״ר"], ["Apt. 22", "6", "2 rooms", "62.6 sqm"], "apt-22", sold=True),
            apt(["דירה 23", "6", "5 חדרים", "111.2 מ״ר"], ["Apt. 23", "6", "5 rooms", "111.2 sqm"], "apt-23"),
            apt(["דירה 24", "7", "4 חדרים", "99.4 מ״ר"], ["Apt. 24", "7", "4 rooms", "99.4 sqm"], "apt-24"),
            apt(["דירה 25", "7", "2 חדרים", "63 מ״ר"], ["Apt. 25", "7", "2 rooms", "63 sqm"], "apt-25", sold=True),
            apt(["דירה 26", "7", "5 חדרים", "111.2 מ״ר"], ["Apt. 26", "7", "5 rooms", "111.2 sqm"], "apt-26"),
            apt(["דירה 27", "8", "3 חדרים", "78 מ״ר"], ["Apt. 27", "8", "3 rooms", "78 sqm"], "apt-27"),
            apt(["דירה 28", "8", "3 חדרים", "73.2 מ״ר"], ["Apt. 28", "8", "3 rooms", "73.2 sqm"], "apt-28", sold=True),
            apt(["דירה 29", "8", "4.5 חדרים", "94.6 מ״ר"], ["Apt. 29", "8", "4.5 rooms", "94.6 sqm"], "apt-29"),
            apt(["דירה 30", "9", "3 חדרים", "66.2 מ״ר"], ["Apt. 30", "9", "3 rooms", "66.2 sqm"], "apt-30"),
            apt(["דירה 31", "9", "3 חדרים", "86.3 מ״ר"], ["Apt. 31", "9", "3 rooms", "86.3 sqm"], "apt-31"),
        ],
        gallery=[("arlozorov-front", "w4"), ("arlozorov-back", "w4"), ("arlozorov-view-1", "w4"), ("arlozorov-interior", "w6"), ("arlozorov-int-2", "w6")],
        spec=L([("הבניין", ["10 קומות ו-4 קומות מרתף, 2 מעליות שקטות וחכמות, לובי מרווח בעיצוב אדריכלי עם פינות נוי, צמחייה, מראה ותאורה דקורטיבית.",
                            "גינה מעוצבת על ידי מומחה נוף, עם השקיה ותאורה חסכונית חכמה.",
                            "בנייה על פי תקן בנייה ירוקה ותקני החיזוק מפני רעידות אדמה (תמ״א 38)."]),
                ("הדירה", ["בקומות העליונות 3 דירות בקומה בלבד, בקומות הנמוכות 4 דירות בקומה. לכל דירה 2 כיווני אוויר.",
                           DOOR["he"], "חשמל, אביזרי קצה גוויס או ביטיצ׳ינו או שווה ערך.",
                           "מטבח מעוצב מחברת אביבי או סמל או שווה ערך, בגודל לפי התכנון האדריכלי ותכניות הדירה.", BATH["he"], WINDOWS["he"],
                           "לכל דירה מחסן דירתי, מרפסת שמש וחניה אחת במרתף."]),
                ("המרפסת", BALCONY["he"])],
               [("The building", ["Ten storeys and four basement levels, two quiet smart lifts, a generous architect-designed lobby with planting, a large mirror and decorative lighting.",
                                  "A garden designed by a landscape specialist, with irrigation and smart low-energy lighting.",
                                  "Built to green building and earthquake reinforcement (TAMA 38) standards."]),
                ("The apartment", ["Only three apartments per floor on the upper floors, four on the lower floors. Two exposures for every apartment.",
                                   DOOR["en"], "Electrical system with Gewiss or Bticino fittings, or equivalent.",
                                   "Designed kitchen by Avivi or Semel, or equivalent, sized according to the architectural plan of each apartment.", BATH["en"], WINDOWS["en"],
                                   "A storage room, a sun balcony and one basement parking space for every apartment."]),
                ("The balcony", BALCONY["en"])]),
        spec_note=True,
        people=L([("האדריכל", "משה אלפסי אדריכלים",
                   "המשרד, שהוקם בשנת 2013 על ידי האדריכל משה אלפסי, בוגר המחלקה לארכיטקטורה בבצלאל, פועל בפרויקטי מגורים ותכנון עירוני ומגבש בכל פרויקט רעיון אדריכלי מתוך מחקר ותשומת לב למאפייני המקום."),
                  LAWYER["he"]],
                 [("Architect", "Moshe Alfasi Architects",
                   "Founded in 2013 by architect Moshe Alfasi, a graduate of the Bezalel Academy's architecture department, the practice works on residential and urban planning projects, developing each design from research into the site's distinctive character."),
                  LAWYER["en"]]),
    ),
}
# Virtual tours (Louis Marshall only), loaded only when the visitor asks for them
MARSHALL_PANORAMA = "https://reelook-public.s3.eu-west-1.amazonaws.com/panoramas/LuiMarshel11/tour.html"
MARSHALL_3D = "https://www.theasys.io/viewer/pd9r6wvGUtRFF7JIuHks3KeXBsT8LP/"

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def v(x, lang):
    """Return the language variant of a bilingual value (or the value itself)."""
    if isinstance(x, dict) and "he" in x:
        return x[lang]
    return x


def pfx(lang):
    return "/en" if lang == "en" else ""


def alt_path(path, lang):
    """Path of the same page in the other language."""
    if lang == "he":
        return "/en" + path if path != "/404.html" else "/en/404.html"
    return path[3:] or "/"


def picture(name, alt, sizes, cls="", eager=False):
    m = IMAGES[name]
    variants = m["sizes"]
    avif = ", ".join(f"/assets/img/{name}-{s['w']}.avif {s['w']}w" for s in variants)
    webp = ", ".join(f"/assets/img/{name}-{s['w']}.webp {s['w']}w" for s in variants)
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
    srcset = ", ".join(f"/assets/img/{name}-{s['w']}.avif {s['w']}w" for s in m["sizes"])
    return f'<link rel="preload" as="image" fetchpriority="high" type="image/avif" imagesrcset="{srcset}" imagesizes="{sizes}">'


def place(p, lang):
    city, area = v(p["city"], lang), v(p["area"], lang)
    return f"{city}, {area}" if area else city


CARD_SIZES = {2: "(max-width:560px) 92vw, 46vw", 3: "(max-width:560px) 92vw, (max-width:900px) 46vw, 30vw", 4: "(max-width:560px) 92vw, (max-width:900px) 46vw, 22vw"}


def card(p, lang, cols=3):
    href = p.get("redirect") or f"{pfx(lang)}/projects/{p['slug']}/"
    return f"""<a class="card rv-img" href="{href}" data-status="{p['group']}">
  <div class="frame">{picture(p['img'], f"{v(p['name'], lang)}, {v(p['city'], lang)}", CARD_SIZES[cols])}</div>
  <div class="meta">
    <h3>{esc(v(p['name'], lang))}</h3>
    <div class="sub"><span>{esc(place(p, lang))}</span><span class="status">{esc(v(p['status'], lang))}</span></div>
  </div>
</a>"""


def cards(items, cols, lang):
    return f'<div class="cards cards--{cols}">\n' + "\n".join(card(p, lang, cols) for p in items) + "\n</div>"


def project_groups(lang, cols, level="h3"):
    t = T[lang]
    out = []
    for key in GROUP_ORDER:
        title, note = t["groups"][key]
        items = [p for p in PROJECTS if p["group"] == key]
        out.append(f"""<div class="group" id="{key}">
  <div class="group-head"><{level}>{title}</{level}><span class="note">{note}</span></div>
  {cards(items, cols[key], lang)}
</div>""")
    return "\n".join(out)


def rows(items):
    return "".join(
        f"""<div class="row rv"><span class="num">0{i + 1}</span><h3>{a}<small>{b}</small></h3><p>{c}</p></div>"""
        for i, (a, b, c) in enumerate(items))


def head(lang, title, desc, path, extra="", og_image=None):
    t = T[lang]
    full = t["site_title"] if path in ("/", "/en/") else f"{title} | {t['brand_short']}"
    other = alt_path(path, lang)
    he_path, en_path = (path, other) if lang == "he" else (other, path)
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{t['dir']}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{path}">
<link rel="alternate" hreflang="he" href="{SITE}{he_path}">
<link rel="alternate" hreflang="en" href="{SITE}{en_path}">
<link rel="alternate" hreflang="x-default" href="{SITE}{he_path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:site_name" content="{esc(t['brand'])}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/assets/img/{og_image or t['og_default']}.webp">
<meta name="theme-color" content="#f6f4ef">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/plex-hebrew-300-{'hebrew' if lang == 'he' else 'latin'}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plex-hebrew-400-{'hebrew' if lang == 'he' else 'latin'}.woff2" as="font" type="font/woff2" crossorigin>
{extra}
<style>{CSS}</style>
<script>document.documentElement.classList.remove('no-js')</script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
"""


def header(lang, current, path):
    t = T[lang]
    px = pfx(lang)
    items = [(px + "/", t["home"]), (px + "/about/", t["about"]), (px + "/projects/", t["projects"]),
             (px + "/how-we-start/", t["how"]), (px + "/contact/", t["contact"])]
    links = "".join(
        f'<a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if h == current else ""}>{lbl}</a>' for h, lbl in items)
    other_lang = "en" if lang == "he" else "he"
    return f"""<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{px}/" aria-label="{esc(t['brand'])}"><img src="/assets/img/logo.png" width="150" height="43" alt="{esc(t['brand'])}"></a>
    <nav class="menu" id="menu" aria-label="{'ניווט ראשי' if lang == 'he' else 'Main navigation'}">
      {links}
      <a class="lang" href="{alt_path(path, lang)}" lang="{other_lang}" hreflang="{other_lang}">{t['lang_switch']}</a>
      <a class="menu-phone" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a>
    </nav>
    <a class="head-phone" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a>
    <button class="burger" type="button" aria-controls="menu" aria-expanded="false" aria-label="{t['menu_open']}"><span></span></button>
  </div>
</header>
<main id="main">
"""


def footer(lang, path):
    t = T[lang]
    px = pfx(lang)
    other_lang = "en" if lang == "he" else "he"
    return f"""</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="/assets/img/logo.png" width="150" height="43" alt="" loading="lazy">
        <p>{t['foot_p']}</p>
      </div>
      <div class="foot-col">
        <p class="foot-h">{t['foot_nav']}</p>
        <a href="{px}/about/">{t['about']}</a>
        <a href="{px}/projects/">{t['projects']}</a>
        <a href="{px}/how-we-start/">{t['how']}</a>
        <a href="{px}/contact/">{t['contact']}</a>
        <a href="{px}/accessibility/">{t['accessibility']}</a>
        <a href="{px}/privacy/">{t['privacy']}</a>
        <a href="{alt_path(path, lang)}" lang="{other_lang}">{t['lang_switch_full']}</a>
      </div>
      <div class="foot-col foot-col--wide">
        <p class="foot-h">{t['foot_contact']}</p>
        <a href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <span>{t['address']}</span>
        <a href="{FACEBOOK}" target="_blank" rel="noopener">{t['facebook']}</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© {date.today().year} {t['brand']}. {t['foot_rights']}</span>
      <span>{t['foot_note']}</span>
    </div>
  </div>
</footer>
<div class="stick" id="stick" hidden>
  <div class="wrap stick-row">
    <p class="stick-title">{t['stick_title']}</p>
    <form class="form stick-form" action="https://api.web3forms.com/submit" method="POST" novalidate>
      <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
      <input type="hidden" name="subject" value="{t['f_subject']}">
      <input type="hidden" name="from_name" value="keremltd.co.il">
      <input type="hidden" name="redirect" value="{SITE}{px}/contact/?sent=1">
      <label class="hp" aria-hidden="true">{t['f_hp']} <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></label>
      <label class="sr" for="s-name">{t['stick_name']}</label><input id="s-name" name="name" type="text" autocomplete="name" placeholder="{t['stick_name']}">
      <label class="sr" for="s-phone">{t['stick_phone']}</label><input id="s-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" placeholder="{t['stick_phone']}" required minlength="7" pattern="[0-9+\\-\\s()]{{7,}}">
      <button class="btn btn--light" type="submit">{t['stick_send']}</button>
      <p class="form__msg" aria-live="polite" tabindex="-1"></p>
    </form>
    <a class="stick-phone" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a>
    <button class="stick-close" type="button" aria-label="{t['stick_close']}">×</button>
  </div>
</div>
<script src="/assets/js/site.js" defer></script>
<script src="/assets/js/a11y.js" defer></script>
</body>
</html>
"""


def contact_form(lang):
    t = T[lang]
    px = pfx(lang)
    topics = "".join(f"<option>{esc(x)}</option>" for x in t["f_topics"])
    opts = "".join(f'<option value="{esc(v(p["name"], lang))}" data-slug="{p["slug"]}">{esc(v(p["name"], lang))}, {esc(v(p["city"], lang))}</option>' for p in PROJECTS if p["group"] != "done")
    return f"""<form class="form" action="https://api.web3forms.com/submit" method="POST" novalidate>
    <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
    <input type="hidden" name="subject" value="{t['f_subject']}">
    <input type="hidden" name="from_name" value="keremltd.co.il">
    <input type="hidden" name="redirect" value="{SITE}{px}/contact/?sent=1">
    <label class="hp" aria-hidden="true">{t['f_hp']} <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></label>
    <div><label for="f-name">{t['f_name']}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
    <div><label for="f-phone">{t['f_phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required minlength="7" pattern="[0-9+\\-\\s()]{{7,}}"></div>
    <div class="full"><label for="f-email">{t['f_email']}</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
    <div class="full"><label for="f-building">{t['f_building']}</label><input id="f-building" name="building" type="text" autocomplete="street-address"></div>
    <div class="full"><label for="f-topic">{t['f_topic']}</label>
      <select id="f-topic" name="topic"><option value="">{t['f_topic_pick']}</option>{topics}</select></div>
    <div class="full"><label for="f-project">{t['f_project']}</label>
      <select id="f-project" name="project"><option value="">{t['f_project_none']}</option>{opts}</select></div>
    <div class="full"><label for="f-msg">{t['f_msg']}</label><textarea id="f-msg" name="message"></textarea></div>
    <label class="consent"><input type="checkbox" name="consent" value="yes" required><span>{t['f_consent']}<a href="{px}/privacy/" class="link">{t['f_privacy']}</a>.</span></label>
    <div class="actions"><button class="btn" type="submit">{t['f_send']}</button><span class="small muted">{t['f_or']} <a href="tel:{PHONE_TEL}" dir="ltr" class="link">{PHONE}</a></span></div>
    <p class="form__msg" aria-live="polite" tabindex="-1" data-sent="{t['f_sent']}"></p>
  </form>"""


def contact_section(lang):
    t = T[lang]
    return f"""<section class="section rule" id="contact">
  <div class="wrap grid">
    <div class="contact-info rv">
      <h2>{t['contact_h2']}</h2>
      <p class="lead">{t['contact_lead']}</p>
      <dl class="dl">
        <div><dt>{t['phone']}</dt><dd><a href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a></dd></div>
        <div><dt>{t['email']}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>{t['office']}</dt><dd>{t['address']}</dd></div>
      </dl>
    </div>
    <div class="contact-form rv">{contact_form(lang)}</div>
  </div>
</section>"""


def crumbs(lang, *items):
    t = T[lang]
    parts = [f'<a href="{pfx(lang)}/">{t["crumb_home"]}</a>']
    for i, (label, href) in enumerate(items):
        parts.append("<span>/</span>")
        parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{esc(label)}</span>")
    return f'<nav class="crumbs" aria-label="{t["crumbs_label"]}">{"".join(parts)}</nav>'


def write(path, html):
    if path.endswith(".html"):
        full = os.path.join(WWW, path.strip("/"))
    else:
        full = os.path.join(WWW, path.strip("/"), "index.html") if path.strip("/") else os.path.join(WWW, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", path)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Hero variants (preview pages under /hero/N/ until one is chosen)
# --------------------------------------------------------------------------

HERO_VARIANTS = {
    1: dict(img="hoshea", sizes="100vw", name=L("תמונה ברוחב מלא ולוח טקסט", "Full-bleed photo with a text plate"),
            desc=L("הצילום נמתח מקצה לקצה, וכותרת הפתיחה יושבת על לוח בהיר שחופף לתחתית התמונה. פתיחה קולנועית ושקטה.",
                   "The photograph runs edge to edge and the headline sits on a light plate overlapping its lower edge. Cinematic and quiet.")),
    2: dict(img="herut", sizes="(max-width:1280px) 92vw, 1184px", name=L("טיפוגרפיה קודם, תמונה רחבה מתחת", "Typography first, wide photo beneath"),
            desc=L("כותרת ענקית ברוחב הדף, כמו שער של מגזין אדריכלות, ומתחתיה צילום פנורמי עם כיתוב. הכי עיתונאי.",
                   "A page-wide headline like an architecture magazine cover, with a panoramic photograph and caption below. The most editorial.")),
    3: dict(img="bernstein", sizes="(max-width:900px) 92vw, 50vw", name=L("חצי־חצי עם תמונה לגובה המסך", "Half and half, image to full height"),
            desc=L("הטקסט ממורכז לגובה מול הדמיה אנכית שממלאת את כל גובה המסך ונצמדת לקצה. שער ספר, לא באנר.",
                   "Vertically centred text against a portrait rendering that fills the full viewport height and meets the edge. A book cover, not a banner.")),
    4: dict(img="hero", sizes="(max-width:900px) 92vw, 58vw", name=L("שתי תמונות בקומפוזיציה א־סימטרית", "Two photographs, asymmetric composition"),
            desc=L("כותרת ברוחב הדף, ומתחתיה תמונה גדולה ותמונה קטנה מוסטת כלפי מטה, כל אחת עם כתובת. עמוד מתוך ספר פרויקטים.",
                   "A page-wide headline, then a large and a small photograph offset downward, each with its address. A spread from a project book.")),
    5: dict(img="hero", sizes="(max-width:1280px) 92vw, 1184px", name=L("פתיחה בכחול כהה, תמונה פורצת מתחת", "Navy opening, photo breaking out beneath"),
            desc=L("הכותרת בלבן על משטח כחול כהה ברוחב מלא, והצילום חופף לקצה התחתון של המשטח. יציב, ממסדי, בטוח בעצמו.",
                   "The headline in white on a full-width navy field, with the photograph overlapping the field's lower edge. Solid, established, assured.")),
}


def hero_html(lang, variant=0):
    t = T[lang]
    px = pfx(lang)
    text = f"""<span class="eyebrow">{t['hero_eyebrow']}</span>
      <h1>{t['hero_h1']}</h1>
      <p class="lead">{t['hero_lead']}</p>
      <div class="cta-row"><a class="btn" href="{px}/projects/">{t['cta_projects']}</a><a class="btn btn--ghost" href="{px}/how-we-start/">{t['cta_how']}</a></div>"""
    if variant == 0:
        sizes = "(max-width:900px) 92vw, 52vw"
        return f"""<section class="hero">
  <div class="wrap grid">
    <div class="hero-text">
      {text}
    </div>
    <div class="hero-media">
      <figure>
        <div class="frame">{picture("hero", t['hero_caption'], sizes, eager=True)}</div>
        <figcaption>{t['hero_caption']}</figcaption>
      </figure>
    </div>
  </div>
</section>"""
    hv = HERO_VARIANTS[variant]
    cap_hoshea = t['about_caption']
    cap_herut = t['how_caption']
    cap_bern = L("אדוארד ברנשטיין 11, תל אביב. אושר בוועדה המקומית.", "Eduard Bernstein 11, Tel Aviv. Approved by the local committee.")[lang]
    cap_yafo = L("דרך יפו 13, תל אביב. שימור ושחזור, הסתיים ואוכלס.", "Jaffa Road 13, Tel Aviv. Preservation and restoration, completed.")[lang]
    if variant == 1:
        return f"""<section class="hero hero--v1">
  <div class="frame">{picture("hoshea", cap_hoshea, "100vw", eager=True)}</div>
  <div class="wrap"><div class="plate">
      {text}
  </div></div>
  <p class="wrap hero-cap">{cap_hoshea}</p>
</section>"""
    if variant == 2:
        text_light = f"""<span class="eyebrow">{t['hero_eyebrow']}</span>
      <h1>{t['hero_h1']}</h1>"""
        return f"""<section class="hero hero--v2">
  <div class="wrap">
    {text_light}
    <div class="v2-row">
      <p class="lead">{t['hero_lead']}</p>
      <div class="cta-row"><a class="btn" href="{px}/projects/">{t['cta_projects']}</a><a class="btn btn--ghost" href="{px}/how-we-start/">{t['cta_how']}</a></div>
    </div>
    <figure>
      <div class="frame">{picture("herut", cap_herut, hv['sizes'], eager=True)}</div>
      <figcaption>{cap_herut}</figcaption>
    </figure>
  </div>
</section>"""
    if variant == 3:
        return f"""<section class="hero hero--v3">
  <div class="wrap grid">
    <div class="hero-text">
      {text}
    </div>
    <div class="hero-media">
      <figure>
        <div class="frame">{picture("bernstein", cap_bern, hv['sizes'], eager=True)}</div>
        <figcaption>{cap_bern}</figcaption>
      </figure>
    </div>
  </div>
</section>"""
    if variant == 4:
        return f"""<section class="hero hero--v4">
  <div class="wrap">
    <div class="v4-head"><span class="eyebrow">{t['hero_eyebrow']}</span><h1>{t['hero_h1']}</h1></div>
    <div class="grid v4-grid">
      <figure class="v4-big">
        <div class="frame">{picture("hero", t['hero_caption'], hv['sizes'], eager=True)}</div>
        <figcaption>{t['hero_caption']}</figcaption>
      </figure>
      <figure class="v4-small">
        <div class="frame">{picture("yafo", cap_yafo, "(max-width:900px) 44vw, 30vw")}</div>
        <figcaption>{cap_yafo}</figcaption>
      </figure>
      <div class="v4-text">
        <p class="lead">{t['hero_lead']}</p>
        <div class="cta-row"><a class="btn" href="{px}/projects/">{t['cta_projects']}</a><a class="btn btn--ghost" href="{px}/how-we-start/">{t['cta_how']}</a></div>
      </div>
    </div>
  </div>
</section>"""
    if variant == 5:
        return f"""<section class="hero hero--v5">
  <div class="band band--navy v5-band">
    <div class="wrap">
      <span class="eyebrow">{t['hero_eyebrow']}</span>
      <h1>{t['hero_h1']}</h1>
      <p class="lead">{t['hero_lead']}</p>
      <div class="cta-row"><a class="btn btn--light" href="{px}/projects/">{t['cta_projects']}</a><a class="btn btn--outline-light" href="{px}/how-we-start/">{t['cta_how']}</a></div>
    </div>
  </div>
  <div class="wrap v5-media">
    <figure>
      <div class="frame">{picture("hero", t['hero_caption'], hv['sizes'], eager=True)}</div>
      <figcaption>{t['hero_caption']}</figcaption>
    </figure>
  </div>
</section>"""


def page_hero_index(lang):
    t = T[lang]
    px = pfx(lang)
    path = f"{px}/hero/"
    items = "".join(
        f"""<li><a class="link" href="{px}/hero/{n}/">{'אפשרות' if lang == 'he' else 'Option'} {n}: {v(hv['name'], lang)}</a><p class="small muted">{v(hv['desc'], lang)}</p></li>"""
        for n, hv in HERO_VARIANTS.items())
    html = head(lang, "Hero options", "Hero design options for review.", path, '<meta name="robots" content="noindex">')
    html += header(lang, "", path)
    html += f"""<section class="wrap page-head">
  <h1>{'חמש אפשרויות לפתיחת דף הבית' if lang == 'he' else 'Five options for the home page opening'}</h1>
  <p class="lead">{'כל אפשרות היא דף הבית המלא עם פתיחה אחרת. הטקסט זהה; רק הקומפוזיציה משתנה.' if lang == 'he' else 'Each option is the full home page with a different opening. Same copy, different composition.'}</p>
</section>
<section class="wrap prose" style="padding-bottom:var(--section)">
  <ol class="hero-list">{items}</ol>
  <p><a class="link" href="{px}/">{'הגרסה הנוכחית' if lang == 'he' else 'Current version'}</a></p>
</section>
"""
    html += footer(lang, path)
    write(path, html)


def page_home(lang, variant=0):
    t = T[lang]
    px = pfx(lang)
    path = px + "/" if not variant else f"{px}/hero/{variant}/"
    marketing = [p for p in PROJECTS if p["group"] == "marketing"]
    planning = [p for p in PROJECTS if p["group"] == "planning"]
    done = [p for p in PROJECTS if p["group"] == "done"]
    steps = "".join(f"<li>{s}</li>" for s in v(FIRST_STEP, lang)[:4])
    hv = HERO_VARIANTS.get(variant, {"img": "hero", "sizes": "(max-width:900px) 92vw, 52vw"})
    extra = preload(hv["img"], hv["sizes"]) + ('\n<meta name="robots" content="noindex">' if variant else "")
    html = head(lang, t["brand"], t["site_desc"], px + "/", extra)
    html += header(lang, px + "/", px + "/")
    html += hero_html(lang, variant) + f"""

<section class="section" id="projects">
  <div class="wrap">
    <div class="sec-head rv"><h2>{t['projects_h2']}</h2><a class="link" href="{px}/projects/">{t['cta_projects']}</a></div>
    <div class="group">
      <div class="group-head"><h3>{t['groups']['marketing'][0]}</h3><span class="note">{t['groups']['marketing'][1]}</span></div>
      {cards(marketing, 2, lang)}
    </div>
    <div class="group">
      <div class="group-head"><h3>{t['groups']['planning'][0]}</h3><a class="note link" href="{px}/projects/#planning">{t['more_projects'].format(n=len(planning) - 4)}</a></div>
      {cards(planning[:4], 4, lang)}
    </div>
    <div class="group">
      <div class="group-head"><h3>{t['groups']['done'][0]}</h3><span class="note">{t['groups']['done'][1]}</span></div>
      {cards(done, 4, lang)}
    </div>
  </div>
</section>

<section class="bleed rv-img">
  <figure>
    <div class="frame">{picture("hoshea", t['about_caption'], "100vw")}</div>
    <figcaption class="wrap">{t['about_caption']}</figcaption>
  </figure>
  <div class="wrap bleed-text rv">
    <h2>{t['about_h2']}</h2>
    <p>{t['about_p']}</p>
    <p><a class="link" href="{px}/about/">{t['about_link']}</a></p>
  </div>
</section>

<section class="section rule">
  <div class="wrap">
    <div class="sec-head rv"><h2>{t['spec_h2']}</h2></div>
    <div class="rows">{rows(v(SPECIALTIES, lang))}</div>
  </div>
</section>

<section class="band band--navy statement">
  <div class="wrap grid">
    <div class="statement-text rv">
      <h2>{t['statement_h2']}</h2>
      <p>{t['statement_p1']}</p>
      <p>{t['statement_p2']}</p>
      <div class="cta-row"><a class="btn btn--light" href="{px}/contact/">{t['cta_contact']}</a><a class="link link--light" style="align-self:center" href="{px}/how-we-start/">{t['cta_steps']}</a></div>
    </div>
    <div class="statement-aside rv">
      <ol>{steps}</ol>
    </div>
  </div>
</section>

{contact_section(lang)}
"""
    html += footer(lang, px + "/")
    write(path, html)


def page_projects(lang):
    t = T[lang]
    px = pfx(lang)
    path = px + "/projects/"
    html = head(lang, t["projects"], t["projects_lead"], path)
    html += header(lang, path, path)
    html += f"""<section class="wrap page-head">
  {crumbs(lang, (t['projects'], None))}
  <h1>{t['projects_h1']}</h1>
  <p class="lead">{t['projects_lead']}</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  {project_groups(lang, {"marketing": 2, "planning": 4, "done": 4}, level="h2")}
</section>
{contact_section(lang)}
"""
    html += footer(lang, path)
    write(path, html)


def page_project(p, lang):
    t = T[lang]
    px = pfx(lang)
    path = f"{px}/projects/{p['slug']}/"
    name, city = v(p["name"], lang), v(p["city"], lang)
    title = f"{name}, {city}"
    html = head(lang, title, v(p["short"], lang), path, preload(p["img"], "(max-width:1280px) 92vw, 1184px"), og_image=f"{p['img']}-1200")
    html += header(lang, px + "/projects/", path)

    facts = [(t["p_type"], v(p["type"], lang)), (t["p_city"], place(p, lang))]
    if p.get("floors"):
        facts.append((t["p_floors"], v(p["floors"], lang)))
    if p.get("units"):
        facts.append((t["p_units"], v(p["units"], lang)))
    if p.get("shops"):
        facts.append((t["p_shops"], f"{v(p['shops'], lang)} {t['p_shops_unit']}"))
    facts.append((t["p_status"], v(p["status"], lang)))
    spec = "".join(f"<div><dt>{k}</dt><dd>{esc(val)}</dd></div>" for k, val in facts)
    body = "".join(f"<p>{esc(d)}</p>" for d in v(p["desc"], lang))

    same = [q for q in PROJECTS if q is not p and q["group"] == p["group"]]
    rest = [q for q in PROJECTS if q is not p and q["group"] != p["group"]]
    others = (same + rest)[:3]

    ext = ""

    extra_fig = ""
    if p.get("extra_img"):
        extra_fig = f"""<figure class="rv-img extra-fig"><div class="frame">{picture(p['extra_img'], f"{name}, {city}", "(max-width:900px) 92vw, 58vw")}</div></figure>"""

    rich_html = ""
    r = RICH.get(p["slug"])
    if r:
        pdf_dir = f"/assets/pdf/{p['slug']}"
        has_notes = any(row.get("note") for row in r["rows"])
        thead = list(v(r["head"], lang)) + ([t["m_notes"]] if has_notes else []) + [t["m_plan"]]
        trs = ""
        for row in r["rows"]:
            cells = "".join(f"<td>{esc(c)}</td>" for c in v(row["cells"], lang))
            if has_notes:
                n = v(row["note"], lang) if row.get("note") else ""
                cells += f'<td>{"<span class=tag>" + esc(n) + "</span>" if n else ""}</td>'
            plan = (f'<a class="pdf" href="{pdf_dir}/{row["pdf"]}.pdf" download aria-label="{t["m_pdf"]}, {t["m_pdf_label"]}: {esc(v(row["cells"], lang)[0])}">{t["m_pdf"]}</a>'
                    if row.get("pdf") else "")
            cells += f"<td>{plan}</td>"
            sold = f' <span class="sold-tag">{SOLD[lang]}</span>' if row.get("sold") else ""
            cells = cells.replace("</td>", sold + "</td>", 1)
            trs += f'<tr class="{"sold" if row.get("sold") else ""}">{cells}</tr>'
        # mobile accordion (desktop keeps the table)
        heads = list(v(r["head"], lang))
        cards_html = ""
        for row in r["rows"]:
            cells = list(v(row["cells"], lang))
            key_parts = [c for c in cells[2:4]] if len(cells) >= 4 else cells[1:]
            rest = [(heads[i], cells[i]) for i in range(1, len(cells)) if i not in (2, 3)] if len(cells) >= 4 else []
            n = v(row["note"], lang) if row.get("note") else ""
            if n:
                rest.append((t["m_notes"], n))
            dl = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(val)}</dd></div>" for k, val in rest)
            plan = (f'<a class="pdf" href="{pdf_dir}/{row["pdf"]}.pdf" download>{t["m_pdf"]} · {t["m_pdf_label"]}</a>' if row.get("pdf") else "")
            sold = f'<span class="sold-tag">{SOLD[lang]}</span>' if row.get("sold") else ""
            cards_html += f"""<details class="apt{' sold' if row.get('sold') else ''}">
  <summary><span class="apt-name">{esc(cells[0])}{sold}</span><span class="apt-key">{esc(' · '.join(key_parts))}</span></summary>
  <div class="apt-body"><dl>{dl}</dl>{plan}</div>
</details>"""
        rich_html += f"""
<section class="wrap section rule apts-wrap apts-v3" id="apts">
  <div class="sec-head rv"><h2>{t['m_apts']}</h2></div>
  <p class="rv" style="margin-top:-16px;margin-bottom:24px">{v(r['note'], lang)}</p>
  <p class="table-hint">{t['m_scroll_hint']}</p>
  <div class="table-wrap"><table class="apts">
    <thead><tr>{"".join(f"<th>{h}</th>" for h in thead)}</tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
  <div class="apts-cards">{cards_html}</div>
  {'<p class="notice">' + t['m_notice'] + '</p>' if r.get('sale_notice') else ''}
</section>"""
        if r.get("tours"):
            rich_html += f"""
<section class="wrap section rule">
  <div class="sec-head rv"><h2>{t['m_tours']}</h2><span class="small muted">{t['m_tours_note']}</span></div>
  <div class="grid tours">
    <div class="tour rv-img" data-embed="{MARSHALL_PANORAMA}" data-title="{t['m_pano']}">
      <div class="frame">{picture("apt-8", t['m_pano'], "(max-width:900px) 92vw, 48vw")}<button type="button" class="btn btn--light tour-open">{t['m_pano_btn']}</button></div>
      <h3>{t['m_pano']}</h3>
      <p class="small muted">{t['m_pano_p']} <a class="link" href="{MARSHALL_PANORAMA}" target="_blank" rel="noopener">{t['m_ext_open']}</a></p>
    </div>
    <div class="tour rv-img" data-embed="{MARSHALL_3D}" data-title="{t['m_3d']}">
      <div class="frame">{picture("apt-4", t['m_3d'], "(max-width:900px) 92vw, 48vw")}<button type="button" class="btn btn--light tour-open">{t['m_3d_btn']}</button></div>
      <h3>{t['m_3d']}</h3>
      <p class="small muted">{t['m_3d_p']} <a class="link" href="{MARSHALL_3D}" target="_blank" rel="noopener">{t['m_ext_open']}</a></p>
    </div>
  </div>
</section>"""
        if r.get("gallery"):
            figs = "".join(
                f'<figure class="rv-img {w}"><div class="frame">{picture(img, f"{name}: {t["m_gallery"]} {i + 1}", "(max-width:640px) 92vw, 48vw")}</div></figure>'
                for i, (img, w) in enumerate(r["gallery"]))
            rich_html += f"""
<section class="wrap section rule">
  <div class="sec-head rv"><h2>{t['m_gallery']}</h2><span class="small muted">{t['m_gallery_note']}</span></div>
  <div class="gallery">{figs}</div>
</section>"""
        if r.get("spec"):
            groups = ""
            for title, items in v(r["spec"], lang):
                groups += (f"<h3>{title}</h3>" if title else "") + "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
            people = "".join(f'<div><p class="role">{role}</p><h3>{who}</h3><p class="small muted">{txt}</p></div>' for role, who, txt in v(r["people"], lang))
            rich_html += f"""
<section class="wrap section rule">
  <div class="grid">
    <div class="proj-body prose rv">
      <h2 style="margin-top:0">{t['m_spec']}</h2>
      {groups}
      {'<p class="notice">' + t['m_spec_note'] + '</p>' if r.get('spec_note') else ''}
    </div>
    <div class="proj-side rv">
      <h2 class="side-h">{t['m_team']}</h2>
      <div class="people">{people}</div>
    </div>
  </div>
</section>"""

    html += f"""<section class="wrap page-head">
  {crumbs(lang, (t['projects'], px + '/projects/'), (name, None))}
  <p class="meta">{esc(v(p['status'], lang))}. {esc(v(p['type'], lang))}</p>
  <h1>{esc(name)}, {esc(city)}</h1>
  <p class="lead">{esc(v(p['short'], lang))}</p>
</section>
<section class="wrap proj-hero">
  <figure>
    <div class="frame">{picture(p['img'], f"{name}, {city}", "(max-width:1280px) 92vw, 1184px", eager=True)}</div>
    <figcaption>{t['p_render']}</figcaption>
  </figure>
</section>
<section class="wrap section">
  <div class="grid">
    <div class="proj-body prose rv">
      <h2 style="margin-top:0">{t['p_about']}</h2>
      {body}
      {ext}
      {extra_fig}
    </div>
    <aside class="proj-side rv">
      <dl class="spec">{spec}</dl>
      <div class="cta-row"><a class="btn" href="{px}/contact/?project={p['slug']}">{t['cta_contact']}</a></div>
      <p class="small muted" style="margin-top:14px">{t['p_or_call']} <a class="link" href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a></p>
    </aside>
  </div>
</section>
{rich_html}
<section class="wrap section rule">
  <div class="sec-head rv"><h2>{t['p_more']}</h2><a class="link" href="{px}/projects/">{t['cta_projects']}</a></div>
  {cards(others, 3, lang)}
</section>
{contact_section(lang)}
"""
    html += footer(lang, path)
    write(path, html)


def page_about(lang):
    t = T[lang]
    px = pfx(lang)
    path = px + "/about/"
    body = "".join(f"<p>{x}</p>" for x in t["about_body"])
    html = head(lang, t["about_title"], t["about_desc"], path)
    html += header(lang, path, path)
    html += f"""<section class="wrap page-head">
  {crumbs(lang, (t['about'], None))}
  <h1>{t['about_h1']}</h1>
  <p class="lead">{t['about_lead']}</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  <div class="grid split">
    <div class="split-text prose rv">{body}</div>
    <div class="split-media rv-img">
      <figure>
        <div class="frame" style="aspect-ratio:3/2">{picture("rothschild", t['about_caption2'], "(max-width:900px) 92vw, 48vw")}</div>
        <figcaption>{t['about_caption2']}</figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="bleed rv-img">
  <figure>
    <div class="frame">{picture("pinsker", t['about_caption3'], "100vw")}</div>
    <figcaption class="wrap">{t['about_caption3']}</figcaption>
  </figure>
  <div class="wrap bleed-text rv">
    <h2>{t['about_mgmt_h2']}</h2>
    <p class="lead">{t['about_mgmt_lead']}</p>
    <p>{t['about_mgmt_p']}</p>
  </div>
</section>
<section class="section rule">
  <div class="wrap">
    <div class="sec-head rv"><h2>{t['spec_h2']}</h2></div>
    <div class="rows">{rows(v(SPECIALTIES, lang))}</div>
  </div>
</section>
<section class="section rule">
  <div class="wrap">
    <div class="sec-head rv"><h2>{t['group_h2']}</h2></div>
    <div class="rows">{rows(v(GROUP_COMPANIES, lang))}</div>
  </div>
</section>
{contact_section(lang)}
"""
    html += footer(lang, path)
    write(path, html)


def page_how(lang):
    t = T[lang]
    px = pfx(lang)
    path = px + "/how-we-start/"
    steps = "".join(f"<li>{s}</li>" for s in v(FIRST_STEP, lang))
    body = "".join(f"<p>{x}</p>" for x in t["how_body"])
    side = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in t["how_side"])
    html = head(lang, t["how_title"], t["how_desc"], path)
    html += header(lang, path, path)
    html += f"""<section class="wrap page-head">
  {crumbs(lang, (t['how'], None))}
  <h1>{t['how_h1']}</h1>
  <p class="lead">{t['how_lead']}</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  <div class="grid split">
    <div class="split-text prose rv">{body}</div>
    <div class="split-media rv-img">
      <figure>
        <div class="frame" style="aspect-ratio:3/2">{picture("herut", t['how_caption'], "(max-width:900px) 92vw, 48vw")}</div>
        <figcaption>{t['how_caption']}</figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="section rule">
  <div class="wrap grid">
    <div class="proj-body prose rv">
      <h2 style="margin-top:0">{t['how_step_h2']}</h2>
      <p>{t['how_step_p']}</p>
      <ol>{steps}</ol>
      <p style="margin-top:24px">{t['how_after']}</p>
      <p class="small muted">{t['how_small']}</p>
    </div>
    <aside class="proj-side rv">
      <dl class="spec">{side}</dl>
      <p style="margin-top:22px">{t['how_important']}</p>
      <div class="cta-row"><a class="btn" href="{px}/contact/">{t['cta_contact']}</a></div>
    </aside>
  </div>
</section>
{contact_section(lang)}
"""
    html += footer(lang, path)
    write(path, html)


def page_contact(lang):
    t = T[lang]
    px = pfx(lang)
    path = px + "/contact/"
    html = head(lang, t["contact_title"], t["contact_desc"], path)
    html += header(lang, path, path)
    html += f"""<section class="wrap page-head">
  {crumbs(lang, (t['contact'], None))}
  <h1>{t['contact_h1']}</h1>
  <p class="lead">{t['contact_page_lead']}</p>
</section>
<section class="wrap" style="padding-bottom:var(--section)">
  <div class="grid">
    <div class="contact-info rv">
      <dl class="dl" style="margin-top:0">
        <div><dt>{t['phone']}</dt><dd><a href="tel:{PHONE_TEL}" dir="ltr">{PHONE}</a></dd></div>
        <div><dt>{t['email']}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>{t['contact_address_label']}</dt><dd>{t['address']}<br><a class="small" href="{MAPS}" target="_blank" rel="noopener">{t['maps']}</a></dd></div>
        <div><dt>{t['facebook']}</dt><dd><a href="{FACEBOOK}" target="_blank" rel="noopener">facebook.com/keremltd</a></dd></div>
      </dl>
    </div>
    <div class="contact-form rv">{contact_form(lang)}</div>
  </div>
</section>
"""
    html += footer(lang, path)
    write(path, html)


ACCESSIBILITY = {
    "he": """<p>אנו בכרם יזמות והתחדשות עירונית משקיעים ככל שניתן כדי לספק לכל לקוחותינו שירות שוויוני ונגיש, ולאפשר חוויית גלישה נוחה לכלל האוכלוסייה, לרבות אנשים עם מוגבלויות, בהתאם לחוק שוויון זכויות לאנשים עם מוגבלות.</p>
  <p>באתר זה בוצעו התאמות נגישות על פי דרישות תקנות שוויון זכויות לאנשים עם מוגבלות (התאמות נגישות לשירות), התשע״ג-2013, בצורה קפדנית ככל שניתן. ההתאמות בוצעו על פי המלצות התקן הישראלי (ת״י 5568) לנגישות תכנים באינטרנט ברמת AA ומסמך WCAG 2.0 הבינלאומי.</p>
  <h2>מידע על נגישות האתר</h2>
  <p>באתר מוטמע תפריט נגישות, הנפתח באמצעות כפתור הנגישות בתחתית המסך. התפריט כולל:</p>
  <ul><li>הגדלת טקסט והקטנת טקסט</li><li>גווני אפור</li><li>ניגודיות גבוהה וניגודיות הפוכה</li><li>רקע בהיר</li><li>הדגשת קישורים</li><li>פונט קריא</li><li>איפוס ההגדרות</li></ul>
  <p>בנוסף, האתר נבנה עם מבנה כותרות תקין, ניווט מלא באמצעות מקלדת, טקסט חלופי לתמונות, תמיכה בהעדפת הפחתת תנועה (Reduced Motion) ותגיות ARIA בתפריטים ובטפסים.</p>
  <h2>פנייה בנושא נגישות</h2>
  <p>אנו ממשיכים לפעול לשיפור נגישות האתר כחלק ממחויבותנו לאפשר לכלל האוכלוסייה לקבל שירות שווה והוגן. אם נתקלתם בבעיה כלשהי בנושא הנגישות, נשמח שתעדכנו אותנו ונעשה כל מאמץ למצוא פתרון מתאים ולטפל בבעיה בהקדם.</p>
  <p>טלפון: <a class="link" href="tel:{tel}" dir="ltr">{phone}</a><br>דוא״ל: <a class="link" href="mailto:{email}">{email}</a></p>
  <h2>פרסום הצהרת הנגישות</h2>
  <p>הצהרת הנגישות עודכנה ביום {today}.</p>""",
    "en": """<p>At Kerem we invest as much as possible in providing all our customers with equal and accessible service, and in making the site comfortable to use for everyone, including people with disabilities, in accordance with the Equal Rights for Persons with Disabilities Law.</p>
  <p>Accessibility adjustments were made to this site as strictly as possible under the Equal Rights for Persons with Disabilities Regulations (Service Accessibility Adjustments), 2013, following the Israeli Standard (SI 5568) for web content accessibility at level AA and the international WCAG 2.0 guidelines.</p>
  <h2>Site accessibility</h2>
  <p>The site includes an accessibility menu, opened with the accessibility button at the bottom of the screen. The menu includes:</p>
  <ul><li>Increase and decrease text size</li><li>Greyscale</li><li>High contrast and inverted contrast</li><li>Light background</li><li>Highlight links</li><li>Readable font</li><li>Reset settings</li></ul>
  <p>In addition, the site is built with a proper heading structure, full keyboard navigation, alternative text for images, support for the reduced motion preference and ARIA attributes in menus and forms.</p>
  <h2>Accessibility enquiries</h2>
  <p>We continue to work on improving the accessibility of the site as part of our commitment to equal and fair service. If you encounter any accessibility problem, please let us know and we will make every effort to find a suitable solution promptly.</p>
  <p>Phone: <a class="link" href="tel:{tel}" dir="ltr">{phone}</a><br>Email: <a class="link" href="mailto:{email}">{email}</a></p>
  <h2>Publication</h2>
  <p>This accessibility statement was updated on {today}.</p>""",
}

PRIVACY = {
    "he": """<p>המידע המוצג להלן נועד לעזור למשתמש להבין מה המידע הנאסף על ידי כרם יזמות והתחדשות עירונית במהלך השימוש באתר האינטרנט שהיא מנהלת ומפעילה בכתובת keremltd.co.il (להלן: ״האתר״), מה השימושים שאנו עשויים לעשות במידע ומהם הכלים הטכנולוגיים שבהם אנו עשויים לעשות שימוש באתר.</p>
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
  <p>מדיניות הפרטיות והשימוש באתר כפופים לחוקי מדינת ישראל. סמכות השיפוט הבלעדית בכל מחלוקת שתתעורר תהיה בבתי המשפט בתל אביב-יפו. בעלת האתר רשאית לשנות מדיניות זו מעת לעת ותודיע על כך באמצעות פרסום מדיניות מתוקנת באתר עם תאריך עדכון. המשך השימוש באתר לאחר עדכון יהווה הסכמה למדיניות המתוקנת.</p>
  <h2>דרכי יצירת קשר</h2>
  <p>בכל שאלה ובקשה הנוגעת למדיניות פרטיות זו, ניתן לפנות אלינו בטלפון <a class="link" href="tel:{tel}" dir="ltr">{phone}</a> או בדוא״ל <a class="link" href="mailto:{email}">{email}</a>.</p>
  <p class="small muted">תאריך עדכון: {today}</p>""",
    "en": """<p>This policy explains what information Kerem Real Estate Development and Urban Renewal collects while you use the website it operates at keremltd.co.il (the "Site"), how we may use that information, and which technologies we may use on the Site.</p>
  <p>In this policy, "user" means anyone who uses the Site in any way, including viewing, browsing or reading. "Personal information" means data relating to an identified or identifiable person. "Processing" or "use" means any operation performed on information, including receiving, collecting, storing, copying, reviewing, transferring or granting access to it.</p>
  <h2>Consent</h2>
  <p>Subject to law, using the Site constitutes your consent to providing information and to its use for the purposes set out in this policy. You are under no legal obligation to provide us with information. If you choose not to, you may not be able to use the Site and its services. Where you do provide information, you confirm that it is provided of your own free will and with your consent, and you agree to its collection, processing, use, transfer and storage in accordance with this policy.</p>
  <h2>Information we collect</h2>
  <p>In general, you can browse the Site without providing any personal information. The personal information we may collect is what you choose to give us when contacting us through the Site (such as name, email address and phone number). We may also collect analytical and statistical information about how our services are used (pages visited, links clicked and so on) and about how you connect (approximate location, IP address, browser type, language preference, landing pages, device and so on), either ourselves or through third-party services and monitoring tools such as cookies.</p>
  <h2>How we use information</h2>
  <p>We may use personal information you provide to contact you, for example to offer services we provide, to improve the quality of our services and to respond to you. Such information is disclosed to employees or service providers only to the extent necessary for contacting you and for operating, maintaining and supporting the Site. Statistical information is used to improve the Site and our services, subject to law.</p>
  <h2>Cookies</h2>
  <p>This Site does not set tracking cookies and does not use third-party analytics tools. The accessibility menu stores the preferences you choose (such as text size or contrast) in your browser's local storage only. This information is not sent to us and does not identify you.</p>
  <h2>Sharing with third parties</h2>
  <ul>
    <li>Information may be shared with third parties in accordance with this policy, proportionately and for the defined purposes, and limited to what is relevant for that purpose.</li>
    <li>We may share information with third parties that provide us with services such as information security, IT, data storage (including the form delivery service), legal advice and other professional services.</li>
    <li>We may also disclose information where a court order requires it; in disputes or legal proceedings between you and us; in the event of a transfer of ownership, merger or change of control; and where we believe disclosure is needed to prevent or reduce harm.</li>
  </ul>
  <h2>Security and limitation of liability</h2>
  <p>We take reasonable, customary technical and physical measures to protect the privacy and security of information. However, transmission over the internet cannot be completely secure, and we do not guarantee that the Site will operate without interruption or that the Site, our databases and the data collected will be entirely immune from unauthorised access. Use of the Site is conditional on your agreement that information is provided at your own risk. If you suspect a security breach, please contact us as soon as possible.</p>
  <p>The Site may contain links to other websites that are not under our control. Use of third-party sites is subject to their terms, and we accept no liability for any damage or loss arising from their use.</p>
  <h2>Retention</h2>
  <p>We keep information for as long as needed for the purposes set out in this policy, unless a longer retention period is required by law.</p>
  <h2>Information about third parties</h2>
  <p>If you provide us with personal information about third parties, you must ensure that you have obtained the consent required by law.</p>
  <h2>Your rights</h2>
  <p>Subject to law, you may review personal information about you held in our databases and ask us to correct or delete it if it is inaccurate, incomplete, unclear or out of date. You may also ask us to delete personal information that was obtained or collected contrary to law, or that is no longer needed for the purposes for which it was collected. To exercise these rights, contact us through the <a class="link" href="/en/contact/">contact page</a>.</p>
  <h2>General</h2>
  <p>This policy and use of the Site are governed by the laws of the State of Israel. The courts of Tel Aviv-Jaffa have exclusive jurisdiction over any dispute. The Site owner may change this policy from time to time and will publish an updated policy on the Site with a revision date. Continued use of the Site after an update constitutes acceptance of the revised policy.</p>
  <h2>Contact</h2>
  <p>For any question or request about this policy, call <a class="link" href="tel:{tel}" dir="ltr">{phone}</a> or email <a class="link" href="mailto:{email}">{email}</a>.</p>
  <p class="small muted">Last updated: {today}</p>""",
}


def page_legal(lang, key, title_key, desc_key, body_map):
    t = T[lang]
    px = pfx(lang)
    path = f"{px}/{key}/"
    body = body_map[lang].format(tel=PHONE_TEL, phone=PHONE, email=EMAIL, today=STATEMENT_DATE)
    html = head(lang, t[title_key], t[desc_key], path)
    html += header(lang, path, path)
    html += f"""<section class="wrap page-head">
  {crumbs(lang, (t[title_key], None))}
  <h1>{t[title_key]}</h1>
</section>
<section class="wrap prose" style="padding-bottom:var(--section)">
  {body}
</section>
"""
    html += footer(lang, path)
    write(path, html)


def page_404(lang):
    t = T[lang]
    px = pfx(lang)
    path = px + "/404.html"
    html = head(lang, t["nf_title"], t["nf_desc"], path)
    html += header(lang, "", path)
    html += f"""<section class="wrap not-found">
  <div>
    <span class="eyebrow">404</span>
    <h1>{t['nf_title']}</h1>
    <p class="lead">{t['nf_lead']}</p>
    <div class="cta-row" style="justify-content:center"><a class="btn" href="{px}/">{t['cta_home']}</a><a class="btn btn--ghost" href="{px}/projects/">{t['cta_projects']}</a></div>
  </div>
</section>
"""
    html += footer(lang, path)
    write(path, html)


def sitemap():
    urls = []
    for lang in ("he", "en"):
        px = pfx(lang)
        urls += [px + "/", px + "/about/", px + "/projects/", px + "/how-we-start/", px + "/contact/", px + "/accessibility/", px + "/privacy/"]
        urls += [f"{px}/projects/{p['slug']}/" for p in PROJECTS if not p.get("redirect")]
    today = date.today().isoformat()
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
    xml += "</urlset>\n"
    with open(os.path.join(WWW, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(xml)
    with open(os.path.join(WWW, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    # Cloudflare Pages redirects: projects with a dedicated site send visitors there directly
    lines = [f"{pfx(lang)}/projects/{p['slug']}/ {p['redirect']} 302" for p in PROJECTS if p.get("redirect") for lang in ("he", "en")]
    with open(os.path.join(WWW, "_redirects"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def main():
    for lang in ("he", "en"):
        page_home(lang)
        for n in HERO_VARIANTS:
            page_home(lang, n)
        page_hero_index(lang)
        page_projects(lang)
        for p in PROJECTS:
            if not p.get("redirect"):
                page_project(p, lang)
        page_about(lang)
        page_how(lang)
        page_contact(lang)
        page_legal(lang, "accessibility", "a11y_title", "a11y_desc", ACCESSIBILITY)
        page_legal(lang, "privacy", "privacy_title", "privacy_desc", PRIVACY)
        page_404(lang)
    sitemap()


if __name__ == "__main__":
    main()
