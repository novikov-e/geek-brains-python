from itertools import count
from itertools import cycle

prog_lang = ["python", "java", "perl", "javascript"]
iterator = cycle(prog_lang)
for el in count(len(prog_lang)):
    print(next(iterator))
    print(el)
    if el > 15:
        break
