	
get_A_code_arr()
功能说明：返回A股代码类型标识
get_B_code_arr()
功能说明：返回B股代码类型标识
get_all_rule()
功能说明：返回所有已定义的股票类型（含基金等）的规则字典
 
Returns
-------
返回值：所有已定义的股票类型（含基金等）的规则字典。
get_api_list()
功能说明：本接口不对外使用，仅用于向调用模块返回本模块能提供的接口列表
get_bad_name_arr()
功能说明：返回股票名称（不是股票代码）中有ST等各种垃圾字符的 list, 这个 list 专门收集了各种垃圾字符，返回给调用者当过滤器用
 
Returns
-------
list, 每个元素是指出垃圾字符。
get_bj_code_arr()
功能说明：返回北交所股票代码类型标识
get_cyb_code_arr()
功能说明：返回创业板股代码类型标识
get_index_code(index_name='shzz')
说明：根据输入的指数名称，返回相应的指数代码
参数：index_name, 指数名称，可取值是：'shzz'(上证综指)，'szcz'(深证成指)等 
返回值：带前缀'sh'的8位数的上证综指代码（字符串形式）
get_jijin_code_arr()
功能说明：返回基金代码类型标识
get_kcb_code_arr()
功能说明：返回科创板股代码类型标识
get_market_found_date(category='stock', market='hushen')
功能说明：获取指定交易市场证券类别的创建日，一般指中国股市创建时间
参数：
        category: str型，默认值'stock', 表示股票类别
        market: str型，默认值 'hushen', 表示市场
返回值：创建日期（str型）
get_prefixed_code(code, by='LETTER', index=False, category='stock')
说明：对传入的证券代码加上市场前缀后返回（支持沪深A股，B股，基金等代码）
参数：
        code: 6位或8位的股票代码（字符串形式）；
        by: 表示加何种类型前缀，可取值为'LETTER'和'NUMBER'，LETTER表示加字符前缀，如'sh',NUMBER表示加数字前缀，如'0'；
        index: 表示传入的 code 是否为指数，默认为 False，表示传入的是普通股票代码;
        category: 表示证券类别（如股票，基金,期货等等）
返回值：加上市场前缀后的股票代码（字符串形式）
get_prefixed_code_arr(code_arr, by='letter', index=False, category='stock')
说明：对传入的证券代码加上市场前缀后返回（支持沪深A股，B股，基金等代码）
参数：
        code_arr: 6位或8位的股票代码（字符串形式）构成的 list；
        by: 表示加何种类型前缀，可取值为'LETTER'和'NUMBER'，LETTER表示加字符前缀，如'sh',NUMBER表示加数字前缀，如'0'；
        index: 表示传入的 code 是否为指数，默认为 False，表示传入的是普通股票代码;
        category: 表示证券类别（如股票，基金,期货等等）
返回值：加上市场前缀后的股票代码（字符串形式）形成的 list
get_rule(code_type=None)
说明：根据传入的股票代码类别，返回该类别的交易规则
参数：code_type：股票代码类别，可取值为 cf.RULE_DICT 中的 key，或接受下面出错提示那些值；若 code_type 为 None，则返回 DEFAULT 所指向的规则
返回值：该类型交易规则（dict 形式）
get_sh60_code_arr()
功能说明：返回创业板股代码类型标识
get_symbol_N()
功能说明：获取新股符号N
 
Returns
-------
返回新股符号 N
get_symbol_st()
功能说明：获取st符号
 
Returns
-------
返回st符号
get_symbol_star()
功能说明：获取 星号 * 
        因为很多 st 股是 * 开头的, 甚至是两个**
Returns
-------
返回 星号 *
get_sz00_code_arr()
功能说明：返回创业板股代码类型标识
