# The Great Unfair Horse Race for Python

This is a Python dice rolling game.

There is a starter trinket for this project called UnfairHorserace_starter. Log in to your trinket account, then go to this link:

[https://trinket.io/python/709010f605](https://trinket.io/python/709010f605)

## Links to video summaries of the online sessions

### Video for first session - Saturday 6 March 2021

In this video we build up the game by writing code to create turtles for the horses and make the dice roll.

[https://youtu.be/fVMG_7_WARA](https://youtu.be/fVMG_7_WARA)

### Video for second session - Saturday 20 March 2021

In this video we finish coding the horse race and find out why it's called "unfair".

[https://youtu.be/n-0EHBDM6hc](https://youtu.be/n-0EHBDM6hc)

### Video for third session - Saturday 3 April 2021

In this video we discuss why the race is so unfair and write some code to turn the game into a superfast simulator to run tens of thousands of races automatically and keep track of how many times each horse wins.

[https://youtu.be/Oa5hFftY5F0](https://youtu.be/Oa5hFftY5F0)

Here are the six lines of code referred to at the end of the third video for you to paste into your project:

```python
bar_chart = pygal.Bar()
bar_chart.title = 'Outcomes of ' + str(num_sims) + ' races'
bar_chart.x_title = 'Horse number'
bar_chart.x_labels = range(13)
bar_chart.add('Wins', winners)
bar_chart.render()
```

[Back to index](README.md)
