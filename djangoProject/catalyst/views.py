from django.http import HttpResponse
from django.http import JsonResponse
from djangoProject import settings
import os
import json

import pandas as pd

def getRecom1(user_id, loc):
    # os.system('pwd')
    df_cust = pd.read_csv(os.path.join(settings.BASE_DIR, 'category_pattern.csv'))
    df_loc = pd.read_csv(os.path.join(settings.BASE_DIR, 'mapping_btw_local_trenda_and_coupons.csv'))
    df_hot = pd.read_csv(os.path.join(settings.BASE_DIR, 'offers_hotels.csv'))
    print(df_hot)
    user_cat = df_cust[df_cust['USER_ID']==user_id].sort_values('rank', ascending=False)['MERCHANT_CATEGORY'].to_list()
    user_cat = user_cat[0: len(user_cat) if len(user_cat)<=3 else 4]
    merchs = df_loc[df_loc['LOCATION']==loc]
    merchs = merchs[merchs['MERCHANT_CATEGORY'].isin(user_cat)]
    resp = merchs.groupby('MERCHANT_CATEGORY').head(2).reset_index(drop=True)[['MERCHANT_CATEGORY', 'MERCHANT_NAME', 'coupon', 'desc']]
    # resp = df_hot.sample(4)[['MERCHANT_CATEGORY', 'MERCHANT_NAME', 'coupon', 'desc']]._append(resp, ignore_index=True)
    resp = pd.concat([df_hot.sample(4)[['MERCHANT_CATEGORY', 'MERCHANT_NAME', 'coupon', 'desc']], resp], axis=0, ignore_index=True)
    # print(df_hot)
    # print(resp)
    return json.loads(resp.to_json())

def index(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return JsonResponse(data)


def detail(request):
    id = request.GET.get('id')
    location = request.GET.get('location')

    # print(getRecom1(int(id),location))

    return JsonResponse(getRecom1(int(id),location), safe=False)