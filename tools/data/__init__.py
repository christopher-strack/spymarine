# ruff: noqa: E501

DEVICE_COUNT_RESPONSE = b"\x00\x00\x00\x00\x00\xff\x02\x85\xde\xc3\x46\x00\x11\xff\x01\x01\x00\x00\x00\x1f\xff\x02\x01\x00\x00\x00\x29\xff\x13\x14"

DEVICE_INFO_RESPONSES = [
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x01\x61\xff\x00\x01\x00\x00\x00\x00\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x0a\xff\x02\x01\x00\x00\x00\x00\xff\x03\x01\x85\xde\xc3\x46\xff\x04\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x05\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x06\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x07\x03\x65\x0c\x5d\xae\xff\x00\x00\x00\x02\xff\x08\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x09\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x0a\x04\x00\x00\x00\x00\xff\x50\x69\x63\x6f\x38\x37\x31\x30\x00\xff\x0b\x03\x00\x00\x00\x00\xff\xc0\xa8\x01\x01\xff\x0c\x03\x00\x00\x00\x00\xff\x00\x00\x13\x89\xff\x0d\x03\x00\x00\x00\x00\xff\xc0\xa8\x01\xff\xff\x0e\x03\x00\x00\x00\x00\xff\x00\x00\xa8\xca\xff\x0f\x04\x00\x00\x00\x00\xff\x70\x69\x63\x6f\x32\x32\x34\x35\x00\xff\x10\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x11\x03\x64\xe2\xb5\x94\xff\x00\x00\x00\x64\xff\x12\x03\x64\xe3\xa0\xc9\xff\x00\x00\x00\x0a\xff\x13\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x14\x03\x00\x00\x00\x00\xff\x00\x00\x00\x28\xff\x15\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x16\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x17\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x18\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x19\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x1a\x01\x00\x00\x00\x00\xff\x1b\x03\x00\x00\x00\x00\xff\x00\x00\x00\x3c\xff\x1c\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff\x1d\x03\x65\x1a\x5b\xd6\xff\x00\x00\x00\x18\xff\x57\xea",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x54\xff\x00\x01\x00\x00\x00\x01\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x07\xff\x02\x01\x00\x00\x00\x00\xff\x03\x01\x85\xde\xc3\x46\xff\x04\x03\x65\x33\xcf\xb8\xff\x00\x00\x1c\x20\xff\x05\x03\x3f\xce\x97\x24\xff\x00\x00\x00\x00\xff\x06\x03\x00\x00\x00\x00\xff\x00\x00\x00\xff\xff\x07\x03\x00\x00\x00\x00\xff\xc9\x62\xf6\x46\xff\x4f\x4f",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x6c\xff\x00\x01\x00\x00\x00\x02\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x04\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x00\x00\x00\x00\xff\x53\x65\x6e\x73\x6f\x72\x20\x31\x00\xff\x04\x01\x85\xde\xc3\x46\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\xd2\xad\x42\x4e\xff\x00\x00\x00\x00\xff\x07\x03\x69\xc8\x7c\x55\xff\x00\x00\x00\x00\xff\x08\x03\x00\x00\x00\x00\xff\x00\x00\x00\xff\xff\x09\x03\x00\x00\x00\x00\xff\x69\x96\x0d\x9a\xff\x1a\x82",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x16\xff\x00\x01\x00\x00\x00\x03\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff\x16\x9f",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x16\xff\x00\x01\x00\x00\x00\x04\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff\x19\x5b",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x72\xff\x00\x01\x00\x00\x00\x05\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x05\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x00\x00\x00\x00\xff\x42\x61\x72\x6f\x6d\x65\x74\x65\x72\x00\xff\x04\x01\x85\xde\xc3\x46\xff\x05\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff\x06\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x07\x03\x00\x00\x00\x00\xff\x00\x00\x00\xff\xff\x08\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x09\x03\x00\x00\x00\x00\xff\x6a\xe5\xc8\x5d\xff\x07\xd5",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x59\xff\x00\x01\x00\x00\x00\x06\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x01\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x00\x00\x00\x00\xff\x50\x49\x43\x4f\x20\x49\x4e\x54\x45\x52\x4e\x41\x4c\x00\xff\x04\x01\x85\xde\xc3\x46\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\x00\x00\x00\x00\xff\x00\x00\x00\xff\xff\x07\x03\x00\x00\x00\x00\xff\x78\x66\x4c\x81\xff\x60\xcd",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x16\xff\x00\x01\x00\x00\x00\x07\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff\x74\xac",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x16\xff\x00\x01\x00\x00\x00\x08\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff\xbf\x0e",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x16\xff\x00\x01\x00\x00\x00\x09\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff\x6b\x24",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x5a\xff\x00\x01\x00\x00\x00\x0a\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x01\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x20\x31\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x1a\xff\x07\x03\x00\x00\x00\x00\xff\x5c\x20\x52\x0b\xff\x21\xcb",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x5a\xff\x00\x01\x00\x00\x00\x0b\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x01\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x20\x32\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x02\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x1c\xff\x07\x03\x00\x00\x00\x00\xff\x53\x2e\xe4\x5d\xff\xe7\xeb",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x5a\xff\x00\x01\x00\x00\x00\x0c\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x01\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x20\x33\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x03\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\xff\xff\x07\x03\x00\x00\x00\x00\xff\x57\x1e\xe8\x91\xff\xaa\x7a",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x66\xff\x00\x01\x00\x00\x00\x0d\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x06\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x20\x31\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x00\xff\x07\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x1d\xff\x08\x03\x00\x00\x00\x00\xff\x39\xd8\x68\x8f\xff\x71\x46",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x66\xff\x00\x01\x00\x00\x00\x0e\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x06\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x20\x32\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x02\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x00\xff\x07\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x1e\xff\x08\x03\x00\x00\x00\x00\xff\xdc\xc7\x9f\x4e\xff\x6d\x3c",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x66\xff\x00\x01\x00\x00\x00\x0f\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x06\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x20\x33\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x03\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x00\xff\x07\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x1f\xff\x08\x03\x00\x00\x00\x00\xff\x9d\x5b\x04\x6f\xff\xcb\x31",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x66\xff\x00\x01\x00\x00\x00\x10\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x06\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x20\x34\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x04\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x00\xff\x07\x03\x64\x39\xb5\xea\xff\x00\x00\x00\xff\xff\x08\x03\x00\x00\x00\x00\xff\xf4\xd1\x7f\x4a\xff\xc0\xd2",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x58\xff\x00\x01\x00\x00\x00\x11\xff\x01\x03\x64\x39\xb5\xea\xff\x00\x00\x00\x0e\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x39\xb5\xea\xff\x53\x54\x31\x30\x37\x20\x5b\x35\x35\x39\x36\x5d\x00\xff\x04\x01\x08\x56\x2d\xfc\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\x64\x39\xb5\xea\xff\x00\x00\x00\xff\xff\x07\x03\x00\x00\x00\x00\xff\x49\xa6\x97\xa3\xff\x42\xb4",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\xac\xff\x00\x01\x00\x00\x00\x12\xff\x01\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x02\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x72\x39\xbd\xff\x53\x43\x33\x30\x33\x20\x5b\x35\x34\x39\x39\x5d\x00\xff\x04\x01\x2a\x1b\xce\xdb\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x64\xff\x07\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x02\xff\x08\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x01\xff\x09\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x01\xff\x0a\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x18\xff\x0b\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x01\xff\x0c\x03\x00\x00\x00\x00\xff\xaf\xa3\x75\x2b\xff\x0d\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x7f\xff\x0e\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x02\xff\x9e\x3a",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x5a\xff\x00\x01\x00\x00\x00\x13\xff\x01\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x01\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x72\x39\xbd\xff\x53\x43\x33\x30\x33\x20\x5b\x35\x34\x39\x39\x5d\x20\x31\x00\xff\x04\x01\x2a\x1b\xce\xdb\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x18\xff\x07\x03\x00\x00\x00\x00\xff\xe3\x6d\xa2\xc2\xff\x98\xe1",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x5a\xff\x00\x01\x00\x00\x00\x14\xff\x01\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x01\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x72\x39\xbd\xff\x53\x43\x33\x30\x33\x20\x5b\x35\x34\x39\x39\x5d\x20\x32\x00\xff\x04\x01\x2a\x1b\xce\xdb\xff\x05\x01\x00\x00\x00\x02\xff\x06\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x1b\xff\x07\x03\x00\x00\x00\x00\xff\x92\xcd\x27\x18\xff\x42\x57",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x66\xff\x00\x01\x00\x00\x00\x15\xff\x01\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x06\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x72\x39\xbd\xff\x53\x43\x33\x30\x33\x20\x5b\x35\x34\x39\x39\x5d\x20\x31\x00\xff\x04\x01\x2a\x1b\xce\xdb\xff\x05\x01\x00\x00\x00\x01\xff\x06\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x00\xff\x07\x03\x64\x72\x39\xbd\xff\x00\x00\x00\xff\xff\x08\x03\x00\x00\x00\x00\xff\x19\x54\x5d\x50\xff\xe1\x12",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x66\xff\x00\x01\x00\x00\x00\x16\xff\x01\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x06\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x72\x39\xbd\xff\x53\x43\x33\x30\x33\x20\x5b\x35\x34\x39\x39\x5d\x20\x32\x00\xff\x04\x01\x2a\x1b\xce\xdb\xff\x05\x01\x00\x00\x00\x02\xff\x06\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x00\xff\x07\x03\x64\x72\x39\xbd\xff\x00\x00\x00\xff\xff\x08\x03\x00\x00\x00\x00\xff\x4d\x19\x42\xef\xff\xdb\xc7",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\x66\xff\x00\x01\x00\x00\x00\x17\xff\x01\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x06\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x72\x39\xbd\xff\x53\x43\x33\x30\x33\x20\x5b\x35\x34\x39\x39\x5d\x20\x33\x00\xff\x04\x01\x2a\x1b\xce\xdb\xff\x05\x01\x00\x00\x00\x03\xff\x06\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x00\xff\x07\x03\x64\x72\x39\xbd\xff\x00\x00\x00\x19\xff\x08\x03\x00\x00\x00\x00\xff\x12\x7e\x7a\x38\xff\x45\xa5",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x01\x06\xff\x00\x01\x00\x00\x00\x18\xff\x01\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x09\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x72\x3e\x77\xff\x42\x75\x6c\x6c\x74\x72\x6f\x6e\x00\xff\x04\x03\x00\x00\x00\x00\xff\x00\x00\x00\x13\xff\x05\x03\x64\x72\x3e\x77\xff\x00\x00\x75\x30\xff\x06\x03\x64\x72\x3e\x77\xff\xff\xff\xfc\x18\xff\x07\x03\x64\x72\x3e\x77\xff\xff\xff\xfc\x18\xff\x08\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x06\xff\x09\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x7d\xff\x0a\x03\x64\x77\x7a\x8b\xff\x00\x00\x00\x19\xff\x0b\x03\x64\x72\x3e\x77\xff\x00\x00\x00\xff\xff\x0c\x03\x00\x00\x00\x00\xff\x48\x22\x6a\x52\xff\x0d\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x02\xff\x0e\x03\x64\x72\x3e\x77\xff\x00\x00\x00\xc8\xff\x0f\x03\x64\x72\x3e\x77\xff\x00\x00\x03\xe8\xff\x10\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x01\xff\x11\x03\x64\x72\x3e\x77\xff\x00\x00\x27\x10\xff\x12\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x01\xff\x13\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x73\xff\x14\x03\x64\x72\x3e\x77\xff\x00\x00\x00\x0a\xff\x15\x03\x64\x72\x3e\x77\xff\x00\x00\x01\x2c\xff\x48\xa2",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\xa8\xff\x00\x01\x00\x00\x00\x19\xff\x01\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\x03\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x7b\x3f\x64\xff\x42\x61\x74\x74\x65\x72\x69\x65\x00\xff\x04\x01\x00\x00\x00\x00\xff\x05\x01\x00\x00\x00\x00\xff\x06\x03\x64\x72\x3f\x7e\xff\x00\x00\x00\x01\xff\x07\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\x00\xff\x08\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\xff\xff\x09\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\x01\xff\x0a\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\x00\xff\x0b\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\x00\xff\x0c\x03\x00\x00\x00\x00\xff\x4b\xeb\xdc\xb2\xff\x0d\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\x01\xff\x0e\x03\x64\x72\x3f\x6a\xff\x00\x00\x00\x00\xff\xc1\x03",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x01\x18\xff\x00\x01\x00\x00\x00\x1a\xff\x01\x03\x64\x73\x5c\x09\xff\x00\x00\x00\x08\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x73\x5c\x09\xff\x46\x72\x69\x73\x63\x68\x77\x61\x73\x73\x65\x72\x00\xff\x04\x01\x36\xe8\x50\x6d\xff\x05\x01\x00\x00\x00\x00\xff\x06\x03\x64\x73\x5c\x09\xff\x00\x00\x00\x01\xff\x07\x03\x64\x73\x5c\x09\xff\x00\x00\x03\xe8\xff\x08\x03\x64\x73\x5c\x09\xff\x00\x00\x00\x02\xff\x09\x03\x64\x81\xac\x12\xff\x00\x00\x00\x21\xff\x0a\x03\x64\x81\xac\x12\xff\x00\x64\x02\x0a\xff\x0b\x03\x64\x81\xac\x12\xff\x00\xc8\x03\x36\xff\x0c\x03\x64\x81\xaf\x0a\xff\x01\x2c\x03\x84\xff\x0d\x03\x64\x81\xaf\x0a\xff\x01\x90\x03\xf4\xff\x0e\x03\x64\x81\xaf\x0a\xff\x01\xf4\x04\x42\xff\x0f\x03\x64\x81\xaf\x0a\xff\x02\x58\x04\x88\xff\x10\x03\x64\x81\xaf\x0a\xff\x02\xbc\x04\xe3\xff\x11\x03\x64\x81\xaf\x43\xff\x03\x52\x05\x47\xff\x12\x03\x64\x81\xaf\xce\xff\x03\xe8\x05\xae\xff\x13\x03\x64\x73\x5c\x09\xff\x7f\xff\xff\xff\xff\x14\x03\x64\x73\x5c\x09\xff\x00\x00\x00\xff\xff\x15\x03\x64\x73\x5c\x09\xff\x00\x00\x00\x01\xff\x16\x03\x00\x00\x00\x00\xff\x6d\xfe\xe7\xb0\xff\x17\x03\x64\x73\x5c\x09\xff\x00\x00\x00\x01\xff\xb6\x10",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x01\x0d\xff\x00\x01\x00\x00\x00\x1b\xff\x01\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x09\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x77\x7a\xd0\xff\x53\x74\x61\x72\x74\x65\x72\x62\x61\x74\x74\x65\x72\x69\x65\x00\xff\x04\x03\x00\x00\x00\x00\xff\x00\x00\x00\x14\xff\x05\x03\x64\x77\x7a\xd0\xff\x00\x00\x27\x10\xff\x06\x03\x64\x77\x7a\xd0\xff\xff\xff\xfc\x18\xff\x07\x03\x64\x77\x7a\xd0\xff\xff\xff\xfc\x18\xff\x08\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x03\xff\x09\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x7d\xff\x0a\x03\x00\x00\x00\x00\xff\x00\x00\x00\xff\xff\x0b\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\xff\xff\x0c\x03\x00\x00\x00\x00\xff\x22\x94\x91\xfb\xff\x0d\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x02\xff\x0e\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\xc8\xff\x0f\x03\x64\x77\x7a\xd0\xff\x00\x00\x03\xe8\xff\x10\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x01\xff\x11\x03\x64\x77\x7a\xd0\xff\x00\x00\x27\x10\xff\x12\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x01\xff\x13\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x73\xff\x14\x03\x64\x77\x7a\xd0\xff\x00\x00\x00\x0a\xff\x15\x03\x64\x77\x7a\xd0\xff\x00\x00\x01\x2c\xff\x53\xb4",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x01\x14\xff\x00\x01\x00\x00\x00\x1c\xff\x01\x03\x64\x78\x6d\x87\xff\x00\x00\x00\x08\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x78\x6d\x87\xff\x41\x62\x77\x61\x73\x73\x65\x72\x00\xff\x04\x01\x46\x2a\xcd\x7d\xff\x05\x01\x00\x00\x00\x00\xff\x06\x03\x64\x78\x6d\x87\xff\x00\x00\x00\x03\xff\x07\x03\x64\x81\xc1\x07\xff\x00\x00\x02\xbc\xff\x08\x03\x64\x78\x6d\x87\xff\x00\x00\x00\x02\xff\x09\x03\x64\x81\xb2\x9c\xff\x00\x46\x00\x5b\xff\x0a\x03\x64\x81\xb3\x70\xff\x00\x8c\x00\xd4\xff\x0b\x03\x64\x81\xbc\x3b\xff\x00\xd2\x01\x85\xff\x0c\x03\x64\x81\xbc\xf7\xff\x01\x18\x02\x2f\xff\x0d\x03\x64\x81\xbd\xbe\xff\x01\x5e\x02\xce\xff\x0e\x03\x64\x81\xbe\x66\xff\x01\xa4\x03\x7b\xff\x0f\x03\x64\x81\xbe\xfd\xff\x01\xea\x04\x01\xff\x10\x03\x64\x81\xbf\x9f\xff\x02\x30\x04\xc5\xff\x11\x03\x64\x81\xc0\x5a\xff\x02\x76\x06\x2f\xff\x12\x03\x64\x81\xc1\x01\xff\x02\xbc\x07\x8b\xff\x13\x03\x64\x78\x6d\x87\xff\x7f\xff\xff\xff\xff\x14\x03\x64\x78\x6d\x87\xff\x00\x00\x00\xff\xff\x15\x03\x64\x78\x6d\x87\xff\x00\x00\x00\x01\xff\x16\x03\x00\x00\x00\x00\xff\x11\x19\x50\x40\xff\x17\x03\x64\x78\x6d\x87\xff\x00\x00\x00\x01\xff\xa8\x20",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\xa5\xff\x00\x01\x00\x00\x00\x1d\xff\x01\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x03\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x79\xe1\xb2\xff\x49\x6e\x6e\x65\x6e\x00\xff\x04\x01\x00\x00\x00\x00\xff\x05\x01\x00\x00\x00\x00\xff\x06\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x01\xff\x07\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x00\xff\x08\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\xff\xff\x09\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x01\xff\x0a\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x00\xff\x0b\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x00\xff\x0c\x03\x00\x00\x00\x00\xff\x39\xf3\xee\xbc\xff\x0d\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x03\xff\x0e\x03\x64\x79\xd9\xc7\xff\x00\x00\x00\x00\xff\x22\xff",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\xa6\xff\x00\x01\x00\x00\x00\x1e\xff\x01\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x03\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x79\xe1\xc6\xff\x41\x75\xa3\x65\x6e\x20\x00\xff\x04\x01\x00\x00\x00\x00\xff\x05\x01\x00\x00\x00\x00\xff\x06\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x01\xff\x07\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x00\xff\x08\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\xff\xff\x09\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x01\xff\x0a\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x00\xff\x0b\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x00\xff\x0c\x03\x00\x00\x00\x00\xff\x40\xcd\xf9\xee\xff\x0d\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x02\xff\x0e\x03\x64\x79\xe1\xc6\xff\x00\x00\x00\x00\xff\x07\x0c",
    b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x00\xa6\xff\x00\x01\x00\x00\x00\x1f\xff\x01\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x03\xff\x02\x01\x00\x00\x00\x00\xff\x03\x04\x64\x7a\xf8\xbf\xff\x42\x6f\x69\x6c\x65\x72\x00\xff\x04\x01\x00\x00\x00\x00\xff\x05\x01\x00\x00\x00\x00\xff\x06\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x01\xff\x07\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x00\xff\x08\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\xff\xff\x09\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x01\xff\x0a\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x00\xff\x0b\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x00\xff\x0c\x03\x00\x00\x00\x00\xff\x76\x6d\xe3\x7e\xff\x0d\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x07\xff\x0e\x03\x64\x7a\xf8\xbf\xff\x00\x00\x00\x00\xff\x79\x25",
]


STATE_RESPONSE = b"\x00\x00\x00\x00\x00\xff\xb0\x85\xde\xc3\x46\x01\x14\xff\x00\x01\x65\x46\x86\xea\xff\x01\x01\x65\x46\xa2\xdf\xff\x02\x01\xff\xff\xfc\x16\xff\x03\x01\x00\x01\x7e\xbf\xff\x04\x01\xff\xff\xff\xb9\xff\x05\x01\x00\x00\x33\xcc\xff\x09\x01\x65\x1a\x5b\xd6\xff\x0a\x01\xff\xff\xfc\x16\xff\x0b\x01\x00\x00\x00\x00\xff\x0c\x01\x00\x00\x00\x23\xff\x0d\x01\x00\x00\x00\x00\xff\x0e\x01\x00\x00\x4a\xb1\xff\x0f\x01\x00\x00\x50\x77\xff\x10\x01\x00\x00\x15\x67\xff\x11\x01\x00\x00\xff\xff\xff\x12\x01\x3f\xce\x97\x24\xff\x13\x01\xff\xff\xff\x85\xff\x14\x01\x00\x03\xd8\xa8\xff\x15\x01\x00\x00\x34\x02\xff\x16\x01\x00\x00\x2f\xe4\xff\x17\x01\x00\x00\xff\xff\xff\x18\x01\x00\x00\xff\xff\xff\x19\x01\x00\x00\x4c\xc3\xff\x1a\x01\x36\xf0\x67\x02\xff\x1b\x01\xff\xff\xff\x85\xff\x1c\x01\x00\x00\x34\x02\xff\x1d\x01\x7f\xff\xff\xff\xff\x1e\x01\xff\xf6\x71\xae\xff\x1f\x01\x00\x00\x00\x65\xff\x20\x01\x00\x00\x00\x00\xff\x21\x01\x1d\x50\x1f\x18\xff\x22\x01\x7f\xff\xff\xff\xff\x23\x01\x00\x00\x2f\xe4\xff\x24\x01\x7f\xff\xff\xff\xff\x25\x01\x7f\xff\xff\xff\xff\x26\x01\x00\x34\x00\x25\xff\x27\x01\x00\x00\x00\x6b\xff\x28\x01\x00\x00\x00\x5b\xff\x29\x01\x00\x00\x01\x8a\xff\xa4\xe9"
