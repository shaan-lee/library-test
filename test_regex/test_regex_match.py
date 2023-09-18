import re

# string = "https://dojang.io/jpgmod/page/view.php?id=2435png dfdfd "
# string2 = "https://velog.io/@hyukstory/python8-%EC%A0%95%EA%B7%9C%EC%8B%9D%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-bs4.jpg fs"
# string3 = "sdkdfhs dkdk lls pp"
# string4 = "https://image.tmdb.org/t/p/w154/hovergPwXtxnEgppVaMsrpPNajw1K7LH.jpg 100w, https://image.tmdb.org/t/p/w154/gPwXtxnEgppVaMsrpPNajw1K7LH.jpg 200w, https://image.tmdb.org/t/p/w154/gPwXtxnEgppVaMsrpPNajw1K7LH.jpg 300w"
# string4 = string4.split(",")
# re_string = "(?:.*(?:jpg|jpeg|png|gif|tiff|svg)$)|(?:.*[^(?:hover)].*(?:jpg|jpeg|png|gif|tiff|svg)) "
# regex = re.compile(re_string)
# tmp_list = []
# tmp_list.append(string)
# string = tmp_list
# url = regex.findall(string[0])
# url2 = regex.findall(string2)
# url3 = regex.findall(string3)
# url4 = regex.findall(string4[0])
# url5 = re.findall(re_string, string4[0])

num1 = "123dkdk233dkdk2342slaf234"

re_num = "([0-9]+)"
find_num = re.findall(re_num, num1)
print(find_num)
