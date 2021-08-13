Programming language used: python 3.6
Libraries used: datetime, calendar, pandas
Testing framework: unittest

Standards and methods followed:
1) Code style: Pep 8 (https://www.python.org/dev/peps/pep-0008)
2) Code Development Approach: Test Driven Development

A "Campaign" is the top-level advertising unit. Among other things, a campaign
will have a unique name, a start date, and end date.
"CampaignScheduler" service class can be used to store a set of campaigns. 
Each campaign being scheduled should have a unique name, a start date, and an end date.
The time of day is ignored.
The class provide's the following two operations:

1. schedule_campaign(campaign) This function adds a new campaign to the scheduler.

2. find_gaps() This function returns a list of date ranges that are not covered by the
current set of scheduled campaigns. For example, if the first scheduled campaign covers
the date range 1/1/2021-1/5/2021, a second event covers 1/10/2021-1/15/2021, and a
third event covers 1/20/2021-1/25/2021, then find_gaps method would return a list of
date ranges including 1/6/2021-1/9/2021 and 1/16/2021-1/19/2021. Note that campaign
schedules can also overlap, in which case there would be no gap between schedules.

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


Future improvements:
1) Include the below in input for more specific targetting

"region":<geographical region to market lat/long>, 
"device":<mobile/desktop>
"url":<campaign_url>

2) Make use of the data collected for analytics and find conversions, click through rates etc

