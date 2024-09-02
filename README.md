# corprit

The COnsumerR PRIce Tracker. The idea behind this is to
provide a mechanism for tracking consumer prices found 
in google queries for various items over time. It is meant
to be completely independent of nation state funded 
agencies and for-profit corporations who have significant 
political and economic skin in the game for presenting data 
in a way that helps push their agenda. 

I however, as a generic consumer, just want the data without 
the bias. And I want to see how its evolving over time.

This repository is an attempt at bringing that 'just give me
the numbers and let me interpret them' approach to consumer
prices over time.

## developers

- The `requirements-dev.txt` has `black` in it. I like 
automated code formatters :)

## maths

- The beginnings of the maths will just be dumb averages
of various items spread over a spectrum of somewhat arbitrary
item price categories.
- item price categories:
    - low-low
    - low-moderate
    - low-high
    - moderate-low
    - moderate-moderate
    - moderate-high
    - high-low
    - high-moderate
    - high-high
- *Disclaimer*: I am not an economist.
