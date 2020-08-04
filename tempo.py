contador=0

import time

start = time.time()

while contador < 100000:
    contador +=1

end = time.time()

elapsed = end - start


print(elapsed)