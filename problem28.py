# vim: sw=4:ts=4:et:ai

def main():
    # Welke ring zitten we in?
    ring = 1
    # Totaal van de diagonalen
    total = 1 
    # Sprong die we maken tussen de diagonalen
    step = 2
    # Het getal waar we zitten
    n = 1
    while True:
        for i in range(4):
            n += step
            total += n
        step += 2
        ring += 1
        if ring > 500:
            break
    return total

 
if __name__ == '__main__':
    print("Result: %i" % main())

