import socket as sk #socket library
# send through internet and protocol(is a set of rules) used as udp(user datagram protocol)
# ip address command -> ipconfig ->IP:PORT
# socket ka through message send and receive

s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM) #(internet,portocol(used udp) )
# ip_address="192.168.1.76"
ip_address="127.0.0.1"
port_no =2525
address=(ip_address,port_no)
s.bind(address)  #register
# while True:
#     Data=s.recvfrom(100)  #character limit 100
#     message=Data[0]
#     ip_address=Data[1][0]
#     # message=message.decode()
#     print(ip_address,">>>>>>>>",message)


# demo.txt -> hii upflairs
#  sender file send to receiver
#  file handling before sending the file read it and then write in another file


# file=open("DemoP.txt","w")
# file.write("hi upflairs")
# file.close()

with open("DemoP.txt", "wb") as f:
    while True:
        # Receive data from sender
        data, addr = s.recvfrom(100)  # buffer size is 1024 bytes
        print(f"Received message from {addr}: {data}")

        if not data:
            break

        # Write data to the file
        f.write(data)

    print("File transfer complete.")