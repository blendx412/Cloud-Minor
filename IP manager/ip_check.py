import subprocess,os,argparse

def main():
    parser = argparse.ArgumentParser(description='-----------Internet Protocol Checker IPv4 only--------------')
    parser.add_argument('-ip','--ip', help='Ip4 Address to be checked',required=True)
    parser.add_argument('-range','--range',help='Range for IP address to scan for',required=False)
    
    args = parser.parse_args()

    IP = args.ip
    #validate ip here
    if(validate_ip(IP)==0):
        print "Invalid IP"
        exit()
    
    if args.range != None:
        #process multiple ip
        IP_RANGE=int(args.range)
        check_multi_IP(IP, IP_RANGE)
    else:
        #process single ip
        check_single_IP(IP)



#function to validate IP Address
def validate_ip(IP):
    valid_ip=0
    a = IP.split('.')
    if(len(a)==4):
        valid_ip=1
        
    return valid_ip

#function to check Single IP         
def check_single_IP(IP):
    with open(os.devnull, "wb") as no_display_console:
            result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", IP],
                                        stdout=no_display_console, stderr=no_display_console).wait()
            predict_ip(IP,result)

#function to check Multiple IP            
def check_multi_IP(IP,IP_RANGE):
    split_ip = IP.split('.')
    temp = split_ip[0]+"."+split_ip[1]+"."+split_ip[2]
    with open(os.devnull, "wb") as no_display_console:
        for n in xrange(IP_RANGE):
                ip=temp+"."+str(int(split_ip[3])+n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                        stdout=no_display_console, stderr=no_display_console).wait()
                predict_ip(ip,result)

#function to Predict Valid or Invalid IP based on The result form Ping Command                                        
def predict_ip(ip,result):
    if result:
        print ip,"inactive"
    else:
        print ip,"active"

#calling main here
if __name__ == "__main__":
    main()