import molotov

#using google was for testing
@molotov.scenario()
async def scenario(session):
      async with session.get("https://www.google.com") as resp:
         assert resp.status == 200


