#hardware platform:FireBeetle-ESP8266
fd=open('/sd/dfrobot.txt','rw')     #open file 'dfrobot.txt' in sdcard ,the mode is read and write,and create the file descriptor as fd
fd.write('hello dfrobot')           #write "hello dfrobot" to the file 'dfrobot.txt'
fd.seek(0)                          #move the file pointer to the start
print(fd.read())                    #read from the start of "dfrobot.txt"
fd.close()                          #close file
os.umount("/sd")                    #unmount sdcard