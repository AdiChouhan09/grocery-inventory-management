from typing import List, Optional


class Item:
    def __init__(self, item_id: int, name: str, quantity: int, price: float):
        self.item_id = int(item_id)
        self.name = str(name)
        self.quantity = int(quantity)
        self.price = float(price)

    def display(self) -> None:
        print(f"ID: {self.item_id}, Name: {self.name}, Qty: {self.quantity}, Price: {self.price:.2f}")


class Inventory:
    def __init__(self):
        self.items: List[Item] = []

    # ---------- Core ops ----------
    def insert_item(self, item: Item) -> bool:
        """Insert only if the item_id is unique."""
        if any(it.item_id == item.item_id for it in self.items):
            print("Insert failed: duplicate item_id")
            return False
        self.items.append(item)
        print("Item added successfully")
        return True

    def delete_item(self, item_id: int) -> bool:
        for i in range(len(self.items)):
            if self.items[i].item_id == item_id:
                del self.items[i]
                print("Item deleted successfully")
                return True
        print("Item not found")
        return False

    # ---------- Search ----------
    def search_item(self, key) -> Optional[Item]:
        """Search by ID (int/str) or by name (case-insensitive)."""
        kstr = str(key).strip().lower()
        for it in self.items:
            if str(it.item_id) == kstr or it.name.lower() == kstr:
                it.display()
                return it
        print("Item not found")
        return None

    # ---------- Inventory adjustments ----------
    def restock(self, item_id: int, qty_added: int, new_price: Optional[float] = None) -> bool:
        if qty_added <= 0:
            print("Invalid restock quantity")
            return False
        for it in self.items:
            if it.item_id == item_id:
                it.quantity += qty_added
                if new_price is not None:
                    if new_price < 0:
                        print("Invalid price")
                        return False
                    it.price = float(new_price)
                print("Restocked successfully")
                return True
        print("Item not found")
        return False

    def sell(self, item_id: int, qty_sold: int) -> bool:
        if qty_sold <= 0:
            print("Invalid sell quantity")
            return False
        for it in self.items:
            if it.item_id == item_id:
                if it.quantity < qty_sold:
                    print("Insufficient stock")
                    return False
                it.quantity -= qty_sold
                print("Sale recorded")
                return True
        print("Item not found")
        return False

    def update_price(self, item_id: int, new_price: float) -> bool:
        if new_price < 0:
            print("Invalid price")
            return False
        for it in self.items:
            if it.item_id == item_id:
                it.price = float(new_price)
                print("Price updated")
                return True
        print("Item not found")
        return False

    # ---------- Reports / Views ----------
    def price_quantity_table(self):
        n = len(self.items)
        table = [[self.items[i].price, self.items[i].quantity] for i in range(n)]

        print("\nRow-Major Order:")
        for row in table:
            print(row)

        print("\nColumn-Major Order:")
        for col in range(2):
            col_values = []
            for row in range(n):
                col_values.append(table[row][col])
            print(col_values)

        return table

    def sparse_representation(self, threshold: int = 2):
        sparse = []
        for i in range(len(self.items)):
            if self.items[i].quantity <= threshold:
                sparse.append((i, self.items[i].item_id, self.items[i].quantity))
        print(f"\nSparse Representation (index, item_id, quantity) with threshold <= {threshold}:")
        for row in sparse:
            print(row)
        return sparse

    def low_stock_report(self, threshold: int) -> List[Item]:
        out = [it for it in self.items if it.quantity <= threshold]
        out.sort(key=lambda x: (x.quantity, x.name.lower()))
        print(f"\nLow-Stock (<= {threshold}):")
        for it in out:
            it.display()
        return out

    def summary(self) -> None:
        total_skus = len(self.items)
        total_units = sum(it.quantity for it in self.items)
        total_value = sum(it.quantity * it.price for it in self.items)
        print("\nSummary:")
        print(f"Total SKUs: {total_skus}")
        print(f"Total Units: {total_units}")
        print(f"Inventory Value: {total_value:.2f}")


# ---------- Quick demo ----------
if __name__ == "__main__":
    store = Inventory()

    item1 = Item(101, "Milk", 10, 40.5)
    item2 = Item(102, "Bread", 2, 25.0)
    item3 = Item(103, "Eggs", 1, 6.0)

    store.insert_item(item1)
    store.insert_item(item2)
    store.insert_item(item3)
    store.insert_item(Item(101, "DuplicateMilk", 5, 41.0))  # duplicate id -> rejected

    print("\nALL Items:")
    for it in store.items:
        it.display()

    print("\nSearch Result:")
    store.search_item(102)
    store.search_item("eggs")

    store.restock(103, 5, new_price=6.5)
    store.sell(101, 3)
    store.update_price(102, 27.0)

    store.delete_item(101)

    store.price_quantity_table()
    store.sparse_representation(threshold=2)
    store.low_stock_report(threshold=3)
    store.summary()
