import logging, socket, typing

from struct import unpack
# from dataclasses import dataclass
from collections import namedtuple

# @dataclass(init=True)
# class IMUData:
#     # Attitude
#     latitude: double
#     longitude: double
#     altitude: double
#     heading: double
#     velocityN: double
#     velocityE: double
#
#     # IMU
#     accelX: double
#     accelY: double
#     accelZ: double
#     rateRoll: double
#     ratePitch: double
#     rateYaw: double
#
#     # trailer
#     magic: int

IMUData = namedtuple('IMUData', [
    'latitude', 'longitude', 'altitude',
    'heading', 'velocityN', 'velocityE',
    'accelX', 'accelY', 'accelZ',
    'rateRoll', 'ratePitch', 'rateYaw',
    'magic'
    ])

log = logging.getLogger('udpserver')
dd  = '!12dI'


def udpserver(host='127.0.0.1', port=5501):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    log.info("Listening on udp %s:%s" % (host, port))
    s.bind((host, port))
    while True:
        (data, addr) = s.recvfrom(128 * 1024)
        yield IMUData(*unpack(dd, data))


FORMATCONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMATCONS)

if __name__ == '__main__':
    for data in udpserver():
        log.debug("%r" % (data,))
