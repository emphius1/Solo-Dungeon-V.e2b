from django.db import models

class CampaignSettings(models.Model):
    # Define the fields for the CampaignSettings model based on the CampaignSettingsSchema
    campaign_name = models.CharField(max_length=255)
    campaign_description = models.TextField(blank=True)
    world_setting = models.TextField(blank=True)
    ruleset = models.CharField(max_length=100)
    max_players = models.IntegerField()
    difficulty_level = models.CharField(max_length=50)
    campaign_status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign_name

    class Meta:
        verbose_name = 'Campaign Setting'
        verbose_name_plural = 'Campaign Settings'