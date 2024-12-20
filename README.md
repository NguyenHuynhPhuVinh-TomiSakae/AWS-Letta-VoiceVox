# AWS-Letta-VoiceVox

Hướng dẫn cài đặt và chạy Letta và VoiceVox trên AWS EC2

## Cài đặt Letta

### Bước 1: Kết nối SSH
```bash
ssh -i "Letta.pem" ubuntu@<Public-IPv4-DNS>
```

### Bước 2: Cài đặt môi trường
## Cập nhật package
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv tmux
```
## Tạo môi trường ảo
```bash
python3 -m venv letta-env
source letta-env/bin/activate
```
## Cài đặt Letta
```bash
pip install letta
```

### Bước 3: Cấu hình Security Group
1. Truy cập AWS Console > EC2 > Security Groups
2. Chọn Security Group của instance
3. Thêm Inbound Rule:
   - Type: Custom TCP
   - Port: 8283
   - Source: 0.0.0.0/0 (hoặc IP cụ thể)

### Bước 4: Cấu hình Firewall
```bash
sudo ufw allow 8283
sudo ufw reload
```

### Bước 5: Chạy Letta Server
## Tạo tmux session mới
```bash
tmux new -s Letta
```
## Chạy server
```bash
letta server --host 0.0.0.0
```
## Thoát tmux (Ctrl + b, sau đó nhấn d)

Truy cập Letta tại: `http://<Public-IPv4>:8283`

## Cài đặt VoiceVox

### Bước 1: Kết nối và copy file
## Copy thư mục linux-cpu
```bash
scp -i "VoiceVox.pem" -r linux-cpu ubuntu@<Public-IPv4-DNS>:~
```
## Kết nối SSH
```bash
ssh -i "VoiceVox.pem" ubuntu@<Public-IPv4-DNS>
```

### Bước 2: Cấu hình Security Group
1. Truy cập AWS Console > EC2 > Security Groups
2. Chọn Security Group của instance
3. Thêm Inbound Rule:
   - Type: Custom TCP
   - Port: 50021
   - Source: 0.0.0.0/0 (hoặc IP cụ thể)

### Bước 3: Cấu hình Firewall
```bash
sudo ufw allow 50021
sudo ufw reload
```

### Bước 4: Chạy VoiceVox Server
```bash
cd ~/linux-cpu
chmod +x run
./run --host 0.0.0.0
```

Truy cập VoiceVox tại: `http://<Public-IPv4>:50021`

## Lưu ý
- Thay thế `<Public-IPv4-DNS>` và `<Public-IPv4>` bằng địa chỉ thực tế của EC2 instance
- Đảm bảo file .pem có quyền truy cập phù hợp (chmod 400)
- Để quay lại session tmux: `tmux attach -t Letta`
