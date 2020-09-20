# Brutef0rc3
<h1 align="center">
  BFF
</h1>
<h4 align="center">
  Brute force Facebook
</h4>
<div align="center">
  <a href="https://github.com/yudhaha">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.8-blue.svg"/>
  </a>
  <a href="https://github.com/yudhaha">
    <img alt="Last Commit" src="https://img.shields.io/github/last-commit/yudhaha/Brutef0rc3.svg"/>
  </a>
  <a href="https://github.com/yudhaha">
    <img alt="Language" src="https://img.shields.io/github/languages/count/yudhaha/Brutef0rc3.svg"/>
  </a>
  <a href="https://github.com/yudhaha">
    <img alt="Top Language" src="https://img.shields.io/github/languages/top/dz-id/mbf.svg"/>
  </a>
  <a href="https://github.com/yudhaha">
    <img alt="Search" src="https://img.shields.io/github/search/yudhaha/Brutef0rc3/Brutef0rc3.svg"/>
  </a>
  <a href="https://github.com/yudhaha">
    <img alt="Repo Size" src="https://img.shields.io/github/repo-size/yudhaha/Brutef0rc3.svg"/>
  </a>
  <a href="https://github.com/yudhaha">
    <img alt="Starts" src="https://img.shields.io/github/stars/yudhaha/Brutef0rc3.svg"/>
  </a>
  <a href="https://github.com/yudhaha">
    <img alt="Forks" src="https://img.shields.io/github/forks/yudhaha/Brutef0rc3.svg"/>
  </a>
</div>
<p align="center">
 </p>

### Fitures
```
> crack id teman
> crack id publik
> crack id lewat reactions post
> crack id lewat nama
> crack id dari postingan group
> auto login
> dual login
          > Login <
     • Cookies
     • password
     • Token Facebook
```
### Install
```
🔻🔻🔻🔻🔻🔻🔻🔻🔻
pkg install python
Pkg install git
git clone https://github.com/yudhaha/Brutef0rc3
🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺
```
### And run this script
```
cd Brutef0rc3
python go.py
```

#!/usr/bin/python3
# go.py

•••••••••••••••••••••••••••••••••••••••
              go.py
  author: Yudhaha
  Ig    : https://instagram.com/yudamxr?igshid=oz075ik01ree
  fb    : https://www.facebook.com/damar.ky.16
  wa bot: Wa.me//+17145921008
•••••••••••••••••••••••••••••••••••••••
import shutil, platform

py_version = platform.python_version()

if py_version < '3.8':
    exit

cache = ['src/__pycache__', 'src/data/__pycache__']

for path in cache:
    try:
        shutil.rmtree(path)
    except:
        pass

__import__('src.app')
