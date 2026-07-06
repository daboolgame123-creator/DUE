المرحلة 1 — الأساس (اكتملت تقريبًا) ✅
✅ هيكل المشروع.
✅ النماذج (Models).
✅ Readers.
✅ Pipeline.
✅ Stages.
✅ أول Detectors.
✅ Layout Models.
المرحلة 2 — Layout Engine ⭐ (الحالية)

الهدف: جعل المشروع يفهم الصفحة.

2.1 استخراج التخطيط
✅ Text Blocks
✅ Text Lines
✅ Text Spans
⬜ Font Size
⬜ Font Name
⬜ Font Flags
⬜ Bounding Boxes
⬜ Page Size
⬜ Rotation
2.2 عناصر الصفحة
⬜ Images
⬜ Drawings
⬜ Tables (استخراج أولي)
⬜ Links
⬜ Annotations
2.3 Page Layout
⬜ Header
⬜ Footer
⬜ Margins
⬜ Columns
⬜ Reading Order
المرحلة 3 — Detection Engine

الهدف: فهم أجزاء المستند.

صفحات خاصة
⬜ Cover
⬜ Title Page
⬜ Copyright
⬜ Dedication
⬜ Acknowledgment
⬜ Abstract
⬜ TOC
⬜ References
⬜ Appendix
عناصر
⬜ Chapter
⬜ Section
⬜ Subsection
⬜ Figure
⬜ Table
⬜ Caption
⬜ Footnote
المرحلة 4 — Extraction Engine

استخراج البيانات الوصفية.

⬜ Title
⬜ Subtitle
⬜ Author
⬜ Supervisors
⬜ University
⬜ College
⬜ Department
⬜ Degree
⬜ Year
⬜ Keywords
⬜ Abstract
⬜ Language
⬜ Publisher
⬜ ISBN
⬜ DOI
المرحلة 5 — Media Engine

استخراج الوسائط.

⬜ Cover Image
⬜ Embedded Images
⬜ Logos
⬜ Tables
⬜ Charts
⬜ Vector Graphics
⬜ Attachments
المرحلة 6 — Knowledge Engine

هذه من أهم المراحل.

بدل استخراج النص فقط:

University of Baghdad

يصبح:

Entity
    Type = University
    Country = Iraq

أو:

Computer Science

يصبح:

Department
Field = Computing

أي أن المعرفة تصبح كيانات وليست نصوصًا.

المرحلة 7 — Normalization

مثال:

كل هذه:

Univ. Baghdad
Baghdad University
University of Baghdad
جامعة بغداد

تصبح:

جامعة بغداد
المرحلة 8 — Inference Engine

إذا لم نجد السنة مباشرة:

يستنتجها.

إذا لم نجد اللغة:

يحسبها.

إذا وجد كلية فقط:

يستنتج الجامعة بدرجة ثقة إذا كانت معروفة.

المرحلة 9 — Confidence Engine

كل قيمة سيكون معها:

Title
Confidence = 0.99

Author
Confidence = 0.92

University
Confidence = 0.81
المرحلة 10 — Validation Engine

يتحقق من:

وجود التناقضات.
القيم الناقصة.
التكرار.
صحة التواريخ.
العلاقات بين الحقول.
المرحلة 11 — Output Engine

بدل أن يعرف المحرك كيف يعرض النتائج:

ننشئ محولات.

مثلًا:

Academic Profile

أو:

JSON

أو:

CSV

أو:

Database

كلها من نفس البيانات.

المرحلة 12 — UI

واجهة احترافية.

تبويبات:

الملف
البيانات
الصور
الجداول
البنية
السجل
الثقة
التصدير
المرحلة 13 — Search

داخل آلاف الملفات.

المرحلة 14 — Indexing

بناء فهرس سريع.

المرحلة 15 — AI

تلخيص.

تصنيف.

الإجابة عن الأسئلة.

ربط الوثائق.

المرحلة 16 — Plugins

إضافة دعم:

EPUB
DOCX
PPTX
XLSX

بدون تعديل قلب المشروع.

هناك إضافة واحدة أراها مهمة جدًا للمشروع

أقترح إدراج مرحلة مستقلة بين Layout Engine وDetection Engine اسمها:

Document Object Model (DOM)

أي بدل أن يتعامل الـ Detectors مع TextBlocks مباشرة، نبني تمثيلًا موحدًا للمستند:

Document
│
├── Pages
│
├── Sections
│
├── Paragraphs
│
├── Headings
│
├── Figures
│
├── Tables
│
└── References

هذا يشبه فكرة DOM في HTML، لكنه خاص بالمستندات. سيجعل جميع المراحل اللاحقة (الاستخراج، الاستدلال، التحقق، التصدير) تتعامل مع نموذج موحد بدل تفاصيل كل صيغة ملف.

إذا حافظنا على هذه الخارطة، فأعتقد أننا سنبني محركًا قابلًا للتوسع لسنوات دون الحاجة إلى إعادة كتابة الأساسيات.