import json
import os

DATA_FILE = "items.json"

class InventoryService:
    def __init__(self, filepath=DATA_FILE):
        self.filepath = filepath
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.filepath):
            return {"products": [], "serials": []}
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_data(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def search_rgb_ram(self, sync_system=None, brand=None):
        """US-01: กรอง RAM ตามคุณสมบัติ RGB, RGB Sync และ Brand"""
        results = []
        for p in self.data["products"]:
            if sync_system:
                if not p.get("hasRgb"):
                    continue
                sync_match = any(sync_system.lower() in s.lower() for s in p.get("rgbSyncSystems", []))
                if not sync_match:
                    continue
            if brand:
                if brand.lower() not in p.get("brand", "").lower() and brand.lower() not in p.get("productName", "").lower():
                    continue
            results.append(p)
        return results

    def sell_by_serial(self, serial_number):
        """US-02: ตัดสต็อกด้วย Serial Number"""
        serial_entry = None
        for s in self.data["serials"]:
            if s["serialNumber"] == serial_number:
                serial_entry = s
                break

        if not serial_entry:
            return False, "ไม่พบรหัส Serial Number ในระบบ"

        if serial_entry["status"] == "SOLD":
            return False, f"Serial Number {serial_number} ถูกขายและตัดสต็อกไปแล้ว ไม่สามารถขายซ้ำได้"

        # ค้นหาสินค้าเพื่อตัดสต็อก
        product = None
        for p in self.data["products"]:
            if p["productId"] == serial_entry["productId"]:
                product = p
                break

        if not product:
            return False, "ไม่พบข้อมูลสินค้าที่ตรงกับ Serial นี้"

        if product["stockQuantity"] <= 0:
            return False, "จำนวนสินค้าคงเหลือไม่เพียงพอสำหรับการตัดสต็อก"

        # ดำเนินการตัดสต็อก
        serial_entry["status"] = "SOLD"
        product["stockQuantity"] -= 1
        self._save_data()
        return True, f"ตัดสต็อกสำเร็จ: สินค้า {product['productName']} (คงเหลือ: {product['stockQuantity']})"

    def filter_kits(self, min_capacity_gb=64):
        """US-04: กรอง RAM แบบ Kit of 2 หรือ Kit of 4 ความจุรวม >= min_capacity_gb"""
        results = []
        for p in self.data["products"]:
            if p.get("packageType") == "KIT" and p.get("capacityGb", 0) >= min_capacity_gb:
                results.append(p)
        return results

    def get_advanced_specs(self, product_id):
        """US-05: แสดงข้อมูลเชิงลึก Advanced Tech Specs"""
        for p in self.data["products"]:
            if p["productId"].lower() == product_id.lower():
                return {
                    "productName": p["productName"],
                    "timing": p.get("timing", "ไม่มีข้อมูล"),
                    "voltage": p.get("voltage", "ไม่มีข้อมูล"),
                    "chipManufacturer": p.get("memoryChipManufacturer", "ไม่มีข้อมูล"),
                    "chipType": p.get("memoryChipType", "ไม่มีข้อมูล"),
                    "speed": p.get("speed", "ไม่มีข้อมูล"),
                    "package": f"{p.get('packageType')} ({p.get('moduleCount')} modules)"
                }
        return None
