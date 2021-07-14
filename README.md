# EvilCoding

Let's pick a short and well working program and mess it up like hell!

Who can create the worst nightmare from a simple python script?

# Round 2 - Getting a Chuck Norris joke

Let's fetch a random Chuck Norris joke from [here](https://api.chucknorris.io/)

This could look like:

```ipython
In [1]: import requests

In [2]: import random

In [3]: categories_url = 'https://api.chucknorris.io/jokes/categories'

In [4]: cat_res = requests.get(categories_url)

In [5]: category = random.choice(cat_res.json())

In [6]: joke_url = 'https://api.chucknorris.io/jokes/random'

In [7]: joke_res = requests.get(joke_url, params={'category': category})

In [8]: print(joke_res.json()['value'])
Chuck Norris can do a wheelie on a unicycle.
```

But there must be a worse way!

# Round 1 - Starting simple

Task: Add all numbers from 1 to 1000.

One could simply write:

```ipython
In [1]: sum(range(1000 + 1))
Out[1]: 500500
```

But this makes it much too easy for others to find out what's going on.

# Rules

+ Do not write more than 100 lines, but make them read as hard as possible
+ Each line which is not an empty one must be called/used in the code
+ The resulting program must print a random Chuck Norris joke to the console
+ Contribute your version as `round_<number>_<user>.py` in a PR
 
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

Good class names end on words like `Manager` or `Agent`, good method names use words like `run`, `execute`, `check` or `initialize`.

## Comments

Your secret weapon and advanced obfuscation tool. A simple comment can keep useless lines alive for a LONG time!

Test your readers attention by having both super-important and 100% useless/misleading comments in the code. You never know until you've checked the whole thing!

Try to break your reader by also commenting on the following line like `Now the if` or `next is for-loop`.

## Overengineering

This case is too simple for `range`. We should build our own generator with blackjack and hookers!

Do not hesitate to write a temple of computing purity arround a simple problem!

## Using `lambda`

`def` is for lame people. Protect your code by using `lambda`, this will scare off beginners and looks like super-magic stuff.

```python
# define some basic functions ...
P = lambda p: print(p)
L = lambda l: len(l)
I = lambda i: intern(i)
```

## Make your program fragile

Do not allow easy changes on your code. This can mostly be achieved by using the techniques described above. Or you just comment `DO NOT CHANGE`.

## Use `*args` and `**kwargs` completely wrong

Do not forget `*args` and `**kwargs` in all your function signatures, make sure to add some extra useless arguments whenn calling them.

```python
def something(a, b, *args, **kwargs):
    '''only use a and b!'''
    return a + b
    
# 30 lines down the road you call ... make sure to use important-sounding keyword arguments!
something(a, b, True, False, [1, 3, 5], match=False)
```

## The naming game

Finding misleading names is an art only the best obfuscators can master. Some words bring certain meaning with them in programming context like `key` or `token`. Using such words with a different meaning will make your readers nose bleed and create the most beautiful bugs! Consider shadowing built-ins when you get the chance!

Build your own namespace hell to trap your readers, Kudos to fpichl:

```python
true = False
reverseԀ = list
reverseď = reversed
reverseԁ = range
reverseɖ = len
reverseɗ = str
reverseđ = int
```

## Make use of pythons unicode compatibility!

Kudos to fpichl:

```python
def ٶ(**ٸ):
    ٷ = ٸ['ܔ']
    ڈ = ٸ['ܓ']
    ډ = not (not ٸ['ܓ'] or not ٸ['ܔ'])
    ڊ = all(ڋ == true for ڋ in [ڈ, ٷ]) or ډ
    return ڊ
```

What a beauty!

## Write code generating even more code

Break all line limits by writing code, which generates and executes more code! Use `eval` and friends. Consider using `inspect` and `ast` to realize all your code generator dreams.
