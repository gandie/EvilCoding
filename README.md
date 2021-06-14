# EvilCoding

Let's pick a short and well working program and mess it up like hell!

Who can create the worst nightmare from a simple python script?

# Round 1 - Starting simple

Task: Add all numbers from 1 to 1000.

One could simply write:

```ipython
In [1]: sum(range(1001))
Out[1]: 500500
```

But this makes it much too easy for others to find out what's going on.

# Rules

+ Do not write more than 300 lines, but make them read as hard as possible
+ Each line which is not an empty one must be called/used in the code
+ The result of your program must be the given one
+ Contribute your version as `round_1_<user>.py` in a PR
 
# Ideas

Some inspiring ideas to get you started.

## Avoid built-ins

Cool kids code their own `sum`. Try to find a good name for it. Nobody shall know it's actually `sum`.

```python
def add_up_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
```

## Use short variable names

Why not start with `a`, `b`, ... , `A`, `B`, ... , `aa`, `bb`. This will make your code look dense and thoughtful.

```python
c = a.text  # python3!
d = b in c
e = a.url
f = e == A + U
```

## Wrap primitive data into complex objects

And find important-sounding names for both the class and its methods.

Good class names end on words like `Manager` or `Agent`, good method names use words like `run`, `check` or `initialize`.

## Comments

Your secret weapon and advanced obfuscation tool. A simple comment can keep useless lines alive for a LONG time!

Test your readers attention by having both super-important and 100% useless/misleading comments in the code. You never know until you've checked the whole thing!

Try to break your reader by also commenting on the follinw line like `Now the if` or `next is for-loop`.

## Overengineering

This case is too simple for `range`. We should build our own generator with blackjack and hookers!

## Using `lambda`

`def` is for lame people. Protect your code by using `lambda`, this will scare off beginners and looks like super-magic stuff.


```python
# define some basic functions ...
P = lambda p: print(p)
L = lambda l: len(l)
I = lambda i: intern(i)
```
