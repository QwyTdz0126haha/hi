from minecraft.networking.connection import Connection
from minecraft.networking.packets import PacketListener

# Thông tin server và tên bot
server_address = "localhost"  # Thay bằng IP server nếu cần
server_port = 25565
username = "BotName"          # Đổi tên bot tùy ý

# Tạo kết nối
connection = Connection(server_address, server_port, username=username)

# Xử lý sự kiện khi bot vào game
def handle_join_game(join_game_packet):
    print(f"{username} đã join vào server Minecraft thành công!")

# Đăng ký listener
connection.register_packet_listener(
    handle_join_game, 
    packet_type=connection.protocol.join_game_packet
)

# Kết nối đến server
connection.connect()
