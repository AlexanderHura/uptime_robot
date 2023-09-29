from datetime import datetime
from core.models import Website, Report, ReportStatuses
from typing import Optional
import requests



class Checker:
    def get_sites(self):
        return Website.objects.all()
   
    
    def generate_report(self, site: Website, time: datetime) -> Report:
        response = requests.get(url=(site.url))
        if  response.status_code == 200:
            return Report(
                site = site,
                status=ReportStatuses.AVAILABLE.value,
                created_at=time,
            )
        return Report(
                site = site,
                status=ReportStatuses.NOTAVAILABLE.value,
                created_at=time,
            )

    def save_report(self, report: Report) -> Optional[Report]:
        instance = report.save()
        return instance
    
    def generate_reports(self):
        websites = self.get_sites()
        now = datetime.now()
        
        for site in websites:
            report = self.generate_report(site, now)
            self.save_report(report)

            print(">>> DONE")

