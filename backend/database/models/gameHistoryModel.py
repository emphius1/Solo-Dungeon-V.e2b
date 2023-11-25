from django.db import models

class GameHistory(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    session_date = models.DateTimeField(auto_now_add=True)
    actions_taken = models.JSONField()
    quest_progress = models.JSONField()
    combat_outcomes = models.JSONField()
    decisions_made = models.JSONField()
    experience_earned = models.IntegerField(default=0)
    items_collected = models.JSONField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Game Histories"

    def __str__(self):
        return f"Game History for {self.character.name} on {self.session_date.strftime('%Y-%m-%d %H:%M:%S')}"