from hashlib import md5, sha1

print("MD5 SECTION------------------------")
print("ENSEA:" ,md5(b"ENSEA").hexdigest())
print("eNSEA:" ,md5(b"eNSEA").hexdigest())
print("ENSEA:" ,md5(b"ENSEA").hexdigest())

print("SHA1 SECTION-----------------------")
print("ENSEA:" ,sha1(b"ENSEA").hexdigest())
print("eNSEA:" ,sha1(b"eNSEA").hexdigest())
print("ENSEA:" ,sha1(b"ENSEA").hexdigest())

texte_long="这是中文内核文档树的顶级目录。modification aléatoire de la chaine内核文档，就像内核本身一样，在很大程度上是一 项正在进行的工作；当我们努力将许多分散的文件整合成一个连贯的整体时尤其如此。 另外，随时欢迎您对内核文档进行改进；如果您想提供帮助，请加入vger.kernel.org 上的linux-doc邮件列表，并按照Documentation/translations/zh_CN/how-to.rst的 指引提交补丁。提交补丁之前请确保执行”make htmldocs”后无与翻译有关的异常输出"
print("long texte",md5(texte_long.encode('utf-8')).hexdigest())


texte_long1=0xd131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70
texte_long2=0xd131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70



texte_long1_bytes = texte_long1.to_bytes((texte_long1.bit_length() + 7) // 8, 'big')
texte_long2_bytes = texte_long2.to_bytes((texte_long2.bit_length() + 7) // 8, 'big')


md5_1 = md5(texte_long1_bytes).hexdigest()
md5_2 = md5(texte_long2_bytes).hexdigest()

if md5_1 == md5_2:
    print("Collision")
else:
    print("Pas collision")

print(md5_1)
print(md5_2)