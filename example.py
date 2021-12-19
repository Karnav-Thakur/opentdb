import asyncio
import aiohttp
import opentdb
import json

opentdb = opentdb.OpenTDB("https://opentdb.com/api.php?amount=10&type=multiple",1,10)

loop = asyncio.get_event_loop()
que = loop.run_until_complete(opentdb.question())
ans = loop.run_until_complete(opentdb.answers())
cat = loop.run_until_complete(opentdb.category())
diff = loop.run_until_complete(opentdb.difficulty())
print(que)
print(ans)
print(cat)
print(diff)
