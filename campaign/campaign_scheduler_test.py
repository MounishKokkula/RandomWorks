import unittest
from campaign_scheduler import CampaignScheduler
from datetime import date, timedelta


class MyTestCase(unittest.TestCase):
    def test_schedule_campaign_greater_than_default_season_start(self):
        products_list = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                         {"product_name": "apple_macbookpro", "campaign_days": 20}]

        campaigns = CampaignScheduler(products_list)
        scheduled_campaigns = campaigns.schedule_campaign()
        season_start = campaigns.season_start

        for camp in scheduled_campaigns:
            self.assertGreaterEqual(camp['camp_start'], season_start,
                                    camp['camp_name'] + "camp start is less than season start")

    def test_schedule_campaign_less_than_default_season_end(self):
        products_list = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                         {"product_name": "apple_macbookpro", "campaign_days": 20},
                         {"product_name": "apple_iphone", "campaign_days": 5, "start_date": "2021-07-17"},
                         {"product_name": "apple_iwatch", "campaign_days": 20}]

        campaigns = CampaignScheduler(products_list)
        scheduled_campaigns = campaigns.schedule_campaign()
        season_end = campaigns.season_end

        for camp in scheduled_campaigns:
            self.assertLessEqual(camp['camp_end'], season_end,
                                 camp['camp_name'] + "camp end is greater than season end")

    def test_schedule_campaign_greater_than_season_start(self):
        products_list = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                         {"product_name": "apple_macbookpro", "campaign_days": 20}]

        campaigns = CampaignScheduler(products_list, season_start=date.today(),
                                      season_end=date.today() + timedelta(days=30))
        scheduled_campaigns = campaigns.schedule_campaign()
        season_start = campaigns.season_start

        for camp in scheduled_campaigns:
            self.assertGreaterEqual(camp['camp_start'], season_start,
                                    camp['camp_name'] + "camp start is less than season start")

    def test_schedule_campaign_less_than_season_end(self):
        products_list = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                         {"product_name": "apple_macbookpro", "campaign_days": 20},
                         {"product_name": "apple_iphone", "campaign_days": 5, "start_date": "2021-07-17"},
                         {"product_name": "apple_iwatch", "campaign_days": 20}]

        campaigns = CampaignScheduler(products_list, season_start=date.today(),
                                      season_end=date.today() + timedelta(days=5))
        scheduled_campaigns = campaigns.schedule_campaign()
        season_end = campaigns.season_end

        for camp in scheduled_campaigns:
            self.assertLessEqual(camp['camp_end'], season_end,
                                 camp['camp_name'] + "camp end is greater than season end")

    def test_schedule_campaign_camp_start_less_than_camp_end(self):
        products_list = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                         {"product_name": "apple_macbookpro", "campaign_days": 20},
                         {"product_name": "apple_iphone", "campaign_days": 5, "start_date": "2021-07-17"},
                         {"product_name": "apple_iwatch", "campaign_days": 20}]

        campaigns = CampaignScheduler(products_list)
        scheduled_campaigns = campaigns.schedule_campaign()
        season_end = campaigns.season_end

        for camp in scheduled_campaigns:
            self.assertLessEqual(camp['camp_start'],
                                 camp['camp_end'], camp['camp_name'] + "camp start is greater than camp end")

    def test_schedule_campaign_unique_campaign_names(self):
        products_list = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                         {"product_name": "apple_macbookpro", "campaign_days": 20},
                         {"product_name": "apple_iphone", "campaign_days": 5, "start_date": "2021-07-17"},
                         {"product_name": "apple_iwatch", "campaign_days": 20}]

        campaigns = CampaignScheduler(products_list, season_start=date.today(),
                                      season_end=date.today() + timedelta(days=30))
        scheduled_campaigns = campaigns.schedule_campaign()
        camp_names = set()
        # compare length of items to len of set of camp names to determine if they are unique
        for camp in scheduled_campaigns:
            camp_names.add(camp["camp_name"])

        self.assertEqual(len(camp_names), len(scheduled_campaigns))

    def test_find_gaps_1(self):

        products_list_1 = [{"product_name": "apple_iphone", "campaign_days": 10, "start_date": "2021-08-07"},
                           {"product_name": "apple_macbookpro", "campaign_days": 20},
                           {"product_name": "apple_iphone", "campaign_days": 5, "start_date": "2021-07-17"},
                           {"product_name": "apple_iwatch", "campaign_days": 20}]

        campaigns = CampaignScheduler(products_list_1, season_start=date.today(),
                                      season_end=date.today() + timedelta(days=30))
        campaigns.schedule_campaign()
        gaps = campaigns.find_gaps()['date']
        for i in gaps:
            self.assertIn(str(i).split(" ")[0], ["2021-08-05", "2021-08-06"])

    def test_find_gaps_2(self):
        products_list_1 = [{"product_name": "apple_iphone", "campaign_days": 20, "start_date": "2021-07-07"}]

        campaigns = CampaignScheduler(products_list_1, season_start=date.today(),
                                      season_end=date.today() + timedelta(days=30))
        campaigns.schedule_campaign()
        gaps = campaigns.find_gaps()['date']
        for i in gaps:
            self.assertIn(str(i).split(" ")[0],
                          ["2021-08-05", "2021-08-06", "2021-08-07", "2021-08-08", "2021-08-09", "2021-08-10",
                           "2021-08-11", "2021-08-12", "2021-08-13", "2021-08-14", "2021-08-15"])


if __name__ == '__main__':
    unittest.main()
