from django.db import models


class House(models.Model):
    """ Model that holds information on each house. """
    area_unit = models.CharField(max_length=100)
    bathrooms = models.CharField(max_length=100)
    bedrooms = models.CharField(max_length=100)
    home_size = models.CharField(max_length=100)
    home_type = models.CharField(max_length=100)
    last_sold_date = models.CharField(max_length=100)
    last_sold_price = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    property_size = models.CharField(max_length=100)
    rent_price = models.CharField(max_length=100)
    rentzestimate_amount = models.CharField(max_length=100)
    rentzestimate_last_updated = models.CharField(max_length=100)
    tax_value = models.CharField(max_length=100)
    tax_year = models.CharField(max_length=100)
    year_built = models.CharField(max_length=100)
    zestimate_amount = models.CharField(max_length=100)
    zestimate_last_updated = models.CharField(max_length=100)
    zillow_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        """ Custom model string representation. """
        return (
            f"{self.id} - {self.address}, {self.city}, "
            f"{self.state}, {self.zipcode}"
            )
