

---

# **Introduction to Programming – Week 6**

### **Lab Logbook Summary: Lists, List Comprehensions & Tuples**

---

## **Lists and Methods**

* Lists are **mutable** sequences supporting indexing, slicing, and iteration.
* Common methods:

  * `append()` – add element at the end
  * `extend()` – add multiple elements
  * `insert()` – add at specific position
  * `remove()` – delete by value
  * `pop()` – remove and return element
  * `clear()` – remove all elements
  * `sort()` – sort in place
  * `reverse()` – reverse elements
* Accessor methods:

  * `index()` – find index of value
  * `count()` – count occurrences
  * `copy()` – make a copy
* `del` can delete elements or entire lists

---

## **List Comprehensions**

* Short and efficient way to create lists:

```python
squares = [x*x for x in range(10)]
```

* Can include conditions:

```python
evens = [x for x in range(10) if x%2==0]
```

---

## **Tuples**

* Tuples are **immutable sequences** similar to lists
* Elements cannot be changed after creation
* Useful for fixed collections of values

---

## **Conclusion**

This lab focused on **managing lists and tuples**, using **methods**, and creating lists efficiently with **list comprehensions**, forming a foundation for handling sequences in Python.

---


