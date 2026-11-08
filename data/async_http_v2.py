#!/usr/bin/env python3

"""
version modernisée de async_http.py (python >= 3.11)

pour des raisons techniques, il n'est pas possible de mettre en ligne
un notebook pour ce genre d'activités liées au réseau

ce code reprend l'esprit de l'exemple illustré dans la vidéo,
mais avec les pratiques actuelles d'asyncio :

* `asyncio.run()` pour lancer la boucle d'événements, plutôt que de la manipuler
* une seule `ClientSession` partagée par toutes les requêtes
* `asyncio.TaskGroup` (structured concurrency) plutôt que `gather`
* des timeouts, et une gestion d'erreur réseau

* lancé sans argument il reproduit l'expérience en mode asynchrone simple
  (cf. fetch)

* utilisez l'option -d (--details) pour utiliser fetch_lines, en montrant donc
  les lignes au fur et à mesure qu'elles arrivent

* utilisez l'option -s (--sequential) pour faire les accès en séquence

Vous pouvez utiliser une autre liste d'URLs en les passant sur la ligne de commande
e.g.:

$ async_http_v2.py http://google.com http://facebook.com http://google.com http://facebook.com

"""

import argparse
import asyncio
import time

import aiohttp
import requests


# ceci sera le défaut si vous ne précisez pas d'URL vous même:
DEFAULT_URLS = [
    "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
]

TIMEOUT_SECONDS = 30


#################### la version séquentielle
def sequential(urls: list[str]) -> None:
    for url in urls:
        try:
            req = requests.get(url, timeout=TIMEOUT_SECONDS)
        except requests.RequestException as exc:
            print(f"{url} failed: {exc!r}")
            continue
        print(f"{url} returned {len(req.content)} bytes")


#################### la version parallèle / asynchrone
# la première version, qui imprime simplement la taille de chaque url
# la session est créée une seule fois et passée en paramètre
async def fetch(session: aiohttp.ClientSession, url: str) -> None:
    print(f"fetching {url}")
    try:
        async with session.get(url) as response:
            print(f"{url} response status {response.status}")
            raw = await response.read()
            print(f"{url} returned {len(raw)} bytes")
    except (aiohttp.ClientError, TimeoutError) as exc:
        print(f"{url} failed: {exc!r}")


# la variante qui affiche un caractère par ligne reçue
async def fetch_lines(session: aiohttp.ClientSession, url: str, i: int) -> None:
    try:
        async with session.get(url) as response:
            print(f"{url} response status {response.status}")
            # avec ici une itération asynchrone
            async for _line in response.content:
                # contrairement au notebook, il faut flusher les impressions
                # sur sys.stdout, qui sinon sont bufferisées
                print(i, end='', flush=True)
    except (aiohttp.ClientError, TimeoutError) as exc:
        print(f"\n{url} failed: {exc!r}")


async def run_async(urls: list[str], details: bool) -> None:
    timeout = aiohttp.ClientTimeout(total=TIMEOUT_SECONDS)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # le TaskGroup attend la fin de toutes les tâches en sortant du with
        async with asyncio.TaskGroup() as group:
            for i, url in enumerate(urls):
                if details:
                    group.create_task(fetch_lines(session, url, i))
                else:
                    group.create_task(fetch(session, url))
    if details:
        print()


####################
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("urls", nargs='*', default=DEFAULT_URLS,
                        help="URL's to be fetched")
    parser.add_argument("-s", "--sequential", action='store_true',
                        help="run sequentially")
    parser.add_argument("-d", "--details", action='store_true',
                        help="show details of lines as they show up (using fetch_lines)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    urls = args.urls

    beg = time.perf_counter()
    if args.sequential:
        print(f"Running sequential mode on {len(urls)} URLs")
        sequential(urls)
    else:
        mode = "detail mode (fetch_lines)" if args.details else "simple mode (fetch)"
        print(f"Running {mode} on {len(urls)} URLs")
        # asyncio.run crée, exécute puis ferme proprement la boucle
        asyncio.run(run_async(urls, args.details))
    print(f"duration = {time.perf_counter() - beg:.2f}s")


if __name__ == '__main__':
    main()
