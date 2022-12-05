print("WELCOME TO SHOP AVENUE MALL!")
S1=['1b','2c','3a','6z','8f','9i','4y','7r','56d','43k','76w','90u','64q']
S2=['1c','22b','4d','9k','8f','9u','3h','7e','5e']
S3=['8f','9g','3h','7k','3s']
S4=['6g', '9k','4i','5j']
S5=['3e','9u']
list=[['Banana','2.25 AED/kg',10],['Apple ','3.75 AED/kg',20],['Orange','1.50 AED/kg',15],['Grapes','4.50 AED/kg',8]]
list1=[['Potato      ','3.25 AED/kg',20],['Onion       ','2.75 AED/kg',25],['Ginger      ','1.25 AED/kg',10],['Garlic      ','1.50 AED/kg',15],['Curry Leaves','3.25 AED/pc',13]]
list2=[['Moong Dal       ','5.50 AED/kg','  ',  7],['Urud Dal        ','4.75 AED/kg',' ', 12],['Toor Dal        ','9.50 AED/kg',' ', 17],['Basmati Rice    ','60.50 AED/5kg','',6],['Parboiled Rice  ','36.75 AED/5kg','',9],['Black Chick Peas','12.25 AED/kg','',12]]
list3=[['Youghurt       ','6.50 AED/L','      ',7],['Milk           ','5.75 AED/L','      ',8],['Milk Powder    ','12.25 AED/kg','    ',6],['Custard Pudding','1.75 AED/pc','    ',13],['Eggs           ','5.50 AED/6 eggs','',14],['Fresh Juice    ','8.25 AED/L','     ',11]]
list4=[['White Bread','4.75 AED(Medium sized)','',6],['Brown Bread','5.25 AED(Medium sized)','',5],['Cake       ','22.50 AED/kg','          ',4],['Biscuits   ','3.25 AED/packet','      ',12],['Chocolates ','7.75 AED/bar','         ',15]]
list5=[['Chicken   ','25.00 AED/kg','',6],['Mutton    ','40.00 AED/kg','',7],['Beef      ','35.00 AED/kg','',5],['Pork      ','20.00 AED/kg','',4],['Camel Meat','33.50 AED/kg','',6]]
list6=[['Shirt ','75.25 AED',' ',16],['Pant  ','150.25 AED','',10],['Suit  ','500.00 AED',' ',7],['Blazer','250.00 AED',' ',9]]
list7=[['Sweatshirts','70.00 AED',' ',20],['Jeans      ','125.50 AED','',17],['Hoodies    ','72.25 AED',' ',12],['Skirts     ','35.75 AED',' ',15],['Tops       ','27.75 AED',' ',22],['Jackets    ','125.50 AED','',11]]
list8=[['Shoes    ','155.75 AED/Pair','',13],['Sneakers ','110.00 AED/Pair','',16],['Converses','180.50 AED/Pair','',12],['Sandals  ','25.75 AED/Pair',' ',14],['Stilettos','100.00 AED/Pair','',10]]
list9=[['Ladies Bag  ','75.50 AED',' ',16],['Gents Wallet','55.00 AED',' ',22],['Sunglasses  ','215.25 AED','',13],['Perfumes    ','75.25 AED',' ',25],['Bracelets   ','5.50 AED','  ',28],['Necklaces   ','7.75 AED','  ',26],['Headbands   ','2.50 AED','  ',20]]
while True:
    print("\nChoose Options To Perform : ")
    print("1.Go shopping")
    print("2.Book Movies")
    print("3.Rent an Arcade")
    print("4.Register for an arcade card")
    print("5.Order food")
    print("6.Exit")
    choice=eval(input("\nEnter Your Choice :"))
    if choice==1:
        print("\nLETS GO SHOPPING!")
        while True:
            print("\n1: Grocery Shopping")
            print("2: Fashion Shopping")
            print("3: Exit")
            pj=eval(input("\nPls enter your choice:"))
            if pj==1:
                print("\nWELCOME TO EASTZONE!")
                s=0
                p2=()
                while True:
                    print("\n1: Shop fruits and vegetables")
                    print("2: Shop cereals and pulses")
                    print("3: Shop dairy products and fresh juices")
                    print("4: Shop bread and confectionaries")
                    print("5: Shop poultry")
                    print("6: Checkout and Exit")
                    p1=eval(input("\nPls enter your choice: "))
                    if p1==1:
                        t,t1,t2,t3,t4,t5,t6,t7,t8=0,0,0,0,0,0,0,0,0
                        print("\nFRUITS")
                        print('ITEM    ',' PRICE     ','    QUANTITY')
                        for i in range(4):
                            for j in range(3):
                                print(list[i][j],end='    ')
                            print()
                        print("\nVEGETABLES")
                        print('ITEM        ','  PRICE    ','    QUANTITY')
                        for i in range(5):
                            for j in range(3):
                                print(list1[i][j],end='   ')
                            print()
                        q=eval(input("\nNo. of items you wish to buy:"))
                        for i in range(q):
                            q1=input("\nEnter item name: ")
                            q2=eval(input("Quantity: "))
                            p2+=(q1,)
                            if q1=="Banana" or q1=="banana" or q1=="BANANA" or q1=="Bananas" or q1=="bananas" or q1=="BANANAS":
                                t=2.25*q2
                                s+=t
                                list[0][2]-=q2
                            elif q1=="Apple" or q1=="apple" or q1=="APPLE" or q1=="Apples" or q1=="apples" or q1=="APPLES":
                                t1=3.75*q2
                                s+=t1
                                list[1][2]-=q2
                            elif q1=="Orange" or q1=="orange" or q1=="ORANGE" or q1=="Oranges" or q1=="oranges" or q1=="ORANGES":
                                t2=1.50*q2
                                s+=t2
                                list[2][2]-=q2
                            elif q1=="Grapes" or q1=="grapes" or q1=="GRAPES" or q1=="Grape" or q1=="grape" or q1=="GRAPE":
                                t3=4.50*q2
                                s+=t3
                                list[3][2]-=q2
                            elif q1=="Potato" or q1=="potato" or q1=="POTATO" or q1=="Potatoes" or q1=="potatoes" or q1=="POTATOES":
                                t4=3.25*q2
                                s+=t4
                                list1[0][2]-=q2
                            elif q1=="Onion" or q1=="onion" or q1=="ONION" or q1=="Onions" or q1=="onions" or q1=="ONIONS":
                                t5=2.75*q2
                                s+=t5
                                list1[1][2]-=q2
                            elif q1=="Ginger" or q1=="ginger" or q1=="GINGER" or q1=="Gingers" or q1=="gingers" or q1=="GINGERS":
                                t6=1.25*q2
                                s+=t6
                                list1[2][2]-=q2
                            elif q1=="Garlic" or q1=="garlic" or q1=="GARLIC" or q1=="Garlics" or q1=="garlics" or q1=="GARLICS":
                                t7=1.50*q2
                                s+=t7
                                list1[3][2]-=q2
                            elif q1=="Curry leaves" or q1=="Curry Leaves" or q1=="curry leaves" or q1=="CURRY LEAVES" or q1=="Curry Leaf" or q1=="Curry leaf" or q1=="curry leaf" or q1=="CURRY LEAF":
                                t8=3.25*q2
                                s+=t8
                                list1[4][2]-=q2
                            else:
                                print("Inputted item is not available")
                    elif p1==2:
                        ta,ta1,ta2,ta3,ta4,ta5=0,0,0,0,0,0
                        print("\nPULSES AND CEREALS")
                        print("ITEM            ","     PRICE","                  QUANTITY")
                        for i in range(6):
                            for j in range(4):
                                print(list2[i][j],end='      ')
                            print()
                        qa=eval(input("\nNo. of items you wish to buy: "))
                        for i in range(qa):
                            qa1=input("\nEnter item name: ")
                            qa2=eval(input("Quantity: "))
                            p2+=(qa1,)
                            if qa1=="Moong Dal" or qa1=="moong dal" or qa1=="MOONG DAL" or qa1=="Moong dal":
                                ta=5.50*qa2
                                s+=ta
                                list2[0][3]-=qa2
                            elif qa1=="Urud Dal" or qa1=="urud dal" or qa1=="URUD DAL" or qa1=="Urud dal":
                                ta1=4.75*qa2
                                s+=ta1
                                list2[1][3]-=qa2
                            elif qa1=="Toor Dal" or qa1=="toor dal" or qa1=="TOOR DAL" or qa1=="Toor dal":
                                ta2=9.50*qa2
                                s+=ta2
                                list2[2][3]-=qa2
                            elif qa1=="Basmati Rice" or qa1=="basmati rice" or qa1=="BASMATI RICE" or qa1=="Basmati rice":
                                ta3=60.50*qa2
                                s+=ta3
                                list2[3][3]-=qa2
                            elif qa1=="Parboiled Rice" or qa1=="parboiled rice" or qa1=="PARBOILED RICE" or qa1=="Parboiled rice":
                                ta4=36.75*qa2
                                s+=ta4
                                list2[4][3]-=qa2
                            elif qa1=="Black Chick Peas" or qa1=="black chick peas" or qa1=="BLACK CHICK PEAS" or qa1=="Black chick peas" or qa1=="Black Chick Pea" or qa1=="black chick pea" or qa1=="Black chick pea" or qa1=="BLACK CHICK PEA":
                                ta5=12.25*qa2
                                s+=ta5
                                list2[5][3]-=qa2
                            else:
                                print("Inputted item is not available")
                    elif p1==3:
                        tb,tb1,tb2,tb3,tb4,tb5=0,0,0,0,0,0
                        print("\nDAIRY PRODUCTS AND FRESH JUICES")
                        print("ITEM               ","PRICE","                             QUANTITY")
                        for i in range(6):
                            for j in range(4):
                                print(list3[i][j],end='     ')
                            print()
                        qb=eval(input("\nNo. of items you wish to buy: "))
                        for i in range(qb):
                            qb1=input("\nEnter item name: ")
                            qb2=eval(input("Quantity: "))
                            p2+=(qb1,)
                            if qb1=="Youghurt" or qb1=="youghurt" or qb1=="YOUGHURT":
                                tb=6.50*qb2
                                s+=tb
                                list3[0][3]-=qb2
                            elif qb1=="Milk" or qb1=="milk" or qb1=="MILK":
                                tb1=5.75*qb2
                                s+=tb1
                                list3[1][3]-=qb2
                            elif qb1=="Milk Powder" or qb1=="milk powder" or qb1=="MILK POWDER" or qb1=="Milk powder":
                                tb2=12.25*qb2
                                s+=tb2
                                list3[2][3]-=qb2
                            elif qb1=="Custard Pudding" or qb1=="custard pudding" or qb1=="CUSTARD PUDDING" or qb1=="Custard pudding":
                                tb3=7.75*qb2
                                s+=tb3
                                list3[3][3]-=qb2
                            elif qb1=="Eggs" or qb1=="EGGS" or qb1=="eggs" or qb1=="Egg" or qb1=="egg" or qb1=="EGG":
                                tb4=5.50*qb2
                                s+=tb4
                                list3[4][3]-=qb2
                            elif qb1=="Fresh Juice" or qb1=="fresh juice" or qb1=="Fresh juice" or qb1=="FRESH JUICE" or qb1=="Fresh Juices" or qb1=="Fresh juices" or qb1=="fresh juices" or qb1=="FRESH JUICES":
                                tb5=8.25*qb2
                                s+=tb5
                                list3[4][3]-=qb2
                            else:
                                print("Inputted item is not available")
                    elif p1==4:
                        tc,tc1,tc2,tc3,tc4=0,0,0,0,0 
                        print("\nBREAD AND CONFECTIONARIES")
                        print("ITEM       ","    PRICE","                          QUANTITY")
                        for i in range(5):
                            for j in range(4):
                                print(list4[i][j],end='     ')
                            print()
                        qc=eval(input("\nNo. of items you wish to buy: "))
                        for i in range(qc):
                            qc1=input("\nEnter item name: ")
                            qc2=eval(input("Quantity: "))
                            p2+=(qc1,)
                            if qc1=="White Bread" or qc1=="white bread" or qc1=="WHITE BREAD" or qc1=="White bread":
                                tc=4.75*qc2
                                s+=tc
                                list4[0][3]-=qc2
                            elif qc1=="Brown Bread" or qc1=="brown bread" or qc1=="BROWN BREAD" or qc1=="Brown bread":
                                tc1=5.25*qc2
                                s+=tc1
                                list4[1][3]-=qc2
                            elif qc1=="Cake" or qc1=="cake" or qc1=="CAKE":
                                tc2=22.50*qc2
                                s+=tc2
                                list4[2][3]-=qc2
                            elif qc1=="Biscuits" or qc1=="biscuits" or qc1=="BISCUITS" or qc1=="Biscuit" or qc1=="biscuit" or qc1=="BISCUIT":
                                tc3=3.25*qc2
                                s+=tc3
                                list4[3][3]-=qc2
                            elif qc1=="Chocolates" or qc1=="chocolates" or qc1=="CHOCOLATES" or qc1=="Chocolate" or qc1=="chocolate" or qc1=="CHOCOLATE":
                                tc4=5.50*qc2
                                s+=tc4
                                list4[4][3]-=qc2
                            else:
                                print("Inputted item is not available")
                    elif p1==5:
                        td,td1,td2,td3,td4=0,0,0,0,0
                        print("\nPOULTRY")
                        print("ITEM      ","    PRICE","                QUANTITY")
                        for i in range(5):
                            for j in range(4):
                                print(list5[i][j],end='     ')
                            print()
                        qd=eval(input("\nNo. of items you wish to buy: "))
                        for i in range(qd):
                            qd1=input("\nEnter item name: ")
                            qd2=eval(input("Quantity: "))
                            p2+=(qd1,)
                            if qd1=="Chicken" or qd1=="chicken" or qd1=="CHICKEN":
                                td=25.00*qd2
                                s+=td
                                list5[0][3]-=qd2
                            elif qd1=="Mutton" or qd1=="mutton" or qd1=="MUTTON":
                                td1=40.00*qd2
                                s+=td1
                                list5[1][3]-=qd2
                            elif qd1=="Beef" or qd1=="beef" or qd1=="BEEF":
                                td2=35.00*qd2
                                s+=td2
                                list5[2][3]-=qd2
                            elif qd1=="Pork" or qd1=="pork" or qd1=="PORK":
                                td3=20.00*qd2
                                s+=td3
                                list5[3][3]-=qd2
                            elif qd1=="Camel Meat" or qd1=="CAMEL MEAT" or qd1=="camel meat" or qd1=="Camel meat":
                                td4=33.50*qd2
                                s+=td4
                                list5[4][3]-=qd2
                            else:
                                print("Inputted item is not available")
                    elif p1==6:
                        print("\nITEMS BOUGHT")
                        for i in range(len(p2)):
                            print(p2[i])
                        print("\nYour Total Bill: AED ",s)
                        jj0=input("\nEnter your name: ")
                        jj1=input("Enter your mobile no.: ")
                        jj2=input("Address: ")
                        jj3=input("Villa/Apartment no.: ")
                        nk=input("\nDo you have EASTZONE shopping card? ")
                        if nk=="Yes" or nk=="yes" or nk=="YES":
                            nm=eval(input("Please enter your shopping card no.: "))
                            print("You will be getting 10% discount on the goods purchased if your bill is above AED 20")
                            if s>20:
                                nk1=(10/100)*s
                                print("Your total bill: AED ",nk1)
                            else:
                                print("Your total bill: AED ",s)
                        elif nk=="no" or nk=="No" or nk=="NO":
                            nm1=input("Would you like to have the EASTZONE shopping card? ")
                            if nm1=="Yes" or nm1=="yes" or nm1=="YES":
                                print("Cost of card: AED 50")
                                print("Your total bill: AED ",s+50)
                        print("\n1: Pay by Cash on delivery")
                        print("2: Card payment")
                        zz2=eval(input("Choice: "))
                        if zz2==1:
                            print("\nName: ",jj0)
                            print("Mobile no.: ",jj1)
                            print("Address: ",jj2)
                            print("Villa/Apartment no.: ",jj3)
                            print("\nYour items will be delivered to "+jj2+" Villa/Apartment no.: "+jj3+" in 45 mins")
                        elif zz2==2:
                            kk1=input("Enter Card no.: ")
                            kk2=input("Enter Card security code: ")
                            kk3=input("Pls enter the OTP no. sent to your number: ")
                            print("\nName: ",jj0)
                            print("Mobile no.: ",jj1)
                            print("Address: ",jj2)
                            print("Villa/Apartment no.: ",jj3)
                            print("\nYour items will be delivered to "+jj2+" Villa/Apartment no.: "+jj3+" in 45 mins")
                        break
            elif pj==2:
                print("\nWELCOME TO DIOR FASHION!")
                ss=0
                p3=()
                while True:
                    print("\n1: Shop clothes")
                    print("2: Shop footwear")
                    print("3: Shop accesssories")
                    print("4: Checkout and Exit")
                    w=eval(input("\nPls enter your choice: "))
                    if w==1:
                        print("\n1: Formals")
                        print("2: Casuals")
                        w1=eval(input("Pls enter your choice: "))
                        if w1==1:
                            m,m1,m2,m3=0,0,0,0
                            print("\nFORMALS")
                            print("ITEM  ",  "    PRICE","              QUANTITY")
                            for i in range(4):
                                for j in range(4):
                                    print(list6[i][j],end='     ')
                                print()
                            r=eval(input("\nNo. of items you wish to buy: "))
                            for i in range(r):
                                r1=input("\nEnter item name: ")
                                r2=eval(input("Quantity: "))
                                p3+=(r1,)
                                if r1=="Shirt" or r1=="shirt" or r1=="SHIRT" or r1=="shirts" or r1=="Shirts" or r1=="SHIRTS":
                                    m=75.25*r2
                                    ss+=m
                                    list6[0][3]-=r2
                                elif r1=="Pant" or r1=="pant" or r1=="PANT" or r1=="Pants" or r1=="pants" or r1=="PANTS":
                                    m1=150.25*r2
                                    ss+=m1
                                    list6[1][3]-=r2
                                elif r1=="Suit" or r1=="suit" or r1=="SUIT" or r1=="suits" or r1=="Suits" or r1=="SUITS":
                                    m2=500.00*r2
                                    ss+=m2
                                    list6[2][3]-=r2
                                elif r1=="Blazer" or r1=="blazer" or r1=="BLAZER" or r1=="blazers" or r1=="Blazers" or r1=="BLAZERS":
                                    m3=250.00*r2
                                    ss+=m3
                                    list6[3][3]-=r2
                                else:
                                    print("Inputted item is not available")
                        elif w1==2:
                            m4,m5,m6,m7,m8,m9=0,0,0,0,0,0
                            print("\nCASUAlS")
                            print("ITEM  ",  "         PRICE","              QUANTITY")
                            for i in range(6):
                                for j in range(4):
                                    print(list7[i][j],end='     ')
                                print()
                            ra=eval(input("\nNo. of items you wish to buy: "))
                            for i in range(ra):
                                ra1=input("\nEnter item name: ")
                                ra2=eval(input("Quantity: "))
                                p3+=(ra1,)
                                if ra1=="Sweatshirts" or ra1=="sweatshirts" or ra1=="SWEATSHIRTS" or ra1=="sweatshirt" or ra1=="Sweatshirt" or ra1=="SWEATSHIRT":
                                    m4=70.00*ra2
                                    ss+=m4
                                    list7[0][3]-=ra2
                                elif ra1=="Jeans" or ra1=="jeans" or ra1=="JEANS":
                                    m5=125.50*ra2
                                    ss+=m5
                                    list7[1][3]-=ra2
                                elif ra1=="Hoodies" or ra1=="hoodies" or ra1=="HOODIES" or ra1=="hoodie" or ra1=="Hoodie" or ra1=="HOODIE":
                                    m6=72.25*rb2
                                    ss+=m6
                                    list7[2][3]-=ra2
                                elif ra1=="Skirts" or ra1=="skirts" or ra1=="SKIRTS" or ra1=="skirt" or ra1=="Skirt" or ra1=="SKIRT":
                                    m7=35.75*ra2
                                    ss+=m7
                                    list7[3][3]-=ra2
                                elif ra1=="Tops" or ra1=="tops" or ra1=="TOPS" or ra1=="top" or ra1=="Top" or ra1=="TOP":
                                    m8=27.75*ra2
                                    ss+=m8
                                    list7[4][3]-=ra2
                                elif ra1=="Jackets" or ra1=="jackets" or ra1=="JACKETS" or ra1=="jacket" or ra1=="Jacket" or ra1=="JACKET":
                                    m9=125.50*ra2
                                    ss+=m9
                                    list7[5][3]-=ra2
                                else:
                                    print("Inputted item is not available")
                    elif w==2:
                        n,n1,n2,n3,n4=0,0,0,0,0
                        print("\nFOOTWEAR")
                        print("ITEM  ",  "       PRICE","                  QUANTITY")
                        for i in range(5):
                            for j in range(4):
                                print(list8[i][j],end='     ')
                            print()
                        rb=eval(input("\nNo. of items you wish to buy: "))
                        for i in range(rb):
                            rb1=input("\nEnter item name: ")
                            rb2=eval(input("Quantity: "))
                            p3+=(rb1,)
                            if rb1=="Shoes" or rb1=="shoes" or rb1=="SHOES" or rb1=="shoe" or rb1=="Shoe" or rb1=="SHOE":
                                n=155.75*rb2
                                ss+=n
                                list8[0][3]-=rb2
                            elif rb1=="Sneakers" or rb1=="SNEAKERS" or rb1=="sneakers" or rb1=="sneaker" or rb1=="Sneaker" or rb1=="SNEAKERS":
                                n1=110.00*rb2
                                ss+=n1
                                list8[1][3]-=rb2
                            elif rb1=="Converses" or rb1=="converses" or rb1=="CONVERSES" or rb1=="converse" or rb1=="Converse" or rb1=="CONVERSE":
                                n2=180.50*rb2
                                ss+=n2
                                list8[2][3]-=rb2
                            elif rb1=="Sandals" or rb1=="sandals" or rb1=="SANDALS" or rb1=="sandal" or rb1=="Sandal" or rb1=="SANDAL":
                                n3=25.75*rb2
                                ss+=n3
                                list8[3][3]-=rb2
                            elif rb1=="Stilettos" or rb1=="stilettos" or rb1=="STILETTOS":
                                n4=100.00*rb2
                                ss+=n4
                                list8[4][3]-=rb2
                            else:
                                print("Inputted item is not available")
                    elif w==3:
                        n5,n6,n7,n8,n9,n10,n11=0,0,0,0,0,0,0
                        print("\nACCESSORIES")
                        print("ITEM  ",  "          PRICE","              QUANTITY")
                        for i in range(7):
                            for j in range(4):
                                print(list9[i][j],end='     ')
                            print()
                        rc=eval(input("\nNo. of items you wish to buy: "))
                        for i in range(rc):
                            rc1=input("\nEnter item name: ")
                            rc2=eval(input("Quantity: "))
                            p3+=(rc1,)
                            if rc1=="Ladies Bag" or rc1=="ladies bag" or rc1=="LADIES BAG" or rc1=="Ladies bag":
                                n5=75.50*rc2
                                ss+=n5
                                list9[0][3]-=rc2
                            elif rc1=="Gents Wallet" or rc1=="Gents wallet" or rc1=="gents wallet" or rc1=="GENTS WALLET":
                                n6=55.00*rc2
                                ss+=n6
                                list9[1][3]-=rc2
                            elif rc1=="Sunglasses" or rc1=="sunglasses" or rc1=="SUNGLASSES" or rc1=="sunglass" or rc1=="Sunglass" or rc1=="SUNGLASS":
                                n7=215.25*rc2
                                ss+=n7
                                list9[2][3]-=rc2
                            elif rc1=="Perfumes" or rc1=="perfumes" or rc1=="PERFUMES" or rc1=="perfume" or rc1=="Perfume" or rc1=="PERFUME":
                                n8=75.25*rc2
                                ss+=n8
                                list9[3][3]-=rc2
                            elif rc1=="Bracelets" or rc1=="bracelets" or rc1=="BRACELETES" or rc1=="bracelet" or rc1=="Bracelet" or rc1=="BRACELET":
                                n9=5.50*rc2
                                ss+=n9
                                list9[4][3]-=rc2
                            elif rc1=="Necklaces" or rc1=="necklaces" or rc1=="NECKLACES" or rc1=="necklace" or rc1=="Necklace" or rc1=="NECKLACE":
                                n10=7.75*rc2
                                ss+=n10
                                list9[5][3]-=rc2
                            elif rc1=="Headbands" or rc1=="headbands" or rc1=="HEADBANDS" or rc1=="headband" or rc1=="Headband" or rc1=="HEADBAND":
                                n11=2.50*rc2
                                ss+=n11
                                list9[6][3]-=rc2
                            else:
                                print("Inputted item is not available")
                    elif w==4:
                        print("\nITEMS BOUGHT")
                        for i in range(len(p3)):
                            print(p3[i])
                        print("\nYour Total Bill: AED",ss)
                        j0=input("\nEnter your name: ")
                        j1=input("Enter your mobile no.: ")
                        j2=input("Address: ")
                        j3=input("Villa/Apartment no.: ")
                        ng=input("\nDo you have DIOR FASHION shopping card? ")
                        if ng=="Yes" or ng=="yes" or ng=="YES":
                            nn=eval(input("Please enter your shopping card no.: "))
                            print("You will be getting 10% discount on the goods purchased if your bill is above AED 20")
                            if ss>50:
                                ng1=(10/100)*ss
                                print("Your total bill: AED ",ng1)
                            else:
                                print("Your total bill: AED ",ss)
                        elif ng=="no" or ng=="No" or ng=="NO":
                            nn1=input("Would you like to have the DIOR FASHION shopping card? ")
                            if nn1=="Yes" or nn1=="yes" or nn1=="YES":
                                print("Cost of card: AED 75")
                                print("Your total bill: AED ",ss+75)
                        print("\n1: Pay by Cash on delivery")
                        print("2: Card payment")
                        z2=eval(input("choice: "))
                        if z2==1:
                            print("\nName: ",j0)
                            print("Mobile no.: ",j1)
                            print("Address: ",j2)
                            print("Villa/Apartment no.: ",j3)
                            print("Your items will be delivered to "+j2+" Villa/Apartment no.: "+j3+" in 45 mins")
                        elif z2==2:
                            k1=input("Enter Card no.: ")
                            k2=input("Enter Card security code: ")
                            k3=input("Pls enter the OTP no. sent to your number: ")
                            print("\nName: ",j0)
                            print("Mobile no.: ",j1)
                            print("Address: ",j2)
                            print("Villa/Apartment no.: ",j3)
                            print("\nYour items will be delivered to "+j2+" Villa/Apartment no.: "+j3+" in 45 mins")
                        break
                        
            elif p==3:
                print("\nTHANK YOU FOR SHOPPING WITH US! HAVE A NICE DAY!")
                break
    elif choice==2:
        movies=[['Bean','1 hour 51 minutes','8.3/10','Family/Comedy'],['Cars','1 hour 29 minutes','8.5/10','Family/Adventure'],['Hugo','1 hour 49 minutes','8.4/10','Family/Adventure'],['Sing','1 hour 54 minutes','7.1/10','Family/Adventure'],['Coco','1 hour 42 minutes','8.1/10','Family/Adventure']]
        t=[]
        print('\nWELCOME TO BOX CINEMAS!\n')
        c='Name :'+input('Enter your name:')
        yi=input('Enter mobile number:')
        if len(yi)!=10:
            print('INVALID MOBILE NUMBER')
        else:
            d='Mobile number :'+yi
        n=int(input('Enter number of tickets:'))
        t=[c,d]
        sp=0
        import random
        while True:
            print('\nPRESS 1: To display the showcasting movies:')
            print('ENTER 2: To see the showtimes of movies and select it:')
            print('ENTER 3: To select the screen and the seat in the theatre:')
            print('ENTER 4: To add condiments:')
            print('ENTER 5: To select the mode of payment and make payment:')
            print('ENTER 6: To display the booked ticket:')
            print('ENTER 7: To exit:')
            ch=input('Enter your choice:')
            if ch=='1':
                print('\nMOVIES   ','RUNTIME             ','IMdb         ','GENRE   ')
                for i in range(5):
                    for j in range(4):
                        print(movies[i][j],end='     ')
                    print()
                lk=input('Enter selected movie:')
                if lk in ['Bean','Cars','Coco','Sing','Hugo']:
                    e='Movie :'+lk
                    t+=[e]
                else:
                    print('Movie not showcasted')
            elif ch=='2':
                m=input('Enter movie:')
                if m  in ['Bean','Cars','Coco','Sing','Hugo']:
                    day=input('Enter day in capital letters:')
                    if day not in ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']:
                        print('INVALID DAY')
                        break
                    else:
                       month=input('Enter month in capital letters:')
                       if month not in ['JANUARY','FEBRUARY']:
                           print('INVALID')
                           break
                       else:
                          D='Date: '+day+','+month+','+'2021'
                          t+=[D]
                          x=random.randint(1,9)
                          print('showtimes for',m,':')
                          k=1
                          for i in range(4):
                              if i==0 or (i%2!=0 and r!=x):
                                  print(x,'am',end='  ')
                                  r=x
                              else:
                                 print(x+k,'pm',end='  ')
                                 k+=1
                          print()
                          y='Showtime :'+input('Enter selected time:')
                          t+=[y]
                else:
                    print('Movie not showcasted')
            elif ch=='3':
                v=input('Enter movie:')
                if v in ['Bean','Cars','Coco','Sing','Hugo']:
                    l=['1:Screen-1-Dubai','2:Screen-2-Sharjah','3:Screen-3-Fujairah','4:Screen-4-Ajman','5:Screen-5-Abudhabi']
                    print('\nScreens:')
                    for j in l:
                        print(j)
                    print()
                    so=int(input('Enter number to select the screen:'))
                    sc='Screen: '+l[so-1]
                    t+=[sc]
                    if so==1:
                        print('Vacant seats:')
                        for k in S1:
                            print(k,end=',')
                        print()
                        print('Number of available seats:',len(S1))
                        bn=1
                        if n<=len(S1):
                            while bn<=n:
                                j=input('Enter you seat:')
                                u='Seat number :'+j
                                t+=[u]
                                for kj in range(len(S1)):
                                    if S1[kj]==j:
                                        del S1[kj]
                                        break
                                bn+=1
                        else:
                            print('Sorry,seats are not available for your desired number.')
                    elif so==2:
                        print('Vacant seats:')
                        for k in S2:
                            print(k,end=',')
                        print()
                        print('Number of available seats:',len(S2))
                        bn=1
                        if n<=len(S2):
                            while bn<=n:
                                j=input('Enter you seat:')
                                u='Seat number :'+j
                                t+=[u]
                                for kj in range(len(S2)):
                                    if S2[kj]==j:
                                        del S2[kj]
                                        break
                                bn+=1
                        else:
                            print('Sorry,seats are not available for your desired number.')
                    elif so==3:
                       print('Vacant seats:')
                       for k in S3:
                           print(k,end=',')
                       print()
                       print('Number of available seats:',len(S3))
                       bn=1
                       if n<=len(S3):
                           while bn<=n:
                               j=input('Enter you seat:')
                               u='Seat number :'+j
                               t+=[u]
                               for kj in range(len(S3)):
                                   if S3[kj]==j:
                                        del S2[kj]
                                        break
                               bn+=1
                       else:
                           print('Sorry,seats are not available for your desired number.')
                    elif so==4:
                       print('Vacant seats:')
                       for k in S4:
                           print(k,end=',')
                       print()
                       print('Number of available seats:',len(S4))
                       bn=1
                       if n<=len(S4):
                           while bn<=n:
                               j=input('Enter you seat:')
                               u='Seat number :'+j
                               t+=[u]
                               for kj in range(len(S4)):
                                   if S4[kj]==j:
                                        del S4[kj]
                                        break
                               bn+=1
                       else:
                           print('Sorry,seats are not available for your desired number.')
                    elif so==5:
                       print('Vacant seats:')
                       for k in S5:
                           print(k,end=',')
                       print()
                       print('Number of available seats:',len(S5))
                       bn=1
                       if n<=len(S5):
                           while bn<=n:
                               j=input('Enter you seat:')
                               u='Seat number :'+j
                               t+=[u]
                               for kj in range(len(S5)):
                                   if S5[kj]==j:
                                        del S4[kj]
                                        break
                               bn+=1
                       else:
                           print('Sorry,seats are not available for your desired number.')
                else:
                    print('Movie not showcasted')
            elif ch=='4':
                j=[['1:Popcorn','-Cost:',25],['2:Nachos','-Cost:',30],['3:Samosas','-Cost:',15],['4:Pepsi','-Cost:',15],['5:Coke','-Cost:',15],['6:Nuggets','-Cost:',35]]
                for ty in range(6):
                    for hj in range(3):
                        print(j[ty][hj],end=' ')
                    print()
                op=int(input('Enter number of condiments:'))
                for c in range(op):
                    oi=int(input('Enter code no of to select condiment:'))
                    q='Condiment  :'+j[oi-1][0]
                    sp+=j[oi-1][2]
                    t+=[q]
            elif ch=='5':
                mode=int(input('Enter 1 to pay by cash or 2 to pay by card:'))
                if mode==1:
                    b='Mode of payment  :'+'cash'
                else:
                    b='Mode of payment  :'+'card'
                if mode==2:
                    print()
                    print('Make your movies more enjoyable with your ABC card!')
                    print()
                    print('Enjoy the exclusive discount of 20% for tickets at BOX Cinemas.')
                    print()
                    card=input('Enter your card:')
                    p=random.randint(150,225)
                    if card=='ABC':
                        print('Cost of one ticket of movie',lk,':',p,'AED')
                        discount=(p*n)*0.8
                        price=round(discount,2)
                        print('Cost of tickets(discounted price):',price,'AED')
                        print('Cost of condiment:',sp,'AED')
                        pl='Total cost:'+str(price+sp)+' AED'
                        print('Total cost:',price+sp,'AED')
                        t+=[b]
                        t+=[pl]
                    else:
                        print('Cost of one ticket of movie',lk,':',p,'AED')
                        print('Cost of tickets:',p*n,'AED')
                        print('Cost of condiment:',sp,'AED')
                        pl='Total cost:'+str(p*n+sp)+' AED'
                        print('Total cost:',p*n+sp,'AED')
                        t+=[b]
                        t+=[pl]
                else:
                    print('Cost of one ticket of movie',lk,':',p,'AED')
                    print('Cost of tickets:',p*n,'AED')
                    print('Cost of condiment:',sp,'AED')
                    pl='Total cost:'+str(p*n+sp)+' AED'
                    print('Total cost:',p*n+sp,'AED')
                    t+=[b]
                    t+=[pl]
            elif ch=='6':
                print()
                for m in t:
                    print(m)
                print()
                print('THANK YOU!')
            elif ch=='7':
                break
    elif choice==3:
        a=input("\nEnter your name: ")
        rz=input("Enter your phone no.")
        z=input("Do you have an existing arcade card?")
        list78=[]
        print("\n",a,"please choose a place to rent: ")
        print("1.Hub zone-Dubai")
        print("2.Magic planet-Sharjah")
        print("3.Fun Zone-Ras al Khaimah")
        arcade=eval(input("Enter Your Choice number :"))
        if arcade==1:
            print("\nThe charge per hour is 250 aed")
            b=eval(input("how many hours do you want to rent?"))
            if z=="YES" or z=="Yes" or z=="yes" :
                print("You will have 10% offer")
                print("Total cost is",250-(250*b*(10/100)))
            elif z=="NO" or z=="No" or z=="no":
                print("Your total cost is",b*250)
            else:
                print("invalid response")
        elif arcade==2:
            print("\nThe charge per hour is 150 aed")
            c=eval(input("how many hours do you want to rent?"))
            print("Your total cost is",c*150)
            if z=="YES" or z=="Yes" or z=="yes" :
                print("You will have 10% offer")
                print("Total cost is",150-(150*c*(10/100)))
            elif z=="NO" or z=="No" or z=="no":
                print("Your total cost is",c*150)
            else:
                print("invalid response")
        elif arcade==3:
            print("\nThe charge per hour is 100 aed")
            d=eval(input("how many hours do you want to rent?"))
            if z=="YES" or z=="Yes" or z=="yes" :
                print("You will have 10% offer")
                print("Total cost is",100-(100*d*(10/100)))
            elif z=="NO" or z=="No" or z=="no":
                print("Your total cost is",d*100)
            else:
                print("invalid response")
        ww1=input("\ndd/mm/yyyy of the date to be booked for: ")
        print("\n1: Pay by cash on arrival")
        print("2: Card Payment")
        zzz1=eval(input("Choice: "))
        if zzz1==1:
            print("Pay on arrival to the arcade")
        elif zzz1==2:
            k1=input("Enter Card no.: ")
            k2=input("Enter Card security code: ")
            k3=input("Pls enter the OTP no. sent to your number: ")
        print("\nRECEIPT")
        print("Name:",a)
        print("Phone no.:",rz)
        if arcade==1:
            print("Location: Hub zone-Dubai")
        elif arcade==2:
            print("Location:Magic Planet-Sharjah")
        elif arcade==3:
            print("Location: Fun zone-RAK")
        print("Date booked for:",ww1)
        if arcade==1:
            if z=="YES" or z=="Yes" or z=="yes" :
                print("Total cost: AED ",250-(250*c*(10/100)))
            elif z=="NO" or z=="No" or z=="no":
                print("Total cost: AED ",c*250)
        elif arcade==2:
            if z=="YES" or z=="Yes" or z=="yes" :
                print("Total cost: AED ",150-(150*c*(10/100)))
            elif z=="NO" or z=="No" or z=="no":
                print("Total cost: AED ",c*150)
        elif arcade==3:
            if z=="YES" or z=="Yes" or z=="yes" :
                print("Total cost: AED ",100-(100*d*(10/100)))
            elif z=="NO" or z=="No" or z=="no":
                print("Total cost: AED ",d*100)
        if z=="YES" or z=="Yes" or z=="yes" :
            print("Has an arcade card")
        else:
            print("No arcade card")
        print("Thank you!")
    elif choice==4:
        fw=input("Enter your phone number: ")
        gw=input("Enter your full name:")
        print("\nDo you have an existing arcade card?")
        option=input("Yes or No: ")
        if option=="Yes" or option=='yes'or option=="YES":
            fw1=eval(input("\nEnter existing amount: "))
            fw2=eval(input("Amount to recharge: "))
            print("Total amount: ",fw1+fw2)
            gw1=input("Enter Card no.: ")
            gw2=input("Enter Card security code: ")
            gw3=input("Pls enter the OTP no. sent to your number: ")
            print("\nName: ",gw)
            print("Phone No.: ",fw)
            print("AED ",fw1+fw2," has been deducted")
        elif option=="No"or option=='no'or option=="NO":
            print("\nCost of the card is AED 210")
            gww1=input("Enter Card no.: ")
            gww2=input("Enter Card security code: ")
            gww3=input("Pls enter the OTP no. sent to your number: ")
            print("\nName: ",gw)
            print("Phone No.: ",fw)
            print("AED 210 has been deducted")
    elif choice==5 :
        e=input("\nEnter your name:")
        print(e,"please choose a combo from the below: ")
        print("111.Veggie Burger Meal = AED 5")
        print("222.Chicken Burger Meal = AED 7")
        print("333.Veg pasta and veg pizza combo = AED 25")
        print("444.Chicken pasta and chicken pizza combo = AED 35")
        food1=eval(input("\nNo. of items you would like to order: "))
        hh=0
        for i in range(food1):
            food=eval(input("\nFood code: "))
            food2=eval(input("Quantity: "))                
            if food==111:
                bb=5*food2
                hh+=bb
            elif food==222:
                dd=7*food2
                hh+=dd
            elif food==333:
                ff=25*food2
                hh+=ff
            elif food==444:
                gg=35*food2
                hh+=gg
        print("Total amount: AED",hh)
        jjjj1=input("\nEnter your mobile no.=")
        jjjj2=input("Address: ")
        jjjj3=input("Villa/Apartment no.: ")
        print("\n1: Pay by cash on delivery")
        print("2: Card Payment")
        zzzz1=eval(input("Choice: "))
        if zzzz1==1:
            print("Your food will be delivered to "+jjjj2+" Villa/Apartment no.: "+jjjj3+" in 45 mins")
        elif zzzz1==2:
            kkkk1=input("Enter Card no.: ")
            kkkk2=input("Enter Card security code: ")
            kkkk3=input("Pls enter the OTP no. sent to your number: ")
            print("Your food will be delivered to "+jjjj2+" Villa/Apartment no.: "+jjjj3+" in 45 mins")
            break
    elif choice==6:
        print("THANK YOU FOR VISITING! SEE YOU NEXT TIME")
        break
    else:
        print("Invalid Option")
                
                                         
                    
