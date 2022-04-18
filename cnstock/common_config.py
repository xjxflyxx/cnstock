"""
本模块定义中国股市的一些常量和规则
"""


# 定义中国股市创建日期，为获取数据的起始日提供准备
STOCK_MARKET_FOUND_DATE = '1988-01-01'

# ------------------------------
# 定义中国股市中的各时间点
"""
TIME_0915 = "09:15:00" 			# 早盘集合竞价开始时间
TIME_0920 = "09:20:00" 			# 早盘集合竞价可撤单结束时间
TIME_0925 = "09:25:00" 			# 早盘集合竞价结束时间

TIME_0930 = "09:30:00" 			# 上午盘连续竞价开始时间
TIME_1130 = "11:30:00" 			# 上午盘连续竞价结束时间

TIME_1300 = "13:00:00" 			# 下午盘连续竞价开始时间
TIME_1457 = "14:57:00" 			# 下午盘收前盘3分钟集合竞价开始时间
TIME_1500 = "15:00:00" 			# 下午盘收盘结束时间

OPEN_TIME = TIME_0915 			# 中国股市开盘时间
CLOSE_TIME = TIME_1500 			# 中国股市收盘时间
"""

OPEN_TIME = "09:15:00" 						# 股市开盘时间

STOP_WITHDRAW_TIME = "09:20:00" 			# 早盘集合竞价停止撤单时间
OPEN_PRICE_TIME = "09:25:00" 				# 早盘集合竞价产生开盘价时间

AM_START_TIME = "09:30:00" 					# 上午盘连续竞价开始时间
AM_STOP_TIME = "11:30:00" 					# 上午盘连续竞价结束时间

PM_START_TIME = "13:00:00" 					# 下午盘连续竞价开始时间
PM_STOP_TIME = "14:57:00" 					# 下午盘连续竞价结束时间

CLOSE_TIME = "15:00:00" 					# 下午盘收盘结束时间





# --------------------
ONE_HAND = 100 					# 一手定义为 100 股

# --------------------------
# 定义涨跌停幅度
# 1. 上证60开头和深证00开头的ST股涨跌幅为上下5%
UPPER_LIMIT_PERCENT5 = 1.05 				# 涨停幅度类型1（1.05 表示在昨收价基础上乘以 1.05 表示今天涨停价）
LOWER_LIMIT_PERCENT5 = 0.95 				# 跌停幅度类型1（0.95 表示在昨收价基础上乘以 0.95 表示今天跌停价）

# 2. 上证60开头和深证00开头的非ST股涨跌幅为上下10%
UPPER_LIMIT_PERCENT10 = 1.1 				# 涨停幅度类型2（1.1 表示在昨收价基础上乘以 1.1 表示今天涨停价）
LOWER_LIMIT_PERCENT10 = 0.9 				# 跌停幅度类型2（0.9 表示在昨收价基础上乘以 0.9 表示今天跌停价）

# 3. 上证科创板（688开头）和深证创业板（30开头）的涨跌幅为上下20% （包括 ST股）
UPPER_LIMIT_PERCENT20 = 1.2 				# 涨停幅度类型3（1.2 表示在昨收价基础上乘以 1.2 表示今天涨停价）
LOWER_LIMIT_PERCENT20 = 0.8 				# 跌停幅度类型3（0.8 表示在昨收价基础上乘以 0.8 表示今天跌停价）


# ---------------------------
# 卖和买必须间隔天数
T0 = 0 				# 0 表示随时可买可卖
T1 = 1 				# 1 表示至少隔 1 天，即今天买进的股明天才能卖

# ----------------------------
# 国家抽税率（仅在回测时用到，实盘会自动扣）
BUY_TAX_RATE = 0 				# 股票买入时向国家交的税率为 0 （即不用交税）
SELL_TAX_RATE = 0.001 			# 股票卖出时向国家交的税率为 0.001（即千分之一）

TAX_RATE = BUY_TAX_RATE + SELL_TAX_RATE

# ----------------------------
# 过户费率（仅在回测时用到，实盘会自动扣）
BUY_TRANSFER_FEE_RATE = 0.00002 		# 买股票的时候要交的过户费率
SELL_TRANSFER_FEE_RATE = 0.00002 		# 卖股票的时候要交的过户费率





# ------------------------------------------
# ------------------------------------------
# 市场、证券（股票）代码、证券名称分类！！

# ---------------------
# 1.下面是市场前缀，一般用于拉取行情数据时加在股票代码前用，经测试，需注意大小写，一般是只认小写（SINA 就是只认小写市场前缀）
SH_LETTER_PREFIX = 'sh' 				# 字母形式的沪市前缀
SZ_LETTER_PREFIX = 'sz' 				# 字母形式的深市前缀

BJ_LETTER_PREFIX = 'bj' 				# 字母形式的北交所前缀

SH_NUMBER_PREFIX = '0' 					# 数字形式的沪市前缀
SZ_NUMBER_PREFIX = '1' 					# 数字形式的深市前缀

# ------------------------------------
# 2. 下面是证券代码前缀含义（包含普通证券和指数）

# -------------------------------------
# 以下是沪市证券代码第 1 位含义
SH0 = '0' 					# 沪市 0 开头的证券代码，表示国债/指数
SH1 = '1' 					# 沪市 1 开头的证券代码，表示债券
SH2 = '2' 					# 沪市 2 开头的证券代码，表示回购
SH3 = '3' 					# 沪市 3 开头的证券代码，表示期货
SH4 = '4' 					# 沪市 4 开头的证券代码，备用
SH5 = '5' 					# 沪市 5 开头的证券代码，表示基金/权证
SH6 = '6' 					# 沪市 6 开头的证券代码，表示 A 股
SH7 = '7' 					# 沪市 7 开头的证券代码，表示非交易业务（发行、权益分配等）
SH8 = '8' 					# 沪市 8 开头的证券代码，备用
SH9 = '9' 					# 沪市 9 开头的证券代码，表示 B 股

# 以下是深市证券代码第 1 位含义
SZ0 = '0' 					# 深市 0 开头的证券代码，表示 A 股
SZ1 = '1' 					# 深市 1 开头的证券代码，表示债券/基金
SZ2 = '2' 					# 深市 2 开头的证券代码，表示 B 股
SZ3 = '3' 					# 深市 3 开头的证券代码，表示创业板/指数

# 以下是京市证券代码第一位
BJ4 = '4'
BJ8 = '8'

# ---------------------------------------
# 以下是沪市证券代码前 3 位含义
SH000 = SH0 + '00' 				# 沪市 000 开头的指数代码 （上证指数，沪深300指数，中证指数等）
SH009 = SH0 + '09' 				# 国债（2000年前发行）
SH010 = SH0 + '10' 				# 国债（2000年到2009年发行）
SH019 = SH0 + '19' 				# 固定收益电子平台交易国债
SH020 = SH0 + '20' 				# 记帐式贴现国债
SH090 = SH0 + '90' 				# 新国债质押式回购质押券出入库（对应010***国债）
SH099 = SH0 + '99' 				# 新国债质押式回购质押券出入库（对应009***国债）

SH100 = SH1 + '00' 				# 可转债（对应600***），其中1009**用于转债回售
SH104 = SH1 + '04' 				# 公司债及国家发改委等核准发行的、登记在证券帐户的债券（对应122***）出入库
SH105 = SH1 + '05' 				# 105000-105899 用于分离债（对应126***）出入库，105900-105999用于企业债（120***，129***）出入库
SH106 = SH1 + '06' 				# 地方政府债出入库（对应130***）
SH107 = SH1 + '07' 				# 记帐式贴现国债出入库（对应020***）
SH110 = SH1 + '10' 				# 可转债（对应600***）
SH112 = SH1 + '12' 				# 可转债（对应600***）
SH113 = SH1 + '13' 				# 可转债（对应601***）
SH120 = SH1 + '20' 				# 企业债
SH121 = SH1 + '21' 				# 资产证券化
SH122 = SH1 + '22' 				# 122000-122499用于公司债，122500-122999用于国家发改委等核准发行的、登记在证券帐户的债券
SH126 = SH1 + '26' 				# 分离交易的可转换公司债
SH128 = SH1 + '28' 				# 可转换公司债
SH129 = SH1 + '29' 				# 企业债
SH130 = SH1 + '30' 				# 地方政府债
SH181 = SH1 + '81' 				# 可转债转股（对应600***），已不再增用
SH190 = SH1 + '90' 				# 可转债转股（对应600***）
SH191 = SH1 + '91' 				# 可转债转股（对应601***）
SH192 = SH1 + '92' 				# 可交换公司债转股（对应601***）

SH201 = SH2 + '01' 				# 国债回购（席位托管方式）
SH202 = SH2 + '02' 				# 企业债回购
SH203 = SH2 + '03' 				# 国债买断式回购
SH204 = SH2 + '04' 				# 债券质押式回购（帐户托管方式）
SH205 = SH2 + '05' 				# 债券质押式报价回购

SH310 = SH3 + '10' 				# 国债期货（暂停交易）

SH500 = SH5 + '00' 				# 契约型封闭式基金
SH510 = SH5 + '10' 				# 交易型开放式指数证券投资基金
SH519 = SH5 + '19' 				# 开放式基金申赎
SH521 = SH5 + '21' 				# 开放式基金认购
SH522 = SH5 + '22' 				# 开放式基金跨市场转托管
SH523 = SH5 + '23' 				# 开放式基金分红
SH524 = SH5 + '24' 				# 开放式基金基金转换
SH580 = SH5 + '80' 				# 权证（含股改权证、公司权证）
SH582 = SH5 + '82' 				# 权证行权

SH60 = SH6 + '0' 				# A 股证券

SH688 = SH6 + '88' 				# A 股证券（科创板）

SH700 = SH7 + '00' 				# 配股（对应600***）
SH702 = SH7 + '02' 				# 职工股配股（对应600***）
SH704 = SH7 + '04' 				# 持股配债
SH705 = SH7 + '05' 				# 基金扩募
SH706 = SH7 + '06' 				# 要约收购
SH730 = SH7 + '30' 				# 申购、增发（对应600***）
SH731 = SH7 + '31' 				# 持股增发（对应600***）
SH733 = SH7 + '33' 				# 可转债申购（对应600***）
SH735 = SH7 + '35' 				# 基金申购
SH738 = SH7 + '38' 				# 网上投票（对应600***）
SH740 = SH7 + '40' 				# 申购款或增发款（对应600***）
SH741 = SH7 + '41' 				# 申购或增发配号（对应600***）
SH743 = SH7 + '43' 				# 可转债发债款（对应600***）
SH744 = SH7 + '44' 				# 可转债配号（对应600***）
SH745 = SH7 + '45' 				# 基金申购款
SH746 = SH7 + '46' 				# 基金申购配号
SH751 = SH7 + '51' 				# 751000-751199用于国债分销，751900-751969用于地方政府债分销，751970-751999用于公司债及国家发改委等核 准发行的、登记在证券帐户的债券分销
SH760 = SH7 + '60' 				# 配股（对应601***）
SH762 = SH7 + '62' 				# 职工股配股（对应601***）
SH780 = SH7 + '80' 				# 申购、增发（对应601***）
SH781 = SH7 + '81' 				# 持股增发（对应601***）
SH783 = SH7 + '83' 				# 可转债申购（对应601***）
SH788 = SH7 + '88' 				# 网络投票（对应601***）
SH790 = SH7 + '90' 				# 申购款或增发款（对应601***）
SH791 = SH7 + '91' 				# 申购或增发配号（对应601***）
SH793 = SH7 + '93' 				# 可转债申购款（对应601***）
SH794 = SH7 + '94' 				# 可转债配号（对应601***）
SH799 = SH7 + '99' 				# 指定交易（含指定交易、撤销指定、回购指定撤销、A股密码服务等）

SH900 = SH9 + '00' 				# B 股证券
SH938 = SH9 + '38' 				# 网上投票（B股）
SH939 = SH9 + '39' 				# B 股网络投票密码服务（现仅用939988）


# -----------------------------------------
# 以下是深市证券代码前 2 位含义
SZ00 = SZ0 + '0' 				# A 股证券
SZ03 = SZ0 + '3' 				# A 股A2权证
SZ07 = SZ0 + '7' 				# A 股增发
SZ08 = SZ0 + '8' 				# A 股 A1权证
SZ09 = SZ0 + '9' 				# A 股转配

SZ10 = SZ1 + '0' 				# 国债现货
SZ11 = SZ1 + '1' 				# 债券
SZ12 = SZ1 + '2' 				# 可转换债券
SZ13 = SZ1 + '3' 				# 国债回购
SZ17 = SZ1 + '7' 				# 原有投资基金
SZ18 = SZ1 + '8' 				# 证券投资基金

SZ20 = SZ2 + '0' 				# B 股证券
SZ27 = SZ2 + '7' 				# B 股增发
SZ28 = SZ2 + '8' 				# B 股权证

SZ30 = SZ3 + '0' 				# 创业板证券
SZ37 = SZ3 + '7' 				# 创业板增发
SZ38 = SZ3 + '8' 				# 创业板权证

SZ39 = SZ3 + '9' 				# 综合指数/成份指数


# ---------------------------------------
# 3.证券（股票）名称分类（下面这些常量定义中，如果是正则表示的，只能用适应正则的代码来处理；如果不是正则表示的，则可以用普通字符串查找方式处事，也可用正则处理）：
ST = 'ST' 			# 表示证券名称中含 'st' 字样的股。一般用大写，如需要小写，则调用者自行 ST.lower() 进行转换
ST_RE = '%s|%s' % (ST.upper(),ST.lower()) 					# 正则，ST股正则
NOT_ST_RE = '^(?!.*%s.*)'	% (ST.upper()) 					# 正则，非ST股的正则

STAR = '*' 			# 定义 星号，因为很多 st 股是 * 开头的
TUI = '退' 			# 表示证券名称中含有'退'字
N = 'N' 			# 表示证券名称中N开头，表示新股

DEFAULT_NAME_TYPE = '' 				# 空表示所有股票名称
DEFAULT_NAME_TYPE_RE = '' 			# 正则，空表示所有股票名称

# 构建一个证券（股票）名称中包含以下字符的 list，以表示他们是垃圾股，用于传递给上层代码当作过滤器，在构买时以去除这些垃圾股。
BAD_NAME_ARR = [STAR,TUI,ST.upper(),ST.lower(),'XD','XR','DR','xd','xr','dr','PT','pt','S','s',] 			

# -------------------------------
# 下面是对上面基本前导符代码的组合，以表达各类别前导符自动识别归类需求
SH_CODE_ARR = [SH5, SH6, SH9] 				# 沪市股票代码前导数字(5开头是沪市基金，6开头是沪市A股，9开头是沪市B股)
SZ_CODE_ARR = [SZ0, SZ1, SZ2, SZ3] 			# 深市股票代码前导数字(1开头是深市基金，0和3开头是深市A股，2开头是深市B股)

SH_INDEX_CODE_ARR = [SH0] 				# 沪市指数代码前导数字
SZ_INDEX_CODE_ARR = [SZ39] 				# 深市指数代码前导数字

SH60_CODE_ARR = [SH60] 					# 沪市 60 开头的股票代码
SZ00_CODE_ARR = [SZ00] 					# 深市 00 开头的股票代码

SH_A_CODE_ARR = [SH60,SH688] 			# 沪市 A 股类型
SZ_A_CODE_ARR = [SZ00,SZ30] 			# 深市 A 股类型
A_CODE_ARR = SH_A_CODE_ARR + SZ_A_CODE_ARR 			# 沪深两市 A 股代码类型

SH_B_CODE_ARR = [SH9] 					# 沪市 B 股类型
SZ_B_CODE_ARR = [SZ2] 					# 深市 B 股类型
B_CODE_ARR = SH_B_CODE_ARR + SZ_B_CODE_ARR 			# 沪深两市 B 股代码类型

SH_JIJIN_CODE_ARR = [SH5] 				# 沪市基金代码类型
SZ_JIJIN_CODE_ARR = [SZ1] 				# 深市基金代码类型
JIJIN_CODE_ARR = SH_JIJIN_CODE_ARR + SZ_JIJIN_CODE_ARR 			# 沪深两市基金代码类型

SH_KCB_CODE_ARR = [SH688] 				# 沪市科创板代码类型
KCB_CODE_ARR = SH_KCB_CODE_ARR 			# 科创板代码类型

SZ_CYB_CODE_ARR = [SZ30] 				# 深市创业板代码类型
CYB_CODE_ARR = SZ_CYB_CODE_ARR 			# 创业板代码类型

BJ_CODE_ARR = [BJ4, BJ8] 				# 京市代码类型
# --------------------
# --------------------------------
# 指数 dict ，前面都加市场前缀，sh 表示上证指数， sz 表示深证指数
# 上海方面的指数dict，由于上证综指 000001 与深证市场平安银行代码 000001 冲突，故用 sh000001 代表上证综证，在向数据源拉数据时请自行转换
SH_INDEX_DICT = {
	'SHZZ':'sh000001', 			# 上证综指
	'SH50':'sh000016' 			# 上证50指数
	}

# 深圳方面的指数，399001 是深证成指
SZ_INDEX_DICT = {
	'SZCZ':'sz399001',			# 深证成指
	'ZXBZ':'sz399005', 			# 中小板指（小票集中度次于创业板）
	'CYBZ':'sz399006', 			# 创业板指
	'SZZZ':'sz399106' 			# 深证综指
	}

# 这个数组存放大盘指数代码，包括上海和深圳的
# INDEX_DICT=dict(list(SH_INDEX_DICT.items()) + list(SZ_INDEX_DICT.items())) 	# 两市指数DICT
INDEX_DICT = dict(**SH_INDEX_DICT,**SZ_INDEX_DICT)

# 指数数组
INDEX_ARR = list(set(INDEX_DICT.values()))


# -------------------------
# DEFAULT_CODE_TYPE = '.*' 		# 默认正则，匹配任意个任意字符（即表示任何股票代码都符合条件）
DEFAULT_CODE_TYPE = '' 			# 空表示所有股票代码

# ------------------


# ---------------------------------------
# 为方便用户输入（下面各 list 中的元素主要用来匹配 get_rule() 的参数），定义一些各种可接受并表示某一类股票的标志，只要用户输入 list 内任一标志，就表示该类股票
SH60_SYMBOL_ARR = ['sh60','SH60',SH60,'6',6,60] 				# 定义一个各种可表示上证 60 开头的股票的识别标志
SH688_SYMBOL_ARR = ['sh688','SH688',SH688,688,'KCB','kcb'] 		# 定义一个各种可表示科创板（688开头的股票）股票的识别标志

SZ00_SYMBOL_ARR = ['sz00','SZ00',SZ00,0] 						# 定义一个各种可表示深证 00 开头的股票的识别标志
SZ30_SYMBOL_ARR = ['sz30','SZ30',SZ30,30,'CYB','cyb'] 			# 定义一个各种可表示深证 创业板（即300开头的股票）股票的识别标志

SH60ST_SYMBOL_ARR = ['sh60st','SH60ST','60st','60ST'] 			# 定义一个各种可表示上证60开头且是st的股票识别标志。
SZ00ST_SYMBOL_ARR = ['sz00st','SZ00ST','00st','00ST'] 			# 定义一个各种可表示深证00开头且是st的股票识别标志。
# --------------
SH900_SYMBOL_ARR = ['sh900','SH900',SH900,900] 					# 定义一个各种可表示沪市B股（900开头的股票）股票的识别标志
SH5_SYMBOL_ARR = ['sh5','SH5',SH5,5] 							# 定义一个各种可表示沪市基金（5开头的证券）的识别标志

SZ20_SYMBOL_ARR = ['sz20','SZ20',SZ20,20] 						# 定义一个各种可表示深市 B股（即200开头的股票）股票的识别标志
SZ1_SYMBOL_ARR = ['sz1','SZ1',SZ1,1] 							# 定义一个各种可表示深市基金（1开头的证券）的识别标志


# ------------------------------------
# -------------------------------
# 各类规则

# 基本时间字典
BASIC_TIME_DICT = {
	'OPEN_TIME': OPEN_TIME,

	'STOP_WITHDRAW_TIME': STOP_WITHDRAW_TIME,
	'OPEN_PRICE_TIME': OPEN_PRICE_TIME,

	'AM_START_TIME': AM_START_TIME,
	'AM_STOP_TIME': AM_STOP_TIME,

	'PM_START_TIME': PM_START_TIME,
	'PM_STOP_TIME': PM_STOP_TIME,

	'CLOSE_TIME': CLOSE_TIME
	}

BASIC_ONE_HAND_DICT = {
	'ONE_HAND': ONE_HAND
	}

BASIC_UPPER_LOWER_LIMIT_PERCENT5_DICT = {
	'UPPER_LIMIT_PERCENT': UPPER_LIMIT_PERCENT5,
	'LOWER_LIMIT_PERCENT': LOWER_LIMIT_PERCENT5
	}

BASIC_UPPER_LOWER_LIMIT_PERCENT10_DICT = {
	'UPPER_LIMIT_PERCENT': UPPER_LIMIT_PERCENT10,
	'LOWER_LIMIT_PERCENT': LOWER_LIMIT_PERCENT10
	}

BASIC_UPPER_LOWER_LIMIT_PERCENT20_DICT = {
	'UPPER_LIMIT_PERCENT': UPPER_LIMIT_PERCENT20,
	'LOWER_LIMIT_PERCENT': LOWER_LIMIT_PERCENT20
	}

BASIC_T0_DICT = {
	'T': T0
	}

BASIC_T1_DICT = {
	'T': T1
	}

BASIC_FEE_DICT = {
	'BUY_TAX_RATE': BUY_TAX_RATE,
	'SELL_TAX_RATE': SELL_TAX_RATE,
	'BUY_TRANSFER_FEE_RATE': BUY_TRANSFER_FEE_RATE,
	'SELL_TRANSFER_FEE_RATE': SELL_TRANSFER_FEE_RATE
	}




# --------------------------------
# 下面这个 RULE_DICT 非常重要，其元素也是 DICT，每一个元素表示不同类型的证券的交易规则，都定义在这里！
# RULE_DICT 中的 CODE_TYPE 和 NAME_TYPE 是普通字符串，用是否包含他们的方式去搜索，
# 而 NAME_TYPE_RE 一般是正则，可用于 df.name.str.contains(NAME_TYPE_RE) 等进行筛选相应的股，pandas 的 contains() 也是接受普通字符串为参数的。
RULE_DICT = {
	# 下面是 SH60 且是 ST 的规则
	SH_LETTER_PREFIX.upper() + SH60 + ST: dict(**{'CODE_TYPE':SH60,'NAME_TYPE':ST,'NAME_TYPE_RE':ST_RE},**BASIC_TIME_DICT,**BASIC_ONE_HAND_DICT,**BASIC_UPPER_LOWER_LIMIT_PERCENT5_DICT,**BASIC_T1_DICT,**BASIC_FEE_DICT), 		# 沪市 60 开头且是ST的股票代码交易规则
	# 下面是 SZ00 且是 ST 的规则
	SZ_LETTER_PREFIX.upper() + SZ00 + ST: dict(**{'CODE_TYPE':SZ00,'NAME_TYPE':ST,'NAME_TYPE_RE':ST_RE},**BASIC_TIME_DICT,**BASIC_ONE_HAND_DICT,**BASIC_UPPER_LOWER_LIMIT_PERCENT5_DICT,**BASIC_T1_DICT,**BASIC_FEE_DICT), 		# 深市 00 开头且是ST的股票代码交易规则

	# 下面是 SH60 且不含 ST 的规则
	SH_LETTER_PREFIX.upper() + SH60: dict(**{'CODE_TYPE':SH60,'NAME_TYPE':DEFAULT_NAME_TYPE,'NAME_TYPE_RE':NOT_ST_RE},**BASIC_TIME_DICT,**BASIC_ONE_HAND_DICT,**BASIC_UPPER_LOWER_LIMIT_PERCENT10_DICT,**BASIC_T1_DICT,**BASIC_FEE_DICT), 		# 沪市 60 开头且不是ST的股票代码交易规则
	# 下面是 SZ00 且不含 ST 的规则
	SZ_LETTER_PREFIX.upper() + SZ00: dict(**{'CODE_TYPE':SZ00,'NAME_TYPE':DEFAULT_NAME_TYPE,'NAME_TYPE_RE':NOT_ST_RE},**BASIC_TIME_DICT,**BASIC_ONE_HAND_DICT,**BASIC_UPPER_LOWER_LIMIT_PERCENT10_DICT,**BASIC_T1_DICT,**BASIC_FEE_DICT), 		# 深市 00 开头且不是ST的股票代码交易规则

	# 下面是 SH688 （不管是否ST） 的规则
	SH_LETTER_PREFIX.upper() + SH688: dict(**{'CODE_TYPE':SH688,'NAME_TYPE':DEFAULT_NAME_TYPE,'NAME_TYPE_RE':DEFAULT_NAME_TYPE_RE},**BASIC_TIME_DICT,**BASIC_ONE_HAND_DICT,**BASIC_UPPER_LOWER_LIMIT_PERCENT20_DICT,**BASIC_T1_DICT,**BASIC_FEE_DICT),		# 沪市 688 开头（无论是否ST）的股票代码交易规则
	# 下面是 SZ30 （不管是否ST） 的规则
	SZ_LETTER_PREFIX.upper() + SZ30: dict(**{'CODE_TYPE':SZ30,'NAME_TYPE':DEFAULT_NAME_TYPE,'NAME_TYPE_RE':DEFAULT_NAME_TYPE_RE},**BASIC_TIME_DICT,**BASIC_ONE_HAND_DICT,**BASIC_UPPER_LOWER_LIMIT_PERCENT20_DICT,**BASIC_T1_DICT,**BASIC_FEE_DICT) 		# 深市 30 开头（无论是否ST）的股票代码交易规则

	}


# 下面这个为默认的证券和交易规则
#DEFAULT_RULE_DICT = RULE_DICT['DEFAULT']
DEFAULT_RULE_DICT = dict(**{'CODE_TYPE':DEFAULT_CODE_TYPE,'NAME_TYPE':DEFAULT_NAME_TYPE,'NAME_TYPE_RE':DEFAULT_NAME_TYPE_RE},**BASIC_TIME_DICT,**BASIC_ONE_HAND_DICT,**BASIC_UPPER_LOWER_LIMIT_PERCENT10_DICT,**BASIC_T1_DICT,**BASIC_FEE_DICT) 		# 默认交易规则


