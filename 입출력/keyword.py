#키워드 매개변수에 대해 알아보자. 키워드 매개변수는 함수 호출시 
#키워드 = 값 형태로 전달하는 매개변수를 받을때 사용한다. 
#키워드 매개변수를 사용할 때는 매개변수 앞에 별2개를 붙인다.

def print_kwargs(**kwargs):
        print(kwargs)

print_kwargs(a=1)
#{'a':1}
print_kwargs(name = 'foo', age =3)
#{'name': 'foo', 'age':3 }
print_kwargs(name ='홍길동', age = '25', city= '서울', job='개발자')
#{'name':'홍길동', 'age' : '25', 'city' : '서울', 'job' : '개발자'}

