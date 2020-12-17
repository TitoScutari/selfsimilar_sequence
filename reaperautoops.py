def automation_write(filename, length, array, type):
    filename += ".ReaperAutoItem"
    f = open(filename, "w")
    f.write("SRCLEN "+ str(length*2) + "\n")

    space = round(2*length/len(array), 5)
    i = 0
    for x in array:
        f.write("PPT "+ str(i) + " "+ str(x)+" " +str(type)+" 0\n")
        i+= space
    
    f.close()