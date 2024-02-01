import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    """
    Product details table
    """

    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        editable=False,
        default=uuid.uuid1(),
        verbose_name=_("product website ID"),
        help_text=_("format: required, unique"),
    )
    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
    )
    slug = models.SlugField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product safe URL"),
        help_text=_("format: required, letters, numbers, underscores or hyphens"),
    )
    is_active = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date product last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    """
    Product inventory table
    """

    sku = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("stock keeping unit"),
        help_text=_("format: required, unique, max-20"),
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("universal product code"),
        help_text=_("format: required, unique, max-12"),
    )
    product_variant = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.PROTECT
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )
    purchase_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("purchase cost"),
        help_text=_("format: optional"),
    )
    initial_stock = models.IntegerField(
        default=0,
        verbose_name=_("initial stock"),
        help_text=_("format: required, default-0"),
    )
    last_ordered = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("date last ordered"),
        help_text=_("format: Y-m-d H:M:S, optional"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return self.product.name


class Stock(models.Model):
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("inventory stock check date"),
        help_text=_("format: Y-m-d H:M:S, null-true, blank-true"),
    )
    total_stock = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("units/qty of stock"),
        help_text=_("format: required, default-0"),
    )
    units_out = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("units taken out to date"),
        help_text=_("format: required, default-0"),
    )


# class ProductAttributes(models.Model):
#     # product = models.ForeignKey(
#     #     ProductInventory,
#     #     null=False,
#     #     blank=False,
#     #     on_delete=models.PROTECT,
#     #     )
#     attribute_name = models.CharField(
#         max_length=255,
#         null=False,
#         blank=False,
#         help_text=_("Product attribute name"),
#     )
#     attribute_description = models.CharField(
#         max_length=255,
#         null=False,
#         blank=False,
#         help_text=_("attribute description")
#     )


# class ProductAttributeValue(models.Model):
#     attribute = models.ForeignKey(
#         ProductAttributes,
#         null=False,
#         blank=False,
#     )
#     value = models.CharField(
#         max_length=255,
#         null=False,
#         help_text=_("value of attribute")
#     )