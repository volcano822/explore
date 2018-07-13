# -*- coding:utf-8 -*-

from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.generic import View
from idl.coupon_info.ttypes import CouponInfo
from idl.coupon_info.ttypes import Response as CouponInfoResponse

# from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.protocol.TJSONProtocol import TJSONProtocol
from thrift.transport.TTransport import TMemoryBuffer

coupon = {
    'cid': "qa_70d9cf47-1870-4d8e-925e-8d9ae0ace08f",
    'name': u"体验金 智能投顾 6期 1000元",
    'amount': 100000,
    'progress': 1,
    'start_time': '2018-01-01 00:00:00',
    'expired_time': '2018-01-01 00:00:00',
    'ctype': 0,
    'use_type': 2,
    'min_invest_time': 3,
    'max_invest_time': 6,
    'min_amount': 200000,
    'desc': u"体验金 智能投顾 3-6期 1000元，最少投资2000元可用",
}


class InfoThriftView(View):
    """获取优惠券信息"""

    def post(self, request):
        out_format = request.POST.get('OutFormat', 'json')

        info = CouponInfo(
                cid=coupon['cid'],
                name=coupon['name'],
                amount=coupon['amount'],
                progress=coupon['progress'],
                start_time=coupon['start_time'],
                expired_time=coupon['expired_time'],
                ctype=coupon['ctype'],
                use_type=coupon['use_type'],
                min_invest_time=coupon['min_invest_time'],
                max_invest_time=coupon['max_invest_time'],
                min_amount=coupon['min_amount'],
                des=coupon['desc'],
        )
        res = CouponInfoResponse(code=0, message='success', info=info)
        tMemory_b = TMemoryBuffer()
        if out_format == 'binary':
            tBinaryProtocol_b = TCompactProtocol(tMemory_b)
            content_type = 'application/octet-stream'
        else:
            tBinaryProtocol_b = TJSONProtocol(tMemory_b)
            content_type = 'application/json'

        res.write(tBinaryProtocol_b)

        memory_buffer = tMemory_b.getvalue()
        return HttpResponse(content=memory_buffer, content_type=content_type)


class InfoJsonView(View):
    def post(self, request):
        result = {
            'coupon': coupon,
            'code': 0,
            'message': 'success',
        }

        return JsonResponse({'coupon': result})
