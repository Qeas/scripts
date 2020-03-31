a = int(input())
b = int(input())
c = int(input())
d = int(input())

out_string = ''
for i in range(c, d + 1):
    out_string += '\t%s' % i

out_string += '\n%s' % a


def inc_out(out_string, horiz, vert):
    if horiz < d:
        mult = horiz * vert
        out_string += '\t%s' % mult
        horiz += 1
        out_string = inc_out(out_string, horiz, vert)
    elif vert <= b:
        mult = d * vert
        out_string += '\t%s' % mult
        vert += 1
        if vert <= b:
            out_string += '\n%s' % vert
            out_string = inc_out(out_string, c, vert)
    return out_string


print(inc_out(out_string, c, a))
