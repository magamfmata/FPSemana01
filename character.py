Banshee = str(input("What is your character name? "))
250 =int(input("Health points? "))
30 =int(input("Level? "))

Mermaid = str(input("What is your character name? "))
130=int(input("Health points? "))
15=int(input("Level? "))

Minotaur = str(input("What is your character name? "))
300=int(input("Health points? "))
30=int(input("Level? "))


print(Banshee)
print(250)
print(30)

print(Mermaid)
print(130)
print(15)

print(Minotaur)
print(300)
print(30)

array=[
    [Banshee,(250,30)],
    [Mermaid,(130,15)],
    [Minotaur,(300,30)]
]

print(array)

def arrumação_characterlvl(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j][1][1]<array[j+1][1][1]:
                array[j],array[j+1] = array[j+1], array[j]

arrumação_characterlvl(array)

for i in array:
    print(i[0])