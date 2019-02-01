from delfiles import del_file

path_1="//192.168.11.35/webcamera/"
img_path=[path_1+"camera1/",path_1+"camera2/",path_1+"camera3/"]


for i in img_path:
    del_file(i)
