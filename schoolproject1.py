import pandas as pd
while True:
    print("1.ADD PROPERTY\n2.ADD TENANT\n3.SHOW PROPERTY\n4.SHOW TENANT\n5.FIND PROPERTY\n6.ON RENT\n7.DELETE PROPERTY\n8.EXIT")
    ch=int(input('enter choice'))
    if ch==1:
        try:
            df=pd.read_csv('property1.csv')
        except FileNotFoundError:
            df=pd.DataFrame(columns= ['houseno','PINCODE','AREA','ADDRESS','RENT'])
        if df.empty:
            next_houseno=1
        else:
            f=len(df)
            next_houseno = f+1
        a= int(input('ENTER PINCODE='))
        b= input('ENTER AREA=')
        c=input('ENTER ADDRESS=')
        d=int(input('ENTER RENT OF HOUSE'))
        df.loc[len(df.index)]=[next_houseno,a,b,c,d]
        df.to_csv('property1.csv',index =False)
    elif ch==2:
        try:
            tf=pd.read_csv('tenant.csv')
        except FileNotFoundError :
            tf=pd.DataFrame(columns=['SNO','NAME','PERMANENT ADDRESS','MOBILE NO.','EMERGENCY MOBILE NO.'])
        if tf.empty:
            next_SNO=1
        else :
            e= len(tf)
            next_SNO = e+1
        g= input('ENTER NAME=')
        h=input ('ENTER PERMANENT ADDRESS=')
        i=int(input('ENTER MOBILE NO.='))
        k=int(input('ENTER EMERGENCY MOBILE NO.='))
        tf.loc[len(tf.index)]=[next_SNO,g,h,i]
        tf.to_csv('tenant.csv',index= False)
    elif ch==3:
        try:
            df=pd.read_csv('property.csv')
            print(df)
        except FileNotFoundError:
            print("try csv file ' property.csv' does not exist or empty.")
    elif ch==4:
        try:
            tf=pd.read_csv('tenant.csv')
            print(tf)
        except FileNotFoundError:
            print("try csv file ' tenant.csv' does not exist or empty.")
    elif ch==5:
        try:
            df=pd.read_csv('property.csv')
            area_find=input('ENTER THE AREA OF PROPERTY TO FIND')
            result=df[df['AREA']==area_find]
            if result.empty:
                print('no data found for ',area_find)
            else:
                print('found data fro',area_find)
                print(result)
                
        except FileNotFoundError:
            print('no data found for ',area_find)
    elif ch==6:
        try:
            df=pd.read_csv('property')
        except FileNotFoundError :
            print("the csv file'tenent.csv' does not exist or is empty")
            
            
            
                
                
        
            
            
    

    
