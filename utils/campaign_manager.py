```python
import json
from database import db_ops

class CampaignManager:
    def __init__(self):
        self.campaigns = self.load_campaigns()

    def load_campaigns(self):
        try:
            with open('data/campaigns.json', 'r') as file:
                campaigns = json.load(file)
        except FileNotFoundError:
            campaigns = {}
        return campaigns

    def save_campaigns(self):
        with open('data/campaigns.json', 'w') as file:
            json.dump(self.campaigns, file)

    def create_campaign(self, campaign_name, campaign_data):
        if campaign_name in self.campaigns:
            raise ValueError(f"Campaign '{campaign_name}' already exists.")
        self.campaigns[campaign_name] = campaign_data
        self.save_campaigns()

    def delete_campaign(self, campaign_name):
        if campaign_name not in self.campaigns:
            raise ValueError(f"Campaign '{campaign_name}' does not exist.")
        del self.campaigns[campaign_name]
        self.save_campaigns()

    def get_campaign(self, campaign_name):
        if campaign_name not in self.campaigns:
            raise ValueError(f"Campaign '{campaign_name}' does not exist.")
        return self.campaigns[campaign_name]

    def update_campaign(self, campaign_name, campaign_data):
        if campaign_name not in self.campaigns:
            raise ValueError(f"Campaign '{campaign_name}' does not exist.")
        self.campaigns[campaign_name] = campaign_data
        self.save_campaigns()

    def list_campaigns(self):
        return list(self.campaigns.keys())
```