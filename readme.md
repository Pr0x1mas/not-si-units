---
layout: default
title: About
permalink: /about/
---

# About

You can also read the [blog post](https://jbritain.github.io/2021/10/31/si-units-are-boring-lets-replace-them.html) I wrote about this.

## Where it came from
The question was simple: why do we have to use SI units? What's to stop us using our own units?

My original idea was to break into France and pull the ol' switcheroo Indiana Jones style, and replace the kilogram with a pigeon (preferably not live as that could get messy). Sadly this was not an option, so I resorted to plan B: create my own system of units instead. With the help of various friends, I created alternative names and values for every base SI unit, as well as renaming [all other named units](https://en.wikipedia.org/wiki/List_of_scientific_units_named_after_people#SI_derived_unit) with inside jokes and names of some people who helped.

## How it works
Each base unit has a ratio which shows how it can be converted from SI, e.g Uncomfortable Pause, a unit of time, has a ratio of 1:8.2, meaning 1 uncomfortable pause is 8.2 seconds. All other unit's conversion ratios are then derived from these ratios and base units.

## Why the name?
Nacia Netradicia is Esperanto for "national unconventional", intended to be the exact opposite of the translation of SI: "international standard".

## How it works (technical details)
All units are stored in two files - [base.csv](https://github.com/Pr0x1mas/not-si-units/blob/main/unitGen/base.csv) (base units) and [units.csv](https://github.com/Pr0x1mas/not-si-units/blob/main/unitGen/units.csv) (other named units). A [python script](https://github.com/Pr0x1mas/not-si-units/blob/main/unitGen/generate_units.py) is then used to take the data in the csv files and generate markdown files for each one. These markdown files are placed in the '_units' folder. Through the use of liquid collections, the tables on the home page are populated with each unit. I previously used js to load directly from the CSV, however this lead to compatibility issues on older browsers and just didn't make sense when I could have it served as static HTML. This means that it is entirely possible to view this site on [Nintendo 3DS](https://i.imgur.com/vfLJN0Q.png).
