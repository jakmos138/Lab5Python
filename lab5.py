import datetime

def run():
    logs = read_log("logtest.txt")
    print(logs)
    request_numbers = ip_requests_number(logs)
    print(request_numbers)

def read_log(path):
    logs = {'ip': [], 'hyphen': [], 'userid': [], 'timestamp': [], 'request': [], 'status': [], 'size': [], 'referer': [], 'header': []}
    with open(path) as log:
        for line in log.readlines():
            firstSplit = line.split(" \"")
            secondSplit = firstSplit[0].rstrip()[:-1].split(" ")
            thirdSplit = firstSplit[1].split("\" ")
            forthSplit = thirdSplit[1].split(" ")
            timestamp = datetime.datetime.strptime(secondSplit[3][1:]+secondSplit[4], "%d/%b/%Y:%H:%M:%S%z")
            logs["ip"].append(secondSplit[0])
            logs["hyphen"].append(secondSplit[1])
            logs["userid"].append(secondSplit[2])
            logs["timestamp"].append(timestamp)
            logs["request"].append(thirdSplit[0].strip())
            logs["status"].append(forthSplit[0])
            logs["size"].append(forthSplit[1])
            logs["referer"].append(firstSplit[2][:-1])
            logs["header"].append(firstSplit[3].rstrip()[:-1])
    return logs

def ip_requests_number(logs):
    request_numbers = {}
    for ip in logs["ip"]:
        try:
            request_numbers[ip] = request_numbers[ip] + 1
        except KeyError:
            request_numbers[ip] = 1
    return request_numbers
            
if __name__ == "__main__":
    run()