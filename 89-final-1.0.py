print("厚骅软件工作室出品。")
keep_going = True
while keep_going:

    try:
        a=eval(input("\n请输入原值（如123xx就输入12300）："))
        b=eval(input("请输入追加最小值（若题目中没提到，就输入0）："))
        c=eval(input("请输入追加最大值（若题目中没提到，就输入空格数目个9）："))
        d=eval(input("请输入除数："))
        
    except:
        print("您的输入有误！")

    else:
        numbers=0
        print("\n以下为题目，请核对：")
        print("给"+str(a)+"加上"+str(b)+"到"+str(c)+
              "之间的数，使其能被"+str(d)+"整除。")
        print("\n以下为所有结果：")
        for x in range (b,c):
            sum = a + x
            if sum % d == 0:
                print(str(sum)+"     （加上"+str(x)+"）")
                numbers += 1
        print("\n共"+str(numbers)+"个结果。")
        
    keep = input("\n继续吗？\n输入任意键以退出，或按[ENTER]以重新运行本程序。")
    if keep != "":
        keep_going = False
