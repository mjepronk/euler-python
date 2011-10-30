# vim: sw=4:ts=4:et:ai
from eulertools import triangle_numbers, pentagonal_numbers, hexagonal_numbers

def main():
    t_gen = triangle_numbers()
    p_gen = pentagonal_numbers()
    h_gen = hexagonal_numbers()
    t_num = next(t_gen)
    p_num = next(p_gen)
    h_num = next(h_gen)
    while True:
        # Synchronize pentagonal number with triangle number
        while p_num < t_num:
            p_num = next(p_gen)
        # Synchronize hexagonal number with triangle number
        while h_num < t_num:
            h_num = next(h_gen)
        # If all are equal and higher than 40755 then we've found it
        if t_num > 40755 and t_num == p_num and t_num == h_num:
            break
        t_num = next(t_gen)
    return t_num

if __name__ == '__main__':
    print("Result: %i" % main())

