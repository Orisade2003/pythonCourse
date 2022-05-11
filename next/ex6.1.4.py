import base64
import codecs


def decode_msg(encoded_msg):
    """
    The function decodes a given encoded message
    :param encoded_msg: given encoded message
    :type encoded_msg: str
    :return: the function returns the decoded message
    :rtype: str
    """
    decoded = base64.b64decode(encoded_msg)
    return codecs.decode(decoded)

def main():
    encoded_msg = """CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAg
    ICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tL
    S0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgIC
    AgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgI
    CAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAg
    ICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X1
    9fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgI
    CAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo="""
    print(decode_msg(encoded_msg))


if __name__ == "__main__":
    main()
