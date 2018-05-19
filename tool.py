def strQ2B(ustring):
	ss = ""
	for s in ustring:
		inside_code = ord(s)
		if inside_code == 12288: # 全形空格直接轉換
			inside_code = 32
		elif (inside_code >= 33 and inside_code <= 126 and s.isalpha()!=1): # 全形字元（除空格）根據關係轉化
			inside_code += 65248
		rstring = ""
		rstring += chr(inside_code)
		ss+=rstring
	return ss


print(strQ2B(input()))