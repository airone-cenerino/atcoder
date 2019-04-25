s = list(input())
t = list(input())
flg=1
for i in range(len(s)):
    flg=1
    for j in range(len(s)):
        num = i+j

        if num >= len(s):
            num -= len(s)

        if s[num] != t[j]:
            flg=0
            break
    
    if flg==1:
        break

if flg==1:
    print("Yes")
else:
    print("No")
    

    





# ??!~<<??11z<<<<<+(J+gQWHMMMHHHHUUUVVz<<<<1OOOOXWWkqHHHHHHHkqkqHHkqHHHHHHHkHHHUHHHHHHHHWWWWWWWWWWWWWWUUUVVOOOOOOOOOOOOOOOOOwZXVwVZZZOOOOOOz<<<<<<<<<<<<
#  ......-_(JgXVB9UUZyyyyWWyVVyWXzvrI<::++z+1zOXfWkkkkkkkkkkkkkkkkkbkbbbbbppHo(dppppfffffVVVVyyyyyyyZZuvrrttttttv1llllllllztrZ!_?rttttttll?;;;;;;::~~~~~
# yUUUUUUWVVk&++?zOwXuuuvvXyVyZuuzZv~~~``~!  (OXkkqkkkkkkkkkkkkkkkkkkkbbbbbbbWbppppf?77T4pVfVVVVyyyyZuvrrttttttt>(ttttlltrrvZ:_-Jrrrtttllz>;;;;;;::~~~~~
# .........-?74WyXx<zOOwrrzuuuuzzZz<_(+<     __zTWkqqqkkqkkqkkkkkkkkkkkkbbbbbbbbpppR....JffffVVVVyyZuzvrrrrrrrrrrrtttttrvvzzw+Owvrrrrrtlz>>>>>>>;:~:~~_(
# VVVVVVyVVVWA..(TWWs<11lOvuuzzwI??1zztO+-(_``.(&dXWWqqqkqqkkqkkkkkkkkbkkkbbbpppbpppppppppfpffffVyyuuuzzzzvvrrrrrrrrrrwwuuzzuuzzzvvrrtlz?>?????<::~~:(<+
# yyVyVyVyVVVyyVk..?WWo<<1OvrvOz?=zOrrvwwXkkwXXXWkWWkkkqkkqkkqkqkkkkkkkkkkbbbbbpbbppppppfppppfffVZZuuuuuuzzzzvvvrvvrzuuuuuuuuzzuzzvrrt=????=??>;::::(+1l
# yyZyyZyyZyZWWWWyW+.?Vk-1lrrO??zzrvzzXXWbkkkkkbkqqkqkqkqqqqqqqqkHHHHHWWWUUUUUWWWWWpbppppfpfppfVyZZuuuuuuuuuzzuzzzzuuZZuuuuuuuuzzzzrt=?zz<!(=?;;:::<1zlt
# `  ` `` ``  ` `(Wyk,(WkyOOz=zzOrzuuXWbbkkkkqkkqqkkqqqqqHHHHyyyyyyyyyyZZZZZZuuuuuzXwzzVTUWppfWyyZZZZZuuuuuuuuuuuuXZyZZZZZuuuuuuuzvO=1v_..J=1>;;:<+1lttt
# X= (o ?WVyyyW> `jVVW,.WVwOzzOrzuuXWbbkkkkkqkkkqkqHHHHyyVyVVyyVyVyyyyZyyyZZZZZZuuuuuzzzrOOz+?TWyyZZZZZZZZZuuuuZZXyZZZZZZZZZZuuuzzOlv!.-(tl=?>>>>+ztrtrr
# !.jVVn.-UVVyC`.- OyVW-(VkrrvzuuXXWbbbbkkkkkqkHWHHWWyVVVyVVyVVVVyVyyyWkkkXZXUXuXkkkXuzzzvrrtl=+-?TXZXZZZZZZZZZZyyyyyZZZZZZZZuuuXOllttrrtt=???>?zzrrrrrr
# .dVyyVk, jV0`.Xk..Wyyn OykzuuZXWppbbbbkkkqkHHyyWKWVVfWfVVVVyVWkVY=<_........`.....-_?7TXwwtttlOw+.?4yyyyZyZyyyyyyyyyyZZZZZZZuzOtttrrrttz==??1zrrvvrrrr
# XyVyVyyW+ ?! JVyn..WVW_(yWuZyWppppbkbkkkHHWyyVWHVVVWHWffWWVY>_~.........``.`..`.`.`.....` ?7CwZvXXx-.?WyyyyyVVVyyyyyyyyyXZZuXZtrrrrrrrtll==zzvzzzzzvvr
# _______._  ..~___` (VW}.VWZXWfpppbbbkkHHyyyVWHHVVVWHWWXY>:~~~~........`.......``.`````````.`..-?CXZkz+.?WyVVVVVVVyyyyyyWsdZXrtrvzzzzvttlllzwzzzuzzzzzv
# yVVVyVyyC .yyWY``.dVVV}.VVVfpppppbpbWHyyyyWWHVVVVWHKY<::::::~~~~...-----(((((J(-(......`.`..`.._..?4XAz<.?WfffVVVVVyyyyyZZXrrrzzuuzzrrtttOwuuuuuuuzzzz
# OVyVyVVf (VWY``.dVyyVW!.fWfpfppppbWHWyyyyWHHVVVVVH3_::::::::((J&QWHHHWHUkyZZZyyyXXWkXXUUX&J-........_Tkz+i.CWpffVVyVVyyyZuvvzuuuuuzzvrrrvzuuuuuuuuuzzv
#  OVyVVf`-WY``.uWVyVVV$ dyffpfppWpWHyyyyVWHHVVfVfWC::::::(+dHHHffVffffWNkWyWZZZZZZwXXkwrwvZWkZUG--~~.~_14yz<.,WpWffVVVVyZ0zzuuuZuuuzzzvvzuuZuuuuuuuuuzz
# +.UyyS!.Y!`.JyVVyVyy0~.VyWffppfpHWyyyyyWHMVVfffpHI::++gHHfWHpfffVfWfVXHkXkWXZXXOOuZOXkOlzrrXWzvwZUa,~._1vk1?- 7WWffVVyWXuuuZZZZZuuuuzuuuZZZZZZZZuuuuuu
# _!.WX!,!`.JVyWyVyVy0!.XVVVVffpWHXyyyyVWgMVffffWWUijdMHppppWpVVVWZWWXXZHHkXWwXZOz=OI?wuO<;1rtZWzZOwrZW&-_1?kl(-`(WpfVyyuuZZZyZZZZZXZuXXXXyyZZZZZZuuuuuu
# .``(:``.JyyyVyVyVWf~.XyyyVVVfWHyZyyyyWHHVVffWWpHdHHppffppVHfSyySuXWXkXdgHkWkwXz+?zXzjuXc;;OZzZRrvzrrrZUn-<zwo(-  TWWyZZZyyyyyZZZZZZ2<dZyyZyZZZZZZuuZZu
# Wn.` .JVyyVyVyVWV^.JVWVVyVVfWHyyyyyVWMMHfffpWpWMHpfppyppXXHV0XZWvvWkWuwHHHwWXZOzi+wI+XZI<>jw<zXkI:zrOOOOXkczZ:<- _?WZZyyyyyyyyyZZXGA(_?74yyyZZyZZZZZZZ
# VyVGJWyVVVfWWkkQgggHHHHyVVfWHZyyyyVWH#HfVWWRXpWMppffSWpWuXHWkwyyXrXWXkXXH@HyWZXvOw&v=dZXO=+wz<wWI:(rIj=zlOUnwO-1_._.WyyyyyyyyyyyyyyXn-.``(ZyyZZZZZZZZZ
# VWWkkHkWgHHWY"4H!(&gQHHWgHHHXyyyyyyWHXWWZuWSWpHHpffWXpHSZWHHywyyWuXWWWWZWHHHkWXXXuuZoJUXXOzwI>zXw<<ww(><vzIzWRo(< .< 4fVVVyyyyyyyyyyyyyn-XXyyZZZZZZZZZ
# Hg#"<?HHN`JH@_,N.JHgggHH#.HH@HkyyVWMXHWXUwWXWW@kpVWXpHpWypWNVXXkWWyWpfWfyWHHHkdkyyyykdWAZOOwI1zdkz<zzcI:?(rOZXO;(- j- CVVVyyyyyyyVVyVyyyyyyyyyyyZyZZZZ
# d@F H.?gg_(HY:,H_(A+&H@7> ((+HHyVVM8dpSuzXWdpW@bWWyXWHppbbWHpffWkppfpbppWfpHHWHdHfffWXfVyyk&z+?VUC<zOcj<:<jwrXkI_1..w.`?WVVVVVVVyVyyyyyyyyyZZyZZyZZZZZ
# Jg\.H$ X@;,e.THM).ggHggHg_dgHWVyWW#wWf0vvXSXpHHbWyyWHpbbbbbHHWppHWWppWHpppfpHHpHkUWWffffVVyyXwwZKuOwkXzI:++dwXWw>1<_(o  (VVVVVVVVyyyyyyyyyyyZZZZyZZZZZ
# HH~(Hg[ W[.HH,.Ur TIu+gHHkHHWVyyyHuXHVXrwW0XpM@pWfpHHbbkbbbWDWbbWNHHbpWHpppppWMkpHkWWpffffVVyyZyHZXXRuzwz+zzkdfkI+O<_0>`_(WVVyyVyyVyyVyyyyyyyyZyZZyZZZ
# TD`dHHH,.h.HHgHHgHHHH9UwdVyyyyZZfHuXHWzzwpXXp@@bppWMbbbHQkHHY9HMHHNNWppWMkpppppHHppHkHpWpWWWkkWkWXZXWZZuwzOwXkpKzztz<zO-._.4VVVyVyyVyyyyyZZZZZuuuuXZOO
# +gkHHZWHHHHUuXZZuZZZZZZyHyyyySuXWKuWWWuXdbXXk@@kbkHHWHMHkkWK_(vWkbWNMWppWMHpppppWHkppWHWHffffffXdHMRkyXZXwwuXHXHuOXOljZz-(i.?WWyyyyyyZZZu0VOOOOXXZI<<~
# UVwvvvzzzk(.(wuuuZZZZZydHyyyySXXWSdMfWyXXpzXW@MHbWMMkbbkkWHt``(c4WbHHHHWbbHMHWpppWWHWppWHHHWfpHKdVW}XWHXyZuZZWdHuXdwtlStz<+O++TWXzOI<<<<<<<<<<+=1<;__.
# trrvvvzzzzuuuuuuuZZZZZXMyVVXy0zXWXMHpWWWWpXXk@HHq@NkbbkkHMK~` `(I?HWNWhWWHpWMMkpbpppWHWWWppWHWHDXfD~dyyWWXyZZWXqZuXWwOXOtz_<zOOOZWXuwzz+--. `__~<<;:__
# rrrrvvvzzzzzuuuuuuuZZXHNWVVZyuuWWW@MpppfpbkXk@@MWMkkkkkHMHt ....(zJTKNJHJWWbbHMMkbbppppHpHHWHHWdHW<~(HVVyWWyyXXqWZuXkXdkO! .OOwwvrrZTUZVz<______~~;<++
# rrrvrvvzzzzuzuuuuuuZuWHHWHVXyXXfWM@NpppfpbRdpM@@HMkkkkkHH#<!` `` _?1J4MeTHvWHbbM@HkpbpWHpppWhHDXW=-_~WVVVyyyyydHkZZZWkXHkXzvwXvXuzvO1+<_?<++<<__~_(<+?
# trrrrrvvzzzzzuzuuuuZXWHWWHVyVWZpH@HNppppppHuWH@@MMbkHHMWHu+NMMMNkC` ~<jWh_THyWkkWMMMHWMppbWHMWMWNJ.(<?kVWVyyykdHkyyZZHkWkXZuuXXkXkO===??+__ ?<+<<;;;;<
# ???OrrrvvzzzuzuuuuuXXqHVWNfVfVypH@HMpppppbpWXH@@MkbkHMNHMNNMN#K79NZ.` ~._T&_?TWHkbbHMMHbWWdMMMMMTM#N,_XfWkVVWSyWHyyyyXHHWkZZZXkUkzzrwOzz1<<<-.`_<+:___
# <>??1zOrrvzwZ7?TuXWXqmHVWMffffVfWHM@WbppbbbWXWH@MkkWMMNMMMMNMMNp__==``   ``.?<.__<79WWHHOMNfMNNMN/(WMNJHWHWfWdVWHyyyyZXHq$<wZZWZOXtzztltOOO&+_~~.-_<_`
# ;<1=zttrOIz____..7WHmgHVfMpWfpfpWMMMHbpbWHbbppMHMkHMMMMNWMMNMMMN.` `        `   ``.JHY77HMMMMMMMM@ _7HHJNWHWSXVWHWVyyXXXHqWkyZXSrOwOtzvzlll1+?1&-<<__-
# ++1=ltrrrvwzz<__._(UmgHVVMfWXpppbMM@NpppbHWbppWHNHHMH1M#MMqMMHHM{     `    `  `  ?"!   .NBW9TGdHMN. _dHv?HWHdfffWHWWVyWXWHqqkyXdkrrZwtlO++1z1=?<<+i+1(
# ztltttrrrrrvvOx<___~ZgHVVMpfXfpppM@@MWbbbWNbkbbM@BM@!.##"4C?HKjM{ ` `  ` ` `  ``  `  ``.{`.Ngv9TH#`  .g]__WdMWfffHWHVVVVkUWHqkXvWkwrrXOl==1+<?<<<<<77?
# JltttttttrrOdHXHgQWHgHHVV@WpXpfppH@@@HbbbbHHbkHHPJ#_  W` dBB6jWY `   `    `     -       ?Hm+-JadgF ` JH' _d@NMkpfHkWkfVVfWy4WqHywWWwvwZXz==z1:` `  ..(
# llllllltOOwWXHmmmmmmHMfff@HpZppppWM@@NHbkkW@HkkbHJW+` .WkmJvY"=!`` `  ` `  `` __< ` `  ```` _?TC=``.7!` .(HW@HHkfWHWHkfffVfWsVWHkXkOXwrOtZwv!.-_-_~(dz
# lllltlzlOdWWqHHmmmHMgHfffMHpZpfpppM@@MHbWbkH@HkkbH/_7  .7_...````````  `     ` _( `  ` ``````.``````   .`jHWHM@MkfWWHgkfpfWHkWAvWWWOtlOXwwv<(:(<((jwZX
# zllzlOGdWWkH@HmHHgmHgHffWMHpyfpfppHMM>HHkkHHH@HkkWH,`...........``````  `` `    `  `  `````` ....... .``.HpWH@H@MHWHHHHHfppfWHHkkzUktltlzI+&z+<?CdSXXX
# lzugkHbHHWHHH9AHHHVWg@ffWMHpZpppppWHD:?HpbbHkHMNbbHH,._....._.._.```` `  ` `  `   ` ` ` ``` _`-.........WpWH@H@@HMNHHWH@HWfpfffWHHkJSZzlll==zTXy+-?XWH
# HkWHHWkHBUOltdHVVVWggMfpM@HpXpfppfpMb~vWbbbkHbHH@HkbH&_.....~....````` `  `  `  `   `  ``````..`_..-_..XWHH@@@H@@H@NqpWH@MHpfpWWXWHHkXyOll==z=uXWkkXZW
# WWU90llllltzdVVyVVHgM#fWMHHfXppppWWHN_>XkbbpWNpHHMVbkkh-.......`.```` ` `  `  `  ` ` ` `````````.`....WWDdM@H@@g@H@NMkpM@@HMkpffWXZWgHXkttltuWqHqHHHWX
# _?TwzzlttldWXyVyVWHNMffWMHHWXffppWXWMp~dHbbppWHbHHb~7WkHe-` `````````  ` ` ` ` ` `    `   ````````` (X=J<H@@@@Mg@M@MMMWW@@@@@MkWfWXvUHHkWwgmmHgHHWUIzz
# ::::<zyOdWXyyVyVWgHHNfWHMHHRWppppWXWMMxJWHppppWHpHH_`._74Wm..``````  ` `  ` ``  ` ``     `  ` `` `.7!`.%(M@@@@HHHWMMH@NW@HmH@MHHkpkXzvWHHHHHBBUWS&O==l
# ::::;:(7kyyyVVVWgHMMHWMM@gpSppfVVSdpMHMgWMWpppfWNbWR.` _ `  _?``` ` ` ` ` `  .... ` `` `  `  `  `  `  Z(@Hg@g@qq#X@@@@MH@mmg@MMgHHkkz1zWHHHWWXuuuXww0y
# :;;:;;:;<4WyVVWkHMM#XWMMggWdWyfXX0dpHHMMWHNpppWWHMHH.?i-`` ``    `  `  ` `.Z1;;<1Zl   ` `  `  `   ` `(ggggqmgHkWSHHHgg@gHqqqHHSXuvwHWyOwWHgKWkXZuuuuuw
# XA&+<;;;;<vWyWHMMkY1WMMMHHSX0XWzwIdpHMHMHHHNpppWXWMHb ` ?<.`` ` `  ` `   (>;;;;;;;d:  `  `  `  `` ` .HgHmHHqqpbKdWmqmmgHHHHWVVyXkmHSdWWyXyHNz=zVWkZXkV
# XwZXWHex>+>?HgMMH[ .dMMMgHXSzXWXwIdpWM@MHWHMNppfWZWMH[  ` (- ` ` `  ` ` `u+;;;;:;+2 `  ` ` ` `  _` .HqqqHpkHHfKwSXkkqqHHWffWWWHHqqHOlzWfVyVHZ====1f'``
# Zy0XXWWVWez=zHHHM#AdMHHgHHdXZWWkwIdfH@MMNW@NWHfVyXOWMH;  ` ..  `  `  ` `  ?<+<<<?``  `  ` ` ` ``` .HHqkHfWWYT77!???7"TWWkWHbHMmkkq6lllzWWVyWb=z=z^``
# UOwyWXXXVWMmyzW@MVVW@@MggSfZWWWkXIXfMMMMNpHNpWHfkwOwXWHx.   _`  ` ` ` ` `` `` .`   `  `   `  `  .dkWHWHV= .!`      ` _._(zTYY9YUW0yuzzlzWyyWH?12``  `
# XyWWSwVyWWgmNWHWHVWM@@MHHXfyVWHWXlXfMMHpHfWMpHMNWkwOwZWNe-.`` ` `  ` `  `  `` _`` `` ` ` `  ``.dHWWpWV! .!`      ` .-~~        `  `` _Tx=WyWWz^``  `.(
# WHSwXVfWgggH@@HHXWHM@HMHXHVVVWHykzVWHpppHWfH@@@HMHfkXZAXWmV&-. ` ``  ` `  `      `  ` ` ``` .dmHHkpK!  .`    `   ``          `          ?wHWY``  ` (::
# WXXVVWHgggH@MgHHWWHbWkHSHHVVyWHy0dVWHbbpWkWWHMM@@@NkffWWwWWHeVu.. ` `  ` `  ` ` ` ` ` `` .JgHHmqqY:   .`                  `   .._________~(^   ` .(;;<
# XWyWHgmgH@MggHMHyHNkbpHXmHyVyHHVkdVWWHkMHNVWM@@@MH@MNWppWkXHHHWxvO+. ``  ` ` ` ` ` ```.(HMHHMNH@<`    _`                ` ..JdWHHHHHHmgJ_J`  ` _<1<<+1
# yWWHHHHMHggg@@MyWH@@M#dmgHVyyHNySXyWM@MMMMXVM@HH@@@@@MNkpfpffpVWHmx+7z-.``` ` `` ` .J=<J@@@@MHD_   ` .           `  ` ` .dWZyWyWQkWkWW@H#`` `  _:<O=uS
# WggmNJMgggH@@HMyX@@@MdMMmHWyyWNyyyyH@@@@HMKVHH@M@@@@@$cdNkppppWhJWWW+;:<71-. `  .JC<:::(MMMHH@_    ` _`  `  `     `   (XZZyyWkY>~_`__:+?%``  `  _:<zSz
# ggggggggg@@HM@@VXMHMX@@NWmHyyWHWyyyWgg@@HHNWWMM@@@@@@g@HH@MkfpppHs+TkW+<:::(??7C(::::::<zdkHM~       :  `      `    (dXyyyWWY~ `  .(<! ._ ` ` `  _:<Oy
# mggggmgg@MM@@@HHWM#X@@@@HHqkyWHHyZyWHHHkHHMHWMg@@Hgg@g@@@@@MMkpHkWh<?UWe<::::::::::::::(dkkH%     ` ._   .    ` ` _(HfpfWW9~    .(!`  ` 1``  `    _::O
# ggmmgmHM@@@HH#WkXBd@@gHHHXqHkXqNyyyXHWHMgggMWWHHqggHg@ggg@HMMMNkWHWW<:?Wn:::::::~::~::(dbkHF       `._  .~    ` .(XHkbbW#>` ``./!   `  ` l ` `     ~::
# gmmgmH@@@HHY3jHMSHHqqkHHHHXHHkWHHyZXSdHHggg@NyHWgggHMggggHM@MM8VWWHHW_:?W<::~::~::::~_dpkbK``  `   ` ;` ~~     _JdHWkHH@:` ` .``  `` `  ` ?+. ....._::
# mmmHH@@@M9>_+MHWHWHHHHHkkHqXHqXqHkyWWggggHHHHNXMHHMgmgggMH@M9Izd?WWMHh:~Jr:::::::~~``JWpWW\          < .~~ `  (+1WHqHHD<``      `    `` ` `j?&``.`.-<<
# mqH@@HHY<<;jMHXkHHHHmHYY1>>vkWHWkHkyWHggg@gHkWMkMHgHggBMMMMz<<<J<?HWMH[~J<:::~::~`` (HHppP  `     ` `(__::_ `.+1j@@@H#:~`` `` `  ` `  ` `` .I(h.` ..(<
# WHMHW6<<<>jMkqkHgHH9z>>>>??<?WUHkHNkZWHHMgHkkmgHHHVY3<(@@MD<;<<>::?HWMN(>:::::~`  ,jHWppW>    `      .<_:~_` <<+d@@@M$:_  `  ` `` ` `  `  ``.%.o ` .-j
# HMW6;;;><jWHkkHHH9<>1z<???????ZwWqkHkXMMmHbbHBY>_?4n_~W@@MI;:::::::JKWN<::::~`` (~.WVVVWP`    `  `   `<:~:~_(::<d@@@M<::_-.  `      ``  ` `.>`._I.` _d
# NV<;;;;;;dmkH$dH$<<>>>+>>??????+HyWkHkXHmHY>~~~~~:~_?4M@@N<<::::::::HfM<::~` ` /  dVVWVK`    `   _    ._::::_:~(d@H@Hz:::::_.` `  ` ` `` `.2 .~(+v+..H
# $(::;;;;jHHH3;WH;>>>>>>><<~~~~<(HHNkWHHkH_~~~~~~~~~~__HHHHo+<((((_(:dX#~` ` ` (` (WVVWX!  `       __~..<~~::~::(jH@@HR<:::::__ `  `  `  `./ ._(+zwwyWK
# (::::;;:dHH$<;?W+>;::::~~:__- .HHHqHHkUWHk&__.....````dHpbh_   ` ```-H] `  ` _ .JffVWX!             _~__1:~~:~:~(W@MHNz+<:::::__.```` `  c`._<1zwXX9=<
# ::::::<<dHX;;;;;1+;;;;;:_((:~(HHkHHpkH6YOwVWa,..``````,NpbWh:__...   H!  ``-_`.XfffWf`  `     `   ` ` _<(<(~:~~::?M@@MN=1i:::::::___.  ./ .(+zOwXHJ(((
# ::::::::WHP:;;;;;;;;;;;>>>><jHWHWXWWk$(_~._<77T1.```   wWppph<~____ .`` ```..WWWfVX^  `            `   ___<+_<_~:~?H@@@Nzz1+::::::::~_(2 _(+zOwZyWk<?7
# :~::::::dHk::;;:;;;;;;;;>>;jWWUV1KWbH~_<....`````       4WppWHx.` ` !``..(WHpfpWK= `       `           `.~_<<1++~:~<THH@Mmzzz<:::::::<2__(+zwwZyyVWHe+
# ~:~~:::::4Xc::::;:;;:;;;;+dWXX6>dWWHR~~(-..````        ` ?WppWpWHkAAQWHHHpfppWY^              `        `..~~~~(?T&~~~<TMMMMNgd&<<<;<<v ~(+zwXZyyVyVfHH

