def create_profile(**info):
    print("===프로필 정보=+=")
    for key, value in info.items():
        print(f"{key}:{value}")

create_profile(이름='김철수', 나이=30, 직업='엔지니어', 취미='독서')

