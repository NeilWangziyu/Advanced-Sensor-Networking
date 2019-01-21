#temporary work in windows system
import serial
import json
import time

def readserial(port):
    ser = serial.Serial(port, 9600, timeout=0.1)
    #every 0.1 Second read one time
    while (1):
        data = ser.readline()
        print(data)

        if len(data) == 5:
            ECG = int.from_bytes(data[1:3], byteorder='big') / 10
            print(humidity)

            tem = int.from_bytes(data[3:5], byteorder='big') / 10
            print(tem)

            dict_json = {}
            dict_json['ECG'] = ECG
            dict_json['temperature'] = tem

            print(dict_json)

            # json_str = json.dumps(dict_json)
            #
            # print(json_str)

            file = open('test.json', 'w', encoding='utf-8')
            json.dump(dict_json, file, ensure_ascii=False)
            file.close()

            ser.close()
            print('read serial successed, JSON created')
            
			
            break

            # file = open('test.json', 'r', encoding='utf-8')
            # s = json.load(file)
            # print(s)


if __name__ == '__main__':
    port = 'COM4'
    # the port should be modified every time
    print('start to read %s' %(port))

    while(1):
       readserial(port)
       time.sleep(0.1)

