import re


pattern=r'[name]'
a='''hello my name is ahil skfkf
fjlksdjf
dskfjskdjfs
fkslgjldksfkjldksjf
f
sflksdjflks
dfs
df
sfdskfsdfksldf
asflkldsfjsdf
sdflkds
fsdfksdf;s kfjldskjfldkjf f kll jlkfjldksjfeirow  je    dfdsajkfa
dkflfjlakdfjeifdljfie kfjdoiefjasdkijfeif   
fsdfjeoi fnldjisoi  jfoeijfikoguwrgieifjgut8ou 
a
 fdsdfoaJf83i oij'''

matc=re.match(pattern,a)
print(matc)

matches=re.finditer(pattern,a)

for i in matches:
    print(i.span())
    print(a[i.span()[0]:i.span()[1]])