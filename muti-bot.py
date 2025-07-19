import threading
import time
from minecraft.networking.connection import Connection
from minecraft.networking.packets import PacketListener

# ===== THÔNG TIN SERVER & BOT =====
server_address = input("Nhập IP server: ")      # VD: 127.0.0.1 hoặc play.server.vn
server_port = 25565                              # Thay nếu server dùng port khác
bot_count = int(input("Số lượng bot muốn join: "))  # VD: 10

def create_bot(index):
    username = f"Bot_{index}"
    try:
        connection = Connection(server_address, server_port, username=username)

        def handle_join_game(join_game_packet):
            print(f"{username} đã vào server thành công!")

        connection.register_packet_listener(
            handle_join_game,
            packet_type=connection.protocol.join_game_packet
        )

        connection.connect()
    except Exception as e:
        print(f"{username} lỗi: {e}")

# ===== TẠO NHIỀU BOT =====
threads = []

for i in range(bot_count):
    t = threading.Thread(target=create_bot, args=(i,))
    t.start()
    threads.append(t)
    time.sleep(0.1)  # Tránh spam quá nhanh

for t in threads:
    t.join()
