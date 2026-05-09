"""
Great, let’s continue.

---

# **Day 6, Chapter 24: Performance (Tuple vs List Speed)**

---

# 1. What is performance?

👉 Performance means:

👉 “How fast and efficient something is”

---

# 2. Key idea

👉 Tuples are faster than lists

👉 Because they are immutable

---

# 3. Basic comparison

```python id="tp24_1"
t = (1, 2, 3)
l = [1, 2, 3]
```

👉 Both store data

👉 But behave differently internally

---

# 4. Why tuples are faster

👉 Tuple:

* Fixed size
* No changes allowed
* Less overhead

👉 List:

* Can grow or shrink
* Needs extra memory
* More operations

---

# 5. Memory usage

👉 Tuple uses less memory

👉 List uses more memory

---

# 6. Speed example (conceptual)

```python id="tp24_2"
t = (1, 2, 3)
l = [1, 2, 3]
```

👉 Access speed:

* Tuple → slightly faster
* List → slightly slower

---

# 7. When performance matters

👉 Use tuple when:

* Large data
* Read-only data
* High performance needed

---

# 8. OCR Example (important)

👉 During processing:

```python id="tp24_3"
data = ["INV001", "12-02-2025", 500]
```

👉 After processing:

```python id="tp24_4"
final_data = ("INV001", "12-02-2025", 500)
```

---

👉 Why tuple here?

* Faster access
* Safe data
* No accidental change

---

# 9. Real use case

```python id="tp24_5"
# thousands of records
records = (
    ("INV1", 100),
    ("INV2", 200)
)
```

👉 Tuple helps in:

* Faster reads
* Stable structure

---

# 10. Common mistakes

---

### ❌ Using list everywhere

👉 Not always efficient

---

### ❌ Over-optimizing

👉 Difference is small for small data

---

# 11. Practice

---

### Task 1

👉 Create tuple and list with same values

---

### Task 2

👉 Use tuple for fixed data

---

### Task 3 (OCR style)

👉 Convert list to tuple after processing

---

# Final One-Line Summary

👉 Tuples are faster and more memory-efficient than lists because they are immutable.

---

Next is **Chapter 25: Safe Access (Avoid Index Error)** 🚀


"""
