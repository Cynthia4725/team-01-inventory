from inventory import InventoryService

def print_table(products):
    if not products:
        print(">> ไม่พบสินค้าที่ตรงกับเงื่อนไข <<")
        return
    print("-" * 75)
    print(f"{'รหัส':<10} | {'ชื่อสินค้า':<32} | {'ความจุ':<6} | {'RGB':<5} | {'คงเหลือ'}")
    print("-" * 75)
    for p in products:
        rgb_tag = "มี" if p.get("hasRgb") else "ไม่มี"
        print(f"{p['productId']:<10} | {p['productName'][:30]:<32} | {p['capacityGb']}GB   | {rgb_tag:<5} | {p['stockQuantity']} ชิ้น")
    print("-" * 75)

def main():
    service = InventoryService()
    while True:
        print("\n=========================================")
        print("   ระบบจัดการและค้นหา RAM (Command Line)   ")
        print("=========================================")
        print("1. [US-01] กรองหา RAM ที่มีไฟ RGB และระบบ Sync")
        print("2. [US-02] สแกน Serial Number เพื่อตัดสต็อกหน้าร้าน (POS)")
        print("3. [US-04] กรอง RAM แบบ Kit (ความจุ 64GB ขึ้นไป)")
        print("4. [US-05] ดูข้อมูลเชิงลึก (Advanced Tech Specs)")
        print("0. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (0-4): ").strip()

        if choice == "1":
            print("\n--- ค้นหา RAM RGB ---")
            sync = input("ระบุระบบ Sync ที่ต้องการ (เช่น ASUS Aura Sync / กด Enter หากไม่ระบุ): ").strip()
            brand = input("ระบุแบรนด์ (เช่น Corsair, ASUS / กด Enter หากไม่ระบุ): ").strip()
            results = service.search_rgb_ram(sync_system=sync if sync else None, brand=brand if brand else None)
            print_table(results)

        elif choice == "2":
            print("\n--- สแกน Serial Number หน้าร้าน ---")
            sn = input("กรุณายิง/พิมพ์ Serial Number: ").strip()
            confirm = input(f"ยืนยันการขาย Serial '{sn}' หรือไม่? (y/n): ").strip().lower()
            if confirm == "y":
                success, msg = service.sell_by_serial(sn)
                print("ผลการทำงาน:", msg)
            else:
                print("ยกเลิกรายการขาย")

        elif choice == "3":
            print("\n--- รายการ RAM แบบ Kit ความจุรวม >= 64GB ---")
            results = service.filter_kits(min_capacity_gb=64)
            print_table(results)

        elif choice == "4":
            print("\n--- ข้อมูลทางเทคนิคเชิงลึก (Advanced Tech Specs) ---")
            pid = input("ระบุ Product ID (เช่น RAM-001): ").strip()
            specs = service.get_advanced_specs(pid)
            if not specs:
                print(">> ไม่พบสินค้ารหัสนี้ <<")
            else:
                print("\n" + "=" * 45)
                print(f"สินค้า: {specs['productName']}")
                print("=" * 45)
                print(f"Timing         : {specs['timing']}")
                print(f"Voltage        : {specs['voltage']}")
                print(f"Memory Chip Mfr: {specs['chipManufacturer']}")
                print(f"Memory Chip Typ: {specs['chipType']}")
                print(f"Speed          : {specs['speed']}")
                print(f"Package Type   : {specs['package']}")
                print("=" * 45)

        elif choice == "0":
            print("ปิดโปรแกรม สวัสดีครับ")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")

if __name__ == "__main__":
    main()
