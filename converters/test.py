before_mid = list(set([1, 2.1, 3.3, 3.4, 3.4,2.4,6.1,6.2,3.8,3.11, 8.1, 8.2, 3.5, 3.6, 8.1, 8.2, 9.1, 9.1, 9.3]))
print(sorted(before_mid))

after_mid = list(set([9.4, 9.7, 9.4,3.7, 10.1, 10.4, 10.5,10.5,10.2,21.1, 21.2, 21.2,13.1, 13.2, 21.5, 23.1, 23.2,23.2 , 23.4, 25.4]))
print(sorted(after_mid))

before_mid.extend(after_mid)

print(sorted(before_mid))