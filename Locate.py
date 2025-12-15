import os
from iplocate import IPLocateClient, AsyncIPLocateClient
import asyncio
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path("/my/path/.env"))
print(os.getenv("IPlocate"))     



async def lookup_multiple_ips():
    async with AsyncIPLocateClient('') as client:
        tasks = [
            client.lookup(""),
            client.lookup(""),
            client.lookup("")
        ]
        results = await asyncio.gather(*tasks)
        
        for result in results:
            print(f"{result.ip}: {result.country}")
client = IPLocateClient(api_key=os.getenv("IPlocate")) 

