# Lecture 07: Python Classes

**LMSC 261 | Introduction to Computer Programming**

## Overview

In this lesson, you will practice **object oriented programming (OOP)** by creating Python classes that represent familiar musical concepts. You will learn how to combine information (attributes) and actions (methods) inside objects, then explore how related classes can share and customize behavior.

Complete both exercises in Python. Run your code and check the results before submitting.

---

## Exercise 1: Build a `Track` Class

### Objective

Create a Python class that represents a track in a music production session. Each track should store information about itself and provide methods to describe the track and change its volume.

### Requirements

1. Define a class named `Track`.
2. Write an `__init__()` method that accepts and stores three attributes:
   - `name`: the track's name (a string)
   - `instrument`: the instrument or sound source (a string)
   - `volume`: the track's volume (a number)
3. Write a `describe()` method that prints the track name, instrument, and current volume.
4. Write a `turn_down(amount)` method that decreases the track's volume by the specified amount.
5. Create **at least two** different `Track` objects.
6. Call `describe()` on each track, change the volume of at least one track, and call `describe()` again to confirm that the value changed.

### Starter Code

```python
class Track:
    def __init__(self, name, instrument, volume):
        # Store the attributes here
        pass

    def describe(self):
        # Print the track information here
        pass

    def turn_down(self, amount):
        # Reduce the volume here
        pass


# Create at least two tracks

# Describe your tracks

# Turn down one track and describe it again
```

### Example Behavior

Your output does not have to match this formatting exactly, but it should show the correct information before and after adjusting the volume.

```text
Beat: Drums @ 0.8
Low End: Bass @ 0.7
Beat: Drums @ 0.6
```

### Check Your Understanding

- What is the difference between the `Track` class and an individual track object?
- What does `self.volume` refer to?
- If you turn down one track, should the other track's volume change? Why or why not?

### Optional Challenge

Update `turn_down()` so that the volume cannot drop below `0.0`.

---

## Exercise 2: Build an Instrument Family

### Objective

Use **inheritance** and **method overriding** to model different musical instruments. Your instrument objects should share common information but produce different results when their `play()` methods are called.

### Requirements

1. Define a parent class named `Instrument`.
2. Write an `__init__()` method that stores two attributes:
   - `name`: the instrument's name
   - `volume`: the instrument's volume
3. Define a `play()` method in `Instrument` that prints a general message.
4. Create two child classes:
   - `Synth`
   - `DrumMachine`
5. Override `play()` in each child class so that it prints a message specific to that instrument.
6. Create at least one instance of each child class.
7. Store the instances in a list and use a `for` loop to call `play()` on every object.

### Starter Code

```python
class Instrument:
    def __init__(self, name, volume):
        # Store the attributes here
        pass

    def play(self):
        # Print a general instrument message
        pass


class Synth(Instrument):
    def play(self):
        # Print a synth-specific message
        pass


class DrumMachine(Instrument):
    def play(self):
        # Print a drum-machine-specific message
        pass


# Create a Synth and a DrumMachine

# Add your objects to a list

# Loop through the list and call play() on each object
```

### Example Behavior

```text
Keys: warm synth chord
Beat: boom bap
```

Your messages can be different. The important part is that the two objects use the **same method name** but produce **different behavior**.

### Check Your Understanding

- What attributes do `Synth` and `DrumMachine` inherit from `Instrument`?
- Why can the child classes use the parent's `__init__()` method without writing their own?
- What does it mean to **override** a method?
- Why can the same loop call `play()` on objects from different classes?

### Optional Challenge

Create a third child class, such as `Guitar`, and give it a different `play()` method. Add it to your list without changing the loop.

---

## Submission

Save your completed exercises as:

```text
exercise1_track.py
exercise2_instruments.py
```

Submit both files to your GitHub repository following the usual course submission procedure.

Before submitting, make sure both programs run without errors, you have tested every required method, and you can explain what each part of your code does.
