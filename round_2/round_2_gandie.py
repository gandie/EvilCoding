import subprocess as s; import random as r
ch=lambda x:r.choice(x);b='-dump';d='https://api.chu\
cknorris.io/jokes/';a='lynx';cl=lambda y:s.check_output(
[a,b,y]).decode();r2=[i for i in cl(f'{d}categories')\
.split('\n') if i];c=ch(r2);d=f'{d}random?category={c}';
r2=cl(d);print(r2)
