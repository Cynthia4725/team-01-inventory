import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inventory import InventoryService


def test_low_stock_all_above_threshold():
    service = InventoryService()
    service.items = [
        {"name": "RAM", "stock": 10},
        {"name": "CPU", "stock": 8}
    ]
    assert service.low_stock_items(threshold=5) == []

def test_low_stock_exactly_at_threshold():
    service = InventoryService()
    service.items = [
        {"name": "RAM", "stock": 5},
        {"name": "GPU", "stock": 10}
    ]
    result = service.low_stock_items(threshold=5)
    assert len(result) == 1
    assert result[0]["name"] == "RAM"

def test_low_stock_multiple_sorted_by_name():
    service = InventoryService()
    service.items = [
        {"name": "SSD", "stock": 2},
        {"name": "Case", "stock": 1},
        {"name": "Cable", "stock": 3}
    ]
    result = service.low_stock_items(threshold=3)
    names = [item["name"] for item in result]
    assert names == ["Cable", "Case", "SSD"]

def test_low_stock_empty_inventory():
    service = InventoryService()
    service.items = []
    assert service.low_stock_items(threshold=5) == []

def test_low_stock_threshold_zero():
    service = InventoryService()
    service.items = [
        {"name": "Mouse", "stock": 0},
        {"name": "Keyboard", "stock": 2}
    ]
    result = service.low_stock_items(threshold=0)
    assert len(result) == 1
    assert result[0]["name"] == "Mouse"

def test_low_stock_negative_threshold():
    service = InventoryService()
    service.items = [
        {"name": "Mouse", "stock": 0}
    ]
    assert service.low_stock_items(threshold=-1) == []