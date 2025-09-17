import datetime
import requests

from event_scrapers.event_listing import EventListing


class Tpl:
    BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
    SHARED_ATTRIBUTES = {"organizer": "Toronto Public Library"}

    @staticmethod
    def get():
        url = Tpl.BASE_URL + "/api/3/action/package_show"
        params = {"id": "library-branch-programs-and-events-feed"}
        package = requests.get(url, params=params).json()

        # To get resource data:

        for idx, resource in enumerate(package["result"]["resources"]):
            # for datastore_active resources:

            if resource["datastore_active"]:
                # To get all records in CSV format:

                url = Tpl.BASE_URL + "/api/3/action/datastore_search"
                p = {"id": resource["id"]}

                resource_search_data = requests.get(url, params=p).json()["result"]

                for record in resource_search_data["records"]:
                    EventListing(
                        name=record["title"],
                        organizer="Toronto Public Library",
                        start_date=Tpl.get_datetime(record),
                        location=record["library"] + " - Toronto Public Library",
                    )

    @staticmethod
    def get_datetime(record) -> datetime.datetime:
        if record["starttime"] is None or record["starttime"] == "None":
            datetime_string = record["startdate"] + " 12:00 AM"
        else:
            datetime_string = record["startdate"] + " " + record["starttime"]

        return datetime.datetime.strptime(datetime_string, "%Y-%m-%d %I:%M %p")


if __name__ == "__main__":
    Tpl.get()
