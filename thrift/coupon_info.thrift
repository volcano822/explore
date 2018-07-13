namespace py common.coupon_info

struct Response{
    1:required i32 code, # 错误码
    2:required string message, # 错误信息
    3:optional CouponInfo info # 优惠券信息
}
struct CouponInfo{
    1:required string name, #名称
    2:required i32 min_amount,  #最小投资金额，单位：分
    3:required string cid,            #uuid
    4:required i32 ctype,  # 类型，1为体验金
    5:required string  start_time, #开始时间
    6: required string expired_time, #失效时间
    7: required i32 max_invest_time, # 最大投资期次
    8: required i32 min_invest_time, # 最小投资期次
    9: required i32 amount, # 优惠券金额，单位：分
    10: required i32 use_type, # 可用类型，0为智能投顾，1为散标，2为智能投顾/散标
    11: required i32 progress, # 状态
    12: required string des, #描述信息
}