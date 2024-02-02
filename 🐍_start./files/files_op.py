my_file=(open("mess.dat","a"));
message = input("Enter message:")
message = message.strip()
my_file.write(message + "\n");
my_file.close