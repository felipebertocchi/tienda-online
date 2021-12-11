class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}
        
        self.cart = cart

    def add(self, product):
        if (str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                "product_id" : product.id,
                "name" : product.name,
                "price" : str(product.price),
                "image" : product.image.url,
                "quantity" : 1,
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] += 1
                    value["price"] = round(float(value["price"]) + product.price, 2)
                    break
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save()

    def substract(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] -= 1
                value["price"] = round(float(value["price"]) - product.price, 2)
                if value["quantity"] < 1:
                    self.remove(product)
                break
        self.save()

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True