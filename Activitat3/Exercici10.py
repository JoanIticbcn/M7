abecedari = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

j=1
while j< len(abecedari):
    if j%3 == 0:
        abecedari.pop(j)
    j+=1

tuplaabc = tuple(abecedari)
print(abecedari)
print(tuplaabc)