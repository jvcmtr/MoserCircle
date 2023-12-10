# Moser's Circle Problem 

**A simple project trying to solve Moser's Circle Problem.** i saw it on a 3blue1brown youtube video. First i tried to solve it on paper and struggle a little to express the recurciveness of the function in mathematical terms, so i decided to solve it on code.

> **Problem statement:** if you define N points in a circle and draw lines connecting all of them, you devided the circle in how many regions (given that 3 lines never intersect)
> * Teaser video: https://www.youtube.com/shorts/VFbyGEZLMZw
> * Solution: https://www.youtube.com/watch?v=YtkIWDE36qU

Unlike 3Blue1Brown beautiful solution using Euler's characteristic formula, my solution started with trying to solve the following problem: 
>How many regions a new point provides ?

Its easy to see that a new point adds n-1 new lines and that each new line divide each region it passes throught into 2 (adding one more region). this is easier to work with if you distiled into the following rule: **A new line creates an extra region when it passes over another line OR gets to it's destination point**.
Now the question becomes
>How many lines a new line crosses over?

**My FIRST aproach** was dividing the existing points into groups depending on how many other points existed between them and the new point. The lines conecting to the ones directly beside it cross no other lines, where the ones connecting further points had to cross many other lines. 

**My SECOND aproach** (the one implemented) started when i realized that each line divides the circunference into 2 parts, and the amount of lines it crosses is equal to the product of the number of points in each part (knowing that 2 points are reserved for beeing the start and finish line so they dont count for the amount in either part). So to solve the problem it only requires a base case and, for each new point, calculate how many regions each line add.
