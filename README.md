Pappardelle
===========

Pappardelle is a Python module that provides helper functions for lists and dates.

# Change Log
* **Version 0.2**
  * compare_lists returns a dictionary with keys: =, +, - (instead of: matched, + -)
  * Added relative date functions
* **Version 0.1**
  * First release with compare_lists and lookup_lists functions

# Author

My name is Katkam Nitin Reddy. I am a former software developer living (mostly) in Dubai. I created this library for functionality that I find myself re-writing for a Terraform-style project.

# Acknowledgement

I would like to thank my mom, Katkam Nita Reddy, and my dad, Katkam Narsing Reddy, who have always motivated me to learn and contribute to the open-source community.

# Getting Started

Install the Python module with
```commandline
python3 -m pip install pappardelle
```

Then, within your Python (.py) source code, like in this example:
```python
from pappardelle import compare_lists
```

Call the imported function:
```python
>>> compare_lists(
    [1, 2, 3],
    [2, 3, 5]
)

# Returns the following
{
    '=': [2, 3],
    '+': [1],
    '-': [5]
}
```

# References

## List Functions

`compare_lists(list1, list2, optional lambda comparator)`

`lookup_lists(list1, list2, optional lambda comparator)`

## Date Functions

`days_before(num_of_days, from_date)`

`days_ago(num_of_days)`

`days_after(num_of_days, from_date)`

`days_since(num_of_days, from_date)`

`tomorrow()`

`yesterday()`

`hours_before(num_of_hours, from_date)`

`hours_ago(num_of_hours)`

`hours_after(num_of_hours, from_date)`

`hours_since(num_of_hours, from_date)`

`minutes_before(num_of_minutes, from_date)`

`minutes_ago(num_of_minutes)`

`minutes_after(num_of_minutes, from_datee)`

`minutes_since(num_of_minutes, from_date)`

`seconds_before(num_of_seconds, from_date)`

`seconds_ago(num_of_seconds)`

`seconds_after(num_of_seconds, from_date)`

`seconds_since(num_of_seconds, from_date)`

`weeks_before(num_of_weeks, from_date)`

`weeks_ago(num_of_weeks)`

`weeks_after(num_of_weeks, from_date)`

`weeks_since(num_of_weeks, from_date)`

`months_before(num_of_months, from_date)`

`months_ago(num_of_months)`

`months_after(num_of_months, from_date)`

`months_since(num_of_months, from_date)`

`years_before(num_of_years, from_date)`

`years_ago(num_of_years)`

`years_after(num_of_years, from_date)`

`years_since(num_of_years, from_date)`

# Examples

TODO