import psutil
import time
try:
    while True:
        print("Monitoring CPU usage...")
        cpu_usage_val=psutil.cpu_percent()
        print("The cpu usage is: "+str(cpu_usage_val))
        if(cpu_usage_val>90.0):
            print("Alert! CPU usage exceeds threshold: 90%")
        if(cpu_usage_val>80.0):
           print("Alert! CPU usage exceeds threshold: 80%")
        time.sleep(2)
        print("...(continues until interrupted)")
except KeyboardInterrupt:    #ctrl+c is interrupt
    print("--Finished Monitoring--")
