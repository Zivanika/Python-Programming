for i in range(5): #since loop can't go to 5 it goes to else instead
    print(i)
    if i==4:
        break  #if not break control executes else also
    
else:
    print("Done")
    
for i in []:
    print(i)
else:
    print("Sorry! No output.")
    
    # the statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.