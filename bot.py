import asyncio
from minecraft.networking.connection import Connection
import random
import string

# Hàm tạo tên ngẫu nhiên cho bot
def random_username(length=8):
    return "Bot_" + ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Hàm join bot vào server
async def join_bot(host, port, username):
    try:
        conn = Connection(host, port, username=username)
        conn.connect()
        print(f"[+] Bot '{username}' đã join server {host}:{port}")
        await asyncio.sleep(60)  # Ở lại server 60 giây rồi thoát
        conn.disconnect()
    except Exception as e:
        print(f"[-] Bot '{username}' không thể join: {e}")

async def main():
    host = input("Nhập IP hoặc hostname server Minecraft: ").strip()
    port_input = input("Nhập port (mặc định 25565): ").strip()
    port = int(port_input) if port_input.isdigit() else 25565

    num_bots_input = input("Nhập số lượng bot muốn tạo: ").strip()
    try:
        num_bots = int(num_bots_input)
    except:
        print("Số lượng bot không hợp lệ, mặc định 5")
        num_bots = 5

    print(f"Đang tạo {num_bots} bot join vào server {host}:{port} ...")

    tasks = []
    for _ in range(num_bots):
        username = random_username()
        tasks.append(join_bot(host, port, username))
        await asyncio.sleep(0.2)  # Delay nhỏ để tránh bị block

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
