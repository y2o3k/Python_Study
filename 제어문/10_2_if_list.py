# 주머니에 돈이 있으면 택시를 타고가고 
# 주머니에 돈은 없지만 키드가 있으면 택시를 타고가고
# 돈도 없고 카드도 없으면 걸어가라

pocket =['paper', 'celphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

        