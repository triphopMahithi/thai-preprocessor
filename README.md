# th-preprocessor

`th-preprocessor` คือไลบรารีสำหรับการเตรียมข้อมูลภาษาไทย (Text Preprocessing)  
เหมาะสำหรับงาน **NLP (Natural Language Processing)**, การทำ Machine Learning, และการทำ Data Cleaning ให้พร้อมก่อนการวิเคราะห์หรือฝึกโมเดล

## 📌 ฟีเจอร์หลัก
- **ลบช่องว่างและตัวอักษรซ้ำ** (เช่น "ดีมากกก" → "ดีมาก")
- **ลบสัญลักษณ์พิเศษ** (เช่น อีโมจิ, HTML tags, punctuation ที่ไม่จำเป็น)
- **ตัดคำภาษาไทย** (รองรับการใช้งานร่วมกับ [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp))
- **แปลงตัวเลขไทย ↔ เลขอารบิก**
- **ลบ stopwords ภาษาไทย** เพื่อให้เหลือเฉพาะคำสำคัญ
- **รองรับการ tokenize และ stemming** สำหรับภาษาไทยและอังกฤษ

---

## 📦 การติดตั้ง

```bash
pip install th-preprocessor
