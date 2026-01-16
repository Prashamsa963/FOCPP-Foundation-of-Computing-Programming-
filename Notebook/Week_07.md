Introduction to Programming – Week 7

Lab Logbook Summary: Sets and Dictionaries

Sets

Sets are unordered collections of unique elements.
Sets are mutable, but elements must be immutable.
No indexing or slicing since sets are unordered.
Fast membership testing using in / not in.
Create sets with {} or set():
vowels = {"a", "e", "i", "o", "u"}
names = set(["John", "Eric", "Terry", "Michael", "Graham"])
Dictionaries

Dictionaries store key-value pairs.
Keys are unique and immutable, values can be any type.
Access values using keys: dict[key]
Add or update entries: dict[key] = value
Remove entries: del dict[key] or pop()
Useful for mapping and quick lookup.
Conclusion

This lab introduced sets for unique collections and dictionaries for key-value storage. These data structures are important for efficient data handling and lookup in Python.