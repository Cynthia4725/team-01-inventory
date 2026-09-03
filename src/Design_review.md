# Design Review

## การตรวจสอบตามเกณฑ์ 4 ด้าน (Design & Code Quality)

1. **Correctness (ความถูกต้องตาม Acceptance Criteria)**
   - ฟังก์ชันใน `inventory.py` รองรับ Business Rules ครบถ้วน:
     - กรอง RGB / Sync System ได้ตรงเงื่อนไข (US-01)
     - ป้องกันการขาย Serial ซ้ำ และลด stockQuantity ลง 1 ชิ้นทันที (US-02)
     - กรองเฉพาะ RAM Kit ที่ >= 64GB (US-04)
     - แสดง Timing, Voltage, ชิป RAM หากไม่มีให้แสดง "ไม่มีข้อมูล" (US-05)

2. **Readability & Architecture (ความสะอาดและการแยกสถาปัตยกรรม)**
   - แยก Business Logic (`inventory.py`) ออกจาก UI/CLI (`main.py`) ตามข้อกำหนด Design Notes 9.1
   - ระบบ Sync System เก็บเป็น List รองรับการขยายโดยไม่ต้องแก้โค้ดหลัก (Design Notes 9.2)

3. **Edge Cases Handled**
   - Serial Number ไม่มีในระบบ -> ปฏิเสธรายการ
   - Serial Number ถูกขายไปแล้ว (SOLD) -> แจ้งเตือนห้ามขายซ้ำ
   - ข้อมูลสินค้าไม่มี Tech Specs -> แสดง "ไม่มีข้อมูล" ไม่ throw exception

4. **Maintainability**
   - Data Source แยกเก็บที่ `items.json` ทำให้ทดสอบง่ายและเปลี่ยนไปใช้ DB ได้สะดวกในอนาคต
