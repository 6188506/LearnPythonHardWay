squares.py:
  def squares(start, stop):
    for i in range(start, stop):
       print i**2

  if __name__ == `__main__`:
    # ...run automated tests...

calc-squares:
  #! /usr/bin/env python
  import squares
  squares.squares(0, 10)