
# w8s2. Quelques exemples simples
-------------

> Prendre l’éditeur IDLE et faire nouveau fichier
 
	import asyncio

	async def morceaux(message):
	    # On appelle le code synchrone normalement
	    print(message, "début")
	    # avec await on rend la main
	    await asyncio.sleep(0.5)
	    
	    print(message, "milieu")
	    await asyncio.sleep(1)
	    
	    print(message, "fin")
	    return f'{message} par morceaux'

> Faire Save As "w8s2 Vidéo.py" puis F5

	morceaux

	morceaux("run")

	loop = asyncio.get_event_loop()

	loop.run_until_complete(morceaux("run"))

	loop.run_until_complete(
	    asyncio.gather(morceaux("run1"),
	                   morceaux("run2")))

> Reprendre sous IDLE le fichier python et ajouter

	import time


	# Exemple de ce qu'il ne faut pas faire
	async def famine(message):
	    
	    print(message, "début")
	    # avec await on rend la main
	    await asyncio.sleep(0.5)
	    
	    print(message, "milieu")
	    # on garde la main au lieu de la rendre
	    time.sleep(1)
	    
	    print(message, "fin")
	    return f'{message} par famine'
	                   

> Faire Ctl-s puis F5

	loop = asyncio.get_event_loop()

	loop.run_until_complete(
	    asyncio.gather(famine("run1"),
	                   famine("run2")))


# w8s4. Extensions asynchrones du langage
-------------

> Prendre un notebook ou un éditeur python
 
	import time

	urls = ["https://www.irs.gov/pub/irs-pdf/f1040.pdf",
			"https://www.irs.gov/pub/irs-pdf/f1040es.pdf",
			"https://www.irs.gov/pub/irs-pdf/f1040c.pdf",
			"https://www.irs.gov/pub/irs-pdf/f1040esn.pdf",
			]

	import requests

	beg = time.time()

	for url in urls:
	    req = requests.get(url)
	    print(f"{url} returned {len(req.text)} chars")
	    
	print(f"duration = {time.time() - beg}s")    
			

> Prendre l'éditeur IDLE sur votre machine, après avoir installé aiohttp (pip install aiohttp)

	import asyncio
	import aiohttp
	import time

	urls = ["https://www.irs.gov/pub/irs-pdf/f1040.pdf",
			"https://www.irs.gov/pub/irs-pdf/f1040es.pdf",
			"https://www.irs.gov/pub/irs-pdf/f1040c.pdf",
			"https://www.irs.gov/pub/irs-pdf/f1040esn.pdf",
			]


	async def fetch(url):

	    async with aiohttp.ClientSession() as session:
	        print(f"fetching {url}")

	        async with session.get(url) as response:
	            raw = await response.read()
	            print(f"{url} returned {len(raw)} bytes")

	async def fetch_urls():
	    await asyncio.gather(*(fetch(url) for url in urls))

> Faire Ctl-s puis F5

	loop = asyncio.get_event_loop()

	beg = time.time()
	loop.run_until_complete(fetch_urls())
	print(f"duration = {time.time() - beg}s")

> Reprendre l'éditeur python sur votre machine et ajouter

	async def fetch2(url, i):
	    async with aiohttp.ClientSession() as session:
	        async with session.get(url) as response:
	            # avec ici une itération asynchrone
	            async for line in response.content:
	                print(f"{i}", end="")
	    return url


	asyncio.get_event_loop().run_until_complete(
	    asyncio.gather(*(fetch2(url, i) for i, url in enumerate(urls)))
	)


# w8s5. Coroutines et awaitables
-------------

> __await__ renvoie un itérateur
> Prendre sous IDLE un nouveau fichier python

	class Awaitable():
	    def __await__(self):
	        print("in Awaitable")
	        yield "yielded"

	# Il nous faut au moins une coroutine pour pouvoir faire await
	async def main():
	    await Awaitable()

> Faire Save As "w8s5 Vidéo.py" puis F5

	# l'objet coroutine	
	coro = main()

	coro.send(None)   

> un peu moins simple
> Reprendre sous IDLE le fichier python

	# itérateur à deux coups
	class Awaitable2():
	    def __await__(self):
	        print("step1")
	        yield "yield1"        
	        print("step2")
	        yield "yield2"        
	        return "returned"

	# boilerplate
	async def main():
	    await Awaitable2()

> Faire Ctl-s puis F5

	# l'objet coroutine
	coro = main()

	coro.send(None)

	coro.send(None)

	try:
	    coro.send(None)
	except Exception as e:
	    x = e
	    print('oops', type(e), e.value)

> plusieurs travaux en même temps
> Toujours sous le shell python

	coro1 = main()

	coro2 = main()

	coro1.send(None)

	coro2.send(None)

	coro1.send(None)

	coro2.send(None)

	try:
	    coro1.send(None)
	except Exception as e:
	    x = e
	    print('oops', type(e), e.value)

	try:
	    coro2.send(None)
	except Exception as e:
	    x = e
	    print('oops', type(e), e.value)

> pile, await et yield
> Reprendre sous IDLE le fichier python

	class w1:

	    def __init__(self, marker):
	        self.marker = marker
	    
	    def __await__(self):
	        # redonner la main à la boucle
	        yield f"yield {self.marker}"
	        # retourné à await
	        return 1

	async def w2():
	    return await w1('first') + await w1('second')

	async def w3():
	    return await w2() + 1

	async def w4():
	    return await w3() + 1

	coro = w4()    

> Faire Ctl-s puis F5

	coro.send(None)

	coro.send(None)

	try:
	    coro.send(None)
	except Exception as e:
	    x = e
	    print('OOPS', type(e), e.value)

> dans les deux sens
> Reprendre sous IDLE le fichier python

	class BothWays():
	    def __await__(self):
	        print("step1")
	        received1 = yield "yielded1"
	        print("received1", received1)
	        print("step2")
	        received2 = yield "yielded2"
	        print("received2", received2)
	        return "returned"

	# boilerplate
	async def main():
	    return await BothWays()

> À la place de coro = w4() taper

	# l'objet coroutine
	coro = main()

> Faire Ctl-s puis F5


	coro.send(None)

	coro.send("message")            


# w8s6. Boucles d'événements
-------------

> Prendre un nouveau fichier sous IDLE ou votre éditeur python

	from datetime import datetime
	import asyncio
	import time

	###############################################################################
	#
	#  pour remplacer 'from asynchelpers import start_timer, show_timer' 
	#
	###############################################################################

	# low-level API
	def _start_timer():
	    return datetime.now()


	def _show_timer(start, *args):
	    delta = datetime.now() - start
	    duration = f"{delta.seconds}s + {delta.microseconds // 1000:03d}ms"
	    print(duration, *args)


	####################
	# Use a module global to keep things simple

	glo_start = None


	def start_timer():
	    global glo_start
	    print("---------- zero")
	    glo_start = _start_timer()


	def show_timer(*args):
	    global glo_start
	    _show_timer(glo_start, *args)


	##############################
	async def sequence(*messages, delay=1):
	    show_timer(">>>", *messages)
	    await asyncio.sleep(delay)
	    show_timer("<<<", *messages)


	##########
	def reset_loop():
	    asyncio.set_event_loop(asyncio.new_event_loop())

	###############################################################################
	#
	#   fin de 'pour remplacer from asynchelpers import start_timer, show_timer'
	#
	###############################################################################

> Faire Save As "w8s6 Vidéo.py" puis F5

	# pour démonstration de l'utilitaire
	start_timer()

	time.sleep(1)

	show_timer('message')

> Reprendre le fichier sous IDLE ou votre éditeur python

	async def c1():
	    show_timer(">>> c1")
	    await asyncio.sleep(1)
	    show_timer("forking")
	    # fork
	    asyncio.ensure_future(c2())
	    await asyncio.sleep(1)
	    show_timer("<<< c1")
	    
	# sera forkée par c1() après une seconde

	async def c2():
	    show_timer(">>> c2")
	    await asyncio.sleep(2)
	    show_timer("<<< c2")

	asyncio.ensure_future(c1())

	start_timer()

	# interrompre après 2s
	try:
	    asyncio.get_event_loop().run_forever()
	except KeyboardInterrupt:
	    print("bye")

> Faire Ctl-s puis F5
> Pour interrompre la boucle "sans fin", taper Ctl-c


> réinitialisation de la boucle

	asyncio.set_event_loop(asyncio.new_event_loop())

> Reprendre le fichier sous IDLE ou votre éditeur python
> et remplacer (après l'utilitaire) par
	    
	async def c1_stop():
	    show_timer(">>> c1")
	    await asyncio.sleep(1)
	    show_timer("forking")
	    # fork
	    asyncio.ensure_future(c2_stop())
	    await asyncio.sleep(1)
	    show_timer("<<< c1")

	# sera forkée par c1_stop() après une seconde
	async def c2_stop():
	    show_timer(">>> c2")
	    await asyncio.sleep(2)
	    show_timer("<<< c2")
	    # attention c'est une méthode bloquante
	    asyncio.get_event_loop().stop()    

	asyncio.ensure_future(c1_stop())

	start_timer()

	# s'arrête tout seul
	try:
	    asyncio.get_event_loop().run_forever()
	except KeyboardInterrupt:
	    print("bye")
	    
	print("done")

> Faire Ctl-s puis F5

> Pour interrompre la boucle "sans fin", taper Ctl-c


# w8s7. Tâches et exceptions
-------------

> Prendre un nouveau fichier sous IDLE ou votre éditeur python

	from asyncio import (
	    get_event_loop, ensure_future, Task )

	async def foo():
	    pass

	task = ensure_future(foo())

> Faire Save As "w8s7 Vidéo.py" puis F5

	task

> Reprendre le fichier sous IDLE ou votre éditeur python

	# attention : retourne un set
	tasks = Task.all_tasks()

> Faire Ctl-s puis F5

	tasks
	task in tasks

	# et comme on n'est pas dans la  boucle
	print(task.current_task())


# w8s8. La librairie asyncio
-------------

> Prendre un nouveau fichier sous IDLE ou votre éditeur python

	from datetime import datetime
	import asyncio
	import time

	####################################################################
	#
	#  pour remplacer 'from asynchelpers import start_timer, show_timer' 
	#
	####################################################################

	# low-level API
	def _start_timer():
	    return datetime.now()


	def _show_timer(start, *args):
	    delta = datetime.now() - start
	    duration = f"{delta.seconds}s + {delta.microseconds // 1000:03d}ms"
	    print(duration, *args)


	####################
	# Use a module global to keep things simple

	glo_start = None


	def start_timer():
	    global glo_start
	    print("---------- zero")
	    glo_start = _start_timer()


	def show_timer(*args):
	    global glo_start
	    _show_timer(glo_start, *args)


	##############################
	async def sequence(*messages, delay=1):
	    show_timer(">>>", *messages)
	    await asyncio.sleep(delay)
	    show_timer("<<<", *messages)


	##########
	def reset_loop():
	    asyncio.set_event_loop(asyncio.new_event_loop())


	####################################################################
	#
	# fin de pour remplacer 'from asynchelpers import start_timer... 
	#
	####################################################################

> Faire Save As "w8s8 Vidéo.py" puis F5

	asyncio.Queue?

> Reprendre le fichier sous IDLE ou votre éditeur python et ajouter

	queue = asyncio.Queue(maxsize=1)

	async def producer(queue):
	    count = 1
	    while True:
	        await queue.put(f'tick{count}')
	        count += 1
	        await asyncio.sleep(1)

	async def consumer(queue):
	    while True:
	        received = await queue.get()
	        show_timer(f"got {received}")

	# on ajoute les coroutines dans la boucle
	asyncio.ensure_future(producer(queue))
	asyncio.ensure_future(consumer(queue))        

	start_timer()

	# interrompre avec la touche 'i' 
	# plusieurs fois si nécessaire

	try:
	    asyncio.get_event_loop().run_forever()
	except KeyboardInterrupt as e:
	    print("bye")

> Faire Ctl-s puis F5

> Pour interrompre la boucle "sans fin", taper Ctl-c

> Réinitialisation de la boucle

	asyncio.set_event_loop(asyncio.new_event_loop())

> Reprendre le fichier et remplacer (après l'utilitaire) par

	#limiter le parallèlisme avec Queue

	window = asyncio.Queue(maxsize = 4)

	async def job(i):
	    # prendre un jeton dans la queue
	    await window.put(None)
	    # pas tout le monde la même durée
	    duration = (i % 3) + 1
	    message = f"job{i} - duration {duration}"
	    show_timer(">>>", message)
	    await asyncio.sleep(duration)
	    show_timer("<<<", message)
	    # libérer le jeton
	    await window.get()

	for i in range(8):
	    asyncio.ensure_future(job(i))

	start_timer()
	try:
	    asyncio.get_event_loop().run_forever()
	except:
	    print('bye')

> Faire Ctl-s puis F5

> Pour interrompre la boucle "sans fin", taper Ctl-c


# w8s9. Bonnes pratiques
-------------

> Écueils classiques

> Prendre un nouveau fichier sous IDLE ou votre éditeur python

> Écueil n°1 : fonction coroutine vs coroutine

import asyncio

	# une fonction coroutine
	async def foo(delay):
	    await asyncio.sleep(1)
	    print("foo")

	# renvoie un objet coroutine
	# si on l'appelle normalement
	# il ne se passe rien
	foo(4)

	# c'est exactement comme 
	# une fonction génératrice
	def squares(scope):
	    for i in scope:
	        print(i)
	        yield i**2

	# qui retourne un
	# itérateur, et là encore
	# il ne se passe rien
	squares(4)

> tous les scénarios
	
> Reprendre le fichier et remplacer par

	def synchro():
	    pass

	async def asynchro():
	    pass


	def foo(): 
	    synchro()        # 1 # OK
	    asynchro()       # 2 # ** ATTENTION **
	    await synchro()  # 3 # SyntaxError
	    await asynchro   # 4 # SyntaxError

> Reprendre le fichier et ajouter

	async def afoo():
	    synchro()        # 5 # OK
	    await asynchro() # 6 # OK
	    asynchro()       # 7 # ** ATTENTION **
	    await synchro()  # 8 # ** ATTENTION **    

> Faire Ctl-s puis F5

> cas n°2 une fonction appelle une coroutine sans await ➠ avertissement
> contenu de call2.py

	import asyncio

	async def coro():
	    # totalement légal
	    print("dans coro")

	def main():
	    # par contre ici il
	    # manque un await !
	    coro()

	main()  

> Faire Ctl-s puis F5

> cas n°7 une coroutine appelle une autre coroutine sans await idem : avertissement
> contenu de call7.py

import asyncio

	async def coro():
	    print("dans coro")

	async def amain():
	    # pareil mais depuis
	    # une coroutine
	    coro()

	asyncio.get_event_loop().\
	   run_until_complete(amain())

> Faire Ctl-s puis F5

> cas n°8

	def synchro():
	    pass

	async def asynchro():
	    await synchro()

> Faire Ctl-s puis F5

	import inspect
	inspect.isawaitable(synchro())


> Écueil n°2 : code trop bloquant

> Reprendre le fichier et ajouter

	async def countdown(n, period):
	    while n >= 0:
	        print('.', end='', flush=True)
	        await asyncio.sleep(period)
	        n -= 1

	import time
	async def compute(n, period):
	    for i in range(n):
	        # on simule un calcul
	        time.sleep(period)
	        print('x', end='', flush=True)


	asyncio.set_event_loop(asyncio.new_event_loop())
	asyncio.get_event_loop().run_until_complete(
	    asyncio.gather(countdown(10, .05), compute(10, .05)))

> Faire Ctl-s puis F5

> Faites respirer votre code

> Reprendre le fichier et remplacer le fonction compute() par

	async def compute(n, period):
	    for i in range(n):
	        # on simule un calcul
	        time.sleep(period)
	        print('x', end='', flush=True)
	        # await None n'est pas valide
	        await asyncio.sleep(0)

> Faire Ctl-s puis F5

> Reprendre le fichier ou bien en prendre un nouveau

	import asyncio

	async def boom(n):
	    return 1/n

	asyncio.ensure_future(boom(1))
	asyncio.ensure_future(boom(0))

	try:
	    asyncio.get_event_loop().run_forever()
	except KeyboardInterrupt:
	    print('bye')

> Faire Ctl-s puis F5

















