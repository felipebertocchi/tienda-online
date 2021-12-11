# para llevar una variable definida en un contexto a que sea global

def total_amount_cart(request):
    total = 0
    # if request.user.is_authenticated:
    for value in request.session["cart"].values():
        total += float(value["price"])
    return {"total_amount_cart":round(total, 2)}

def total_items_cart(request):
    num_items = 0
    for value in request.session["cart"].values():
        num_items += value["quantity"]
    return {"total_items_cart":num_items}