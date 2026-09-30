# การเปรียบเทียบ Prompt แบบสั้น กับ Prompt ที่มี Context

## รอบที่ 1: Prompt สั้นๆ
**Prompt ที่ใช้:**
ช่วยเขียนเมธอด sell_many(orders: dict[str, int]) สำหรับขายสินค้าหลายรายการพร้อมกันในคลังสินค้าให้หน่อย ใช้ภาษา Python

**ผลลัพธ์ที่ AI ให้มา:**
ได้ ถ้า orders เป็นรูปแบบ {ชื่อสินค้า: จำนวนที่ขาย} เมธอด sell_many() สามารถตรวจสอบสินค้าทุกรายการก่อน แล้วค่อยตัดสต๊อกทีเดียว เพื่อป้องกันกรณีขายบางรายการสำเร็จแต่บางรายการไม่สำเร็จ
def sell_many(self, orders: dict[str, int]):
    # ตรวจสอบรายการทั้งหมดก่อน
    for product, quantity in orders.items():
        if product not in self.stock:
            raise ValueError(f"ไม่พบสินค้า: {product}")

        if quantity <= 0:
            raise ValueError(f"จำนวนสินค้าต้องมากกว่า 0: {product}")

        if self.stock[product] < quantity:
            raise ValueError(
                f"สินค้า {product} มีไม่พอ "
                f"(เหลือ {self.stock[product]}, ต้องการ {quantity})"
            )

    # ถ้าทุกรายการผ่าน จึงค่อยตัดสต๊อก
    for product, quantity in orders.items():
        self.stock[product] -= quantity

    return True

ตัวอย่าง ถ้าคลังมี:
self.stock = {
    "RAM 16GB": 10,
    "SSD 1TB": 5,
    "CPU": 3
}

ขายพร้อมกัน:

orders = {
    "RAM 16GB": 2,
    "SSD 1TB": 1,
    "CPU": 1
}

inventory.sell_many(orders)

ผลลัพธ์:

{
    "RAM 16GB": 8,
    "SSD 1TB": 4,
    "CPU": 2
}

จุดสำคัญคือแยกเป็น 2 รอบ: รอบแรกตรวจสอบทุกสินค้า → รอบสองค่อยหักสต๊อก ดังนั้นถ้า SSD 1TB มีไม่พอ จะไม่มีรายการไหนถูกหักสต๊อกเลย.

---

## รอบที่ 2: Prompt ที่แนบ Context ครบถ้วน
**Prompt ที่ใช้:**
(เดี๋ยวเอามาเติม)

**ผลลัพธ์ที่ AI ให้มา:**
(เดี๋ยวเอามาเติม)

---

## สรุปข้อแตกต่าง
(เดี๋ยวเอามาเติม)
