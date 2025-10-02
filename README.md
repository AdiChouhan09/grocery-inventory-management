# Grocery Store Inventory Management System  

---

## 1. Problem Statement  
The assignment's main goal is to use **arrays and complexity analysis** to create an **inventory system for a grocery store**.  
By storing, updating, and evaluating information about **item names, quantities, and prices**, the system maintains item records.  

It facilitates fundamental functions such as:  
- Search  
- Sparse representation  
- Insertion  
- Deletion  
- Complexity assessment  

This project demonstrates how to use **Python or C++** to implement:  
- Arrays with one or more dimensions  
- Sparse matrices for items that are rarely restocked  
- Data organization using row-major and column-major  
- Analysis of complexity for assessing performance  

---

## 2. Features  
- **Item Storage**: Keep track of the item's name, ID, price, and quantity.  
- **CRUD Operations**: Add, remove, and look up inventory items using their ID or name.  
- **Effective Data Organization**: For price and quantity tables, use both row-major and column-major ordering.  
- **Sparse Representation**: Make storage as efficient as possible for items that are rarely restocked.  
- **Complexity Analysis**: Analyze each function's complexity in terms of time and space.  
- **Scalability**: Ability to analyze efficiency while managing expanding datasets.  

---

## 3. Implementation  

### Inventory Item ADT  
**Attributes:**  
- `ItemID` → Integer (unique identifier)  
- `ItemName` → String (name of the item)  
- `Quantity` → Integer (stock available)  
- `Price` → Float (price per unit)  

**Methods:**  
- `insertItem(data)` → Add new items to inventory  
- `deleteItem(ItemID)` → Remove items from inventory  
- `searchItem(ItemID or ItemName)` → Retrieve details of items  

---

### Inventory Management System  
**Structures:**  
- `ItemArray` → Single/multi-dimensional array storing inventory data  
- `SparseMatrix` → Stores rarely restocked items efficiently  
- `PriceQuantityTable` → Organized in row-major or column-major order  

**Methods:**  
- `addItemRecord()`  
- `removeItemRecord()`  
- `searchByItem()`  
- `managePriceQuantity()`  
- `optimizeSparseStorage()`  

---

## 4. Complexity Analysis  
Each implemented function includes **time and space complexity evaluation**:  

- **Insertion** → O(1) (amortized for arrays)  
- **Deletion** → O(n) (requires shifting elements in arrays)  
- **Search** → O(n) (linear search) / O(log n) (if sorted and binary search applied)  
- **Sparse Storage Optimization** → O(k), where *k* is the number of non-zero entries  
- **Row/Column Access** → O(1) per element  

---

## 5. How to Run
1. Clone this repository or download the .py file.
2. Open the project in PyCharm or any Python IDE.
3. Run the file with: python inventory_management.py

---

## Screenshots
<img width="1337" height="797" alt="Screenshot 2025-10-02 172239" src="https://github.com/user-attachments/assets/2e06ffb8-ac17-432d-8e8d-019c79c9579b" />

<img width="1322" height="184" alt="Screenshot 2025-10-02 172307" src="https://github.com/user-attachments/assets/e5eaf412-e185-44f9-9525-42a9dce3cd47" />

---

## **Author**  
- **Name:** Aditya Chouhan  
- **Roll No:** 2401830001  
- **Course:** B.Sc. (H) Cybersecurity  


