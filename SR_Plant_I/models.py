
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    Pack_dashboard_access = models.BooleanField(_("Pack_MainDashboard"),default=False)
    Pack_sku_access = models.BooleanField(_("Pack_SKU's"),default=False)
    Pack_printing_access = models.BooleanField(_("Pack_Printing"),default=False)
    Pack_production_access = models.BooleanField(_("Pack_Production"),default=False)
    Pack_oilpump_access = models.BooleanField(_("Pack_OilPump"),default=False)
    Pack_pouchcutting_access = models.BooleanField(_("Pack_PouchCutting"),default=False)
    Pack_manualleakchange_access = models.BooleanField(_("Pack_ManualLeakChange"),default=False)
    Pack_expvsact_access = models.BooleanField(_("Pack_ExpVsAct"),default=False)
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
    
    def __str__(self):
        return self.username

# Create your models here.
