convert-csv-plist
=================

Python code to convert CSV to PLIST and be used inside iOS development.

usage
=================

- You can see that it ignores the first row as just labels, and use the
first and second column values for Keys and the third column for Value.  
- Everything key and Value is handled as Strings.
- The main idea is for you to have a 2-layer key like that:

[index]  |  [key] | [value] |
