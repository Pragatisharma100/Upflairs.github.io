import socket as sk

s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

# target_ip = "192.168.1.65"
target_ip="127.0.0.1"
port_no =2525

target_address=(target_ip,port_no)

# quiet=True
# while quiet:
#     message=input("plz enter the message:")
#     message.encode("ascii")  #message is encrpt
#     message_encrypt = message.encode("ascii")
#     s.sendto(message_encrypt,target_address)

#     user_input=input("Do you want to exit it press Y/y")
#     if user_input=="Y" or user_input=="y":
#         quiet =False

    # Open the file demo.txt and read its content
with open("DemoP.txt", "rb") as f:
    while True:
        # Read data from the file
        data = f.read(1024)
        if not data:
            break

        # Send data to the receiver
        s.sendto(data, (target_ip, target_address))
        print(f"Sent data: {data}")

print("File transfer complete.")