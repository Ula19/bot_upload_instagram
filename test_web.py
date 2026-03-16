"""Тест: парсинг user_id из веб-страницы Instagram"""
import asyncio
import aiohttp
import re

SESSION_ID = "44587136753%3AkM8Ka8t4uVnbGi%3A29%3AAYjdf_xFbYnOG7tNYOgz1QVO0vN9UnyUTndDTC6z-g"

async def test():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    }
    cookies = {"sessionid": SESSION_ID}

    async with aiohttp.ClientSession() as session:
        # Тест 1: веб-страница профиля
        print("=== Тест 1: веб-страница ===")
        async with session.get(
            "https://www.instagram.com/welecanoo/",
            headers=headers, cookies=cookies, allow_redirects=True
        ) as resp:
            print(f"HTTP {resp.status}")
            html = await resp.text()
            m = re.search(r'"user_id":"(\d+)"', html)
            if m:
                print(f"user_id={m.group(1)}")
            m2 = re.search(r'profilePage_(\d+)', html)
            if m2:
                print(f"profilePage user_id={m2.group(1)}")
            if not m and not m2:
                print("user_id не найден")
                # посмотрим что в HTML
                print(f"HTML длина: {len(html)}")
                print(html[:500])

        # Тест 2: GraphQL API
        print("\n=== Тест 2: GraphQL API ===")
        gql_url = "https://www.instagram.com/api/v1/users/web_profile_info/?username=welecanoo"
        headers2 = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "X-Requested-With": "XMLHttpRequest",
        }
        async with session.get(
            gql_url, headers=headers2, cookies=cookies
        ) as resp:
            print(f"HTTP {resp.status}")
            if resp.status == 200:
                data = await resp.json()
                uid = data.get("data", {}).get("user", {}).get("id")
                print(f"user_id={uid}")

asyncio.run(test())
