import requests


class Download:

    def __init__(self, url):
        self.url = url

    def download_as(self, output_file):
        r = requests.get(self.url)
        with open(output_file, 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':
    for i in range(2006, 2019):
        print('Downloading ', i, ' ...')
        dl = Download('http://www.annualreports.com/HostedData/AnnualReportArchive/b/NASDAQ_AVGO_' + str(i) + '.pdf')
        dl.download_as('Broadcom_' + str(i) + '.pdf')
