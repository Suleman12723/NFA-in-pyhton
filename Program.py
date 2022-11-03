file = open('nfa.txt')

print("\n#####################################################\n")
print("This an NFA to DFA conversion\n")
print("Your States should be named starting from 0 and so on\n")
print("Your inputs should be digits like 0102.. . Not string like ab..\n")
print("\nGithub userName: Suleman12723\n")
print("\n#####################################################\n")


current_state = input("Enter the current state: ")
final_state = input("Enter the final state: ")
input_string = input("Enter the string to test: ")
transitions = []


# reading through lines and removing \n and split them by " " and storing 2d arrays in transitions[]
# thses are the transitions on each state respectively
for line in file:
    if line[-1] == '\n':
        temp = line[:-1].split(" ")
    else:
        temp = line.split(" ")
    transitions.append(temp)

print(transitions)




def multipleNextStates(next_state):
    current_state = ""
    temp = next_state.split(",")
    for j in temp:
        if j!="-":
            current_state+= (j+",")
    current_state = current_state[:-1]
    return current_state


def multipleCurrentStates(current_state,current_input):
    next_state =""
    temp = current_state.split(",")
    for j in temp:
        if j!="-":
            temp_next_state = transitions[int(j)][int(current_input)]
            if temp_next_state !="-":
                if len(temp_next_state)==1:
                    next_state+=temp_next_state
                    next_state+=","
                elif len(temp_next_state)>1:
                    next_state+=multipleNextStates(temp_next_state)
    if next_state!= "":
        if next_state[-1]==",":
            next_state = next_state[:-1]
            
    return next_state
        



for i in range(len(input_string)):
    if current_state != '-': 
        if len(current_state)==1:
            next_state = transitions[int(current_state)][int(input_string[i])]
            if i!= (len(input_string)-1):
                if len(next_state) > 1:
                    current_state = multipleNextStates(next_state)
                else:
                    current_state = next_state
            elif i==(len(input_string)-1):
                if len(final_state) >1:
                    temp = final_state.split(",")
                    for k in temp:
                        if k in next_state.split(","):
                            print("Passed")
                            break
                elif len(final_state)==1 and final_state in next_state.split(","):
                    print("Passed")
                    break
                else:
                    print("Failed")
                    break
                    
        elif len(current_state)>1:
            next_state = multipleCurrentStates(current_state, input_string[i])
            if i!= (len(input_string)-1):
                if len(next_state) > 1:
                    current_state = multipleNextStates(next_state)
            elif i==(len(input_string)-1):
                if len(final_state) >1:
                    temp = final_state.split(",")
                    for k in temp:
                        if k in next_state.split(","):
                            print("Passed")
                            break
                elif len(final_state)==1 and final_state in next_state.split(","):
                    print("Passed")
                    break
                else:
                    print("Failed")
                    break
    


            
            


        
