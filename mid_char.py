def get_middle(s):
    if len(s)==1:
        return s
    elif len(s)==2:
        return s
    elif len(s)%2==0:
        mid = s[(len(s)//2)-1:len(s)//2]  
        return mid
    elif len(s)%2!=0:
        mid = s[(len(s)//2)] 
        return mid            
print(get_middle('antoniera'))        