# AI Iteration Log

## Iteration 1: Data Model & Project Structure
- **Prompt:** สร้าง Class Diagram และโครงสร้าง JSON สำหรับเก็บข้อมูล RAM และ Serial Number ตาม Spec
- **Output:** Mermaid diagram และ items.json
- **Human Review & Edit:** ปรับเพิ่ม field `capacityGb` เป็น integer เพื่อให้เขียน logic เปรียบเทียบ `>= 64GB` ได้แม่นยำ

## Iteration 2: Core Inventory Service
- **Prompt:** สร้าง inventory.py เพื่อจัดการค้นหา RGB และตัดสต็อกด้วย Serial Number
- **Output:** เมธอด `search_rgb_ram` และ `sell_by_serial`
- **Human Review & Edit:** ตรวจสอบ edge case เรื่อง status "SOLD" และเพิ่มการลดจำนวน `stockQuantity` ควบคู่กันไป
