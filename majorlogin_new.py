"""
majorlogin_new.py  (v17)
New MajorLogin payload (OB55 / 1.134.14 style), taken from the account tool's PyL().
Standalone: only needs pycryptodome. Used by login_engine.build_majorlogin_payload().
"""
import uuid
from datetime import datetime, timezone
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

_KEY = b'Yg&tc%DEuh6%Zc^8'
_IV = b'6oyZDr22E3ychjM%'


def _varint(n):
    d = []
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            b |= 0x80
        d.append(b)
        if not n:
            break
    return bytes(d)


def _proto(fields):
    out = bytearray()
    for f, v in fields.items():
        if isinstance(v, int):
            out += _varint((f << 3) | 0) + _varint(v)
        elif isinstance(v, (str, bytes)):
            b = v.encode() if isinstance(v, str) else v
            out += _varint((f << 3) | 2) + _varint(len(b)) + b
        elif isinstance(v, dict):
            n = _proto(v)
            out += _varint((f << 3) | 2) + _varint(len(n)) + n
    return bytes(out)


def build_fields(access_token, open_id, server_time_str, region, client_version=None):
    P = {}
    if region == "IND":
        P[3] = server_time_str
        P[4] = "free fire"
        P[5] = 1
        P[7] = client_version or "1.134.14"
        P[8] = "Android OS 14 / API-34 (UP1A.231005.007/E156BXXS6AYD4)"
        P[9] = "Handheld"
        P[10] = "airtel"
        P[11] = "CarrierDataNetwork"
        P[12] = 2340
        P[13] = 1080
        P[14] = "295"
        P[15] = "ARM64 FP ASIMD AES | 2200 | 8"
        P[16] = 5586
        P[17] = "Mali-G57 MC2"
        P[18] = "OpenGL ES 3.2 v1.r38p1"
        P[19] = f"Google|{uuid.uuid4()}"
        P[20] = "27.61.46.111"
        P[21] = "en"
        P[22] = open_id
        P[23] = "4"
        P[24] = "Handheld"
        P[25] = "samsung SM-A155F"
        P[26] = "IND"
        P[29] = access_token
        P[30] = 1
        P[41] = "airtel"
        P[42] = "4G"
        P[57] = "7428b253defc164018c604a1ebbfebdf"
        P[60] = 108009
        P[61] = 3859
        P[62] = 5023
        P[64] = 3987
        P[65] = 108009
        P[66] = 3987
        P[67] = 108009
        P[70] = 4
        P[73] = 3
        P[74] = "/data/app/~~OlJmIW-Yzl-44x2WnJP4Nw==/com.garena.game.ffi-_eDk_pQQMiFk1YUeqwJBvQ==/lib/arm64"
        P[76] = 3
        P[77] = "dd9d4c174e0472d34b7fd34bd5924bc9|/data/app/~~OlJmIW-Yzl-44x2WnJP4Nw==/com.garena.game.ffi-_eDk_pQQMiFk1YUeqwJBvQ==/base.apk"
        P[78] = 3
        P[79] = 2
        P[81] = "64"
        P[83] = "2019121269"
        P[85] = 3
        P[86] = "OpenGLES2"
        P[87] = 8191
        P[88] = 4
        P[90] = "Coimbatore"
        P[91] = "TN"
        P[92] = 9570
        P[93] = "android"
        P[94] = "KqsHT54jON6bxITmlrRyOrXWBqKqZ4BoqPzT/mhtriAfRt2dt7gC8pnAJfj11alcEUA5sD8BshSYQhxXT9RFmU6YzcI1FKK4MwxJcF4+kvelPD1H"
        P[95] = 111207
        P[96] = '{"cur_rate":null,"support_etc2":false}'
        P[97] = 1
        P[99] = "4"
        P[100] = "4"
        P[104] = 11921
        P[105] = 1
        P[106] = "https://dl-tata.freefireind.in/live/ABHotUpdates/|https://core-tata.freefireind.in/live/ABHotUpdates/|dff941d41e6e3a9e76f05ed71fdc8d87"
        P[107] = "1.6168622e0868ddbd"
    else:
        P[3] = server_time_str
        P[4] = "free fire"
        P[5] = 1
        P[7] = client_version or "1.134.14"
        P[8] = "Android OS 14 / API-34 (UP1A.231005.007/V816.0.15.0.UNQMIXM)"
        P[9] = "Handheld"
        P[10] = "Grameenphone"
        P[11] = "CarrierDataNetwork"
        P[12] = 1666
        P[13] = 750
        P[14] = "352"
        P[15] = "ARM64 FP ASIMD AES | 2400 | 8"
        P[16] = 5563
        P[17] = "Mali-G57 MC2"
        P[18] = "OpenGL ES 3.2 v1.r32p1-01eac0.0a0b917d9265b4c01be9925306306139"
        P[19] = f"Google|{uuid.uuid4()}"
        P[20] = "59.152.5.188"
        P[21] = "en"
        P[22] = open_id
        P[23] = "8"
        P[24] = "Handheld"
        P[25] = "Xiaomi 2312DRAABI"
        P[26] = "BD"
        P[29] = access_token
        P[30] = 1
        P[41] = "Grameenphone"
        P[42] = "Cellular"
        P[57] = "7428b253defc164018c604a1ebbfebdf"
        P[60] = 109685
        P[61] = 58294
        P[62] = 797
        P[63] = 18000
        P[64] = 58818
        P[65] = 109685
        P[66] = 58818
        P[67] = 109685
        P[73] = 2
        P[74] = "/data/app/~~cqQgpdMykLQEM3odipXatw==/com.dts.freefireth-G6e5yOt1dtuXG5Ambhj18g==/lib/arm64"
        P[76] = 1
        P[77] = "b8e0cd5e295eee42f5860d3c86e483dd|/data/app/~~cqQgpdMykLQEM3odipXatw==/com.dts.freefireth-G6e5yOt1dtuXG5Ambhj18g==/base.apk"
        P[78] = 3
        P[79] = 2
        P[81] = "64"
        P[83] = "2019121229"
        P[85] = 3
        P[86] = "OpenGLES2"
        P[87] = 4095
        P[88] = 8
        P[89] = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
        P[90] = "Dhaka"
        P[91] = "C"
        P[92] = 8043
        P[93] = "android"
        P[94] = "KqsHT4XbSZhqerDNUhjbS3DxG/4+I62zQU2tZFJN91kBUICAlZ5yujshLKvjlk/KiShfKfis8EeB1PMhFHIodWPncZC4fCHYF3TcTwNj95aWY/S3"
        P[95] = 111207
        P[96] = '{"cur_rate":[60,90,120],"support_etc2":false}'
        P[97] = 1
        P[98] = 1
        P[99] = "4"
        P[100] = "4"
        P[102] = "GQ]        e"
        P[103] = 1
        P[104] = 45174
        P[105] = 1
        P[106] = "https://dl-bs.ggpolarbear.com/live/ABHotUpdates/|https://core-bs.ggpolarbear.com/live/ABHotUpdates/|a4332cb1c1a84e51dd77441e4856ed5a"
        P[107] = "1.9393e7b8e53e8aeb"

    return P


def build_payload(access_token, open_id, region="BD", client_version=None):
    """returns the AES-encrypted MajorLogin body (bytes)"""
    region = "IND" if str(region).upper() == "IND" else "BD"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    P = build_fields(str(access_token), str(open_id), now, region, client_version)
    return AES.new(_KEY, AES.MODE_CBC, _IV).encrypt(pad(_proto(P), 16))