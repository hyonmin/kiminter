print("{0: >10}" .format(50))
print("{0:>10}" .format(50))
print("{0: >+10}" .format(50))
print("{0: >10}" .format(-50))
print("{0:->10}" .format(50))
print("{0:_<10}" .format(5000))
print("{0:,<10}" .format(5000))

print("{0:,}" .format(1000000))
print("{0:+,}" .format(1000000))
print("{0:,}" .format(-1000000))
print("{0:+,}" .format(-1000000))

print("{0:^<+30,}" .format(1000000))

print("{0:f}" .format(5/3))
print("{0:.2f}" .format(5/3))
print("{0}" .format(round(5/3, 2)))
