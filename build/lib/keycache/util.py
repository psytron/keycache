import platform as p
import uuid
import hashlib


def basic():
    sb = []
    sb.append(p.node())
    sb.append( ''.join([ x for x in p.architecture() ]) )
    sb.append(p.machine())
    sb.append(p.processor())
    sb.append(p.system())
    sb.append(str(uuid.getnode())) # MAC address
    text = '.'.join(sb)
    return text