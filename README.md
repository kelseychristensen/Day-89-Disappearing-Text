<h1 align="center">Writer Unblock</h1>

<p align="center">
A desktop application that erases all your text after 5 seconds if you don't keep typing!</p>



## Links

- [Repo](https://github.com/kelseychristensen/Day-89-Disappearing-Text "Disappearing-Text")

## Screenshots
![Full-Screen](/gif.gif "Full-Screen")

### Built with

- Python
- TKinter

### What went into this project

This is a GUI made with TKinter that will make your text disappear in 5 seconds if you're not continuously typing. There is a progress bar on top that turns from green to red as you get closer to the 5 second threshold that returns to 0 if you type. 
Other than that, there is a simple text box where the user can write. 

```python
def countdown():
    window.after(20, countdown)
    time_remaining['value'] += 1
    if time_remaining['value'] < 70:
        s.configure("bar.Horizontal.TProgressbar", background='forest green')
    if time_remaining['value'] >= 70:
        s.configure("bar.Horizontal.TProgressbar", background='yellow green')
    if time_remaining['value'] >= 75:
        s.configure("bar.Horizontal.TProgressbar", background='gold')
    if time_remaining['value'] >= 80:
        s.configure("bar.Horizontal.TProgressbar", background='orange')
    if time_remaining['value'] >= 85:
        s.configure("bar.Horizontal.TProgressbar", background='dark orange')
    if time_remaining['value'] >= 90:
        s.configure("bar.Horizontal.TProgressbar", background='orange red')
    if time_remaining['value'] >= 95:
        s.configure("bar.Horizontal.TProgressbar", background='red')
    if time_remaining['value'] >= 100:
        typing.delete("1.0", END)
```

### Acknowedgments

This is the Day 89 Project from <a href="https://appbrewery.com/">AppBrewery's</a> <a href="https://www.udemy.com/course/100-days-of-code/?couponCode=E98776F2DCA6FF71910B">100 Days of Python</a>
## Author

Kelsey Christensen

- [Profile](https://github.com/kelseychristensen "Kelsey Christensen")
- [Email](mailto:kelsey.c.christensen@gmail.com?subject=Hi "Hi!")
- [Dribble](https://dribbble.com/kelseychristensen "Hi!")
- [Website](http://kelseychristensen.com/ "Welcome")
