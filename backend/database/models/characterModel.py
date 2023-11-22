from django.db import models

class Character(models.Model):
    # Character attributes based on D&D standards
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    # Additional character details
    skills = models.JSONField()
    equipment = models.JSONField()
    spells = models.JSONField(null=True, blank=True)
    backstory = models.TextField(null=True, blank=True)

    # Game state related
    hit_points = models.IntegerField()
    mana_points = models.IntegerField(null=True, blank=True)
    gold = models.IntegerField(default=0)
    status_effects = models.JSONField(null=True, blank=True)

    # Relationships
    allies = models.JSONField(null=True, blank=True)
    enemies = models.JSONField(null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'