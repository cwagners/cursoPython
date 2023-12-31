import beepy
import time
contagem = 10;
while contagem >= 0:
    print(contagem)
    contagem -= 1;
    time.sleep(1)

beepy.beep(sound=1)
   
number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1