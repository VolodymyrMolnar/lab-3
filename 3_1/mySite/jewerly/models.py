from django.db import models

# Client model
class Client(models.Model):
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Employee model
class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=45, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    hire_date = models.DateField(null=False)

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=45, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    order_date = models.DateField(null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=50, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"Order {self.id} - {self.status}"

# OrderDetails model
class OrderDetails(models.Model):
    quantity = models.IntegerField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_details")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_details")

