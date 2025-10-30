# class <class name>

class RestaurantOrder:
    def __init__(self,order_id,rest_id,bill_amount):
        # order_id
        # rest_id
        # bill_amount
        self.order_id = order_id
        self.rest_id = rest_id
        self.bill_amount = bill_amount
        self.recipes =["idly","pizza"]

    def get_order_id(self):
        print(self.order_id)

    def get_rest_id(self):
        print(self.rest_id)

    def get_bill_amount(self):
        print(self.bill_amount)

    def get_find_recipes(self):
        print(self.recipes)

#variable = call your class with attributes

order_1 = RestaurantOrder(order_id=1,rest_id=173,bill_amount=1200)
# now instance will get created

# printing my order_id

order_1.get_order_id()



class student:
    # student name
    # student_id
    # email
    # section-b
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email
        self.section = "section-b"

    def get_name(self):
        print(self.name)
        return 

    def get_id(self):
        print(self.id)


class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_length_breadth(self):
        return self.length , self.breadth
        
                            