import re


def solve(arr):
    line=arr
    numbers,ans=arr.split('=')
    num1,num2=numbers.split('+')
    ans=ans.strip()
    num1=num1.strip()
    num2=num2.strip()
    # print(num1,num2)
    cheker=0
    # We want 3 conditions
    if "#" in num1 :
        place1=num1.find("#")
        num1_l=num1[:place1]
        num1_r=num1[place1+1:]
        length1_l=len(num1_l)
        length1_r=len(num1_r)
        delta_1=str(int(ans)-int(num2))
        # length1=len(str(int(ans)-int(num2)))-len(num1_l+num1_r)
        replac_num1=delta_1[place1:len(delta_1)-length1_r]
        # print(replac_num1)
        regex1='^'+num1_l+'.*'+num1_r+'$'
        if re.match(regex1,str(int(ans)-int(num2))):
            line=re.sub('#',replac_num1,line)
            return line
        else:
            return '-1'
        # print(num1_l,num1_r)
    
    elif "#" in num2 :
        place2=num2.find("#")
        num2_l=num2[:place2]
        num2_r=num2[place2+1:]
        length2_l=len(num2_l)
        delta_2=str(int(ans)-int(num1))
        length2_r=len(num2_r)
        replac_num2=delta_2[place2:len(delta_2)-length2_r]
        # print(replac_num2)
        # length1=len(str(int(ans)-int(num2)))-len(num1_l+num1_r)
        regex2='^'+num2_l+'.*'+num2_r+'$'
        if re.match(regex2,str(int(ans)-int(num1))):
            line=re.sub('#',replac_num2,line)



            return line
        else:
            return '-1'
                    
        # print(num2_l,num2_r)


    elif "#" in ans :
        sum_num=str(int(num1)+int(num2))
        place3=ans.find("#")
        num3_l=ans[:place3]
        num3_r=ans[place3+1:]
        length3_l=len(num3_l)
        length3_r=len(num3_r)
        replac_num3=sum_num[place3:len(sum_num)-length3_r]

        regex3='^'+num3_l+'.*'+num3_r+'$'
        if re.match(regex3,sum_num):
            line=re.sub('#',replac_num3,line)
            return line
        else:
            return '-1'
    else:
        return '-1'



    pass


