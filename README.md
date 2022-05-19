<div id="header" align="center">
  <img src="https://media.giphy.com/media/cmqZM1lFsKHqo/giphy.gif" width="200"/>
</div>

<br>
<div id="badges" align="center">
 <a href="#">
    <img src="https://img.shields.io/badge/python-version?style=for-the-badge&logo=python&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.linkedin.com/in/ahmed-yasser-elbrmbaly/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  
</div>
<br><br>

# Task01: Plotter

This is an implementation for a function plotter.
<br>

### User enters

* Polynomial Function
* Values Range

Then the app plots the graph on the specified range.
<br><br>

## Prerequisites

* Python
* tkinter
* matplotlib
* numpy
<br><br>

## Structure

* **main.py** contains main function
* **GUI.py** contains GUI Code
* **Plotting.py** contains Plotting code
<br><br>

## Task Requirements Progress

1. Write a GUI program that plots arbitrary user-entered functions.
![100%](https://progress-bar.dev/100/)
2. Take a function of x from the user, e.g., 5*x^3 + 2*x.
![100%](https://progress-bar.dev/100/)
3. Take min and max values of x from the user.
![100%](https://progress-bar.dev/100/)
4. The following operators must be supported: + - / * ^.
![100%](https://progress-bar.dev/100/)
5. The GUI should be simple and beautiful (well organized).
![50%](https://progress-bar.dev/50/)
6. Apply appropriate input validation to the user input.
![50%](https://progress-bar.dev/50/)
7. Display messages to the user to explain any wrong input.
![50%](https://progress-bar.dev/50/)
8. You may use the programming language and platform of your choice.
![100%](https://progress-bar.dev/100/)
9. You must test your program. Include the testing codes in your repository.
![0%](https://progress-bar.dev/0/)
10. Your code should be well organized and well documented.
![50%](https://progress-bar.dev/50/)

<br><br>

## Breaking down the requirements

### 1. GUI

* [x] Function Label
* [x] Function Entry
* [x] Max Label
* [x] Max Entry
* [x] Min Label
* [x] Min Entry
* [x] Plot button
* [x] Exit button
* [ ] Input Example as Placeholder
* [ ] window fixed size
* [ ] matplotlib embed in tkinter as a widget

### 2. Input and Validation

* [x] Function Input
* [ ] Function Validation with re
* [x] Max Input
* [x] Max Validation
* [x] Min Input
* [x] Min Vlaidation

### 3. Plotting

* [x] Installing matplotlib
* [x] getting range from GUI
* [x] eval function to get y values
* [x] plot the graph

### 4. Testing

* [ ] unit test

<br><br>

## Progam OverView

### Program GUI

![01](https://github.com/ahmedelbrmbaly/plotter/blob/main/snapshots/01.png)

### Enter Valid Values

![02](https://github.com/ahmedelbrmbaly/plotter/blob/main/snapshots/02.png)

### Graph

![03](https://github.com/ahmedelbrmbaly/plotter/blob/main/snapshots/03.png)

### Enter non numerical value as max or min

![04](https://github.com/ahmedelbrmbaly/plotter/blob/main/snapshots/04.png)

### Error message 1

![05](https://github.com/ahmedelbrmbaly/plotter/blob/main/snapshots/05.png)

### Enter Min value bigger than Max

![06](https://github.com/ahmedelbrmbaly/plotter/blob/main/snapshots/06.png)

### Error message 2

![07](https://github.com/ahmedelbrmbaly/plotter/blob/main/snapshots/07.png)

<br><br>

## ToDo

* [ ] Fix Functional bugs
* [ ] Testing
* [ ] GUI Inhance
* [ ] Build the program

<br><br>

## Bugs

* [ ] we need to press exit twice
* [ ] program doesn't stop after an error acuors
* [ ] function validation

<br><br>

## License

The project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License)
