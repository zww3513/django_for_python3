from django.db import models

# Create your models here.

class machine_info(models.Model):
    ip_out = models.CharField(max_length=30, default='NULL')
    ip_out2 = models.CharField(max_length=30, default='NULL')
    ip_in = models.CharField(max_length=30, default='NULL')
    vip = models.IntegerField()
    idc = models.CharField(max_length=30, default='NULL')
    os = models.CharField(max_length=64, default='NULL')
    cpu = models.CharField(max_length=64, default='NULL')
    mem = models.CharField(max_length=64, default='NULL')
    swap = models.CharField(max_length=64, default='NULL')
    disk = models.CharField(max_length=64, default='NULL')
    usage = models.CharField(max_length=32, default='NULL')
    max_deploy = models.IntegerField()
    status = models.IntegerField()
    platform = models.CharField(max_length=32, default='NULL')
    project = models.CharField(max_length=32, default='NULL')

    class Meta:
        db_table = "machine_info"

    def __unicode__(self):
        return str(self.ip_in)

class game_info(models.Model):
    server_id = models.IntegerField()
    wan_id = models.IntegerField()
    ip_out = models.CharField(max_length=30, default='NULL')
    ip_out2 = models.CharField(max_length=30, default='NULL')
    ip_in = models.CharField(max_length=30, default='NULL')
    vip = models.CharField(max_length=30, default='NULL')
    install_id = models.IntegerField()
    web_ver = models.CharField(max_length=16, default='NULL')
    res_ver = models.CharField(max_length=16, default='NULL')
    is_deploy = models.BooleanField(default='0')
    is_open = models.BooleanField(default='0')
    kf_time = models.DateTimeField(default='2025-06-12 12:00')
    is_hefu = models.BooleanField(default='0')
    last_hf_target = models.IntegerField()
    cur_hf_target = models.IntegerField()
    hf_time = models.DateTimeField(default='2025-06-12 12:00')
    type = models.CharField(max_length=16, default='NULL')
    status = models.BooleanField(default='0')
    platform = models.CharField(max_length=16, default='NULL')
    project = models.CharField(max_length=16, default='NULL')
    server_dir = models.CharField(max_length=255, default='NULL')
    user_info = models.CharField(max_length=30, default='NULL')
    class Meta:
        db_table = "game_info"

    def __unicode__(self):
        return str(self.server_id)
