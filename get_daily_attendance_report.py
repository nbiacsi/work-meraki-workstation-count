'''
    Author: Sloth
    Date: 3/28/2025
    Description: Script that uses the Meraki API to get the count of unique UHM laptops on the Strongsville main campus by day.
'''

from dotenv import load_dotenv
import requests
from requests import Response

from datetime import date, timedelta
import os
from statistics import mean

from reports import Report


load_dotenv(override=True)


def get_device_count(headers: dict[str, str], network_id: str, timespan: int) -> int:
    '''
    Gets the count of the number of unique devices within this month.

    Args:
        headers (dict[str, str]): Meraki API headers.
        network_id (str): ID of the network in Meraki.
        timespan (int): Seconds back you want to look for devices.

    Returns:
        int: Count of unique devices found within the last number of days.
    '''

    url: str = f'https://dashboard.meraki.com/api/v1/networks/{network_id}/clients'
    params: dict[str, str | int] = {
        'timespan': timespan,
        'perPage': 1000
    }

    while True:
        response: Response = requests.get(url=url, params=params, headers=headers)
        devices: dict[str, str | int] = {}
        for client in response.json():
            client_name: str = str(client['description'])
            if not client_name.startswith('UHM-'):
                continue

            if devices.get(client_name) == None:
                devices.update(
                    {
                        client_name: 1
                    }
                )

        next_link: dict[str, str] | None = response.links.get('next')
        if not next_link:
            return sum(list(devices.values()))  # type: ignore
            
        params.clear()
        url: str = next_link['url']


def get_meraki_headers() -> dict[str, str]:
    '''
    Gets the Meraki headers used to authenticate to the Meraki API.

    Args:
        None.

    Returns:
        dict[str, str]: Meraki API headers.
    '''

    return {
        'X-Cisco-Meraki-API-Key': os.getenv('MERAKI_API_KEY')  # type: ignore
    }


def main() -> None:
    today: date = date.today()
    report: Report = Report(f'Attendance Count - {date.strftime(today, '%B').split(' ')[0]}.csv')
    headers: dict[str, str] = get_meraki_headers()
    network_id: str = os.getenv('NETWORK_ID')  # type: ignore
    device_count: int = get_device_count(headers, network_id, 86_400)
    report.add_row([date.strftime(today - timedelta(days=1), '%m-%d'), device_count])

    if report.exists():
        report.export_csv()
    else:
        report.export_csv(['Date', 'Device Count'])


if __name__ == '__main__':
    main()