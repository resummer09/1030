import binascii
import ipaddress as ipa

# IPv4 / IPv6 주소를 저장하는 리스트형 변수 생성
Addresses = [
    '192.168.0.5',
    '2001:0:9d38:6abd:480:f1f:3f57:fffb',
]

for ipaddr in Addresses:
    # ipaddress 클래스를 이용하여 주소 객체 생성
    addr = ipa.ip_address(ipaddr)
    # ip주소 객체의 여러가지 속성을 표시한다.
    print(f'IP address:{addr!r}') # 주소를 epr(을 사용하여 강제 형변환
    print(f'IP version:{addr.version}')
    # packed 속성을 사용하여 점 십진법 주소의 각 자리를 2진수로 표현
    ## binascii.hexlify(a) 바이너리 데이터를 16진수로 표현 = a.hex()
    print(f'Packed addr:{binascii.hexlify(addr.packed)}')
    print(f'Integer addr:{int(addr)}')
    print(f'Is private?:{addr.is_private}')
    print()
