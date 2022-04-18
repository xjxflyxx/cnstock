__all__ = [
		'get_api_list',
		'get_A_code_arr',
		'get_B_code_arr',
		'get_jijin_code_arr',
		'get_kcb_code_arr',
		'get_cyb_code_arr',
		'get_sh60_code_arr',
		'get_sz00_code_arr',
		'get_bj_code_arr',
		'get_bad_name_arr',
		'get_all_rule',
		'get_rule',
		'get_prefixed_code',
		'get_prefixed_code_arr',
		'get_index_code',
		'get_market_found_date',
		'get_symbol_star',
		'get_symbol_st',
		'get_symbol_N'
		]

#coding=utf-8

"""
作者：xjxfly
邮箱：xjxfly@qq.com

说明：
这是中国股市规则库
调用本模块中的各接口，将返回中国股市中各类别股票的交易规则
注意：本包各种接口只提供规则，不提供数据！！！切记！！！


"""


#from . import common_config as cf
from cnstock import common_config as cf

# --------------------------------------------------










# ================================================================
# ================================================================
# ================================================================
# ================================================================
# ================================================================
# ================================================================
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# public API start




def get_api_list():
	"""
	功能说明：本接口不对外使用，仅用于向调用模块返回本模块能提供的接口列表
	"""
	return __all__







def get_A_code_arr():
	"""
	功能说明：返回A股代码类型标识
	"""
	return cf.A_CODE_ARR






def get_B_code_arr():
	"""
	功能说明：返回B股代码类型标识
	"""
	return cf.B_CODE_ARR




def get_jijin_code_arr():
	"""
	功能说明：返回基金代码类型标识
	"""
	return cf.JIJIN_CODE_ARR





def get_kcb_code_arr():
	"""
	功能说明：返回科创板股代码类型标识
	"""
	return cf.KCB_CODE_ARR




def get_cyb_code_arr():
	"""
	功能说明：返回创业板股代码类型标识
	"""
	return cf.CYB_CODE_ARR




def get_sh60_code_arr():
	"""
	功能说明：返回创业板股代码类型标识
	"""
	return cf.SH60_CODE_ARR




def get_sz00_code_arr():
	"""
	功能说明：返回创业板股代码类型标识
	"""
	return cf.SZ00_CODE_ARR





def get_bj_code_arr():
	"""
	功能说明：返回北交所股票代码类型标识
	"""
	return cf.BJ_CODE_ARR





def get_bad_name_arr():
	"""
	功能说明：返回股票名称（不是股票代码）中有ST等各种垃圾字符的 list, 这个 list 专门收集了各种垃圾字符，返回给调用者当过滤器用

	Returns
	-------
	list, 每个元素是指出垃圾字符。
	"""
	return cf.BAD_NAME_ARR
	
	
	
	
	




def get_all_rule():
	"""
	功能说明：返回所有已定义的股票类型（含基金等）的规则字典

	Returns
	-------
	返回值：所有已定义的股票类型（含基金等）的规则字典。

	"""	
	return cf.RULE_DICT 		# 这个 dict 中的每个元素也是 DICT
	
	
	
	
	
	
	
	
def get_rule(code_type=None):
	"""
	说明：根据传入的股票代码类别，返回该类别的交易规则
	参数：code_type：股票代码类别，可取值为 cf.RULE_DICT 中的 key，或接受下面出错提示那些值；若 code_type 为 None，则返回 DEFAULT 所指向的规则
	返回值：该类型交易规则（dict 形式）
	"""
	rule_dict = None 		# 初始化股市规则字典为  None
	if code_type is None:
		rule_dict = cf.DEFAULT_RULE_DICT
	else:
		code_type = str(code_type).upper() 		# 转成大写
		# 上证60开头且是st的股
		if code_type in cf.SH60ST_SYMBOL_ARR:
			code_type = cf.SH_LETTER_PREFIX.upper() + cf.SH60 + cf.ST

		# 深证00开头且是st的股
		if code_type in cf.SZ00ST_SYMBOL_ARR:
			code_type = cf.SZ_LETTER_PREFIX.upper() + cf.SZ00 + cf.ST

		# 上证60开头的正常股(也可能包含ST, 如果不要 st，则把这个类型传递到上层代码后，由上层代码去处理并去掉 st 股)
		if code_type in cf.SH60_SYMBOL_ARR:
			code_type = cf.SH_LETTER_PREFIX.upper() + cf.SH60

		# 深证00开头的正常股(也可能包含ST, 如果不要 st，则把这个类型传递到上层代码后，由上层代码去处理并去掉 st 股)
		if code_type in cf.SZ00_SYMBOL_ARR:
			code_type = cf.SZ_LETTER_PREFIX.upper() + cf.SZ00

		# 上证688开头的股（可能也包含st，因为688 中的 st 与 688 中的其他股交易规则一样）
		if code_type in cf.SH688_SYMBOL_ARR:
			code_type = cf.SH_LETTER_PREFIX.upper() + cf.SH688

		# 深证30开头的股（可能也包含st，因为30 中的 st 与 30 中的其他股交易规则一样）
		if code_type in cf.SZ30_SYMBOL_ARR:
			code_type = cf.SZ_LETTER_PREFIX.upper() + cf.SZ30

		# -------------------
		if code_type in cf.RULE_DICT: 		# 这种表达式表示在 cf.RULE_DICT 是否一个键为 code_type , 如果有，下面这行就取这个键对应的值（在这里，值本身又是一个 dict）
			rule_dict = cf.RULE_DICT[code_type]
		else:
			print('错误！请确保传入的参数 code_type 只能取以下值之一，然后本函数将返回对应股票类型的交易规则（字典形式）：')
			print('目前只支持获取沪深A股交易规则，暂不支持沪深B股及沪深基金的交易规则（但获取行情不受影响，即可以获取沪深A股、B股及基金的行情。')
			print(cf.SH60ST_SYMBOL_ARR)
			print(cf.SZ00ST_SYMBOL_ARR)
			print(cf.SH60_SYMBOL_ARR)
			print(cf.SH688_SYMBOL_ARR)
			print(cf.SZ00_SYMBOL_ARR)
			print(cf.SZ30_SYMBOL_ARR)
			#print(list(cf.RULE_DICT.keys()))

	return rule_dict






def get_prefixed_code(code, by='LETTER', index=False, category='stock'):
	"""
	说明：对传入的证券代码加上市场前缀后返回（支持沪深A股，B股，基金等代码）
	参数：
		code: 6位或8位的股票代码（字符串形式）；
		by: 表示加何种类型前缀，可取值为'LETTER'和'NUMBER'，LETTER表示加字符前缀，如'sh',NUMBER表示加数字前缀，如'0'；
		index: 表示传入的 code 是否为指数，默认为 False，表示传入的是普通股票代码;
		category: 表示证券类别（如股票，基金,期货等等）
	返回值：加上市场前缀后的股票代码（字符串形式）
	"""
	prefixed_code = None
	if category.upper() == 'STOCK':
		prefixed_code = get_prefixed_stock_code(code=code, by=by, index=index)
		
	return prefixed_code








def get_prefixed_code_arr(code_arr, by='letter', index=False, category='stock'):
	"""
	说明：对传入的证券代码加上市场前缀后返回（支持沪深A股，B股，基金等代码）
	参数：
		code_arr: 6位或8位的股票代码（字符串形式）构成的 list；
		by: 表示加何种类型前缀，可取值为'LETTER'和'NUMBER'，LETTER表示加字符前缀，如'sh',NUMBER表示加数字前缀，如'0'；
		index: 表示传入的 code 是否为指数，默认为 False，表示传入的是普通股票代码;
		category: 表示证券类别（如股票，基金,期货等等）
	返回值：加上市场前缀后的股票代码（字符串形式）形成的 list
	"""
	prefixed_code_arr = None
	if category.upper() == 'STOCK':
		for i,code in enumerate(code_arr):
			prefixed_code = get_prefixed_code(code=code, by=by, index=index, category=category)
			if prefixed_code is None:
				continue
			else:
				if prefixed_code_arr is None:
					prefixed_code_arr = [prefixed_code]
				else:
					prefixed_code_arr.append(prefixed_code)
					
	return prefixed_code_arr
				



	

def get_index_code(index_name='shzz'):
	"""
	说明：根据输入的指数名称，返回相应的指数代码
	参数：index_name, 指数名称，可取值是：'shzz'(上证综指)，'szcz'(深证成指)等 
	返回值：带前缀'sh'的8位数的上证综指代码（字符串形式）
	"""
	try:
		return cf.INDEX_DICT[index_name.upper()]
	except:
		raise







def get_market_found_date(category='stock', market='hushen'):
	"""
	功能说明：获取指定交易市场证券类别的创建日，一般指中国股市创建时间
	参数：
		category: str型，默认值'stock', 表示股票类别
		market: str型，默认值 'hushen', 表示市场
	返回值：创建日期（str型）
	"""
	market_found_date = None
	if category.upper() == 'STOCK' and market.upper() == 'HUSHEN':
		market_found_date = cf.STOCK_MARKET_FOUND_DATE

	return market_found_date








def get_symbol_star():
	"""
	功能说明：获取 星号 * 
		因为很多 st 股是 * 开头的, 甚至是两个**
	Returns
	-------
	返回 星号 *

	"""
	return cf.STAR
	
	
	
	
	

def get_symbol_st():
	"""
	功能说明：获取st符号

	Returns
	-------
	返回st符号

	"""
	return cf.ST
	
	
	
	
	
	
def get_symbol_N():
	"""
	功能说明：获取新股符号N

	Returns
	-------
	返回新股符号 N
	"""
	return cf.N
	
	
	
	
	
	
def z():
	"""
	功能说明：这个函数没有实际功能，仅仅是表明上面的公开接口到此为止，下面的函数都是内部私有函数。

	Returns
	-------
	None.

	"""
	print('这个函数没有实际功能，仅仅是表明上面的公开接口到此为止，下面的函数都是内部私有函数。')
	pass

# public API end
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# ================================================================
# ================================================================
# ================================================================
# ================================================================
# ================================================================
# ================================================================




# ================================================================
# ================================================================
# ================================================================
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# private API start 

def get_prefixed_stock_code(code, by='LETTER', index=False):
	"""
	说明：对传入的证券代码加上市场前缀后返回（支持沪深A股，B股，基金等代码）
	参数：
		code: 6位或8位的股票代码（字符串形式）；
		by: 表示加何种类型前缀，可取值为'LETTER'和'NUMBER'，LETTER表示加字符前缀，如'sh',NUMBER表示加数字前缀，如'0'；
		index: 表示传入的 code 是否为指数，默认为 False，表示传入的是普通股票代码;
	返回值：加上市场前缀后的股票代码（字符串形式）
	"""
	prefixed_stock_code = None			# 初始化一个变量，用于保存加前缀后的股票代码
	# ------------------------------------
	# 先判断股票代码是否已加了市场前缀'sh' 或 'sz'，如果已经加了市场前缀就不用管他是否是指数，表明用户明确知道自己输入了市场前缀和股票代码
	code = str(code).lower() 		# 转换成小写
	if code.startswith(cf.SH_LETTER_PREFIX):
		if by.upper() == 'LETTER':
			prefixed_stock_code = code
			return prefixed_stock_code
		if by.upper() == 'NUMBER':
			prefixed_stock_code = code.replace(cf.SH_LETTER_PREFIX, cf.SH_NUMBER_PREFIX, 1) 			# 将 letter 替换为 number，最后的 1 表示最多替换一次，即把前缀替换掉即可
			return prefixed_stock_code
		
	if code.startswith(cf.SZ_LETTER_PREFIX):
		if by.upper() == 'LETTER':
			prefixed_stock_code = code
			return prefixed_stock_code
		if by.upper() == 'NUMBER':
			prefixed_stock_code = code.replace(cf.SZ_LETTER_PREFIX, cf.SZ_NUMBER_PREFIX, 1) 			# 将 letter 替换为 number，最后的 1 表示最多替换一次，即把前缀替换掉即可
			return prefixed_stock_code
			
	# -----------------------------
	# 普通股票代码进入这个 if	
	if index == False:
		for code_type in cf.SH_CODE_ARR:
			if code.startswith(code_type):
				if by.upper() == 'LETTER':
					prefixed_stock_code = cf.SH_LETTER_PREFIX + code
					return prefixed_stock_code
				if by.upper() == 'NUMBER':
					prefixed_stock_code = cf.SH_NUMBER_PREFIX + code
					return prefixed_stock_code
						
		for code_type in cf.SZ_CODE_ARR:
			if code.startswith(code_type):
				if by.upper() == 'LETTER':
					prefixed_stock_code = cf.SZ_LETTER_PREFIX + code
					return prefixed_stock_code					
				if by.upper() == 'NUMBER':
					prefixed_stock_code = cf.SZ_NUMBER_PREFIX + code
					return prefixed_stock_code
	# -----------------
	# 沪深两市指数代码进入这个 if
	if index == True:
		for code_type in cf.SH_INDEX_CODE_ARR:
			if code.startswith(code_type):
				if by.upper() == 'LETTER':
					prefixed_stock_code = cf.SH_LETTER_PREFIX + code
					return prefixed_stock_code
				if by.upper() == 'NUMBER':
					prefixed_stock_code = cf.SH_NUMBER_PREFIX + code
					return prefixed_stock_code
						
		for code_type in cf.SZ_CODE_ARR:
			if code.startswith(code_type):
				if by.upper() == 'LETTER':
					prefixed_stock_code = cf.SZ_LETTER_PREFIX + code
					return prefixed_stock_code					
				if by.upper() == 'NUMBER':
					prefixed_stock_code = cf.SZ_NUMBER_PREFIX + code
					return prefixed_stock_code

	return prefixed_stock_code




# private API end 
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# ================================================================
# ================================================================
# ================================================================



if __name__ == "__main__":
	pass
