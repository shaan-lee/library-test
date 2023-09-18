import instaloader

loader = instaloader.Instaloader()

##계정 이름으로 프로필 사진 다운로드 (계정 이름, 사진만 가져올지 아니면 다른 정보도 가져올지)
#loader.download_profile("hhh.e_c.v", profile_pic_only=True)

##해시태그로 해당 해시태그 포스트 리스트 가져오기
#search_hashtag = "웹툰"
#hashtag = loader.get_hashtag_posts(search_hashtag)
#for post in hashtag:
#    print(post)
#    #포스트 id로 포스트 내용 다운로드 (post 객체, 다운로드 폴더 이름)
#    loader.download_post(post, search_hashtag)

##프로필 아이디를 계정 이름으로 가져오기
#profile = loader.check_profile_id("dlwlrma")
##프로필이 태그된 게시물 다운로드
#loader.download_tagged(profile)