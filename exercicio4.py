import beepy
import time
contagem = 10;
for i in range(11):
    print(contagem)
    contagem -= 1;
    time.sleep(1)

beepy.beep(sound=1)
   