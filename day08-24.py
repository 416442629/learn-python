lax_coordinates=(33.84,-118.23)
city,year,pop,chg,area=('tokyo',2003,3245,0.66,8014)
trealer_ids=[('USA','311123123123'),('Bra','3ce123'),('Bra2','12312312sss')]
for passport in sorted(trealer_ids):
    print('%s/%s' % passport)
#拆包:
for country,_ in sorted(trealer_ids):
    print(country)
