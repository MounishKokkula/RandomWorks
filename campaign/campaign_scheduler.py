"""
Assumptions and behaviours:
1) A campaign is a single product which requires campaigning.
2) For each campaign - the following are provided as input to the CampaignScheduler class
    - Season: season_start/season_end [OPTIONAL] set to default for the next 6 months
    - products_list
        [{"product_name":"apple_iphone", "campaign_days": 10, "start_date": ""]

        # TODO possible improvements
        [{"product_name":"apple_iphone", "campaign_days": 10, "start_date": "",
         "region":<geographical region to market lat/long>, "device":<mobile/desktop>, "url":<campaign_url>}
        ]
3) Same product can have have multiple campaigns
4) If the input start date for a camp is greater than or equals to season start => set "camp_start" to "season_start"
5) If camp end date is greater than or equals to season end=> set "camp_end" to "season_end"
"""

from datetime import date, timedelta, datetime
import calendar
import pandas as pd


class CampaignScheduler:
    """
    # Stores a set of campaigns
    # Each campaign scheduled has a unique name Start and End date
    """

    # compute the default days in the next 6 months
    default_start = date.today()
    days_in_month = calendar.monthrange(default_start.year, default_start.month)[1]
    total_days = 0
    for i in range(6):
        total_days += calendar.monthrange(default_start.year, default_start.month + int(i))[1]
    default_end = default_start + timedelta(days=total_days)

    def __init__(self, products_list, season_start=default_start, season_end=default_end):
        """
        :param products_list: list of products which require campaigning
            Format [{"product_name":
             {"campaign_days": 10 [REQUIRED],
              "start_date": "" [OPTIONAL]}]
        :param season_start: Start date for the campaigning season / Default Start Date = today
        :param season_end: End date for the campaigning season / Default End date = today + 6 months
        """

        # TODO possible improvements
        # use @property to validate the input data
        # Check if dates in products_list are within the season start and end dates

        self.season_start = season_start
        self.season_end = season_end
        self.products_list = products_list
        self.scheduled_campaigns = []

    def schedule_campaign(self):
        """
        Input: Campaign season start & end dates
        :return:  scheduled_campaigns [type:DICTIONARY(hashmap)] /

        Example format for scheduled_campaigns
        scheduled_campaigns = {"product_name_startMMDD_endMMDD":
        {"camp_start": <start_date from product_list> | default season_start ,
        "camp_end": <camp_start + total campaign days>}
        """

        for product in self.products_list:
            camp_start = self.season_start
            if "start_date" in product:
                # check if start date is greater than or equals to season start=> else camp_start is "season_start"
                if self.season_end >= datetime.strptime(product["start_date"], '%Y-%m-%d').date() >= self.season_start:
                    camp_start = datetime.strptime(product["start_date"], '%Y-%m-%d').date()

            camp_end = camp_start + timedelta(days=product["campaign_days"] - 1)

            # check if camp end is greater than or equals to season end=> else camp_end is "season_end"
            if camp_end > self.season_end:
                camp_end = self.season_end

            camp_name = product["product_name"] + "_" + camp_start.strftime("%m%d") + "_" + camp_end.strftime("%m%d")
            self.scheduled_campaigns.append({"camp_name": camp_name, "camp_start": camp_start, "camp_end": camp_end})

        return self.scheduled_campaigns

    def find_gaps(self):
        """
        Input: Campaign start & end dates, scheduler
        Use the scheduler from class to find the gaps.
        :return: scheduler [type:DICTIONARY(hashmap)]
        """
        season = pd.DataFrame(pd.Series(pd.date_range(self.season_start, self.season_end)), columns=['date'])

        for sched_camp in self.scheduled_campaigns:
            camp_dates = pd.DataFrame(pd.Series(pd.date_range(sched_camp['camp_start'], sched_camp['camp_end'])),
                                      columns=['date'])
            for i in camp_dates['date']:
                season = season.drop(season['date'].index[season['date'] == str(i).split(" ")[0]], errors='ignore')

        return season


if __name__ == '__main__':
    products_list_1 = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                       {"product_name": "apple_macbookpro", "campaign_days": 20},
                       {"product_name": "apple_iphone", "campaign_days": 5, "start_date": "2021-07-17"},
                       {"product_name": "apple_iwatch", "campaign_days": 20}]

    products_list_2 = [{"product_name": "apple_iwatch", "campaign_days": 2}]

    campaigns = CampaignScheduler(products_list_1, season_start=date.today(),
                                  season_end=date.today() + timedelta(days=30))
    scheduled_camps = campaigns.schedule_campaign()
    print("Scheduled campaigns ")
    for i in scheduled_camps:
        print("Name: {}, Start: {}, End: {}".format(i['camp_name'], i['camp_start'], i['camp_end']))

    print("\nThe gaps from season start to season end ")
    for i in campaigns.find_gaps()['date']:
        print("{} ".format(i).split(" ")[0])
