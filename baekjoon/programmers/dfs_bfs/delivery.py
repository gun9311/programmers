def solution(cap, n, deliveries, pickups):
    answer = 0
        
    def truck_deliver(truck,visiting) :
        for i in range(n-1,-1,-1) :
            if deliveries[i] != 0 :
                if truck + deliveries[i] >= cap :
                    visiting.append(i+1)
                    deliveries[i] = deliveries[i]-(cap-truck)
                    truck = cap
                    break
                else :
                    visiting.append(i+1)
                    truck += deliveries[i]
                    deliveries[i] = 0
        if visiting:
            return max(visiting)
        else :
            return 0
    
    def truck_pickup(truck, visiting) :        
        for i in range(n-1,-1,-1) :
            if pickups[i] != 0 :
                if truck + pickups[i] >= cap :
                    visiting.append(i+1)
                    pickups[i] = pickups[i]-(cap-truck)
                    truck = cap
                    break
                else :
                    visiting.append(i+1)
                    truck += pickups[i]
                    pickups[i] = 0
        if visiting:
            return max(visiting)
        else :
            return 0
        
    while sum(deliveries) != 0 or sum(pickups) != 0 :
        result = set()
        if sum(deliveries) != 0 :
            truck = 0
            visiting = []
            result.add(truck_deliver(truck,visiting))
        if sum(pickups) != 0 :
            truck = 0
            visiting = []
            result.add(truck_pickup(truck,visiting))
        answer += max(result)   
    return answer*2

cap = 2
n = 7
deli = [1, 0, 2, 0, 1, 0, 2]	
pu = [0, 2, 0, 1, 0, 2, 0]
solution(cap,n,deli,pu)