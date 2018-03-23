"""
Gautam Mehta
CIS 41A Fall 2017
Unit H take-home assignment 
"""

'''
First Script
'''
def main():
    extractRecord()
        
def extractRecord():
    
    record={}
    count = 0
    with open("USPresidents.txt") as myfile:
        for line in myfile:
            fields =line.split()
            if fields [0] in record:
                record[fields[0]].append(fields[1])
            else:
                record[fields[0]] = [fields[1]]
    for state, presidents in record.items():
        if len(presidents) > count:
            count = len(presidents)
            highest_state = state
    print ("The state with the most presidents is", highest_state, "with", count, "presidents:")
    for president in record[highest_state]:
        print (president)
                
main()
"""
Execution Results:
The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
"""

'''
Second Script
'''

def main ():
    count_presidents()
def count_presidents():
    record2= {}
    
    with open("USPresidents.txt") as infile:
        for line in infile:
            fields = line.split()
            
            if fields[0] in record2:
                record2[fields[0]] +=1
            else:
                record2[fields[0]] = 1
    most_states = {"CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"}
    pop_states = set(record2).intersection(most_states)
    print(len(pop_states), "of the", len(most_states), end = " ")
    print("high population states have had presidents born in them:")
    
    for state in sorted(pop_states):
        print (state, record2[state])
main()
"""
Execution Results:
8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2
"""
'''
Third Script
'''
def main():
    overseerSystem(temperature = 550)
    overseerSystem(temperature = 475)
    overseerSystem(temperature = 450, miscError = 404)
    overseerSystem(CO2level = .18)
    overseerSystem(CO2level = .2, miscError = 503)

def overseerSystem(**kwargs):
    if "temperature" in kwargs and kwargs["temperature"] >500:
        print("Warning: temperature is", kwargs["temperature"])
    if "CO2level" in kwargs and kwargs["CO2level"] > 0.15:
        print("Warning: CO2level is", kwargs["CO2level"])
    if "miscError" in kwargs:
        print("Misc error #", kwargs["miscError"])

main()
"""
Execution Results:
Warning: temperature is 550
Misc error # 404
Warning: CO2level is 0.18
Warning: CO2level is 0.2
Misc error # 503
"""

