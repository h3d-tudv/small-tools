import os
start_path = "d:/test" # current directory

#file for logging
logPath = os.path.join(start_path,"read_dir.log")
logFile = open(logPath, "w+")

for path,dirs,files in os.walk(start_path):
    for filename in files:
        # Đọc nội dung file
        if (".vtt" in filename):
            try:
                print(os.path.join(path,filename))
                f = open(os.path.join(path,filename), "r")
                lines = f.readlines()
                f.close()
                f = open(os.path.join(path,filename), "w")
                line1 = lines[0]
                if ("WEBVTT" in line1):
                    f.writelines(lines[2:])

                f.close();
            except:
                logFile.write("[Error] Fail to read file | " + os.path.join(path,filename))

