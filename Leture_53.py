def VAT(totalprice):
  result = totalprice+(totalprice*7/100)
  return  result

print(VAT(int(input("totalprice:"))))